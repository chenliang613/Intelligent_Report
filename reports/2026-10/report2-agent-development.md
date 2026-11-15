# 2026年10月 智能体发展报告

- **期数**：2026-10
- **覆盖窗口**：2026-10-01 ~ 2026-10-31
- **生成日期**：2026-11-15

## 1. 本期摘要

1. **Anthropic 发布主动式个人智能体 Claude Duet**（10-21）——基于 Claude Opus 5.5，主动监控邮件/日历/工作应用、发晨报、在私有云电脑上执行任务，敏感操作（付款/发文/签署/删除）均需人工批准，面向美国 Pro/Max 订阅者限候补试用（来源 [1][2]）——通用智能体从「被动应答」走向「主动值守」的标志性商业化产品。
2. **DeepSeek 开源自主智能体原型 dsh-superagent**（10-31，MIT）——同日发布《Super-agent 设计探索》技术文章，双层 Router-Worker 架构、监听 GitHub/飞书「主动接活」，仓库明文标注「研究原型、非官方产品」（来源 [5][8]）——自主智能体架构探索从「被动」向「主动、低注意力」范式演进。
3. **Anthropic Claude Code v2.1.316 引入团队级成本治理**（10-31）——新增 pooled group budgets（组共享月度预算）与 `CLAUDE_CODE_SUBAGENT_EFFORT`（子代理努力度），并弃用 Opus 4.8 fast mode（来源 [3][4]）——编码智能体进入团队预算与算力精细治理阶段。
4. **OpenAI 将 ChatGPT Chrome 扩展升级为浏览器智能体**（10-15）——Chat/Work 双模式读标签页、接管填表/发消息/下载文件，向所有套餐开放（来源 [12][13]）；同期 Codex 新增 Composer predictions（10-09）与 faster steering（10-08）（来源 [10][11]）。
5. **Google 关停异步编码智能体 Jules**（10-27~10-29 公告）——能力沉淀并入 Antigravity，11-11 进入只读、12-31 全面下线（来源 [15][16]）；同期 ADK 扩展至五语言（10-14）（来源 [14]）——大厂编码智能体产品线收拢聚焦。
6. **月之暗面发布 Kimi K3.1 Pro**（10-24）——开放权重模型在 Terminal-Bench 4.0 达 65.7%，超过 GPT-6 Astra（58.2%）、逼近 Claude Opus 5.5（66.4%），并落地 Kimi Code；另于 10-29 在腾讯云沙箱上线 Kimi Hosted Agent 企业托管代理（来源 [19][20][21]）。

## 2. 月度总览

| 厂商 | 产品/发布 | 类型 | 简述 | 日期 |
| --- | --- | --- | --- | --- |
| Anthropic | Claude Duet | 通用/主动式 | Opus 5.5 驱动的个人智能体，晨报+云电脑执行，敏感操作需审批 | 10-21 |
| Anthropic | Claude Code v2.1.316 | 编码 | 组共享预算、子代理努力度、Opus 4.8 fast 弃用 | 10-31 |
| OpenAI | Codex faster steering | 编码 | 桌面端纠偏指令响应更快 | 10-08 |
| OpenAI | Codex Composer predictions（beta） | 编码 | 预测下一条消息，Tab 接受，不占用量 | 10-09 |
| OpenAI | ChatGPT dot 增强 | 通用/自动化 | 移动端创建 dot、可编辑 Work automations、接 Codex | 10-05~10-09 |
| OpenAI | ChatGPT Chrome 扩展浏览器智能体 | 浏览器 | Chat/Work 双模式读写标签页 | 10-15 |
| OpenAI | Decisions API 全面开放 | 智能体基础设施 | 面向智能体「有界决策」的判断 API，输出 Token 免费 | 10-22 |
| OpenAI | AgentKit Evals 平台进入只读 | 生态收拢 | Evals 只读，11-30 全面关闭 | 10-31 |
| Google | ADK 五语言 | 开发框架 | Python/Go/TypeScript/Java/Kotlin 原生覆盖 | 10-14 |
| Google | Jules 关停 | 编码 | 异步编码智能体停用，并入 Antigravity | 10-27~10-29 |
| 智谱 GLM | — | — | 本期未发现可核实的智能体产品新发布（AutoGLM 无新版） | — |
| Kimi（月之暗面） | Kimi Code CLI 2.2.0~2.4.1 | 编码 | 会话导入、模型切换、Tower 任务编排等多项更新 | 10-14~10-30 |
| Kimi（月之暗面） | Kimi K3.1 Pro / Highspeed | 模型支撑 | 编码/智能体能力显著提升，Terminal-Bench 4.0 达 65.7% | 10-24 |
| Kimi（月之暗面） | Kimi Hosted Agent | 企业托管代理 | 基于腾讯云沙箱的托管 Harness，企业直接调用 | 10-29 |
| DeepSeek | DeepSeek Harness v0.2.2-alpha.2（subagent_oar） | 编码 | 实验性外部子代理工具，统一调度本机 Codex/Claude CLI | 10-28 |
| DeepSeek | Super-agent 架构 + dsh-superagent 原型 | 自主/编码 | 双层 Router-Worker，MIT 开源，主动接活 | 10-31 |

## 3. 分厂商详情

### 3.1 Anthropic

#### 3.1.1 智能体产品发布与更新

- **Claude Duet 主动式个人智能体（研究预览，10-21）**：Anthropic 于 10-21/10-22 发布 Claude Duet，一款基于 Claude Opus 5.5 的主动式 AI 智能体，定位「在你发起提问之前主动行动」。它连接用户的邮件、日历与工作应用，每天发送早间摘要（morning brief），每隔数小时检查已连接账户，仅在需要你处理时主动发消息，并在独立的私有云电脑（虚拟机）上执行后台任务——用户关机也不影响工作。目前为限候补研究预览，面向美国 Pro/Max 订阅者，iOS、Android 与 claude.ai 可用，试用期不额外收费。来源 [1]（Anadolu Agency，10-22）、[2]（Technology KSA，10-26，事件 10-21）。
- **Claude Code v2.1.316（10-31）**：新增 pooled group budgets（组共享月度预算，叠加在成员个人额度之上，通过 spend limits admin API 的 `pooled_budget` 配置）、`CLAUDE_CODE_SUBAGENT_EFFORT`（子代理努力度环境变量）、`CLAUDE_CODE_DISABLE_ULTRATHINK`；同时弃用 Opus 4.8 的 fast mode（10-30 起弃用，11-30 移除）。来源 [3]（GitHub 官方 release，10-31）、[4]（DevelopersIO 详解，10-31）。
- **订阅额度解禁第三方（约 10-07）**：官方文档更新确认 Claude Max/Ultra/Team 计划现包含月度 API Credits，可覆盖 Claude API、Claude Managed Agents、Claude Agent SDK 与 `claude -p`（以关联 Cloud Console 组织的 API key 运行时）。来源 [23]（johnzfitch/claude-wiki 转载官方条目，更新 10-07）。

#### 3.1.2 产品形态与能力

- **Claude Duet 形态**：独立 App（区别于主 Claude App，但继承记忆、技能与已连接应用），以一条连续线程、文字或语音交互；通过 Claude marketplace 接入 6000+ 连接器/插件（Gmail、Slack、QuickBooks、Stripe、Gusto、LinkedIn、Docusign、HubSpot、Canva、Shopify 等），购物经 Stripe Link 钱包或 Shopify Shop Pay 完成。来源 [2]。
- **Claude Code 团队级治理**：v2.1.316 将编码智能体的成本管理从「个人工具」升级为「团队预算+权限」——组共享预算在成员个人额度之外再加一层团队总量约束；子代理 effort 不再一律继承会话设置，可单独指定。来源 [3][4]。

#### 3.1.3 突破的智能体挑战

- **安全与对齐（权限控制/人类审批）**：Claude Duet 将「敏感操作必审批」作为核心护栏——发文、付款、签署、删除前展示精确动作（含收件人与内容）等待批准；付款/转账/开户永远不可设为「不再询问」；证券交易、账户间资金转移即使批准也被硬性禁止；模型之外另设独立验证系统核对动作与意图（网页隐藏指令无法干扰）；支付采用一次性虚拟卡；凭据隔离使智能体无法读取密码/cookie/令牌；敏感信息分类器阻断登录凭据、卡号、账户号与证件号外泄。来源 [2]。
- **多智能体协作/算力调度**：v2.1.316 引入 `CLAUDE_CODE_SUBAGENT_EFFORT`，使主会话与子代理的努力度解耦，子代理 effort 不再一律继承会话设置。来源 [3][4]。
- **权限/治理修正**：v2.1.316 修复 `--restricted` 会话可越界上传文件（当 Read 允许规则覆盖时）、Claude apps gateway 未对所有请求做 `availableModels/deniedModels` 校验等问题。来源 [4]。

#### 3.1.4 商业化与生态

- **Claude Duet 分发**：研究预览期免费含于 Pro（$100/月）与 Max（$200/月）订阅；Anthropic 明示「审批疲劳」（approval fatigue）风险并承诺持续调优询问频率；产品纳入公开 bug bounty 计划。来源 [2]。
- **「自带订阅（BYOS）」扫清第三方生态障碍**：约 10-07 官方政策更新，订阅月度 API Credits 可直接用于 Claude Agent SDK、`claude -p` 及第三方 App（来源 [23]），打破「用户已订阅 Claude 仍须向第三方开发者二次付费」的僵局。

### 3.2 OpenAI

#### 3.2.1 智能体产品发布与更新

- **Codex faster steering（10-08，GA）**：桌面端 ChatGPT 中，向正在运行的任务发送后续指令以调整方向时，Codex 能更快响应；可在「设置→通用→后续行为」中选择后续消息是「修正当前运行」还是「等下一轮」。来源 [10]（官方 Release Notes，10-08）、[28]（reconn-ai 转载，10-08）。
- **Codex Composer predictions（10-09，beta）**：Codex 可根据当前线程对话预测你的下一条消息，Tab 接受、发送前可编辑；beta 期间生成预测不计入 Codex 用量/额度，Personal Pro 用户默认开启。来源 [11]（官方 Release Notes，10-09）、[29]（MIXED，10-11）。
- **ChatGPT dot 增强（10-05~10-09）**：dot（常驻后台智能体）现可在移动端 App 创建与配置（命名、外观、连接插件）；并可读取/编辑已设置的 ChatGPT Work automations，在 Codex 中开始新任务或接续既有线程。来源 [30]（官方 ChatGPT Learn「Create your dot」，10-05~10-09）、[31]（MIXED，10-11）。
- **ChatGPT Chrome 扩展升级为浏览器智能体（10-15）**：官方 X 帖宣布扩展支持 Chat 与 Work 模式——Chat 模式跨标签页查找信息，Work 模式可在授权后操作网页（发消息、填表、下载文件），面向所有套餐开放。来源 [12]（TechRepublic，10-21）、[13]（Mashable，10-16）。
- **AgentKit Evals 平台进入只读（10-31）**：按既定关停计划，Evals 平台 10-31 起只读，Agent Builder 与 Evals API/面板 11-30 全面关闭，代码类工作流被引导至 Agents SDK 或 ChatGPT Workspace Agents。来源 [32]（simstudioai PR，10-30）、[33]（apidog，10-02）。

#### 3.2.2 产品形态与能力

- **dot 与 Codex / Work automation 打通**：dot 作为常驻智能体获得「读取并改写已排程任务」的主动能力，并接入 Codex 线程执行编码工作；移动端即可创建并配置。来源 [30][31]。
- **浏览器操作（computer use）能力**：Chrome 扩展由「读标签页回答」升级为「接管标签页执行操作」，Chat 模式只读、Work 模式需授权操作，构成浏览器智能体的双模式安全边界。来源 [12][13]。
- **智能体决策基础设施**：10-22 Decisions API 全面开放（GA，由 GPT-6 Luna 支撑），面向「有界决策」（bounded answers，从若干预设选项中选出而非生成叙述文本），输出 Token 免费；用于软件自动化与智能体监控等需快速、低成本的判断场景。来源 [34]（CNMO，10-23）、[35]（Economic Times，10-24）。

#### 3.2.3 突破的智能体挑战

- **任务可靠性/人机协同**：faster steering 缩短「纠偏指令→智能体收到」延迟，提升长任务实时干预效率（来源 [10][28]）；dot 对「续既有 Codex 线程 vs 新起线程」的判别与 Work automation 编辑，指向长程任务上下文延续（来源 [30][31]）。
- **安全与权限**：浏览器智能体以「Chat 只读 / Work 需授权」双模式施加授权边界（来源 [12][13]）；Decisions API 通过「有界答案」约束模型输出空间，降低叙述式输出带来的不可控成本与延迟（来源 [34][35]）。

#### 3.2.4 商业化与生态

- **Codex CLI 版本迭代**：Codex CLI rust-v0.165.0（10-27）加入内置 Vertex AI provider、GPT-6.1 Terra 写入模型目录、memory v2 默认开启（来源 [36]，Havoptic，10-27）。
- **AgentKit 收拢**：Evals 平台 10-31 只读、11-30 全面关闭，是 AgentKit「可视化/无代码」路径收缩的执行节点（该停用计划自 6-03 已公布，本窗口为落地节点）。来源 [32][33]。

### 3.3 Google

#### 3.3.1 智能体产品发布与更新

- **Jules 逐步关停（约 10-27~10-29 公告）**：Google 在官方 X 账号（10-27）公告，逐步停用 2024-12 上线的异步 AI 编码智能体 Jules，并将积累的异步智能体、代码调试、工程任务经验整合进 Antigravity 智能体优先开发平台。时间表：11-11 前完成进行中会话并进入只读，12-31 全面下线。来源 [15]（The Verge，10-29/10-31）、[16]（NSTL 转载，10-27）。
- **Agent Development Kit（ADK）五语言（10-14）**：Google Cloud 官方博客宣布 ADK 覆盖 Python、Go、TypeScript、Java、Kotlin 五种语言，各自原生适配运行时与类型系统，共享统一架构并通过开放协议互通。来源 [14]（Google Cloud Blog，10-14）。

#### 3.3.2 产品形态与能力

- **ADK 形态**：每门语言原生含 MCP 客户端（自定义工具以 MCP server 形式暴露即可被任一语言立即调用）；多智能体系统经 Agent2Agent（A2A）协议跨语言、跨框架 HTTP 互通。Python 为参考实现（最广的 BigQuery/Spanner/Bigtable 集成与 Gemini/Anthropic/OpenAI/LiteLLM 适配器）；Go 面向生产后端（已首发 ADK 2.0 Graph Workflow，静态 2MiB 镜像、goroutine 高并发）；TypeScript 配 Zod 静态推断、支持 WebMCP + Chrome 端侧 Prompt API 浏览器内运行；Java 配 RxJava 响应式与 Spring AI/LangChain4j 桥接；Kotlin 用 KSP 编译器插件做构建期类型安全，零反射可运行于 Android 端侧（LiteRT-LM/Gemini Nano）。来源 [14]。
- **Jules 关停后形态**：能力并入 Antigravity，形成「单一智能体优先编码平台」聚焦形态，开发者被引导迁移至 Antigravity。来源 [15][16]。

#### 3.3.3 突破的智能体挑战

- **多智能体协作/互操作**：ADK 五语言经 MCP + A2A 协议实现跨语言、跨框架互操作，异构多智能体系统的协作边界进一步打开。来源 [14]。
- **工具使用**：ADK 各语言均原生接入 MCP 工具与 A2A 远程智能体调用，工具生态统一是本月重点；`adk.dev/llms.txt` 为编码智能体提供按需 API 文档，`agents-cli scaffold` 一步生成含 A2A 端点与 Cloud Run/GKE 部署配置的项目。来源 [14]。
- **产品治理**：Jules 关停表明 Google 将异步编码智能体资源聚拢于 Antigravity，产品线收拢聚焦（来源 [15][16]）。

#### 3.3.4 商业化与生态

- 产品线收拢聚焦：Jules 关停、能力并入 Antigravity 是一体两端；开发者被引导至 Antigravity 平台（来源 [15][16]）。ADK 以 `agents-cli` 脚手架 + `adk.dev/llms.txt` + 五语言 SDK 强化开发者生态，面向企业工程团队释放「Python-only」框架束缚（来源 [14]）。

### 3.4 智谱 GLM

#### 3.4.1 智能体产品发布与更新

检索未发现可核实动态/案例。本窗口内未见智谱 AutoGLM 的官方新版本发布公告；AutoGLM 2.0 为 2025-08 已发布的历史产品（App Store 最近一次更新为 2026-07-09，v2.0.20），开源项目 Open-AutoGLM 最近一次推送为 2026-03-06，均非本窗口事件（来源 [37]，ai-agent-map，记录日期 2026-04-09）。

#### 3.4.2 产品形态与能力

检索未发现可核实动态/案例。当前可核实形态仍为 2025 年 8 月发布的手机通用智能体 AutoGLM 2.0（云机/云电脑底座），本窗口内无新增官方能力公告。

#### 3.4.3 突破的智能体挑战

检索未发现可核实动态/案例。

#### 3.4.4 商业化与生态

检索未发现可核实的智能体产品商业化动态。相关但非本报告核心内容：智谱于 10-12 发布基于 GLM-5.3-Flash 的 GLM-Legal「法律智能体」模型（面向合同审阅、证据分析与合规工作流，属模型层产品而非智能体产品），以及 GLM-5.3 于 10-5/10-6 上架 Amazon Bedrock（面向企业编码与长周期智能体，AWS 托管推理，仅向符合条件企业开放）。此二项均为模型层动态，仅作提示，不纳入智能体产品发布表。来源 [38]（ailyre，10-13）、[39]（AWS 官方 What's New，10-05）。

### 3.5 Kimi（月之暗面）

#### 3.5.1 智能体产品发布与更新

- **Kimi Code CLI 密集更新（10-14~10-30，v2.2.0→2.4.1）**：官方 changelog 显示本月发布多个版本——2.2.0（10-14）新增 opt-in NotifyUser 进度更新、`kimi app` 打开桌面聊天、sticky 用户消息摘要；2.3.0（10-21）插件技能以 `<pluginID>:<skillName>` 限定名调用、会话占用提示、自动生成会话标题、远程控制流式传输（上限 10MiB→100MiB）；2.4.0（10-28）新增 `/import-sessions` 导入 Claude Code/Codex 会话、`/provider refresh`、Tower 每任务模型选择与 max_running_tasks、默认 agent 并发上限 16→256；2.4.1（10-30）文件读取上限收紧。来源 [22]（Kimi Code CLI 官方 changelog，10-30）。
- **Kimi K3.1 Pro / K3.1 Pro Highspeed（10-24）**：K3.1 系列首款模型、迄今最强 3T 级开放权重模型、1M 上下文，同步落地 Kimi.com、Kimi Work、Kimi Code（`/model` 切换）与 Kimi API（`kimi-k3.1-pro` / `kimi-k3.1-pro-highspeed`，支持零数据保留），完整权重 11-04 前发布。来源 [19]（官方技术博客，10-24）、[20]（新浪财经，10-24）。
- **Kimi Hosted Agent（10-29）**：月之暗面在腾讯云沙箱上构建 Harness 并上线 Kimi Hosted Agent，企业可直接调用托管 Harness 执行环境，由月之暗面 ToB 业务负责人在腾讯云活动上披露（10-29 与 30 余家企业分享 AI Agent 落地实践）。来源 [21]（chinaz 转载腾讯云活动，11-03）。

#### 3.5.2 产品形态与能力

- **Kimi Code CLI 形态**：终端编码智能体，MIT 许可单二进制分发；本月新增会话迁移（导入 Claude Code/Codex）、运行时模型/提供方刷新、Tower 任务编排（每任务模型选择、并发上限调高），并强化多目录技能合并、SSH/Docker/自定义命令环境等能力。来源 [22]。
- **Kimi K3.1 Pro 能力**：强化编码、3D 创作、金融研究与「其他智能体能力」，支持端到端完成完整金融工作流与长步骤多任务（OfficeQA Pro v2 64.4、Frontier Finance 提升）。来源 [19]。
- **Kimi Hosted Agent 形态**：将 Harness 层托管到腾讯云沙箱，企业无需自行追更「每三个月更新一次的 Harness」，直接调用托管执行环境。来源 [21]。

#### 3.5.3 突破的智能体挑战

- **长程任务可靠性 / 工具使用**：K3.1 Pro 在 Terminal-Bench 4.0 得分 65.7%（高于 GPT-6 Astra 58.2%，略低于 Claude Opus 5.5 66.4%）；在内部长程基准 Kimi Code Bench 3.0 Long-horizon 得分 61.2%（高于 K3 的 55.95%），该基准考察编码智能体的多步执行、工具使用与端到端求解（来源 [19]）。在内测中跨 167 个任务迭代训练人类步态控制器，主动诊断并修正 36 处肩部肌肉力矩臂计算错误，展示长程自主调试能力（来源 [19]）。
- **记忆/上下文**：1M 上下文窗口支撑超长任务（来源 [19]）。
- **安全与对齐（权限收敛/多智能体控制）**：Kimi Code CLI 2.3.2（10-25）变更——默认直接处理任务而非主动派生子代理，请求委派须在消息/AGENTS.md/技能/多智能体模式中显式声明；Agent swarms 仅在你打开 swarm 模式时启动，智能体不能自行拉起 AgentSwarm（`kimi -p` 与 ACP 客户端如 Zed 中不再可用 swarms）。此为对多智能体自主性的主动收敛（来源 [22]）。K3.1 Pro 在中训练与 RL 两阶段主动识别并移除网络安全相关数据，xdev-bench-hard 由未清洗的 90.5% 降至 81.0%（pass@3），以降低开放权重误用风险（来源 [19]）。
- **事实准确性（幻觉）**：K3.1 Pro 在 Kimi Hallu Bench Hard 上将 claim 级幻觉率由 K3 的 23.4% 降至 8.3%（来源 [19]）。

#### 3.5.4 商业化与生态

- K3.1 Pro 经全产品族免费/会员分发：Kimi Agents（App）、Kimi Work（桌面端 3.1.0+）、Kimi Code（`/model` 切换）、Kimi API；企业管理员默认关闭、可手动开启；Kimi Business 提供企业级数据隔离。来源 [19]。
- 上线后因限流与额度浪费向付费用户致歉，返还每位付费会员 25% 月额度，并削减不必要的子代理调用（10-26，来源 [40]，Pandaily/Cryptopolitan，10-26）。
- Kimi Researcher 本窗口内未见新的公开动态。

### 3.6 DeepSeek

#### 3.6.1 智能体产品发布与更新

- **DeepSeek Harness v0.2.2-alpha.2 + 实验性 subagent_oar 工具（10-28）**：DeepSeek 官方开源智能体运行时 DeepSeek Harness 发布预发布版本，新增实验性「subagent_oar 工具」插件，可将独立任务交给本机 Codex CLI 或 Claude CLI（统一调度外部编码智能体），另有 PR 视图、统计插件、工作树（worktree）等（来源 [6]，GitHub release，10-28；[25]，Pandaily，10-30）。
- **Super-agent 架构公开（10-31 晚）**：DeepSeek Harness 团队发布技术文章《Super-agent 设计探索：迈向更自主的 Agent 系统》，公开面向自主智能体的新架构（来源 [7]，人民网日文，11-02 转述；[8]，GitHub 仓库）。
- **`dsh-superagent-prototype` 开源（10-31，MIT）**：同日上线官方 GitHub 组织，仓库明文标注「研究原型，仅供参考，非官方 DeepSeek 产品」，大部分工程由编码智能体完成。原型为面向单个 GitHub 仓库的主动编码智能体，监听 GitHub 及（可选）飞书；当被允许者提出工作时，开启工作项、在自有智能体会话与目录中工作，并以 PR 等形式回复。来源 [8]（GitHub，10-31）。

#### 3.6.2 产品形态与能力

- **双层 Router-Worker 架构**：Super-agent 采用「上层单个 Router 模型 + 下层多个执行任务的 Worker 模型」两层结构，Router 负责调度、Worker 负责执行，实现「AI 指挥 AI」；强调事件驱动、异步多信道交互（来源 [7][26]）。
- **被动→主动范式**：原型贯彻「尽可能少占用人类注意力、尽可能多产出价值」的哲学——只在被明确要求或团队规则允许时行动，只在必须有人决策或可用结果时发声（来源 [8][26]）。

#### 3.6.3 突破的智能体挑战

- **长程任务可靠性 / 多智能体协作**：Router-Worker 分层实现任务编排与自主执行分工，是长程、多智能体系统的架构性探索（来源 [7][26]）；subagent_oar 将外部 Codex/Claude CLI 统一到单一模型可见入口，实现跨厂商编码智能体委派（来源 [6][25]）。
- **权限控制 / 安全对齐**：原型自带 Authorization（授权）文档（docs/002-authorization），设计「谁可以要求智能体干活」的授权边界与「最低注意力」行为原则（来源 [8]）。

#### 3.6.4 商业化与生态

- 本次为工程架构与开源原型公开，非商业产品发布；官方文档明确「非 DeepSeek 产品」「非生产就绪」，需自行评审后使用（来源 [8]）。
- DeepSeek Harness 为开源智能体运行时持续迭代，v0.2.2-alpha.2 面向「从 AI 编程工具迈向 Agent 编排平台」演进（来源 [6][25][24]）。

## 4. 智能体挑战突破对照

| 挑战维度 | Anthropic | OpenAI | Google | 智谱 GLM | Kimi | DeepSeek |
| --- | --- | --- | --- | --- | --- | --- |
| 长程任务可靠性 | —（本月无新评测成绩） | faster steering 提升纠偏实时性 [10] | — | — | Terminal-Bench 4.0 65.7%、Kimi Code Bench 3.0 Long-horizon 61.2% [19] | Router-Worker 分层面向长程自主 [7][26] |
| 工具使用 | Duet 接入 6000+ 连接器 [2] | 浏览器 Work 模式接管标签页 [12][13]；Decisions API 有界决策 [34] | ADK 五语言原生 MCP/A2A [14] | — | Kimi Code 支持 SSH/Docker/自定义命令环境 [22] | subagent_oar 调度本机 Codex/Claude CLI [6] |
| 记忆 | — | dot 判别「续线程 vs 新线程」[30][31] | — | — | 1M 上下文支撑长任务 [19] | — |
| 多智能体协作 | CLAUDE_CODE_SUBAGENT_EFFORT 解耦子代理努力度 [3][4] | — | ADK 经 A2A 跨语言互操作 [14] | — | Tower 每任务模型选择、并发上限 16→256 [22]；swarms 收敛为显式开启 [22] | Router-Worker 双层多 Worker [7][26] |
| 安全与对齐 | Duet 敏感操作强制审批+凭证隔离+独立验证 [2] | Chat/Work 双模式授权边界 [12][13] | Jules 关停聚焦 Antigravity（产品治理）[15][16] | — | 子代理/群组收拢为显式启动 [22]；网络数据主动移除 [19] | 授权文档 + 最低注意力原则 [8] |

> 说明：表格「—」表示本期窗口内该厂商未发现公开可核实的对应维度动态；矩阵内容均与第 3 节事实一致。

## 5. 本月趋势观察

1. **自主智能体从「被动应答」走向「主动值守」**：Anthropic 发布主动式智能体 Claude Duet（10-21，晨报、主动监控、云电脑后台执行，来源 [1][2]），DeepSeek 10-31 开源 dsh-superagent 强调「尽量少占人类注意力」并能在无人 @AI 时自主复现缺陷（来源 [8][26]），OpenAI 的 dot 获得「改写已排程自动化」的主动能力（来源 [30][31]）。三家厂商在同一月不约而同向「主动值守、按需行动」收敛，「何时行动、何时发声」的授权与注意力管理成为新一代自主智能体的核心竞争点。
2. **编码智能体治理进入团队精细化阶段**：Anthropic v2.1.316 引入 pooled group budgets 与子代理 effort 级设置（来源 [3][4]）；Google 以 Jules 关停、聚焦 Antigravity 收拢产品线（来源 [15][16]）；Kimi 则在 10-25 将子代理/群组的自主性显式收拢（默认不主动派生子代理）（来源 [22]）——表明「智能体自主性」正在普遍被用权限与治理机制「加约束」。
3. **开源自主智能体架构与跨厂商协作成为新焦点**：DeepSeek 在一个窗口内同时开源 dsh-superagent 原型（10-31）与 subagent_oar（10-28，统一调度本机 Codex/Claude CLI）（来源 [6][8]），Kimi Code 新增导入 Claude Code/Codex 会话（10-28）（来源 [22]）——编码智能体之间的「互操作/互相调度」链路开始成形。
4. **模型层持续为编码智能体下移成本、抬高能力下限**：Kimi K3.1 Pro 以开放权重在 Terminal-Bench 4.0 逼近最强闭源模型（来源 [19]），GLM-5.3 上架 Amazon Bedrock 面向企业编码智能体（来源 [39]），OpenAI Codex CLI 引入 GPT-6.1 Terra 与 memory v2（来源 [36]）。
5. **浏览器操作（computer use）进入大众化、但伴随授权边界收紧**：OpenAI 将 ChatGPT 扩展升级为可接管标签页的浏览器智能体并向所有套餐开放（来源 [12][13]）；Anthropic 通过 Duet 的「敏感操作强制审批+一次性虚拟卡」给出高权限智能体的安全范式（来源 [2]）——能力开放与安全护栏在本月被并行推进。

## 附录 A：参考来源

1. [Anthropic launches Claude Duet AI agent to rival Meta's Muse, OpenAI's Dots](https://f.aa.com.tr/en/americas/anthropic-launches-claude-duet-ai-agent-to-rival-metas-muse-openais-dots/4096538) — Anadolu Agency，2026-10-22
2. [Claude Duet by Anthropic: The New Personal AI Agent](https://technologyksa.com/en/blog/claude-duet-personal-agent) — Technology KSA，2026-10-26（事件 10-21）
3. [anthropics/claude-code v2.1.316（官方 release）](https://github.com/anthropics/claude-code/releases/tag/v2.1.316) — GitHub，2026-10-31
4. [Key Updates in Claude Code v2.1.316](https://devio2025-ecs-main-v3.developers.io/en/articles/20261031-cc-updates-v2-1-316/) — DevelopersIO，2026-10-31
5. [dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype) — deepseek-ai（GitHub），2026-10-31
6. [Release v0.2.2-alpha.2 · deepseek-ai/DeepSeek-Harness](https://github.com/deepseek-ai/DeepSeek-Harness/releases/tag/dsh-v0.2.2-alpha.2) — GitHub，2026-10-28
7. [AIがAIを管理 DeepSeekが新エージェントアーキテクチャ「Super-agent」を公開](https://j.people.com.cn/n3/2026/1102/c94476-20514657.html) — 人民網日本語版，2026-11-02（事件 10-31）
8. [DeepSeek 发布全新 Agent 架构「Super-agent」，让 AI 调度 AI](https://m.sohu.com/coo/zmtq/1095634733_99900743) — 环球网/搜狐，2026-11-01（事件 10-31）
9. [OpenAI 官方 Release Notes（Notas de lançamento）](https://openai.com/pt-BR/products/release-notes/) — openai.com，2026-10
10. [October 8, 2026 — Faster steering in Codex](https://reconn-ai.com/chatgpt-october-8-2026-faster-steering-in-codex) — reconn-ai，2026-10-08
11. [Codex now writes your next message for you（Composer predictions）](https://mixed-news.com/en/codex-composer-predictions-beta-on-by-default-tab-to-accept/) — MIXED，2026-10-11（事件 10-09）
12. [ChatGPT Can Now Do More in Chrome](https://www.techrepublic.com/article/news-openai-chatgpt-chrome-browser-integration-privacy/) — TechRepublic，2026-10-21（事件 10-15）
13. [Inside OpenAI's Chrome update](https://me.mashable.com/tech/77297/inside-openais-chrome-update-web-tab-context-automation-and-privacy-risks) — Mashable，2026-10-16
14. [One Agent Development Kit, five languages](https://cloud.google.com/blog/topics/developers-practitioners/one-agent-development-kit-five-languages/?hl=en) — Google Cloud Blog，2026-10-14
15. [Google is sunsetting its AI coding agent, Jules](https://www.theverge.com/tech/1022729/google-is-sunsetting-its-ai-coding-agent-jules) — The Verge，2026-10-29/10-31
16. [谷歌宣布 Jules AI 编程助手逐步关停](http://portal.nstl.gov.cn/choiceness/getChoicenessDetail.htm?controlType=openhome&recommendId=193906&serverId=82&uuid=743dfa8a0c84f4366941e430430d7950) — 国家科技图书文献中心（NSTL）转载，2026-10-27
17. [Kimi Code CLI GitHub 仓库（MoonshotAI/kimi-code）](https://github.com/moonshotai/kimi-code) — GitHub
18. [Kimi Code CLI Changelog](https://www.kimi.com/code/docs/en/kimi-code-cli/changelog.html) — kimi.com/code/docs，2026-10-30
19. [Introducing Kimi K3.1 Pro（官方技术博客）](https://www.kimi.com/en/blog/kimi-k3-1-pro) — Moonshot AI，2026-10-24
20. [月之暗面，发布新模型](https://finance.sina.com.cn/roll/2026-10-24/doc-iniwiutr7274146.shtml) — 新浪财经，2026-10-24
21. [让AI真正上线，腾讯云与三十家企业交出AI Agent落地答卷](https://www.chinaz.com/2026/1103/1785950.shtml) — chinaz，2026-11-03（事件 10-29）
22. [Kimi Code CLI Changelog（2.2.0~2.4.1 条目）](https://www.kimi.com/code/docs/en/kimi-code-cli/changelog) — kimi.com，2026-10
23. [Use the Claude Agent SDK with your Claude plan（官方条目转载，更新 10-07）](https://github.com/johnzfitch/claude-wiki/blob/main/17-Billing-Plans/use-the-claude-agent-sdk-with-your-claude-plan.md) — johnzfitch/claude-wiki
24. [DeepSeek Harness 0.2.2更新详解](https://news.qq.com/rain/a/20261031A0CQZE00) — 腾讯新闻，2026-10-31
25. [DeepSeek Harness Pre-Release Lets Its Main Agent Hand Off Tasks to Local Codex and Claude Code](https://pandaily.com/deepseek-harness-v0-2-2-alpha-2-subagent-oar-delegate-tasks-codex-cli-claude-code) — Pandaily，2026-10-30
26. [DeepSeek开源超级智能体：人终于不用再给Agent当保姆了](https://m.163.com/dy/article/LAVUH0FL051481US.html) — 网易，2026-11-05（事件 10-31）
27. [DeepSeek开源Agent架构，想让人少给AI打工](https://news.sohu.com/a/1095881565_115207) — 搜狐，2026-11-02（事件 10-31）
28. [Faster steering in Codex（官方 Release Notes 对应条）](https://openai.com/pt-BR/products/release-notes/) — openai.com，2026-10-08
29. [Your ChatGPT dot can now edit the automations you scheduled](https://mixed-news.com/en/chatgpt-dots-mobile-app-codex-threads-work-automations/) — MIXED，2026-10-11（事件 10-05~10-09）
30. [Create your dot in the ChatGPT mobile app](https://learn.chatgpt.com/docs/whats-new/dots-october-9-2026) — OpenAI ChatGPT Learn，2026-10-05~10-09
31. [OpenAI Dots Mobile Version Launches 5 Days Post Debut](https://eu.36kr.com/en/p/4019410492346244) — 36氪（英文），2026-10-10
32. [Lead the OpenAI AgentKit page with the Agent Builder shutdown migration（PR #9460）](https://github.com/simstudioai/sim/pull/9460/files) — simstudioai/sim，2026-10-30
33. [OpenAI Agents API vs Responses API vs Agents SDK vs AgentKit](https://apidog.com/blog/openai-agents-api-vs-responses-api-vs-agents-sdk/) — apidog，2026-10-02
34. [OpenAI全面开放Decisions API：输出Token不收费](https://ai.cnmo.com/news/820930.html) — CNMO，2026-10-23（事件 10-22）
35. [OpenAI enters Jev's turf with a decision API for AI agents](https://economictimes.indiatimes.com/ai/ai-insights/openai-enters-jevs-turf-with-a-decision-api-for-ai-agents/printarticle/135168886.cms) — The Economic Times，2026-10-24
36. [Codex CLI Changelog: rust-v0.165.0](https://www.havoptic.com/tools/openai-codex) — Havoptic，2026-10-27
37. [ai-agent-map/agents/autoglm.md](https://github.com/weijt606/ai-agent-map/blob/main/agents/autoglm.md) — weijt606/ai-agent-map，记录日期 2026-04-09
38. [智谱发布 GLM-Legal 法律智能体模型](https://www.ailyre.com/source/?id=zhipu-glm-legal-launch-2026-10-12&lang=zh) — ailyre，2026-10-13（事件 10-12）
39. [GLM 5.3 by Z.ai 现已在 Amazon Bedrock 上正式推出](https://aws.amazon.com/cn/about-aws/whats-new/2026/10/amazon-bedrock-glm-5-3/) — AWS，2026-10-05
40. [Moonshot resets Kimi K3.1 Pro quotas after rate-limit apology](https://coinmarketcap.com/community/articles/6adf1ec5e62f6a7c33638415/) — CoinMarketCap/Cryptopolitan，2026-10-26

---

**生成说明**：本报告基于 keyword.md 第二部分「智能体厂商发展报告」关键字与六家厂商清单联网检索，优先采用官方公告、技术文档（GitHub release、官方 changelog、官方技术博客、Google Cloud Blog、AWS What's New）与企业原始案例；每条动态区分事件日期与报道日期，均附可访问 Markdown 来源链接。覆盖窗口严格限定 2026-10-01 ~ 10-31，窗口外事件（如 Anthropic Message Threads beta 于 11-02 发布、Codex `/voice` 于 9 月末引入）未纳入本期。

需说明：**智谱 GLM 本窗口内未发现可核实的新智能体产品发布**，各小节已按规范标注「检索未发现可核实动态/案例」，GLM-Legal（法律模型）与 GLM-5.3 Bedrock 上架属模型层动态，仅作提示不纳入产品表。旧报告中经检索确认不存在以「> **用户观点**」标记的原文，故本期无用户观点块需要延续保留；其余事实均已重新联网核实，未将旧报告作为事实来源。
