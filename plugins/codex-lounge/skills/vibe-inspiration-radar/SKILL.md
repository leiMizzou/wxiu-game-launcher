---
name: vibe-inspiration-radar
description: Build a concise, task-aware inspiration radar from live YouTube videos and X/Twitter posts, grounded in the current repository and coding objective. Use when the user asks for coding inspiration, relevant talks, tutorials, demos, creators, posts, trends, what to watch, what people are saying, 技术灵感, 找教程, 看看 X 上怎么讨论, or wants media relevant to current code.
---

# Vibe Inspiration Radar

Find a small set of useful inputs without turning the coding session into endless browsing.

## Workflow

1. Inspect the current repository read-only and extract at most five search anchors: framework, language, feature, error, design direction, or deployment target.
2. Convert the goal into one narrow YouTube query and one narrow X query when both platforms are requested. Do not spray many guessed queries.
3. Use the Browser plugin to inspect live results and visible metadata.
4. Select at most five items total: one actionable tutorial or demo, one deeper explanation, one current implementation post, and one optional wild card.
5. Return each item with title or author, platform, visible freshness signal when available, and one sentence connecting it to the coding task.
6. End with one decisive `先看这个` recommendation. Open it only when requested or when opening was part of the original request.

## Quality Rules

- Do not claim a video or post was watched in full when only metadata was inspected.
- Separate platform-visible facts from inference.
- Avoid ragebait, generic productivity content, and duplicate reposts.
- Prefer primary creators, maintainers, conference channels, and direct project demos.
- Stop after enough evidence exists to make a useful choice.
