---
name: track-vibe-session
description: Persist Vibe Coding sessions locally with a focus goal, mode, intended duration, workspace label, links, notes, completion outcome, and recent-session dashboard. Use when the user asks to start tracking, remember this session, save a video or post, add a coding note, show session history, finish the session, 记录这次 coding, 保存这个链接, 会话日志, 今天做了什么, or asks Codex to remember Vibe Coding progress across tasks.
---

# Track Vibe Session

Use the bundled deterministic script instead of recreating storage logic.

## Script

Resolve `scripts/session.py` relative to this SKILL.md and run it with Python 3. The default store is:

`~/.codex/codex-lounge/sessions.json`

The user may override it with `--file /absolute/path/sessions.json`.

## Commands

Start or return the active session:

```bash
python3 scripts/session.py start --focus "FOCUS" --mode deep-focus --minutes 45 --workspace "PROJECT"
```

Add a useful link:

```bash
python3 scripts/session.py add-link --url "URL" --title "TITLE" --kind youtube
```

Add a short local note:

```bash
python3 scripts/session.py note --text "NOTE"
```

Finish the active session:

```bash
python3 scripts/session.py finish --outcome completed --summary "SUMMARY"
```

Show the dashboard:

```bash
python3 scripts/session.py show
```

## Persistence Rules

- A request to track, remember, save, note, or finish authorizes the corresponding local write.
- Mention the storage path briefly on the first write in a conversation.
- Store only explicit session metadata and user-requested notes. Never store credentials, cookies, private messages, full feed contents, source files, or browser history.
- Use a short workspace label by default, not an absolute path.
- The script intentionally has no reset or delete command.
