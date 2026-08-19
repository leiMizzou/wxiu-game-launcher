# Wxiu Game Launcher for Codex

[中文](#中文说明) · [English](#english)

An open-source Codex plugin that turns `wxiu.com` into a persistent arcade companion inside Codex's built-in Browser.

![Codex opening King of Fighters '98 from wxiu.com in the built-in Browser](assets/promo-codex-wxiu-v0.2.0.png)

## 中文说明

### 功能

- 指定游戏直达，例如“打开拳皇 98 游戏室”
- 街机雷达：按实时玩家、房间和类型扫描大厅
- 游戏轮盘：根据人数、时间、心情和排除条件选游戏
- 生成随机或主题街机挑战
- 保存每日挑战、连续打卡、游玩历史与六种成就徽章
- 协助创建好友房间、复制邀请链接并起草邀请文案
- 兼容 wxiu.com 的中文和英文界面

### 前置条件

- 支持插件的 ChatGPT/Codex 桌面端或 Codex CLI
- 已安装并启用 OpenAI 官方 `Browser` 插件
- 使用内嵌 Browser 时，首次访问 `wxiu.com` 可能需要确认站点权限

### 安装

```bash
codex plugin marketplace add leiMizzou/wxiu-game-launcher --ref main
codex plugin add wxiu-game-launcher@wxiu-arcade
```

安装后新建一个 Codex 任务，然后尝试：

```text
打开拳皇 98 游戏室
扫描大厅，给我一份实时街机雷达
转一下游戏轮盘：两个人，20 分钟，想轻松玩
生成一个适合两个人的随机街机挑战
生成并保存今天的街机挑战
我完成挑战了，记录一下并看看解锁了什么成就
帮我开恐龙快打，生成发给朋友的邀请链接
```

每日挑战和成就默认保存在 `~/.codex/wxiu-game-launcher/progress.json`。其中只包含游戏名称、模式、挑战状态、日期和可选备注，不保存账号、聊天内容、邀请链接或 Browser 数据。

### 更新

重新添加 Git marketplace 以刷新快照，然后重新安装插件：

```bash
codex plugin marketplace add leiMizzou/wxiu-game-launcher --ref main
codex plugin add wxiu-game-launcher@wxiu-arcade
```

更新后请新建一个 Codex 任务。

### 安全与边界

插件不会自动登录、购买、发送消息、加入陌生玩家的房间，或绕过网站限制。邀请链接只会复制到本地 Browser 剪贴板，发送动作仍由用户决定。

本项目不包含或分发 ROM、模拟器文件、游戏资源或 wxiu.com 的网站代码，也不隶属于 wxiu.com。使用者需要遵守网站规则，并合法拥有相应游戏的原版拷贝。游戏名称和商标归各自权利人所有。

## English

### Features

- Open a named arcade game directly in the built-in Browser
- Scan a live arcade radar using current player and room counts
- Spin a game roulette using party size, time, mood, and exclusions
- Generate random or themed arcade challenges
- Persist daily challenges, streaks, play history, and six achievement badges
- Prepare a friend-room invitation link and draft message without sending it
- Work with both Chinese and English wxiu.com interfaces

### Requirements

- A ChatGPT/Codex surface with plugin support, or Codex CLI
- OpenAI's official `Browser` plugin installed and enabled
- Normal site permission approval for `wxiu.com` when first used

### Install

```bash
codex plugin marketplace add leiMizzou/wxiu-game-launcher --ref main
codex plugin add wxiu-game-launcher@wxiu-arcade
```

Start a new Codex task after installation and ask it to scan the radar, spin the roulette, save a daily challenge, open a game, or prepare a friend invite.

## Repository layout

```text
.
├── .agents/plugins/marketplace.json
├── plugins/wxiu-game-launcher/
│   ├── .codex-plugin/plugin.json
│   └── skills/
├── scripts/validate.py
└── tests/test_progress.py
```

## Development

Run the dependency-free repository checks:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The plugin has also been validated locally with Codex's official plugin and skill validators.

## License

The plugin source and instructions are licensed under the [MIT License](LICENSE). Third-party websites, games, names, artwork, and trademarks are not covered by this license.
