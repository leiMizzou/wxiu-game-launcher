---
name: wxiu-friend-invite
description: Help the user start a time-boxed wxiu.com arcade break for friends, obtain the site's shareable invitation link, and draft a concise invite without sending it. Use when the user asks to play with friends, open a co-op game, create a room or invite, 发给朋友, 好友开黑, 双人游戏, 联机, 邀请链接, or 开房.
---

# Wxiu Friend Invite

Prepare a friend game session in the built-in Browser and hand the invitation back to the user.

## Workflow

1. Use the installed `Browser` plugin's in-app-browser capability. Reuse the current `wxiu.com` tab when practical; otherwise open `https://wxiu.com/`.
2. If the game is missing, ask one short question for the title. If it is supplied, proceed without reconfirming the choice.
3. Use a fresh DOM snapshot to locate the site's visible invite control. It may be labeled `开个游戏发给朋友`, `Start a game and send it to a friend`, or include the stable visible marker `INVITE`. Use semantic page controls rather than guessed coordinates.
4. After every click or navigation, inspect the resulting visible state before continuing. Select the exact requested game; do not substitute a similarly named title.
5. Stop before any login, purchase, personal-data entry, or action that would send a message to another person.
6. When the site displays a shareable `wxiu.com` invitation or room URL, verify its domain, copy it to the in-app Browser clipboard, and keep the relevant page visible.
7. Return the link plus a short, editable invitation message containing the exact game name. Never claim that the invitation was sent.

## Invite message style

Use a casual template such as: `来一局《{游戏名}》？点这里直接进房：{链接}`. Keep it short and do not add contact details, tracking parameters, or claims about who is online.

## Safety and failure handling

- Creating an invitation is authorized when the user explicitly asks to invite friends, create a room, or open a co-op session. Follow any Browser confirmation that appears at the point of action.
- Writing the link to the local clipboard is allowed; sending or posting it is a separate action and requires the user's explicit request and normal confirmation flow.
- If no shareable link appears, report where the workflow stopped and leave the tab open. Do not invent a room code or URL.
- If Browser is unavailable, explain that it must be installed or enabled. Do not silently use Chrome, another external browser, or web search.
