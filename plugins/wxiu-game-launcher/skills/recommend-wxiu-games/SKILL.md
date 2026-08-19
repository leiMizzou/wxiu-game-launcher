---
name: recommend-wxiu-games
description: Build a live wxiu.com arcade radar from current per-game player and room counts, then recommend or open games by activity and genre. Use when the user asks what is active, what to play, which games have people online, for a lobby scan or radar, or says phrases such as 街机雷达, 扫描大厅, 推荐游戏, 现在玩什么, 哪个房间有人, 谁最多, or 当前最热.
---

# Wxiu Arcade Radar

Use the live `wxiu.com` lobby rather than memory to produce a compact activity radar and recommendations.

## Workflow

1. Use the installed `Browser` plugin's in-app-browser capability. Reuse the current `wxiu.com` tab when practical; otherwise open `https://wxiu.com/`.
2. Wait until the homepage game cards are rendered, then collect a fresh DOM snapshot.
3. Identify game cards by links whose URLs begin with `/playroom/`. Read the player and room counts associated with those cards. Support both Chinese forms such as `人 · 房` and English forms such as `players · rooms`.
4. Do not use the global online sidebar or chat participants as a substitute for per-game activity.
5. Deduplicate carousel and grid links by `/playroom/` href. Keep the most informative card text for each game.
6. Classify the snapshot into the smallest useful set of lanes:
   - `🔥 最热`: highest current player counts;
   - `🤝 合作优先`: active cooperative progression titles;
   - `⚔️ 对战优先`: active fighting or versus titles;
   - `🌙 安静选择`: zero-player games that still fit solo or low-pressure play.
7. Return at most three games per requested lane with game name, current players/rooms, and one short reason. Include the snapshot time and state that counts may change.
8. End with one decisive `现在就玩` recommendation. If the user asks to open it, navigate to its verified `/playroom/` link and leave the tab visible.

## Ranking guidance

- Prefer a game with active players over an empty room when the user wants multiplayer.
- For two-player cooperation, favor the site's cooperative progression section over head-to-head fighting games.
- For quick competitive play, favor active fighting games.
- When all suitable games are empty, say so plainly and recommend a good solo option rather than implying that players are present.
- Do not classify a genre solely from a translated title. Use the site's visible section when available; otherwise label the genre as uncertain.
- Never fabricate ratings, difficulty, popularity, or live counts that are not visible on the current page.

## Safety

- Do not join a specific player's room, start a match, spend a coin, sign in, or share data unless the user separately asks.
- If Browser is unavailable, explain that it must be installed or enabled. Do not silently substitute web search or an external browser.
