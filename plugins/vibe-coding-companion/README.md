# Vibe Coding 伴侣

一个把 Codex 内嵌 Browser 变成编码伴侣的开源插件。它根据当前项目启动专注、学习、探索、发布或休息会话，并提供：

- YouTube 视频、节目、频道、播放列表和专注音乐
- X/Twitter 首页、个人主页、自己的帖子、书签、列表和项目相关搜索
- 与当前仓库相关的 YouTube + X 灵感雷达
- 本地会话目标、链接、笔记、结果和最近记录
- 测试、diff、文档、release notes 与宣传草稿的发布收尾
- 仅限免费、无现金价值的德州扑克 Break Mode
- wxiu.com 街机雷达、轮盘、挑战、成就和好友邀请

典型提示：

```text
开始一个 45 分钟的 Vibe Coding 会话
根据当前项目找一个 YouTube 节目，然后陪我实现
打开 X 看我自己的帖子
记录本次 coding 会话，并保存这个链接
帮我收尾并准备 GitHub release notes
开一个免费的德州扑克好友房，不要真钱
```

需要同时安装并启用 OpenAI Browser 插件。媒体、游戏和扑克页面会留在内嵌 Browser 中供用户操作；登录、发帖、发送邀请、付费和其他外部动作不会被默认执行。

本地会话保存在 `~/.codex/vibe-coding-companion/sessions.json`，街机记录保存在 `~/.codex/vibe-coding-companion/arcade-progress.json`。不保存账号、Cookie、私信、源码、完整 Feed、Browser 历史或邀请链接。
