---
name: recommend-wxiu-games
description: Inspect the live wxiu.com arcade lobby and recommend games based on current player and room activity or the user's preferred genre. Use when the user asks what is active, what to play, which games have people online, for recommendations, or says phrases such as 推荐游戏, 现在玩什么, 哪个房间有人, or 谁最多.
---

# Recommend Wxiu Games

Use the live `wxiu.com` lobby rather than memory to recommend games that are playable now.

## Workflow

1. Use the installed `Browser` plugin's in-app-browser capability. Reuse the current `wxiu.com` tab when practical; otherwise open `https://wxiu.com/`.
2. Wait until the homepage game cards are rendered, then collect a fresh DOM snapshot.
3. Identify game cards by links whose URLs begin with `/playroom/`. Read the player and room counts associated with those cards. Support both Chinese forms such as `人 · 房` and English forms such as `players · rooms`.
4. Do not use the global online sidebar or chat participants as a substitute for per-game activity.
5. Apply the user's requested filters, such as fighting, cooperative beat-'em-up, short session, solo-friendly, or currently active. If no preference was given, rank primarily by players, then rooms, while keeping some genre variety.
6. Return three concise recommendations with game name, current players/rooms, and a one-line reason. Label live counts as a snapshot that may change.
7. If the user says to choose or open one, navigate to the selected game's `/playroom/` link and leave the tab visible and interactive.

## Ranking guidance

- Prefer a game with active players over an empty room when the user wants multiplayer.
- For two-player cooperation, favor the site's cooperative progression section over head-to-head fighting games.
- For quick competitive play, favor active fighting games.
- When all suitable games are empty, say so plainly and recommend a good solo option rather than implying that players are present.
- Never fabricate ratings, difficulty, popularity, or live counts that are not visible on the current page.

## Safety

- Do not join a specific player's room, start a match, spend a coin, sign in, or share data unless the user separately asks.
- If Browser is unavailable, explain that it must be installed or enabled. Do not silently substitute web search or an external browser.
