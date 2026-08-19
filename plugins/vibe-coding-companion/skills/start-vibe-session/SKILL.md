---
name: start-vibe-session
description: Start a context-aware Vibe Coding session by inspecting the current workspace, choosing a focus mode, creating a small execution plan, optionally opening matching media, and recording the session locally. Use when the user says 开始写代码, 开个 vibe coding, 进入状态, 专注一会儿, 陪我写代码, start a coding session, focus mode, learning session, exploration mode, or ship mode.
---

# Start Vibe Session

Turn the current Codex task into a deliberate coding session instead of a loose collection of actions.

## Workflow

1. Inspect the workspace read-only before asking questions: repository root, branch, concise `git status`, primary languages, package manifests, likely validation commands, and the user's stated objective.
2. Infer a session mode. Ask one short question only when the mode or intended outcome materially changes the workflow:
   - `deep-focus`: one coding outcome, minimal media, no feed browsing;
   - `learn-and-build`: one relevant tutorial or talk followed by implementation;
   - `explore`: a small inspiration radar across YouTube and X before coding;
   - `ship`: validation, diff review, documentation, and launch preparation;
   - `break`: a time-boxed arcade, free poker, YouTube, or X intermission.
3. Produce a three-part kickoff: `目标` with one observable outcome, `节奏` with a short sequence of work blocks, and `氛围` with an optional media or break choice.
4. Use `$track-vibe-session` to save the session when the user asks to remember it or when persistence is part of the request.
5. Use `$open-vibe-media`, `$vibe-inspiration-radar`, `$open-free-poker`, or the wxiu skills only for the selected mode.
6. Return to repository work after media navigation. Opening content is supporting work, not the main deliverable.

## Guardrails

- Never hide a dirty worktree or imply unrelated changes belong to the session.
- Do not start media, games, posts, commits, pushes, or public actions unless requested.
- Prefer one strong media choice over many distracting tabs.
- Keep break modes explicitly time-boxed and easy to exit.
