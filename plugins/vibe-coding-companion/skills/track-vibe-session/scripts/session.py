#!/usr/bin/env python3
"""Persist local Vibe Coding sessions without external dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


SCHEMA_VERSION = 1
DEFAULT_FILE = Path.home() / ".codex" / "vibe-coding-companion" / "sessions.json"
MODES = ("deep-focus", "learn-and-build", "explore", "ship", "break")
OUTCOMES = ("completed", "partial", "blocked", "abandoned")
LINK_KINDS = ("youtube", "x", "docs", "repo", "other")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def empty_data() -> dict[str, Any]:
    return {"version": SCHEMA_VERSION, "created_at": utc_now(), "sessions": []}


def clean_text(value: str, field: str, limit: int = 500) -> str:
    cleaned = " ".join(value.strip().split())
    if not cleaned:
        raise SystemExit(f"{field} must not be empty")
    if len(cleaned) > limit:
        raise SystemExit(f"{field} is too long")
    return cleaned


def clean_url(value: str) -> str:
    cleaned = value.strip()
    parsed = urlparse(cleaned)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise SystemExit("url must be an absolute http(s) URL")
    if len(cleaned) > 2000:
        raise SystemExit("url is too long")
    return cleaned


def load_data(path: Path) -> dict[str, Any]:
    if not path.exists():
        return empty_data()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"could not read session file {path}: {exc}") from exc
    if data.get("version") != SCHEMA_VERSION or not isinstance(data.get("sessions"), list):
        raise SystemExit(f"invalid or unsupported session file {path}")
    return data


def save_data(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def active_session(data: dict[str, Any]) -> dict[str, Any] | None:
    return next((item for item in reversed(data["sessions"]) if item.get("status") == "active"), None)


def session_id(focus: str, started_at: str) -> str:
    stamp = started_at.replace("-", "").replace(":", "")[:15]
    digest = hashlib.sha256(f"{focus}|{started_at}".encode()).hexdigest()[:6]
    return f"vibe-{stamp}-{digest}"


def summarize(data: dict[str, Any], path: Path) -> dict[str, Any]:
    sessions = data["sessions"]
    active = active_session(data)
    completed = [item for item in sessions if item.get("status") == "finished"]
    return {
        "storage": str(path),
        "stats": {
            "sessions": len(sessions),
            "finished": len(completed),
            "total_links": sum(len(item.get("links", [])) for item in sessions),
            "total_notes": sum(len(item.get("notes", [])) for item in sessions),
            "planned_minutes": sum(int(item.get("minutes", 0)) for item in sessions),
        },
        "active": active,
        "recent": list(reversed(sessions[-5:])),
    }


def emit(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def require_active(data: dict[str, Any]) -> dict[str, Any]:
    item = active_session(data)
    if item is None:
        raise SystemExit("no active Vibe Coding session")
    return item


def cmd_start(args: argparse.Namespace) -> None:
    data = load_data(args.file)
    current = active_session(data)
    if current:
        emit({"created": False, "session": current, "dashboard": summarize(data, args.file)})
        return
    focus = clean_text(args.focus, "focus")
    started_at = utc_now()
    item = {
        "id": session_id(focus, started_at),
        "status": "active",
        "focus": focus,
        "mode": args.mode,
        "minutes": args.minutes,
        "workspace": clean_text(args.workspace, "workspace", 120) if args.workspace else None,
        "started_at": started_at,
        "finished_at": None,
        "outcome": None,
        "summary": None,
        "links": [],
        "notes": [],
    }
    data["sessions"].append(item)
    save_data(args.file, data)
    emit({"created": True, "session": item, "dashboard": summarize(data, args.file)})


def cmd_add_link(args: argparse.Namespace) -> None:
    data = load_data(args.file)
    item = require_active(data)
    url = clean_url(args.url)
    existing = next((link for link in item["links"] if link["url"] == url), None)
    if existing:
        emit({"added": False, "link": existing, "session": item})
        return
    link = {
        "url": url,
        "title": clean_text(args.title, "title", 300),
        "kind": args.kind,
        "added_at": utc_now(),
    }
    item["links"].append(link)
    save_data(args.file, data)
    emit({"added": True, "link": link, "session": item})


def cmd_note(args: argparse.Namespace) -> None:
    data = load_data(args.file)
    item = require_active(data)
    note = {"text": clean_text(args.text, "text", 1000), "added_at": utc_now()}
    item["notes"].append(note)
    save_data(args.file, data)
    emit({"added": True, "note": note, "session": item})


def cmd_finish(args: argparse.Namespace) -> None:
    data = load_data(args.file)
    item = require_active(data)
    item["status"] = "finished"
    item["finished_at"] = utc_now()
    item["outcome"] = args.outcome
    item["summary"] = clean_text(args.summary, "summary", 1000)
    save_data(args.file, data)
    emit({"finished": True, "session": item, "dashboard": summarize(data, args.file)})


def cmd_show(args: argparse.Namespace) -> None:
    emit(summarize(load_data(args.file), args.file))


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    root.add_argument(
        "--file",
        type=Path,
        default=Path(os.environ.get("VIBE_SESSION_FILE", DEFAULT_FILE)),
        help="session JSON path",
    )
    commands = root.add_subparsers(dest="command", required=True)

    start = commands.add_parser("start", help="start or return the active session")
    start.add_argument("--focus", required=True)
    start.add_argument("--mode", choices=MODES, required=True)
    start.add_argument("--minutes", type=int, choices=range(5, 481), metavar="5..480", required=True)
    start.add_argument("--workspace")
    start.set_defaults(func=cmd_start)

    link = commands.add_parser("add-link", help="add a link to the active session")
    link.add_argument("--url", required=True)
    link.add_argument("--title", required=True)
    link.add_argument("--kind", choices=LINK_KINDS, required=True)
    link.set_defaults(func=cmd_add_link)

    note = commands.add_parser("note", help="add a note to the active session")
    note.add_argument("--text", required=True)
    note.set_defaults(func=cmd_note)

    finish = commands.add_parser("finish", help="finish the active session")
    finish.add_argument("--outcome", choices=OUTCOMES, required=True)
    finish.add_argument("--summary", required=True)
    finish.set_defaults(func=cmd_finish)

    show = commands.add_parser("show", help="show the session dashboard")
    show.set_defaults(func=cmd_show)
    return root


def main() -> None:
    args = parser().parse_args()
    try:
        args.func(args)
    except OSError as exc:
        print(f"could not update session file {args.file}: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
