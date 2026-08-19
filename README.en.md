<p align="center">
  <a href="README.md">简体中文</a> · <strong>English</strong>
</p>

# Codex Lounge

> Code, watch, explore, and take a break—without leaving Codex.

Codex Lounge is an open-source Codex plugin that turns the built-in Browser into a context-aware coding lounge. It helps you focus, learn, find relevant ideas on YouTube and X, prepare a release, and take deliberate, time-boxed breaks.

![Codex Lounge opening Arcade Break Mode in the built-in Browser](assets/arcade-break-mode.png)

## Five modes

| Mode | Best for | What Codex Lounge does |
| --- | --- | --- |
| `deep-focus` | Finishing one concrete task | Defines one observable outcome and minimizes media |
| `learn-and-build` | Learning through implementation | Finds one relevant video, then moves directly into the code |
| `explore` | Technical or product inspiration | Builds a concise YouTube + X radar with at most five items |
| `ship` | Preparing a contribution or release | Checks the diff, runs tests, and prepares docs and release notes |
| `break` | A short mental reset | Opens YouTube, X, free poker, or arcade games with a clear time boundary |

## What it can do

- Open YouTube videos, shows, channels, playlists, and focus music.
- Navigate X/Twitter home, profiles, your own posts, bookmarks, and lists.
- Build a repository-aware inspiration radar instead of an endless feed.
- Store explicit session goals, modes, durations, links, notes, and outcomes locally.
- Review tests, diffs, and documentation, then prepare release and launch drafts.
- Open free Texas Hold'em breaks plus wxiu arcade radar, roulette, challenges, achievements, and friend rooms.

## Try these prompts

```text
Start a 45-minute Vibe Coding session focused on finishing the login page
Find one YouTube tutorial relevant to this repository, then help me implement it
Build a concise inspiration radar from YouTube and X for this tech stack
Save this video to the current coding session
Run the checks, summarize the diff, and prepare release notes
Open a 15-minute free Texas Hold'em break with no real money
Spin the arcade roulette for two people with 20 minutes to play
```

## Install

You need a Codex/ChatGPT surface with plugin support and OpenAI's Browser plugin installed and enabled.

```bash
codex plugin marketplace add leiMizzou/codex-lounge --ref main
codex plugin add codex-lounge@codex-lounge
```

Start a new Codex task after installation. The first visit to YouTube, X, a poker site, or wxiu.com may require normal site permission or user-completed sign-in.

## Free poker and safety boundaries

Codex Lounge only considers sites whose live pages clearly describe a free or play-money experience with no cash value or real prize. It rechecks the visible landing page before use.

The plugin does not assist with real-money, cash, crypto, sweepstakes, or prize-bearing poker. It does not handle deposits, withdrawals, paid chips, value transfer, geographic evasion, or age-check bypasses. Sign-in, social posts, invitations, commits, pushes, merges, and releases are not performed merely because a draft was prepared.

## Local data

- Vibe Coding sessions: `~/.codex/codex-lounge/sessions.json`
- Arcade challenges and achievements: `~/.codex/codex-lounge/arcade-progress.json`

Only explicit session metadata is stored. Credentials, cookies, private messages, full feeds, source files, Browser history, and invitation links are excluded. The local tools intentionally provide no reset or delete command.

## Development

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The repository contains 12 skills, dependency-free local state tools, and regression coverage for session tracking, arcade progress, and free-poker boundaries.

## License

Plugin source and instructions are available under the [MIT License](LICENSE). Third-party websites, games, videos, posts, names, artwork, and trademarks are not covered by this license.
