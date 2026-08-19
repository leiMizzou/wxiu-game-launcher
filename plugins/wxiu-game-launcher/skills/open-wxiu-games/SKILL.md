---
name: open-wxiu-games
description: Open the wxiu.com portal or go directly to a requested arcade game's room in Codex's built-in Browser. Use when the user asks to open, launch, visit, reload, or play wxiu, 微秀游戏, 微秀游戏大厅, wxiu.com, or a named game such as 拳皇, 合金弹头, 恐龙快打, 三国战纪, 侍魂, 街霸, or 圆桌武士.
---

# Open Wxiu Games

Open `https://wxiu.com/` or a requested game's room in Codex's built-in Browser and leave the resulting tab visible and interactive for the user.

## Required workflow

1. Use the installed `Browser` plugin's in-app-browser capability. The user is explicitly requesting the in-app Browser for this workflow.
2. Reuse an existing visible `wxiu.com` tab when practical. Otherwise navigate to the canonical HTTPS URL `https://wxiu.com/`. Do not replace it with web search, Chrome, another external browser, a copied page, an iframe, or a text-only summary.
3. If the user names a game, resolve common aliases, then use a fresh DOM snapshot to find the matching link whose URL begins with `/playroom/`. The site may render in Chinese or English, so match the verified route slug, image alt text, accessible name, and visible title rather than depending on only one language. Prefer the site's current link over a guessed URL.
4. Open the matching game-room link. Do not click a specific player's room, start a match, spend a coin, or join another player unless the user separately asks.
5. If the requested title is not on the homepage, open `想玩片库` and use its visible search or browsing controls. Do not invent an unavailable game or silently choose a similarly named title.
6. Wait for an interactive rendered state and verify that the final visible page belongs to `wxiu.com` or a domain reached through the site's own navigation.
7. Keep the Browser tab open and visible. Report the final game name, page title, and whether the room appears ready. Keep the response brief.

## Common aliases and verified lobby routes

- `拳皇98`, `KOF98`, `King of Fighters '98` → `拳皇 98`, slug `kof98`
- `拳皇97`, `KOF97`, `King of Fighters '97` → `拳皇 97`, slug `kof97`
- `拳皇2002`, `KOF2002` → `拳皇 2002`, slug `kof2002`
- `合金弹头X`, `Metal Slug X` → `合金弹头 X`, slug `mslugx`
- `合金弹头3`, `Metal Slug 3` → `合金弹头 3`, slug `mslug3`
- `街霸2`, `Street Fighter II` → `街头霸王 II`, slug `sf2`
- `街霸3`, `三度冲击`, `SF III 3rd Strike` → `街头霸王 III 3rd Strike`, slug `sfiii3`
- `三国`, `三国战纪` → `三国战纪`, slug `kov`
- `恐龙`, `恐龙快打` → `恐龙快打`, slug `dino`
- `圆桌`, `圆桌武士` → `圆桌武士`, slug `knights`
- `双截龙`, `Double Dragon` → `双截龙`, slug `doubledr`
- `侍魂2`, `Samurai Shodown II` → `侍魂 II`, slug `samsho2`
- `名将` means `名将`; `名将之王` is a different game and must not be substituted.

Treat slugs as disambiguation hints, not unconditional URLs. Before navigating, verify that the current lobby contains an anchor with the corresponding `/playroom/{slug}` href. If it does not, fall back to the site's visible library controls.

## Interaction rules

- If the built-in Browser asks for site permission, pause for the normal Codex permission flow. Never try to bypass it.
- If the Browser plugin is unavailable or disabled, state that `Browser` must be installed or enabled from the Plugins tab, then stop. Do not silently fall back to another browser.
- Do not sign in, enter personal data, make purchases, or accept payment-related prompts unless the user separately and explicitly asks.
- Do not start a specific game or click through age, account, purchase, or promotional dialogs unless the user asks for that exact action.
- If the site redirects, preserve the user's control and do not navigate away from the site's own game flow.
- Respect the site's requirement that players legally own the corresponding original game copy. Do not help bypass site or game restrictions.
