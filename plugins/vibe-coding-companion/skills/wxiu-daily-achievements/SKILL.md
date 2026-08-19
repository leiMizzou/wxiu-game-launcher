---
name: wxiu-daily-achievements
description: Create, save, complete, and summarize daily wxiu.com arcade-break challenges with local play history, streaks, and achievement badges. Use when the user asks for 今日挑战, 每日挑战, 打卡, 完成挑战, 我的战绩, 连续天数, 成就, 徽章, 最近玩了什么, or asks Codex to remember arcade breaks across tasks.
---

# Wxiu Daily Challenges and Achievements

Persist arcade progress with the bundled deterministic script. Do not recreate its storage logic ad hoc.

## Script

Resolve `scripts/progress.py` relative to this SKILL.md and run it with Python 3. It stores only game progress at:

`~/.codex/vibe-coding-companion/arcade-progress.json`

The user may override the location with `--file /absolute/path/progress.json`. Never store credentials, invitation links, chat text, or browser data.

## Workflows

### Create today's challenge

1. Generate one practical challenge using the `wxiu-arcade-challenge` workflow and a game confirmed to exist on wxiu.com.
2. Save it idempotently:

```bash
python3 scripts/progress.py daily --game "GAME" --mode solo --challenge "CHALLENGE"
```

3. Return the challenge ID, rules, success condition, and current streak. Re-running on the same date returns the existing daily challenge instead of replacing it.

### Complete a challenge

1. Run `show` to identify the pending challenge. If more than one could apply, ask which challenge was completed.
2. Record completion:

```bash
python3 scripts/progress.py complete --id "CHALLENGE_ID" --note "OPTIONAL NOTE"
```

3. Report newly unlocked achievements separately from previously unlocked ones.

### Record ordinary play

```bash
python3 scripts/progress.py record-play --game "GAME" --mode coop --note "OPTIONAL NOTE"
```

Use this only when the user asks to remember or record the session.

### Show dashboard

```bash
python3 scripts/progress.py show
```

Summarize total sessions, unique games, completed challenges, current streak, today's challenge, and unlocked badges. Keep the raw JSON out of the response unless requested.

## Persistence rules

- A request to create/save a daily challenge, record play, complete a challenge, or track achievements authorizes the corresponding local write.
- Mention the storage path briefly on the first write in a conversation.
- Do not reset, erase, or rewrite history. The bundled script intentionally has no reset command.
- If the default path is not writable, offer `--file` in a user-selected writable location instead of silently discarding progress.
