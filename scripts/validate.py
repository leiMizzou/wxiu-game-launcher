#!/usr/bin/env python3
"""Dependency-free structural checks for the wxiu-game-launcher repository."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "wxiu-game-launcher"
MANIFEST = PLUGIN / ".codex-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
SKILLS = PLUGIN / "skills"
PROGRESS_SCRIPT = SKILLS / "wxiu-daily-achievements" / "scripts" / "progress.py"


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"validation failed: {message}")


def main() -> None:
    manifest = load_json(MANIFEST)
    marketplace = load_json(MARKETPLACE)

    require(manifest.get("name") == "wxiu-game-launcher", "unexpected plugin name")
    require(re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", manifest.get("version", "")) is not None, "version is not semver-like")
    require(manifest.get("skills") == "./skills/", "skills path must be ./skills/")
    require(manifest.get("license") == "MIT", "manifest license must be MIT")
    require((ROOT / "LICENSE").is_file(), "LICENSE is missing")

    entries = [entry for entry in marketplace.get("plugins", []) if entry.get("name") == "wxiu-game-launcher"]
    require(len(entries) == 1, "marketplace must contain exactly one plugin entry")
    entry = entries[0]
    require(entry.get("source", {}).get("path") == "./plugins/wxiu-game-launcher", "marketplace source path is incorrect")
    require(entry.get("policy", {}).get("installation") == "AVAILABLE", "installation policy must be AVAILABLE")
    require(entry.get("policy", {}).get("authentication") == "ON_INSTALL", "authentication policy must be ON_INSTALL")

    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    require(len(skill_files) == 6, "expected exactly six skills")
    for skill_file in skill_files:
        text = skill_file.read_text(encoding="utf-8")
        require(text.startswith("---\n"), f"{skill_file} has no front matter")
        front_matter = text.split("---", 2)[1]
        require(re.search(r"^name:\s*\S+", front_matter, re.MULTILINE) is not None, f"{skill_file} has no name")
        require(re.search(r"^description:\s*\S+", front_matter, re.MULTILINE) is not None, f"{skill_file} has no description")
        require("[TODO:" not in text, f"{skill_file} contains a TODO placeholder")

    require(PROGRESS_SCRIPT.is_file(), "daily achievement progress script is missing")
    require("add_parser(\"reset\"" not in PROGRESS_SCRIPT.read_text(encoding="utf-8"), "progress script must not expose destructive reset behavior")

    for metadata in sorted(SKILLS.glob("*/agents/openai.yaml")):
        text = metadata.read_text(encoding="utf-8")
        require("$wxiu-" in text, f"{metadata} default prompt must mention its skill")
        require("[TODO:" not in text, f"{metadata} contains a TODO placeholder")

    print(f"validated {manifest['name']} {manifest['version']} with {len(skill_files)} skills")


if __name__ == "__main__":
    main()
