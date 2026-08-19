#!/usr/bin/env python3
"""Persist wxiu arcade play history, daily challenges, streaks, and badges."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any


SCHEMA_VERSION = 1
DEFAULT_FILE = Path.home() / ".codex" / "wxiu-game-launcher" / "progress.json"
MODES = ("solo", "coop", "versus")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def local_today() -> str:
    return datetime.now().astimezone().date().isoformat()


def empty_data() -> dict[str, Any]:
    return {
        "version": SCHEMA_VERSION,
        "created_at": utc_now(),
        "plays": [],
        "challenges": [],
    }


def load_data(path: Path) -> dict[str, Any]:
    if not path.exists():
        return empty_data()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"could not read progress file {path}: {exc}") from exc
    if data.get("version") != SCHEMA_VERSION:
        raise SystemExit(f"unsupported progress schema in {path}")
    if not isinstance(data.get("plays"), list) or not isinstance(data.get("challenges"), list):
        raise SystemExit(f"invalid progress structure in {path}")
    return data


def save_data(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def normalized_text(value: str, field: str) -> str:
    clean = " ".join(value.strip().split())
    if not clean:
        raise SystemExit(f"{field} must not be empty")
    if len(clean) > 500:
        raise SystemExit(f"{field} is too long")
    return clean


def parse_day(value: str) -> str:
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as exc:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD") from exc


def challenge_id(day: str, game: str, challenge: str) -> str:
    digest = hashlib.sha256(f"{day}|{game}|{challenge}".encode("utf-8")).hexdigest()[:8]
    return f"{day}-{digest}"


def activity_days(data: dict[str, Any]) -> set[date]:
    values: set[date] = set()
    for play in data["plays"]:
        day = play.get("date")
        if day:
            values.add(date.fromisoformat(day))
    for challenge in data["challenges"]:
        if challenge.get("status") == "completed" and challenge.get("date"):
            values.add(date.fromisoformat(challenge["date"]))
    return values


def current_streak(data: dict[str, Any], today: str | None = None) -> int:
    days = activity_days(data)
    if not days:
        return 0
    current = date.fromisoformat(today or local_today())
    if current not in days:
        current -= timedelta(days=1)
    streak = 0
    while current in days:
        streak += 1
        current -= timedelta(days=1)
    return streak


def achievement_rows(data: dict[str, Any]) -> list[dict[str, Any]]:
    completed = sum(1 for item in data["challenges"] if item.get("status") == "completed")
    games = {
        item.get("game")
        for item in [*data["plays"], *data["challenges"]]
        if item.get("game")
    }
    coop_plays = sum(1 for item in data["plays"] if item.get("mode") == "coop")
    active_days = len(activity_days(data))
    definitions = [
        ("first-credit", "First Credit", 1, len(data["plays"]) + completed),
        ("challenge-rookie", "Challenge Rookie", 1, completed),
        ("arcade-explorer", "Arcade Explorer", 5, len(games)),
        ("co-op-buddy", "Co-op Buddy", 3, coop_plays),
        ("seven-day-regular", "Seven-Day Regular", 7, active_days),
        ("challenge-master", "Challenge Master", 10, completed),
    ]
    return [
        {
            "id": badge_id,
            "name": name,
            "unlocked": progress >= target,
            "progress": min(progress, target),
            "target": target,
        }
        for badge_id, name, target, progress in definitions
    ]


def summary(data: dict[str, Any], path: Path) -> dict[str, Any]:
    today = local_today()
    unique_games = sorted(
        {
            item.get("game")
            for item in [*data["plays"], *data["challenges"]]
            if item.get("game")
        }
    )
    daily = next((item for item in reversed(data["challenges"]) if item.get("date") == today), None)
    return {
        "storage": str(path),
        "stats": {
            "plays": len(data["plays"]),
            "unique_games": len(unique_games),
            "completed_challenges": sum(
                1 for item in data["challenges"] if item.get("status") == "completed"
            ),
            "current_streak": current_streak(data, today),
        },
        "today": daily,
        "achievements": achievement_rows(data),
        "recent_plays": list(reversed(data["plays"][-5:])),
        "recent_challenges": list(reversed(data["challenges"][-5:])),
    }


def print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def cmd_show(args: argparse.Namespace) -> None:
    data = load_data(args.file)
    print_json(summary(data, args.file))


def cmd_daily(args: argparse.Namespace) -> None:
    data = load_data(args.file)
    day = args.date or local_today()
    existing = next((item for item in data["challenges"] if item.get("date") == day), None)
    if existing:
        print_json({"created": False, "challenge": existing, "summary": summary(data, args.file)})
        return
    game = normalized_text(args.game, "game")
    challenge = normalized_text(args.challenge, "challenge")
    item = {
        "id": challenge_id(day, game, challenge),
        "date": day,
        "game": game,
        "mode": args.mode,
        "challenge": challenge,
        "status": "pending",
        "created_at": utc_now(),
        "completed_at": None,
        "note": None,
    }
    data["challenges"].append(item)
    save_data(args.file, data)
    print_json({"created": True, "challenge": item, "summary": summary(data, args.file)})


def cmd_complete(args: argparse.Namespace) -> None:
    data = load_data(args.file)
    before = {item["id"] for item in achievement_rows(data) if item["unlocked"]}
    item = next((value for value in data["challenges"] if value.get("id") == args.id), None)
    if item is None:
        raise SystemExit(f"challenge not found: {args.id}")
    changed = item.get("status") != "completed"
    if changed:
        item["status"] = "completed"
        item["completed_at"] = utc_now()
    if args.note:
        item["note"] = normalized_text(args.note, "note")
    save_data(args.file, data)
    after_rows = achievement_rows(data)
    newly_unlocked = [row for row in after_rows if row["unlocked"] and row["id"] not in before]
    print_json(
        {
            "changed": changed,
            "challenge": item,
            "newly_unlocked": newly_unlocked,
            "summary": summary(data, args.file),
        }
    )


def cmd_record_play(args: argparse.Namespace) -> None:
    data = load_data(args.file)
    before = {item["id"] for item in achievement_rows(data) if item["unlocked"]}
    item = {
        "date": args.date or local_today(),
        "game": normalized_text(args.game, "game"),
        "mode": args.mode,
        "note": normalized_text(args.note, "note") if args.note else None,
        "recorded_at": utc_now(),
    }
    data["plays"].append(item)
    save_data(args.file, data)
    after_rows = achievement_rows(data)
    newly_unlocked = [row for row in after_rows if row["unlocked"] and row["id"] not in before]
    print_json(
        {
            "recorded": True,
            "play": item,
            "newly_unlocked": newly_unlocked,
            "summary": summary(data, args.file),
        }
    )


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    root.add_argument(
        "--file",
        type=Path,
        default=Path(os.environ.get("WXIU_PROGRESS_FILE", DEFAULT_FILE)),
        help="progress JSON path",
    )
    commands = root.add_subparsers(dest="command", required=True)

    show = commands.add_parser("show", help="show progress dashboard")
    show.set_defaults(func=cmd_show)

    daily = commands.add_parser("daily", help="create or return a daily challenge")
    daily.add_argument("--game", required=True)
    daily.add_argument("--mode", choices=MODES, required=True)
    daily.add_argument("--challenge", required=True)
    daily.add_argument("--date", type=parse_day)
    daily.set_defaults(func=cmd_daily)

    complete = commands.add_parser("complete", help="complete a saved challenge")
    complete.add_argument("--id", required=True)
    complete.add_argument("--note")
    complete.set_defaults(func=cmd_complete)

    record = commands.add_parser("record-play", help="record an ordinary play session")
    record.add_argument("--game", required=True)
    record.add_argument("--mode", choices=MODES, required=True)
    record.add_argument("--note")
    record.add_argument("--date", type=parse_day)
    record.set_defaults(func=cmd_record_play)
    return root


def main() -> None:
    args = parser().parse_args()
    try:
        args.func(args)
    except OSError as exc:
        print(f"could not update progress file {args.file}: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
