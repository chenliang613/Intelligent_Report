# 2026年11月 智能体发展报告

- **期数**：2026-11
- **覆盖窗口**：2026-11-01 ~ 2026-11-08
- **生成日期**：2026-11-08

## 1. 本期摘要

1. **OpenAI Codex CLI 0.167.0 发布“智能体指挥中心”**：新增 `codex agents --no-daemon` 命令中心与未读结果标记，可并行监督多个后台编码代理，并内置 Vertex AI 配置向导。影响：终端从“单会话编辑器”进一步走向“多代理驾驶舱”。
2. **Claude Code 连续三个版本（v2.1.317–v2.1.319）强化权限与安全**：新增 `permissions.denyInsteadOfPrompting`、终端 MCP 任务后台化，并修复 sed 绕过权限检查、worktree 沙箱逃逸等多项漏洞。影响：长程无人值守代理的可靠性与安全性同步收紧。
3. **Kimi Code 一周内密集迭代（CLI 2.5.0–2.5.2、Desktop 1.3.0）**：新增远程环境（SSH/Docker）内执行工具、从历史轮次/运行中会话分叉、代理运行中切换模型与思考强度。影响：国产编码代理在多目录、远程与长任务工作流上的可用性显著提升。
4. **DeepSeek 公布 Super-agent 架构并公开 Harness 生态数据**：提出“连续、高效、主动、持久”的自主智能体架构（已开源原型），同时 Harness 日活达 154 万、将建官方插件市场。影响：国产智能体从“对话工具”向“持续在线协作者”的形态推进。
5. **Google Jules 退役进程逼近关键节点**：按官方 changelog，Jules 将于 11 月 11 日停止接受新任务、12 月 31 日正式下线，用户需在窗口内完成导出与迁移。影响：Google 编码智能体产品线进一步向 Antigravity 收拢。

## 2. 月度总览

| 厂商 | 产品/发布 | 类型 | 简述 | 日期 |
| --- | --- | --- | --- | --- |
| Anthropic | Claude Code v2.1.317~v2.1.319 | 编码 | 新增 `permissions.denyInsteadOfPrompting`、终端 MCP 任务、`/claude-api latency-optimize`，修复多项权限与沙箱漏洞 | 11-02 ~ 11-06 |
| OpenAI | Codex CLI 0.167.0 | 编码 | 智能体指挥中心、未读标记、后端切换、Vertex AI 向导 | 11-06 |
| Google | Jules 退役进程 | 编码 | 11-11 停止新任务、12-31 下线，官方提供导出与迁移 | （10-29 changelog，11-11 截止） |
| Google | Antigravity 1.5.2 | 编码 | `--remote-agent` 支持云插件技能，收紧 `--dangerously-skip-permissions` | 11-06 |
| Kimi | Kimi Code CLI 2.5.0~2.5.2 / Desktop 1.3.0 | 编码 | 远程环境执行、会话分叉、代理运行中切换模型/思考强度 | 11-04 ~ 11-06 |
| DeepSeek | Super-agent 架构（开源原型） | 通用/编码 | 双层架构、事件驱动、异步多信道、存算分离的自主智能体 | 11-01（报道） |
| DeepSeek | DeepSeek Harness 生态进展 | 智能体平台 | 154 万日活、约 3.5 万第三方插件、将建官方插件市场 | 11-05 |
| 智谱 | AutoGLM-Phone 框架（官方更新记录） | 手机操作 | 基于视觉语言模型的手机智能助理框架（限时免费） | 本期官方记录，具体上线日未核实 |

## 3. 分厂商详情

### 3.1 Anthropic

#### 3.1.1 智能体产品发布与更新

覆盖窗口内，Claude Code 连续发布三个版本：v2.1.317（11-02）、v2.1.318（11-03）、v2.1.319（11-06）。核心增量集中在多智能体协作、权限治理与无头（headless）运行的可观测性。

- v2.1.318 新增了保存的 claude.ai 登录到期日的可见性：`claude auth status` 输出 `loginExpiresAt`、`claude -p` JSON 输出 `credential_expires_at`，到期前 10 天起 `claude -p` 文本输出会在 stderr 打印一行警告。来源：[Claude Code changelog](https://code.claude.com/docs/en/changelog.md)（v2.1.318，2026-11-03）、[DevelopersIO 解析](https://dev.classmethod.jp/articles/20261108-cc-updates-v2-1-319/)（2026-11-07）。
- v2.1.319 在 `/tasks` 中新增 “Earlier in this session” 行，列出已结束的子代理，可在其离开列表或重启后重新打开并继续发消息。来源：[Claude Code changelog](https://code.claude.com/docs/en/changelog.md)（v2.1.319，2026-11-06）。

#### 3.1.2 产品形态与能力

- **多智能体协作**：终端支持 MCP 任务（MCP tasks）——当 MCP 服务器将工具调用作为任务运行时，Claude Code 立即将其移入后台，完成后再把结果告知 Claude，避免阻塞会话；可通过 `CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND` 让其在工具调用内阻塞等待。来源：[Claude Code changelog](https://code.claude.com/docs/en/changelog.md)（v2.1.319，2026-11-06）。
- **入口与集成**：新增 `/claude-api latency-optimize`，用于定位 Claude API 代码中让用户等待的环节并对 eval 尝试更快的设置；`/claude-api managed-agents-onboard` 模板与 Claude Console 对齐。来源：[Claude Code changelog](https://code.claude.com/docs/en/changelog.md)（v2.1.319，2026-11-06）。
- **企业网关（Claude apps gateway）**：新增 `admin.pooled_conflict_rule`、`admin.pooled_priority_order`（设置多组成员预算的扣款优先级）、`login_notice`、`CLAUDE_GATEWAY_LOG_FORMAT=json` 等。来源：[Claude Code changelog](https://code.claude.com/docs/en/changelog.md)（v2.1.319，2026-11-06）。

#### 3.1.3 突破的智能体挑战

- **安全与对齐（权限/沙箱）**：v2.1.319 修复了多项权限与沙箱漏洞——细加工环境变量前缀可隐藏命令部分以绕过 Bash 权限检查、accept-edits 与 auto mode 下 `sed` 绕过权限检查、worktree 创建时的沙箱逃逸、引号内单词绕过 Bash deny/ask 规则等，均已修复。来源：[DevelopersIO 解析](https://dev.classmethod.jp/articles/20261108-cc-updates-v2-1-319/)（2026-11-07）。
- **长程任务可靠性（无人值守）**：新增 `permissions.denyInsteadOfPrompting` 设置，使本会卡在权限提示上的工具调用被直接拒绝、回合继续，适用于终端会话、子代理与 teammates，有利于长时间无人值守运行；同时 `claude -p` 在启动失败或 API 错误截断回复时改为返回非零退出码（exit 1），使 CI 能正确地失败。来源：[Claude Code changelog](https://code.claude.com/docs/en/changelog.md)（v2.1.319，2026-11-06）、[ClaudeWorld 综述](https://claude-world.com/articles/claude-code-november-2026-whats-new/)（2026-11-04）。
- **行为变更（注意）**：auto mode 在关闭遥测或 feature flag 的环境（含 LLM 网关后）不再回退到内置分类器，服务器无法检查的调用将被询问或拒绝（Bedrock/Vertex/Foundry 不变）；自保持 `self-paced` 的 `/loop` 在某一回合结束后不再调度保活唤醒。来源：[Claude Code changelog](https://code.claude.com/docs/en/changelog.md)（v2.1.319，2026-11-06）。

#### 3.1.4 商业化与生态

- 企业网关在预算、身份与策略三方面扩展：`oidc.user_id_claim`（以 id_token 的非 `sub` 声明识别用户）、`pooled_budget`（组成员共享月度预算）、`managed.policy_mode: layered`（多个匹配策略叠加），并新增 `assume_role` 上游支持跨 AWS 账户角色与按开发者成本归因。来源：[ClaudeWorld 综述](https://claude-world.com/articles/claude-code-november-2026-whats-new/)（2026-11-04）。
- 未发现覆盖窗口内 Anthropic 关于编码智能体的新定价或 MCP 生态的独立正式公告；本期更新均经 Claude Code 版本 changelog 落地。

### 3.2 OpenAI

#### 3.2.1 智能体产品发布与更新

覆盖窗口内，OpenAI 发布 Codex CLI 稳定版 **0.167.0**（GitHub 发布说明标注日期为 2026 年 11 月 6 日）。头条功能是新的“智能体指挥中心”：命令 `codex agents --no-daemon` 在不启动后台守护进程的情况下打开指挥中心，且指挥中心与会话选择器都会标记未读结果，便于同时监督多个并行运行的编码代理。来源：[Codex CLI 0.167.0 解析（DEV Community）](https://dev.to/delimitter/openai-ships-codex-cli-01670-with-an-agent-command-center-and-a-vertex-ai-setup-wizard-4ohb)（2026-11-06）、[DevAgentRadar 简报](https://www.devagentradar.com/insights/radar-brief-2026-11-06)（2026-11-06）。

同日另有预发布标签 `rust-v0.168.0-alpha.7`，无发布说明，属预发布而非默认安装目标。来源：[DevAgentRadar 简报](https://www.devagentradar.com/insights/radar-brief-2026-11-06)（2026-11-06）。

#### 3.2.2 产品形态与能力

- **多代理监督（指挥中心）**：`codex agents --no-daemon` 打开指挥中心；指挥中心与会话选择器标记未读结果，使“并行代理运行的突发输出”可按收件箱方式分诊。来源：[Codex CLI 0.167.0 解析](https://dev.to/delimitter/openai-ships-codex-cli-01670-with-an-agent-command-center-and-a-vertex-ai-setup-wizard-4ohb)（2026-11-06）。
- **后端切换与多云**：可直接在终端会话选择器中切换已连接后端并保留草稿；新增 `gcp_setup_wizard` 配置块，以 Application Default Credentials 或凭据文件引导配置 Google Vertex AI。来源：[Codex CLI 0.167.0 解析](https://dev.to/delimitter/openai-ships-codex-cli-01670-with-an-agent-command-center-and-a-vertex-ai-setup-wizard-4ohb)（2026-11-06）。
- **其他改进**：支持在受支持的终端中预览本地图片附件、审批提示中内联展开补丁细节、可选启用 macOS/Windows 系统代理；修复切换模型供应商后保存的聊天仍可见、网络审批提示在请求结束时关闭、上下文压缩计入失败响应的保留输出等。来源：[Codex CLI 0.167.0 解析](https://dev.to/delimitter/openai-ships-codex-cli-01670-with-an-agent-command-center-and-a-vertex-ai-setup-wizard-4ohb)（2026-11-06）。

#### 3.2.3 突破的智能体挑战

- **长程任务的并行监督**：未读标记与指挥中心把“检查多个后台代理进度需逐会话打开”的痛点收敛为统一入口，属多任务/多代理可靠性层面的可用性改进。来源：[Codex CLI 0.167.0 解析](https://dev.to/delimitter/openai-ships-codex-cli-01670-with-an-agent-command-center-and-a-vertex-ai-setup-wizard-4ohb)（2026-11-06）。
- 覆盖窗口内未发现 OpenAI 公布新的 SWE-bench 等量化智能体评测成绩；亦未核实到 ChatGPT agent/Codex/Dots 在窗口内的新版本公告（Dots 为 9 月末 DevDay 发布，早于本窗口）。

#### 3.2.4 商业化与生态

- **AgentKit / Agent Builder 退役进程（背景）**：Agent Builder 于 2026 年 6 月 3 日公告弃用，计划 2026 年 11 月 30 日停止在 OpenAI 平台提供服务；Evals 亦将于同日关停，ChatKit 仍保留。此为该过渡期的既定时间表（非窗口内新事件），但对本期之后的使用有直接影响。来源：[AgentKit Deprecation Guide](https://mcp.directory/blog/openai-agentkit-deprecation-2026)（2026-06-22）。
- 覆盖窗口内，检索未发现 OpenAI 新的智能体相关定价或独立产品发布正式公告。

### 3.3 Google

#### 3.3.1 智能体产品发布与更新

- **Jules 退役进入倒计时（关键节点）**：Google 官方 Jules changelog 于 2026 年 10 月 29 日发布 “Jules Turndown” 条目，设定时间表——至 2026 年 11 月 11 日可继续完成活跃会话，之后转为只读，12 月 31 日正式下线；代码、分支与 PR 保留在 GitHub，官方提供导出（`~/jules-export`，含账号设置、环境变量、定时任务、连接仓库、记忆、setup 脚本及每个会话的 prompt/plan/activity log/补丁）。此为 10-29 公告、覆盖窗口内（11-01~11-08）进入执行期的事件。来源：[explainx.ai Jules 下线导引](https://explainx.ai/blog/google-jules-shutdown-december-31-antigravity-export-guide-2026)（2026-10-30）。
- **Antigravity 1.5.2（11-06 发布）**：`--remote-agent` 会话现支持来自已连接云插件的技能（出现在 `/` 菜单并可输入）；`--dangerously-skip-permissions` 不再自动批准内置受保护命令清单，Enterprise 评审仍可拒绝工作区外的终端/文件访问；工作区外提示改为按路径而非“全部允许”。来源：[DevAgentRadar 简报](https://www.devagentradar.com/insights/radar-brief-2026-11-06)（2026-11-06）。

#### 3.3.2 产品形态与能力

- Jules 的定位为异步编码代理（描述 bug 修复/写测试 → 远程工作区规划执行 → 开 PR）；退役后 Google 将相关能力收拢至 Antigravity（其 agent-first 开发环境），官方 x 账号称“把我们从 Jules 学到的东西带入 @antigravity，兼顾自主远程后台任务执行与 agent-first 开发环境”。但 Antigravity 何时上线 Jules 式的后台任务，官方通知未给日期。来源：[explainx.ai Jules 下线导引](https://explainx.ai/blog/google-jules-shutdown-december-31-antigravity-export-guide-2026)（2026-10-30）。
- **Project Mariner 状态核对**：检索显示 Google 官方实验落地页记录 Project Mariner 已于 2026 年 5 月 4 日结束（早于覆盖窗口），其浏览器控制能力后续转向 Gemini Agent、Chrome 自动浏览与 Gemini API computer use 工具。来源：[invisible_playwright_mcp 文档](https://raw.githubusercontent.com/feder-cr/invisible_playwright_mcp/refs/heads/main/docs/project-mariner-is-gone.md)（获取于 2026-09）。

#### 3.3.3 突破的智能体挑战

- **安全与对齐（权限收紧）**：Antigravity 1.5.2 缩小了 `--dangerously-skip-permissions` 的豁免范围（受保护命令不再自动批准），并让企业策略可覆盖 auto-allow；安全团队的关注点在于无头（headless）与 CI 中的权限默认值变化。来源：[DevAgentRadar 简报](https://www.devagentradar.com/insights/radar-brief-2026-11-06)（2026-11-06）。
- **产品收拢（生态层面）**：Jules 成为继 Gemini CLI 之后第二个被指向 Antigravity 的 Google 编码产品，反映 Google 在减少独立编码交互面、集中单一平台；但若 Antigravity 未在 Jules 只读前上线后台执行，会存在无第一方异步代理的过渡空窗。来源：[explainx.ai Jules 下线导引](https://explainx.ai/blog/google-jules-shutdown-december-31-antigravity-export-guide-2026)（2026-10-30）。

#### 3.3.4 商业化与生态

- Jules 的退役与 Google AI Pro/Ultra 套餐的任务额度（15/100/300 task/天）此前已上线；下线通知未说明套餐额度此后如何处置，官方建议向 Google 支持确认。来源：[explainx.ai Jules 下线导引](https://explainx.ai/blog/google-jules-shutdown-december-31-antigravity-export-guide-2026)（2026-10-30）。
- 覆盖窗口内，未发现 Google 关于智能体的新定价或独立产品正式公告。

### 3.4 智谱 GLM

#### 3.4.1 智能体产品发布与更新

- **AutoGLM-Phone 框架出现在官方发布记录**：智谱官方“模型与产品发布记录”页面列出了 **AutoGLM-Phone AI 手机智能助理框架上线**，支持用自然语言自动完成 App 操作、界面识别/意图规划/设备执行的端到端能力，已适配 50+ 主流中文应用，覆盖购物、出行、外卖、影音、资讯等任务；同类文档标注“新模型上线，限时免费”。来源：[智谱AI开放文档·模型与产品发布记录](https://docs.bigmodel.cn/cn/update/new-releases)、[AutoGLM-Phone 文档](https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone.md)。
- **日期说明**：该发布记录页为滚动更新页面，检索结果中该页快照日期为 2026-11-05；但 AutoGLM-Phone 框架的**精确上线日期在窗口内未能独立核实**，不排除其早于覆盖窗口上线，仅在此报告其被官方更新记录列为产品条目。

#### 3.4.2 产品形态与能力

- **AutoGLM-Phone**：基于视觉语言模型 + ADB 设备控制，支持 `Launch / Tap / Type / Swipe / Back / Home / Long Press / Double Tap / Wait / Take_over` 等完整操作指令集（`Take_over` 用于登录/验证码人工接管）；上下文窗口 20K、最大输出 2048、支持中文、硬件为 Android 7.0+；配套开源项目为 zai-org/Open-AutoGLM。来源：[AutoGLM-Phone 文档](https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone.md)。
- **AutoGLM 2.0（窗口前）**：检索显示 AutoGLM 2.0 于 2026 年 10 月中旬上线（首个手机通用 Agent，无邀请码、免费），早于覆盖窗口，此处仅作背景。来源：[蜻蜓FM·Agent 播客](https://www.qtfm.cn/channels/469577/programs/30576324/)（2026-10-15）。

#### 3.4.3 突破的智能体挑战

- **工具使用（手机操作）**：AutoGLM-Phone 的多模态工具链在文本工具外扩展了画框、截图、读网页（含图片识别）等多模态 Tools，强化 GUI Agent 的“看懂环境—规划动作—执行任务”长流程能力。来源：[智谱AI开放文档·模型与产品发布记录](https://docs.bigmodel.cn/cn/update/new-releases)。
- 覆盖窗口内未核实到 AutoGLM-Phone 或 GLM 智能体在 OSWorld / WebArena / Terminal-Bench 等公开评测上的最新量化成绩。

#### 3.4.4 商业化与生态

- AutoGLM-Phone 框架在官方文档中标注“新模型上线，限时免费”。来源：[AutoGLM-Phone 文档](https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone.md)。
- 覆盖窗口内未发现智谱关于智能体的新定价、企业采用或开发者生态的独立正式公告。

### 3.5 Kimi（月之暗面）

#### 3.5.1 智能体产品发布与更新

覆盖窗口内，Kimi Code 全产品线密集迭代：

- **Kimi Code CLI v2.5.0（2026-11-04）**：新增远程环境绑定（SSH、Docker、自定义命令），可在远程机器/容器中执行文件与 Shell 工具，模型请求与凭据留在本机；支持从所选历史轮次或运行中的会话分叉；代理运行期间可使用 `/model` 与 `/effort`；多目录项目合并所有源目录的 Skills。来源：[Kimi Code CLI 变更记录](https://www.kimi.com/code/docs/kimi-code-cli/changelog)（2.5.0，2026-11-04）。
- **Kimi Code CLI v2.5.1（2026-11-05）**：修复动态工具 schema 生成的空系统消息反复导致 HTTP 400、会话标题、含空格图片路径、工具结果预览等问题。来源：[Kimi Code CLI 变更记录](https://www.kimi.com/code/docs/kimi-code-cli/changelog)（2.5.1，2026-11-05）。
- **Kimi Code CLI v2.5.2（2026-11-06）**：修复 MCP 工具定义变化时 `select_tools` 重复声明工具、Web 会话运行期间 steer 消息错误排队等问题。来源：[Kimi Code CLI 变更记录](https://www.kimi.com/code/docs/kimi-code-cli/changelog)（2.5.2，2026-11-06）。
- **Kimi Code Desktop v1.3.0（2026-11-04）**：支持用项目组织多个工作目录（指定主目录 + 多个源文件夹、文件树切换根目录）、从历史轮次/运行中会话分叉、一键导出诊断信息；最低 macOS 版本提高至 13。来源：[Kimi Code 最新动态](https://www.kimi.com/code/docs/kimi-code/whats-new.html)（v1.3.0，2026-11-04）。

#### 3.5.2 产品形态与能力

- **远程执行**：通过 `--environment <id>` 在创建会话时绑定 SSH/Docker/自定义命令环境，`--environment-cwd <path>` 指定工作目录；文件与 Shell 工具在目标环境执行，模型请求与凭据留在本机（安全隔离）。来源：[Kimi Code 最新动态](https://www.kimi.com/code/docs/kimi-code/whats-new.html)（v2.5.0，2026-11-04）。
- **会话分叉**：从已完成回复的历史轮次“从此处分叉”，或分叉运行中的会话（源会话继续执行）。来源：[Kimi Code 最新动态](https://www.kimi.com/code/docs/kimi-code/whats-new.html)（v2.5.0，2026-11-04）。
- **入口扩展**：v2.4.0（10-28，窗口前）已新增 `/import-sessions` 与 `kimi import-sessions` 导入近 15/30 天的 Claude Code、Codex 会话，便于迁移。来源：[Kimi Code 最新动态](https://www.kimi.com/code/docs/kimi-code/whats-new.html)（v2.4.0，2026-10-28）。

#### 3.5.3 突破的智能体挑战

- **工具使用（远程/容器）**：远程环境内执行工具解决了本地环境无法托管特定依赖或硬件时的长程任务执行问题；v2.5.0 同时提升了远程文件读取、编辑、写入、搜索和补全的速度。来源：[Kimi Code CLI 变更记录](https://www.kimi.com/code/docs/kimi-code-cli/changelog)（2.5.0，2026-11-04）。
- **长程任务的上下文管理**：多目录项目合并 Skills、待办列表连续 10 步未更新才提醒 Agent、subagent 卡片在输出持续增长时保持响应等，均指向长任务的稳定性。来源：[Kimi Code CLI 变更记录](https://www.kimi.com/code/docs/kimi-code-cli/changelog)（2.5.0，2026-11-04）。
- 覆盖窗口内未核实到 Kimi Code 或 Kimi Researcher 新的 SWE-bench Verified 等量化成绩公告。

#### 3.5.4 商业化与生态

- **Kimi Researcher（窗口前背景）**：检索显示 Kimi-Researcher（深度研究）于 2026 年 10 月下旬开启小范围灰度测试，定位为生成带引用来源深度研究报告的智能体，并计划逐步开源其基础预训练模型与强化学习优化版本；该事件早于覆盖窗口。来源：[XFastest 报道](https://www.xfastest.com/thread-301666-1-76.html)（2026-10-26）。
- 覆盖窗口内未发现 Kimi 关于智能体的新定价正式公告（Kimi Code 的会员模型权限为既有体系）。

### 3.6 DeepSeek

#### 3.6.1 智能体产品发布与更新

- **Super-agent 架构公布并开源原型**：DeepSeek Harness 团队于 2026 年 10 月 31 日晚通过官方公众号发表技术文章《Super-agent 设计探索：迈向更自主的 Agent 系统》，正式公开 Super-agent 架构，相关原型已同步开源。**日期说明：文章事件发生日为 10-31（覆盖窗口前一日），但大量报道集中于 11-01**，本文按“事件日期 10-31、报道日期 11-01”如实标注，并予收录以不漏报。来源：[新浪财经转上海证券报](https://finance.sina.com.cn/wm/2026-10-31/doc-inixcwwm7197135.shtml)（事件 2026-10-31）、[环球网科技](https://m.sohu.com/coo/zmtq/1095634733_99900743)（2026-11-01）、[JST spap](https://spap.jst.go.jp/china/news/261101/topic_5_03.html)（2026-11-06）。
- **DeepSeek Harness v0.2.2 系列迭代**：v0.2.2-alpha.3（11-03）新增插件安装失败诊断与 Host 日志；v0.2.2-rc.1（11-04）作为 0.2.2 系列首个候选版，优化连续工具调用间 Auto 自动评审的历史上下文缓存复用、切换更小上下文模型时优先用原模型压缩历史记录，并为全局/项目级 AGENTS.md 设置独立字节预算。来源：[InfoQ/36Kr 报道](https://eu.36kr.com/en/p/4057774236652417)（2026-11-07）。

#### 3.6.2 产品形态与能力

- **Super-agent 四特征**：连续（跨 IM/GitHub 评论等界面交互，无需担心会话上下文割裂）、高效（并行高质量完成多任务、无需等上一命令完成）、主动（持续观察环境事件并主动推进，无需介入时保持安静）、持久（始终在线、接入真实工作环境、异常自动恢复）。来源：[新浪财经转上海证券报](https://finance.sina.com.cn/wm/2026-10-31/doc-inixcwwm7197135.shtml)（2026-10-31）。
- **架构机制**：通过双层架构、事件驱动、异步多信道交互、存算分离与外部 Watchdog 突破单会话绑定；内部 Super-agent 实例已持续运行，参与问题复现与修复、代码审查响应与 Harness 自身迭代（团队群聊反馈问题即可在后台复现并寻找修复方案）。来源：[新浪财经转上海证券报](https://finance.sina.com.cn/wm/2026-10-31/doc-inixcwwm7197135.shtml)（2026-10-31）。
- **Harness 平台化**：官方提出 Harness 目标为“Agent 时代的操作系统”，内置功能亦可被第三方插件替换（“Everything is a Plugin”）。来源：[InfoQ/36Kr 报道](https://eu.36kr.com/en/p/4057774236652417)（2026-11-07）。

#### 3.6.3 突破的智能体挑战

- **多智能体协作 / 自主性**：Super-agent 直接面向“多任务上限取决于人的注意力”这一瓶颈，以跨会话上下文、异步多信道与存算分离让 Agent 成为跨会话保持上下文的连续实体，属自主性/长程协作维度的架构级探索。来源：[新浪财经转上海证券报](https://finance.sina.com.cn/wm/2026-10-31/doc-inixcwwm7197135.shtml)（2026-10-31）。
- **生态治理（插件可靠性）**：插件增多带来上下文溢出、无限循环、配置升级丢失等问题（有用户报告桌面端 v0.2.1-rc.5 → v0.2.2-rc.1 升级丢失 32 个插件配置）；Harness 通过诊断、依赖同步、热重载、上下文压缩回应，官方插件市场将补充审核、质量评级、权限管理与安全提示。来源：[InfoQ/36Kr 报道](https://eu.36kr.com/en/p/4057774236652417)（2026-11-07）。
- 覆盖窗口内未核实到 DeepSeek 智能体在公开评测（SWE-bench Verified 等）的新量化成绩。

#### 3.6.4 商业化与生态

- **Harness 规模数据（11-05 公布）**：截至 2026-11-04，以官方 API 用户统计，日活跃用户达 154 万、日消耗 Token 约 92 万亿；第三方插件约 3.5 万个，约 60% 活跃用户制作或安装过至少一款第三方插件。来源：[IT之家](https://www.ithome.com/1/023/011.htm)（2026-11-05）、[Pandaily](https://pandaily.com/deepseek-harness-1-54-million-daily-active-users-official-plugin-marketplace)（2026-11-06）。
- **插件作者支持计划**：官方将建设官方插件市场，并筹备以 Token 激励、技术交流、作品推荐支持插件作者；同时欢迎创业团队/企业通过插件接入产品与服务。来源：[IT之家](https://www.ithome.com/1/023/011.htm)（2026-11-05）。

## 4. 智能体挑战突破对照

| 挑战维度 | Anthropic | OpenAI | Google | 智谱 GLM | Kimi | DeepSeek |
| --- | --- | --- | --- | --- | --- | --- |
| 长程任务可靠性 | 新增 `denyInsteadOfPrompting` 避免无人值守卡死，`claude -p` 非零退出码改正确失败 | 指挥中心 + 未读标记改善并行代理监督 | `--dangerously-skip-permissions` 范围收紧、企业策略可覆盖 | — | 远程环境执行 + 会话分叉支撑长任务 | Super-agent 以持久/主动特征突破会话绑定 |
| 工具使用 | 终端 MCP 任务后台化（异步不阻塞） | Vertex AI 向导、后端切换、图片预览 | `--remote-agent` 支持云插件技能 | 多模态 Tools（画框/截图/读网页） | SSH/Docker/自定义命令远程执行工具 | 插件热重载、依赖同步、统计工具 |
| 记忆 | — | 压缩计入失败响应输出 | 导出含 memories | — | 多目录 Skills 合并 | 跨会话上下文（Super-agent）、AGENTS.md 字节预算 |
| 多智能体协作 | `/tasks` 重开已结束子代理、MCP 任务后台 | 指挥中心监督多代理 | Jules 退役收拢至 Antigravity | — | Tower/多目录 Skills | 双层架构 + 异步多信道 + Watchdog |
| 安全与对齐 | 修复 sed 绕过、worktree 沙箱逃逸等漏洞 | — | 权限豁免、企业 override 收紧 | `Take_over` 人工接管 | 远程凭证留在本机 | 插件安全机制待官方市场完善 |

（“—” 表示覆盖窗口内检索未发现该厂商在该维度的可核实动态。）

## 5. 本月趋势观察

1. **编码代理从“单机 CLI”走向“可监督的多代理系统”**：OpenAI Codex 的指挥中心/未读标记与 Claude Code 的 MCP 任务后台化、`/tasks` 子代理重开，共同把“同时跑多个后台代理”的监督体验产品化，反映出厂商正将竞争焦点从单会话能力转向多代理编排与可观测性。
2. **无人值守运行的安全与可靠性成为显性投入**：Anthropic 三个版本集中修复 sed 绕过、worktree 沙箱逃逸等漏洞，Google Antigravity 收紧跳过权限的豁免，均指向长程/无人值守代理在权限边界上的治理收紧。
3. **国产智能体平台进入“生态开放”竞争阶段**：DeepSeek Harness 154 万日活 + 约 3.5 万插件并宣布建官方市场，Kimi Code 密集迭代远程/分叉/多目录能力，智谱 AutoGLM-Phone 以开源框架覆盖手机操作，三者都在以“开放插件/框架”而非封闭产品的方式争夺开发者与端侧入口。
4. **国外产品线明显收拢**：Google 于窗口内推进 Jules 退役（11-11 停止新任务、12-31 下线），继续将编码代理收拢至 Antigravity；OpenAI 的 Agent Builder/Evals 也临近 11-30 关停，显示头部海外厂商在智能体基础设施上走向“少而集中”的整合路线。

## 附录 A：参考来源

1. [Claude Code changelog](https://code.claude.com/docs/en/changelog.md) — Anthropic，v2.1.317~v2.1.319，2026-11-02~2026-11-06
2. [Claude Code v2.1.318~v2.1.319 主要更新解析](https://dev.classmethod.jp/articles/20261108-cc-updates-v2-1-319/) — DevelopersIO（Classmethod），2026-11-07
3. [What's New in Claude Code: November 2026 (v2.1.308–2.1.318)](https://claude-world.com/articles/claude-code-november-2026-whats-new/) — ClaudeWorld，2026-11-04
4. [OpenAI Ships Codex CLI 0.167.0 With an Agent Command Center and a Vertex AI Setup Wizard](https://dev.to/delimitter/openai-ships-codex-cli-01670-with-an-agent-command-center-and-a-vertex-ai-setup-wizard-4ohb) — DEV Community，2026-11-06
5. [Radar brief — 2026-11-06](https://www.devagentradar.com/insights/radar-brief-2026-11-06) — DevAgentRadar，2026-11-06
6. [OpenAI AgentKit Deprecation Guide (2026)](https://mcp.directory/blog/openai-agentkit-deprecation-2026) — MCP Directory，2026-06-22
7. [Google Jules Shutdown Dec 31: Export Guide + Alternatives](https://explainx.ai/blog/google-jules-shutdown-december-31-antigravity-export-guide-2026) — explainx.ai，2026-10-30
8. [Project Mariner is gone: what replaced it](https://raw.githubusercontent.com/feder-cr/invisible_playwright_mcp/refs/heads/main/docs/project-mariner-is-gone.md) — invisible_playwright_mcp 文档（GitHub）
9. [模型与产品发布记录](https://docs.bigmodel.cn/cn/update/new-releases) — 智谱AI开放文档，快照 2026-11-05
10. [AutoGLM-Phone 文档](https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone.md) — 智谱AI开放文档
11. [AutoGLM 2.0 上线（Agent 播客）](https://www.qtfm.cn/channels/469577/programs/30576324/) — 蜻蜓FM，2026-10-15
12. [Kimi Code CLI 变更记录](https://www.kimi.com/code/docs/kimi-code-cli/changelog) — 月之暗面，2.5.0~2.5.2，2026-11-04~2026-11-06
13. [Kimi Code 最新动态](https://www.kimi.com/code/docs/kimi-code/whats-new.html) — 月之暗面，v1.3.0 / v2.5.0，2026-11-04
14. [月之暗面发布首个自主强化学习 Agent Kimi-Researcher](https://www.xfastest.com/thread-301666-1-76.html) — XFastest，2026-10-26
15. [DeepSeek 发布全新 Agent 架构](https://finance.sina.com.cn/wm/2026-10-31/doc-inixcwwm7197135.shtml) — 新浪财经（转上海证券报），事件 2026-10-31
16. [DeepSeek 发布全新 Agent 架构 “Super-agent”，让 AI 调度 AI](https://m.sohu.com/coo/zmtq/1095634733_99900743) — 环球网科技，2026-11-01
17. [AIがAIに仕事を振り分ける仕組み DeepSeekが新アーキテクチャを公開](https://spap.jst.go.jp/china/news/261101/topic_5_03.html) — JST さくら Science Portal，2026-11-06
18. [DeepSeek Harness：日活跃用户达 154 万、日消耗 Token 约 92 万亿，将建设官方插件市场](https://www.ithome.com/1/023/011.htm) — IT之家，2026-11-05
19. [DeepSeek Harness Hits 1.54 Million Daily Active Users: Official Team Distributes Tokens to Plugin Developers](https://eu.36kr.com/en/p/4057774236652417) — InfoQ（36Kr 授权转载），2026-11-07
20. [DeepSeek Harness Reaches 1.54 Million Daily Users and Plans an Official Plugin Marketplace](https://pandaily.com/deepseek-harness-1-54-million-daily-active-users-official-plugin-marketplace) — Pandaily，2026-11-06
