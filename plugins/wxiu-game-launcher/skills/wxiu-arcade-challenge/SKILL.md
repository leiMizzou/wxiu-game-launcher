---
name: wxiu-arcade-challenge
description: Generate a playful random or themed arcade challenge for games available on wxiu.com, optionally using the live lobby and opening the chosen game. Use when the user asks for a random game, daily challenge, arcade challenge, challenge mode, 随机一个, 今日挑战, 街机挑战, or 不知道玩什么.
---

# Wxiu Arcade Challenge

Create a short, achievable arcade challenge that makes choosing a game fun.

## Workflow

1. If the user asks for a currently available or active game, use the installed `Browser` plugin's in-app Browser to inspect the live `https://wxiu.com/` homepage before choosing. Otherwise, choose from games visible in the current lobby when available.
2. Respect constraints such as solo/co-op, genre, player count, difficulty, and available time.
3. Produce exactly one primary challenge with:
   - game name;
   - mode: solo, co-op, or versus;
   - one clear restriction;
   - one measurable success condition;
   - one optional bonus objective.
4. Keep the challenge practical for a single session. Do not claim knowledge of unsupported mechanics, hidden content, or a game's exact scoring system unless visible or reliably known.
5. Offer one reroll. If the user asks to begin, open the corresponding game room with the in-app Browser and leave control with the user.

## Challenge patterns

- Survival: finish a stage without using a continue.
- Character variety: use a character the player does not normally choose.
- Resource restraint: clear a stage while limiting special attacks or pickups.
- Co-op teamwork: clear a stage with each player taking a distinct role.
- Versus set: best-of-three with a different character each round.
- Speed round: reach a visible milestone within the user's time limit.

Avoid gambling, payment, drinking, humiliation, dangerous real-world actions, or challenges that require harassment or disruption of other players.
