---
name: ship-vibe-project
description: Close a Vibe Coding session by reviewing the repository, running relevant checks, summarizing the diff, updating documentation, and preparing GitHub release notes or social launch drafts. Use when the user says 收尾, ship it, 准备发布, 上线前检查, 写 release notes, 整理这次改动, 发 GitHub, 宣传项目, or wants Codex to turn the current coding work into a verifiable release.
---

# Ship Vibe Project

Turn finished coding work into a release-ready handoff with evidence.

## Workflow

1. Inspect branch, worktree status, diff, repository instructions, and existing validation commands.
2. Separate intended changes from unrelated user work before staging anything.
3. Run checks proportionate to risk. Report exact commands and failures without hiding them.
4. Produce a compact ship packet: what changed and why, user-visible impact, validation evidence, known limitations, and installation or upgrade notes.
5. Update repository documentation or changelog only when implementation or release preparation is requested.
6. Draft platform-native GitHub release notes and X posts when requested. Do not publish, push, merge, tag, or post without explicit authorization for that external action.
7. Use `$track-vibe-session` to finish a tracked session with its outcome and summary.

## Completion Standard

- A passing command is evidence only for the scope it covers.
- Link to the exact PR, release, deployment, or post after publication.
- If something remains blocked, state the next concrete action instead of calling the project shipped.
