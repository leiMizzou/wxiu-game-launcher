from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "plugins"
    / "wxiu-game-launcher"
    / "skills"
    / "wxiu-daily-achievements"
    / "scripts"
    / "progress.py"
)


class ProgressScriptTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.progress = Path(self.temporary.name) / "progress.json"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_script(self, *args: str) -> dict:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), "--file", str(self.progress), *args],
            check=True,
            capture_output=True,
            text=True,
        )
        return json.loads(completed.stdout)

    def test_daily_is_idempotent_and_completion_unlocks_badges(self) -> None:
        first = self.run_script(
            "daily",
            "--date",
            "2026-08-19",
            "--game",
            "King of Fighters '98",
            "--mode",
            "versus",
            "--challenge",
            "Win a best-of-three set with a different fighter each round.",
        )
        second = self.run_script(
            "daily",
            "--date",
            "2026-08-19",
            "--game",
            "Metal Slug X",
            "--mode",
            "coop",
            "--challenge",
            "This must not replace the first challenge.",
        )
        self.assertTrue(first["created"])
        self.assertFalse(second["created"])
        self.assertEqual(first["challenge"]["id"], second["challenge"]["id"])

        completed = self.run_script("complete", "--id", first["challenge"]["id"])
        badge_ids = {badge["id"] for badge in completed["newly_unlocked"]}
        self.assertEqual(completed["challenge"]["status"], "completed")
        self.assertIn("first-credit", badge_ids)
        self.assertIn("challenge-rookie", badge_ids)

    def test_records_play_and_tracks_unique_games(self) -> None:
        first = self.run_script(
            "record-play",
            "--date",
            "2026-08-18",
            "--game",
            "Double Dragon",
            "--mode",
            "coop",
        )
        second = self.run_script(
            "record-play",
            "--date",
            "2026-08-19",
            "--game",
            "King of Fighters '97",
            "--mode",
            "versus",
        )
        self.assertTrue(first["recorded"])
        self.assertEqual(second["summary"]["stats"]["plays"], 2)
        self.assertEqual(second["summary"]["stats"]["unique_games"], 2)
        self.assertEqual(second["summary"]["stats"]["current_streak"], 2)


if __name__ == "__main__":
    unittest.main()
