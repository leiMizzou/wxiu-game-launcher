# Codex Lounge

[中文](#中文说明) · [English](#english)

**Code, watch, explore, and take a break—without leaving Codex.**

An open-source plugin that turns the built-in Browser into a context-aware coding lounge: focus sessions, relevant YouTube and X inspiration, local progress, release preparation, and deliberate breaks.

![Codex Lounge opening an arcade break inside Codex](assets/arcade-break-mode.png)

## 中文说明

### 它做什么

Codex Lounge 不只是一个游戏启动器。它会先看当前项目，再按你的目标进入五种模式：

- `deep-focus`：只围绕一个可验证的编码结果工作，尽量不打开媒体。
- `learn-and-build`：找一个与项目相关的 YouTube 教程或节目，看完关键内容后立即实现。
- `explore`：从 YouTube 和 X/Twitter 做一份不超过 5 条的项目灵感雷达。
- `ship`：检查 diff、运行测试、整理文档、release notes 和宣传文案。
- `break`：开启有时间上限的 YouTube、X、免费德州扑克或街机休息。

它还可以把目标、模式、时长、保存的链接、笔记和结果记录在本机，方便下一次 Codex 任务继续。

### 可以这样说

```text
开始一个 45 分钟的 Vibe Coding，会话目标是完成登录页
根据这个仓库找一个值得看的 YouTube 教程，然后陪我实现
看看 X 上最近有哪些和这个技术栈相关的高质量帖子
保存这个视频到本次 coding 会话
帮我收尾：跑测试、总结 diff、写 release notes
开一个 15 分钟的免费德州扑克 Break Mode，两个人，不要真钱
转一下街机轮盘：两个人，20 分钟，想轻松玩
```

### 安装

前置条件：Codex/ChatGPT 需要支持插件，并安装启用 OpenAI 官方 Browser 插件。

```bash
codex plugin marketplace add leiMizzou/codex-lounge --ref main
codex plugin add codex-lounge@codex-lounge
```

安装后新建一个 Codex 任务。首次访问 YouTube、X、扑克站点或 wxiu.com 时，可能需要确认站点权限或由你完成登录。

### 免费扑克 Break Mode

插件只使用明确标注为免费或 play-money、没有现金价值和真实奖品的网页扑克候选站点，例如 [Poker Now](https://www.pokernow.com/)、[FlopHaus](https://flophauspoker.com/) 和 [pokr](https://www.pokr.live/)。每次打开前都会重新检查页面说明。

它不会协助真钱、现金、加密货币、抽奖或有奖扑克，也不会处理充值、提现、购买筹码、转移价值、绕过地区限制或年龄检查。私人房间邀请只会起草，不会自动发送。

### 本地数据与隐私

- Vibe Coding 会话：`~/.codex/codex-lounge/sessions.json`
- 街机挑战与成就：`~/.codex/codex-lounge/arcade-progress.json`

插件只保存你明确要求记录的目标、模式、时长、链接、短笔记和结果；不保存登录凭据、Cookie、私信、完整 Feed、源码、浏览历史、邀请链接或 Browser 数据。两个本地工具都故意不提供 reset/delete 命令。

### 游戏边界

街机功能仍可扫描 wxiu.com 大厅、游戏轮盘、每日挑战、成就和好友邀请，但现在属于 Break Mode。本项目不包含 ROM、模拟器文件、游戏资源或第三方网站代码，也不隶属于这些网站。请遵守网站规则和所在地法律。

## English

### Five session modes

- `deep-focus`: one observable coding outcome with minimal media.
- `learn-and-build`: one relevant video followed by implementation.
- `explore`: a concise YouTube and X inspiration radar grounded in the repository.
- `ship`: checks, diff review, documentation, release notes, and launch drafts.
- `break`: a time-boxed YouTube, X, free poker, or arcade intermission.

The plugin can also persist explicit session goals, links, notes, and outcomes locally so another Codex task can pick up the thread.

### Install

Install and enable OpenAI's Browser plugin first, then run:

```bash
codex plugin marketplace add leiMizzou/codex-lounge --ref main
codex plugin add codex-lounge@codex-lounge
```

Start a new Codex task after installation. Try `Start a 45-minute Vibe Coding session`, `Find one YouTube tutorial relevant to this repo`, `Build an inspiration radar from YouTube and X`, or `Open a 15-minute free Texas Hold'em break with no real money`.

### Safety and privacy

Poker support is restricted to clearly free, play-money experiences with no cash value or real prizes. The plugin does not assist with deposits, withdrawals, paid chips, crypto, sweepstakes, geographic evasion, or age-check bypasses. Social actions, invitations, commits, pushes, merges, releases, and public posts are never performed merely because their drafts were prepared.

Local session state is stored under `~/.codex/codex-lounge/`. It excludes credentials, cookies, private messages, source files, full feeds, and Browser history.

## Repository layout

```text
.
├── .agents/plugins/marketplace.json
├── plugins/codex-lounge/
│   ├── .codex-plugin/plugin.json
│   └── skills/
├── scripts/validate.py
└── tests/
```

## Development

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

## License

The plugin source and instructions are licensed under the [MIT License](LICENSE). Third-party websites, games, videos, posts, names, artwork, and trademarks are not covered by this license.
