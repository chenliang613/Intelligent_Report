<!--
由模板 reports/templates/report2-agent-development.md v1.0 填充
本期为半月初稿：覆盖 2026-10-01 ~ 2026-10-15，生成于 10-15；月末需补全下半月动态后定稿
-->
# 2026年10月 Top 智能体厂商发展报告

- **期数**：2026-10
- **覆盖窗口**：2026-10-01 ~ 2026-10-15（半月初稿）
- **生成日期**：2026-10-15

## 1. 本期摘要

1. **Google**：在 Gemini at Work 2026 大会发布 **Gemini agent**——面向企业工作的单一通用智能体，可答题、承担知识工作、生成图文与写代码，并入 Gemini Enterprise（来源：[1]，约2026-10-09）——「通用工作智能体」成为大厂旗舰产品形态。
2. **Anthropic**：Claude Haiku 5.5（10-07）在编码、工具使用、computer use 与智能体任务上较 Haiku 4.5 显著提升（来源：[3]）——模型层持续为智能体任务降本增效。
3. **Anthropic**：Claude Code 本期多版本迭代：10-06 的 2.1.291 修复云会话丢答问题；近期版本加入 subagent `autoCompactWindow` 配置、桌面/插件/MCP/环境控制项（来源：[5]）——编码智能体进入细粒度治理阶段。
4. **Anthropic**：发布 2026 使用政策更新，为 Claude 新能力（含智能体能力）补充滥用判定示例（来源：[2]，约10-08）——能力扩张与安全治理同步推进。

## 2. 月度总览

| 厂商 | 产品/发布 | 类型 | 简述 | 日期 |
| --- | --- | --- | --- | --- |
| Google | Gemini agent | 通用/企业 | Gemini Enterprise 内的单一通用工作智能体 | 约10-09 |
| Anthropic | Claude Code 2.1.291 等 | 编码 | 云会话修复 + subagent/插件/MCP 控制增强 | 10-06 及近期 |
| Anthropic | Claude Haiku 5.5（模型侧） | 模型支撑 | 编码/工具使用/computer use/智能体任务能力提升 | 10-07 |
| Anthropic | 2026 使用政策更新 | 安全 | 为新能力补充滥用判定示例 | 约10-08 |
| OpenAI | — | — | 本期无公开动态 | — |
| 智谱 GLM | — | — | 本期无公开动态 | — |
| Kimi（月之暗面） | — | — | 本期无公开动态 | — |
| DeepSeek | — | — | 本期无公开动态 | — |

## 3. 分厂商详情

### 3.1 Anthropic

#### 3.1.1 智能体产品发布与更新

- **Claude Code 版本迭代**：2.1.291（10-06）修复云会话偶发丢答；近期版本为 subagent 定义（frontmatter / `--agents`）加入 `autoCompactWindow` 支持，并加入桌面端、插件、MCP 与环境控制等新控件。来源：[5]，2026-10。
- **2026 使用政策更新**（约10-08）：针对 Claude 新能力提供新的规则适用示例，覆盖影响力操作等新型滥用模式。来源：[2]。

#### 3.1.2 产品形态与能力

- Claude Code 持续强化多智能体/子代理配置粒度（subagent 上下文压缩窗口可配置）与运行环境管控（插件、MCP、环境控制项）。来源：[5]。

#### 3.1.3 突破的智能体挑战

- **工具使用 / 计算机操作**：Haiku 5.5 相对 Haiku 4.5 在工具使用、computer use 与 agentic 任务上显著提升，且为标准速度下最快的 Claude 模型（来源：[3]）——小型模型开始可靠承接智能体工具链任务。

#### 3.1.4 商业化与生态

本期无公开动态。

### 3.2 OpenAI

#### 3.2.1 ~ 3.2.4（发布/形态/挑战/商业化）

本期无公开动态。背景：9 月末 DevDay 已发布 Codex 多智能体等能力（窗口外）；本期窗口内未见新的智能体产品或定价公告。

### 3.3 Google

#### 3.3.1 智能体产品发布与更新

- **Gemini agent**（Gemini at Work 2026，约10-09）：定位「面向工作的单一通用智能体」，回答问题、承担知识工作、创建图像/媒体并编写运行代码；作为 Gemini Enterprise 的统一智能体入口发布。来源：[1]。
- 配套报道：Gemini agent 可获得自己的邮箱账号/「同事身份」，并配套治理控制，支持长时运行任务。来源：[4]（第三方分析）。

#### 3.3.2 产品形态与能力

- 形态：企业内统一入口（Gemini Enterprise）+ 单一通用智能体，而非多 App 并立；具备持久化（persistent）长任务执行能力。来源：[1][4]。

#### 3.3.3 突破的智能体挑战

- **长程任务 / 记忆**：persistent agent 支持长时运行任务（来源：[4]）。
- **安全与对齐**：为「同事身份」智能体配套治理控制（邮箱账号、权限治理）（来源：[4]）。

#### 3.3.4 商业化与生态

- Gemini agent 随 Gemini Enterprise 面向企业客户推出，与其 10-13 GA 的旗舰模型 Gemini 4 Argon（定位含 cyber defense）形成产品组合。来源：[1]（及报告1来源[5]）。

### 3.4 智谱 GLM

#### 3.4.1 ~ 3.4.4（发布/形态/挑战/商业化）

本期无公开动态。背景：当前产品线以 GLM-5.3（面向复杂软件工程与长程智能体任务、1M 上下文）与 GLM-5V-Turbo（原生多模态 Agent 基座）为主；AutoClaw（澳龙，本地 OpenClaw 客户端）为 3 月发布产品。来源：[6][7][8]。

### 3.5 Kimi（月之暗面）

#### 3.5.1 ~ 3.5.4（发布/形态/挑战/商业化）

本期无公开动态。背景：官网当前主推 K2.6（编码/分析/表格/幻灯片等复杂工作）；K3 于 7 月发布并开放权重。来源：[9][10]。

### 3.6 DeepSeek

#### 3.6.1 ~ 3.6.4（发布/形态/挑战/商业化）

本期无公开动态。背景：最近一次官方更新为 DeepSeek-V4.1-Flash（9-10）。来源：[11]。

## 4. 智能体挑战突破对照

| 挑战维度 | Anthropic | OpenAI | Google | 智谱 GLM | Kimi | DeepSeek |
| --- | --- | --- | --- | --- | --- | --- |
| 长程任务可靠性 | — | — | persistent agent 支持长时任务 [4] | — | — | — |
| 工具使用 | Haiku 5.5 工具使用显著提升 [3] | — | — | — | — | — |
| 记忆 | — | — | — | — | — | — |
| 多智能体协作 | subagent 配置粒度增强 [5] | — | — | — | — | — |
| 安全与对齐 | 使用政策新增能力滥用示例 [2] | — | 「同事身份」+治理控制 [4] | — | — | — |

<!-- 每格一句话；— 表示本期窗口内无该维度公开动态；矩阵内容与第 3 节事实一致 -->

## 5. 本月趋势观察

1. **「通用工作智能体」成为旗舰产品形态**：Google 以单一 Gemini agent 整合问答、知识工作、媒体生成与编码，直接进入企业「数字同事」赛道（来源 [1]）；OpenAI 9 月末的 ChatGPT Work / Codex 多智能体方向与此一致（窗口外背景）。
2. **模型层为智能体降本**：Haiku 5.5 把工具使用与 computer use 能力下放到最快最便宜的小模型（来源 [3]），与报告1中 GPT-6 Sol/Luna 全量铺开相互印证——智能体任务的成本曲线在快速下移。
3. **治理与能力同步演进**：Anthropic 为新能力补充使用政策示例（来源 [2]）、Google 为「同事身份」智能体配套治理控制（来源 [4]）——智能体获得组织身份的同时，滥用面与权限治理被正式提上日程。

## 附录 A：参考来源

1. [Gemini at Work 2026: Introducing Gemini agent](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026) — Google Cloud，约2026-10-09
2. [2026 Usage Policy update](https://www.anthropic.com/news/2026-usage-policy-update) — Anthropic，约2026-10-08
3. [Introducing Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5) — Anthropic，2026-10-07
4. [Gemini agent coworker identity & governance 分析](https://enersys.co.th/en/insights/gemini-agent-coworker-identity-governance-2026) — Enersys Insights，2026-10
5. [Claude Code Updates & Release Notes](https://releasebot.io/updates/anthropic/claude-code) — ReleaseBot，2026-10
6. [智谱官网产品页（GLM-5.3 / GLM-5V-Turbo）](https://www.zhipuai.cn/zh) — 智谱
7. [模型与产品发布记录（GLM-5.3，2026-08-14）](https://docs.bigmodel.cn/cn/update/new-releases) — 智谱开放平台
8. [智谱发布 AutoClaw：国内首个真·一键安装的本地版 OpenClaw](https://www.oschina.net/news/409053) — OSCHINA，2026-03-10（背景）
9. [Moonshot AI 官网（Kimi K2.6）](https://www.moonshot.ai) — 月之暗面
10. [Kimi (AI) — Wikipedia](https://en.wikipedia.org/wiki/Kimi_(AI)) — Wikipedia（K3 时间线）
11. [更新日志（DeepSeek-V4.1-Flash，2026-09-10）](https://api-docs.deepseek.com/zh-cn/updates) — DeepSeek API 文档
