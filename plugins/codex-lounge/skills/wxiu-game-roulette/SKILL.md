---
name: wxiu-game-roulette
description: Pick a time-boxed wxiu.com arcade break from live lobby choices using mood, available time, party size, genre, activity, and exclusions. Use when the user asks what to play, wants a surprise or reroll, says 转一下轮盘, 游戏轮盘, 随便挑一个, 我只有十分钟, 想轻松玩, 不要格斗, or wants Codex to choose and open one game.
---

# Wxiu Game Roulette

Choose one game decisively from the current wxiu.com lobby, explain the pick, and optionally open it.

## Workflow

1. Extract any constraints: minutes available, solo/co-op/versus, mood, genre, active-room requirement, and excluded games.
2. Use the installed Browser plugin's in-app Browser to inspect `https://wxiu.com/`. Reuse an open wxiu.com tab when practical.
3. Build candidates only from current links whose href begins with `/playroom/`. Read card names, player counts, and room counts in either Chinese or English.
4. Remove explicit exclusions and incompatible party modes. Prefer active rooms when the user wants multiplayer; otherwise keep quiet games eligible.
5. Choose one primary game. When several candidates fit equally, vary the choice rather than repeatedly selecting the first DOM item.
6. Return:
   - the selected game;
   - a short reason tied to the user's constraints;
   - the live player/room snapshot when available;
   - one optional wild-card alternative.
7. If the user asked to play now, navigate to the verified `/playroom/` link and leave the tab visible. Otherwise offer `打开它` or one reroll.

## Selection guidance

- `10–15 minutes`: prefer quick versus games or a single-stage challenge.
- `20–40 minutes`: allow cooperative progression and longer sessions.
- `轻松` or `casual`: favor cooperative or low-pressure solo play over active competitive rooms.
- `热闹` or `multiplayer`: rank by current players, then rooms.
- `冷门` or `surprise me`: prefer a compatible low-activity title not already offered in the conversation.
- If no candidates satisfy all constraints, name the conflict and relax exactly one constraint rather than inventing a game.

Do not join a player's room, spend a coin, start a match, or sign in unless the user separately asks.
