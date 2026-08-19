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
    / "vibe-coding-companion"
    / "skills"
    / "track-vibe-session"
    / "scripts"
    / "session.py"
)


class SessionScriptTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.store = Path(self.temporary.name) / "sessions.json"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_script(self, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--file", str(self.store), *args],
            check=check,
            capture_output=True,
            text=True,
        )

    def result(self, *args: str) -> dict:
        return json.loads(self.run_script(*args).stdout)

    def test_start_is_idempotent_and_finish_updates_dashboard(self) -> None:
        first = self.result(
            "start",
            "--focus",
            "Build the Vibe Coding companion",
            "--mode",
            "deep-focus",
            "--minutes",
            "45",
            "--workspace",
            "vibe-coding-companion",
        )
        second = self.result(
            "start",
            "--focus",
            "This should not replace the active session",
            "--mode",
            "explore",
            "--minutes",
            "20",
        )
        self.assertTrue(first["created"])
        self.assertFalse(second["created"])
        self.assertEqual(first["session"]["id"], second["session"]["id"])

        finished = self.result(
            "finish",
            "--outcome",
            "completed",
            "--summary",
            "Implemented and validated the session workflow.",
        )
        self.assertTrue(finished["finished"])
        self.assertEqual(finished["session"]["status"], "finished")
        self.assertEqual(finished["dashboard"]["stats"]["finished"], 1)
        self.assertIsNone(finished["dashboard"]["active"])

    def test_adds_links_and_notes_and_rejects_unsafe_urls(self) -> None:
        self.result(
            "start",
            "--focus",
            "Learn a new framework",
            "--mode",
            "learn-and-build",
            "--minutes",
            "30",
        )
        link = self.result(
            "add-link",
            "--url",
            "https://www.youtube.com/watch?v=example",
            "--title",
            "Framework tutorial",
            "--kind",
            "youtube",
        )
        duplicate = self.result(
            "add-link",
            "--url",
            "https://www.youtube.com/watch?v=example",
            "--title",
            "Duplicate",
            "--kind",
            "youtube",
        )
        note = self.result("note", "--text", "Try the smaller component boundary first.")
        self.assertTrue(link["added"])
        self.assertFalse(duplicate["added"])
        self.assertEqual(len(note["session"]["notes"]), 1)

        rejected = self.run_script(
            "add-link",
            "--url",
            "file:///tmp/private.txt",
            "--title",
            "Private file",
            "--kind",
            "other",
            check=False,
        )
        self.assertNotEqual(rejected.returncode, 0)
        self.assertIn("absolute http(s) URL", rejected.stderr)


if __name__ == "__main__":
    unittest.main()
