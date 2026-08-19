from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (
    ROOT
    / "plugins"
    / "vibe-coding-companion"
    / "skills"
    / "open-free-poker"
    / "SKILL.md"
)


class FreePokerPolicyTest(unittest.TestCase):
    def test_documents_free_candidates_and_hard_boundaries(self) -> None:
        body = SKILL.read_text(encoding="utf-8")
        for url in (
            "https://www.pokernow.com/",
            "https://flophauspoker.com/",
            "https://www.pokr.live/",
        ):
            self.assertIn(url, body)

        for boundary in (
            "real-money",
            "cash",
            "crypto",
            "sweepstakes",
            "deposit",
            "withdraw",
            "geographic restrictions",
            "age checks",
        ):
            self.assertIn(boundary, body)

    def test_requires_live_recheck_before_use(self) -> None:
        body = SKILL.read_text(encoding="utf-8")
        self.assertIn("Re-check the live landing page", body)
        self.assertIn("Verify visible language", body)


if __name__ == "__main__":
    unittest.main()
