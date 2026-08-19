#!/usr/bin/env python3
"""Dependency-free structural checks for Codex Lounge."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "codex-lounge"
PLUGIN = ROOT / "plugins" / PLUGIN_NAME
MANIFEST = PLUGIN / ".codex-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
SKILLS = PLUGIN / "skills"
PROGRESS_SCRIPT = SKILLS / "wxiu-daily-achievements" / "scripts" / "progress.py"
SESSION_SCRIPT = SKILLS / "track-vibe-session" / "scripts" / "session.py"
README_ZH = ROOT / "README.md"
README_EN = ROOT / "README.en.md"


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"validation failed: {message}")


def main() -> None:
    manifest = load_json(MANIFEST)
    marketplace = load_json(MARKETPLACE)

    require(manifest.get("name") == PLUGIN_NAME, "unexpected plugin name")
    require(re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", manifest.get("version", "")) is not None, "version is not semver-like")
    require(manifest.get("skills") == "./skills/", "skills path must be ./skills/")
    require(manifest.get("license") == "MIT", "manifest license must be MIT")
    require((ROOT / "LICENSE").is_file(), "LICENSE is missing")

    require(README_ZH.is_file(), "Chinese README is missing")
    require(README_EN.is_file(), "English README is missing")
    require('href="README.en.md"' in README_ZH.read_text(encoding="utf-8"), "Chinese README has no English switch")
    require('href="README.md"' in README_EN.read_text(encoding="utf-8"), "English README has no Chinese switch")

    entries = [entry for entry in marketplace.get("plugins", []) if entry.get("name") == PLUGIN_NAME]
    require(len(entries) == 1, "marketplace must contain exactly one plugin entry")
    entry = entries[0]
    require(entry.get("source", {}).get("path") == f"./plugins/{PLUGIN_NAME}", "marketplace source path is incorrect")
    require(entry.get("policy", {}).get("installation") == "AVAILABLE", "installation policy must be AVAILABLE")
    require(entry.get("policy", {}).get("authentication") == "ON_INSTALL", "authentication policy must be ON_INSTALL")

    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    require(len(skill_files) == 12, "expected exactly twelve skills")
    skill_names: set[str] = set()
    for skill_file in skill_files:
        body = skill_file.read_text(encoding="utf-8")
        require(body.startswith("---\n"), f"{skill_file} has no front matter")
        front_matter = body.split("---", 2)[1]
        name_match = re.search(r"^name:\s*(\S+)", front_matter, re.MULTILINE)
        require(name_match is not None, f"{skill_file} has no name")
        skill_name = name_match.group(1)
        require(skill_name == skill_file.parent.name, f"{skill_file} name does not match its directory")
        require(skill_name not in skill_names, f"duplicate skill name: {skill_name}")
        skill_names.add(skill_name)
        require(re.search(r"^description:\s*\S+", front_matter, re.MULTILINE) is not None, f"{skill_file} has no description")
        require("[TODO:" not in body, f"{skill_file} contains a TODO placeholder")

    for script in (PROGRESS_SCRIPT, SESSION_SCRIPT):
        require(script.is_file(), f"required local state script is missing: {script}")
        script_body = script.read_text(encoding="utf-8")
        require("add_parser(\"reset\"" not in script_body, f"{script} must not expose reset behavior")
        require("add_parser(\"delete\"" not in script_body, f"{script} must not expose delete behavior")

    for metadata in sorted(SKILLS.glob("*/agents/openai.yaml")):
        body = metadata.read_text(encoding="utf-8")
        skill_name = metadata.parents[1].name
        require(f"${skill_name}" in body, f"{metadata} default prompt must mention ${skill_name}")
        require("[TODO:" not in body, f"{metadata} contains a TODO placeholder")

    print(f"validated {manifest['name']} {manifest['version']} with {len(skill_files)} skills")


if __name__ == "__main__":
    main()
