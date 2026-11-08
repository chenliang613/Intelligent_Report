# 2026年10月 智能体发展报告

- **期数**：2026-10
- **覆盖窗口**：2026-10-01 ~ 2026-10-31
- **生成日期**：2026-11-08

## 1. 本期摘要

1. **DeepSeek**：10-31 晚 DeepSeek Harness 团队发布《Super-agent 设计探索：迈向更自主的 Agent 系统》，并同日以 MIT 协议开源配套原型 `dsh-superagent-prototype`——一个「主动接活」的编码智能体，监听 GitHub 仓库与飞书群聊（来源 [[1]](#来源1)、[[2]](#来源2)）——自主智能体从「被动应答」走向「主动值守、按需行动」。
2. **Anthropic**：Claude Code 整个 10 月密集迭代（2.1.287→2.1.316），月底加入 pooled group budgets（组共享预算）与 `CLAUDE_CODE_SUBAGENT_EFFORT`（子代理努力度设置）（来源 [[3]](#来源3)）——编码智能体进入团队级治理与成本精细化管理阶段。
3. **Anthropic**：约 10-07 更新官方支持页面，正式确认 Claude Max/Team 订阅额度可接入 Claude Agent SDK、`claude -p`、Claude API 及第三方 App（来源 [[4]](#来源4)）——「自带订阅（BYOS）」政策扫清第三方智能体生态的「双重收费」障碍。
4. **OpenAI**：10-15 将 ChatGPT Chrome 扩展升级为浏览器智能体，Chat 模式跨标签页读取、Work 模式直接接管标签页填表/发消息/下载文件（来源 [[5]](#来源5)）——浏览器的「计算机使用」进入大众套餐。
5. **Google**：10 月下旬宣布逐步关停异步编码智能体 Jules，能力沉淀整合进 Antigravity（来源 [[6]](#来源6)、[[7]](#来源7)）——大厂异步编码智能体产品线开始收拢聚焦。
6. **月之暗面**：10-24 发布 Kimi K3.1 Pro（含 Highspeed），显著强化长程智能体能力，并同步在 Kimi Code 中可用（来源 [[8]](#来源8)）——模型层为编码智能体任务提供更强底座。

## 2. 月度总览

| 厂商 | 产品/发布 | 类型 | 简述 | 日期 |
| --- | --- | --- | --- | --- |
| Anthropic | Claude Code 2.1.287–2.1.316 | 编码 | 组共享预算、子代理努力度、Monitor 工具多平台支持等 | 10-01~10-31 |
| Anthropic | 第三方应用政策解禁 | 生态/安全 | 订阅额度可接入 Agent SDK 与第三方 App | 约10-07 |
| OpenAI | Codex Composer predictions（beta） | 编码 | 基于当前会话预测下一条消息 | 10-09 |
| OpenAI | Codex faster steering | 编码 | 桌面端加速任务中途调整响应 | 10-08 |
| OpenAI | ChatGPT dot 增强 | 通用/自动化 | dot 可编辑 Work 自动化并在 Codex 起任务 | 10-05~10-09 |
| OpenAI | ChatGPT Chrome 扩展浏览器智能体 | 浏览器 | Chat/Work 双模式读写标签页 | 10-15 |
| Google | ADK 五语言 | 开发框架 | Python/Go/TypeScript/Java/Kotlin 全覆盖 | 10-14 |
| Google | Jules 关停 | 编码 | 异步编码智能体逐步停用，并入 Antigravity | 约10-27~10-29 |
| 智谱 GLM | — | — | 本期未发现可核实的智能体产品新发布 | — |
| Kimi（月之暗面） | Kimi K3.1 Pro / Highspeed | 模型支撑 | 长程智能体与编码代理能力显著提升 | 10-24 |
| DeepSeek | Super-agent 架构 + dsh-superagent 原型 | 编码/自主 | 双层 Router-Worker 自主智能体，MIT 开源 | 10-31 |

## 3. 分厂商详情

### 3.1 Anthropic

#### 3.1.1 智能体产品发布与更新

- **Claude Code 10 月密集版本迭代**：由第三方版本追踪（Havoptic）汇总，本月覆盖 2.1.287（10-01）至 2.1.316（10-31）多个版本，关键节点包括：2.1.291/2.1.292（10-06）修复聊天消息丢失、支持从插件市场直接安装插件；2.1.293（10-07）默认切换到速度更快、更经济的 Haiku 5.5 并带 1M 上下文；2.1.302（10-16）默认开启 forked subagents；2.1.310（10-23）将 Monitor 工具扩展到 Bedrock、Vertex、Foundry；2.1.316（10-31）加入 pooled group budgets 与 subagent effort 设置。来源 [[3]](#来源3)，2026-10。
- **2026 使用政策更新**（窗口前旧报告背景，约 10-08 前后）已在旧报告记录，本期无新增公开动态。

#### 3.1.2 产品形态与能力

- Claude Code 本月强化了**团队级成本治理**：2.1.316 引入 pooled group budgets——一个组内成员共享的月度预算，并新增 `CLAUDE_CODE_SUBAGENT_EFFORT` 环境变量，可单独指定子代理运行的 effort level，而不再一律继承会话设置。来源 [[3]](#来源3)。
- 多平台运行与监控：2.1.310 将 Monitor 工具（此前仅部分平台）扩展至 AWS Bedrock、Google Vertex、Microsoft Foundry。来源 [[3]](#来源3)。

#### 3.1.3 突破的智能体挑战

- **多智能体协作**：2.1.302 默认开启 forked subagents（分叉子代理），子代理可并行派生；2.1.316 引入 `CLAUDE_CODE_SUBAGENT_EFFORT`，让主会话与子代理的「努力度」解耦——子代理协作的粒度与算力调度更精细。来源 [[3]](#来源3)。
- **记忆/上下文压缩**：本月多个版本围绕 idle compaction（空闲时自动压缩上下文）与 `autoCompactWindow` 行为做修复与优化，长会话记忆管理持续改进。来源 [[3]](#来源3)。

#### 3.1.4 商业化与生态

- **第三方应用政策解禁（约 10-07）**：官方支持页面更新确认，Claude Max 与 Team 计划用户的月度 API Credits 可直接用于 Claude Agent SDK、`claude -p` 命令、Claude API、Claude Managed Agents 及所有基于上述技术的第三方 App。媒体解读为「BYOS（自带订阅）」模式，打破「用户已订阅 Claude 仍须向第三方开发者二次付费」的僵局。来源 [[4]](#来源4)，2026-10-15（报道日期，事件约 10-07）。
- 开发者生态：Claude Agent SDK 持续更新，本月初加入 agent_id、远程会话延迟字段等；第三方插件市场支持在 2.1.292 落地。来源 [[3]](#来源3)、[[9]](#来源9)。

### 3.2 OpenAI

#### 3.2.1 智能体产品发布与更新

- **Codex Composer predictions（10-09，beta）**：Codex 现可根据当前线程的对话预测你的下一条消息，接受建议不会自动发送；beta 期间生成预测不计入 Codex 用量/额度，Personal Pro 用户默认开启。来源 [[10]](#来源10)、[[11]](#来源11)。
- **Codex faster steering（10-08，GA）**：桌面端 ChatGPT 里对正在运行的任务发送后续指令以调整方向时，Codex 能更快响应。来源 [[12]](#来源12)。
- **ChatGPT dot 增强（10-05~10-09）**：dot（9 月末推出的常驻智能体）现可读取并编辑已设置的 ChatGPT Work automations，并能在 Codex 中开始新任务或接续既有线程；同时支持在移动 App 中创建与配置 dot。来源 [[13]](#来源13)。
- **ChatGPT Chrome 扩展升级为浏览器智能体（10-15）**：官方 X 帖子宣布扩展支持 Chat 与 Work 两种模式——Chat 模式跨标签页查找信息，Work 模式可在授权后操作网页（发消息、填表、下载文件），并向所有套餐开放。来源 [[5]](#来源5)、[[14]](#来源14)。

#### 3.2.2 产品形态与能力

- **dot 与 Codex / Work automation 打通**：dot 作为常驻后台智能体，开始获得「读取并改写已排程任务」的能力，并接入 Codex 线程执行编码工作，形成「聊天—编码—自动化」一体化的智能体入口。来源 [[13]](#来源13)。
- **浏览器操作（computer use）能力**：Chrome 扩展由「读标签页回答」升级为「接管标签页执行操作」，浏览器智能体进入大众用户套餐。来源 [[5]](#来源5)、[[14]](#来源14)。

#### 3.2.3 突破的智能体挑战

- **任务可靠性/人机协同**：faster steering 缩短「纠偏指令 → 智能体收到」的延迟，直接提升长任务中对智能体的实时干预效率（来源 [[12]](#来源12)）；dot 对「继续既有 Codex 线程 vs 新起线程」的判别与 Work automation 编辑，指向长程任务上下文延续能力（来源 [[13]](#来源13)）。
- **安全与权限**：浏览器智能体采用「Chat 只读 / Work 需授权操作」的双模式，对操作型能力施加授权边界（来源 [[5]](#来源5)）。

#### 3.2.4 商业化与生态

- **AgentKit 收缩**：Agent Builder 与 Evals 平台按既定计划关停——Evals 平台 10-31 起进入只读，Agent Builder 与 Evals API/面板将于 11-30 全面关闭（该停用于 6-03 即已公布，本窗口内为执行节点）；ChatKit 保留可用，代码类工作流被引导至 Agents SDK 或 ChatGPT Workspace Agents。来源 [[15]](#来源15)、[[16]](#来源16)。

### 3.3 Google

#### 3.3.1 智能体产品发布与更新

- **Jules 逐步关停（约 10-27 ~ 10-29 公告）**：谷歌宣布逐步停用异步 AI 编码智能体 Jules（2024-12 上线），并将其积累的异步智能体、代码调试、工程任务经验整合进 Antigravity 智能体优先开发平台。Jules 文档的「Jules Turndown」条目（10-29）设定时间表：11-11 前可完成进行中会话并进入只读，12-31 全面下线。来源 [[6]](#来源6)、[[7]](#来源7)。
- **Agent Development Kit（ADK）五语言（10-14）**：ADK 现已覆盖 Python、Go、TypeScript、Java、Kotlin 五种语言，各自针对运行时与类型系统原生构建，共享统一架构并通过开放协议互通。来源 [[17]](#来源17)。
- **Gemini CLI 多次版本更新**：v0.63.0（10-06）、v0.64.0（10-13）、v0.65.0（10-20）。来源 [[18]](#来源18)。

#### 3.3.2 产品形态与能力

- **ADK 每一门语言原生支持 MCP 客户端**，多智能体系统通过 Agent2Agent（A2A）协议实现跨语言、跨框架的 HTTP 互通；Python 为参考实现（含最广的 BigQuery/Spanner/Bigtable 集成与 Gemini/Anthropic/OpenAI/LiteLLM 模型适配器），Go 面向生产后端（支持 ADK 2.0 Graph Workflow）、Kotlin 专注构建期类型安全与端侧运行（LiteRT-LM / Gemini Nano）。来源 [[17]](#来源17)。
- Jules 关停后，其能力并入 Antigravity 平台，形成「单一智能体优先编码平台」的聚焦形态。来源 [[6]](#来源6)、[[7]](#来源7)。

#### 3.3.3 突破的智能体挑战

- **多智能体协作/互操作**：ADK 五语言经 MCP + A2A 协议实现跨语言、跨框架的智能体互操作，多智能体系统的异构协作边界被进一步打开。来源 [[17]](#来源17)。
- **工具使用**：ADK 各语言均原生接入 MCP 工具与 A2A 远程智能体调用，工具生态的统一化是本月重点。来源 [[17]](#来源17)。

#### 3.3.4 商业化与生态

- 产品线收拢：Jules 的关停表明谷歌将异步编码智能体资源聚焦于 Antigravity，开发者被引导至该平台（来源 [[6]](#来源6)、[[7]](#来源7)）。ADK 借 `agents-cli` 脚手架与 `adk.dev/llms.txt` 面向编码智能体提供按需文档，强化开发者生态（来源 [[17]](#来源17)）。

### 3.4 智谱 GLM

#### 3.4.1 智能体产品发布与更新

检索未发现可核实动态/案例。本窗口内未见智谱 AutoGLM 的官方新版本发布公告；网传「AutoGLM 2.0 上线」等说法实为 2025-08 已发布的产品（来源为历史报道），并非 2026-10 事件，不纳入本期。当前可核实的 AutoGLM 产品为 2025 年 8 月发布的 ToC 手机通用智能体 AutoGLM 2.0（云机/云电脑形态），本期无新增官方公告。

#### 3.4.2 产品形态与能力

检索未发现可核实动态/案例。当前形态仍以「Agent + 云手机 + 云电脑」为底座，支持 50+ 高频应用操作与离线任务；「定时任务」功能长期处于「即将上线」状态，本窗口内未见官方落地公告。

#### 3.4.3 突破的智能体挑战

检索未发现可核实动态/案例。

#### 3.4.4 商业化与生态

检索未发现可核实动态/案例。开源项目 Open-AutoGLM（Apache-2.0）近期无新提交的公开记录。

### 3.5 Kimi（月之暗面）

#### 3.5.1 智能体产品发布与更新

- **Kimi K3.1 Pro / K3.1 Pro Highspeed（10-24 发布）**：虽属模型发布，但直接服务编码智能体（Kimi Code）与长程智能体能力，本期纳入。K3.1 Pro 同步在 Kimi.com、Kimi Work、Kimi Code 与 Kimi API 上线；Kimi Code 用户可经 `/model` 命令切换到 K3.1 Pro。来源 [[8]](#来源8)、[[19]](#来源19)。
- 完整模型权重预计 11-04 前发布。来源 [[8]](#来源8)。

#### 3.5.2 产品形态与能力

- K3.1 Pro 定位为「3T 级开放权重、1M 上下文」，显著强化编码、3D 创作、金融研究与「其他智能体能力」，支持端到端完成完整金融工作流与长步骤多任务。来源 [[8]](#来源8)、[[19]](#来源19)。
- Kimi Code（终端编码智能体）作为 K3.1 Pro 的落地载体，支持无 API Key 的会员通道使用。来源 [[19]](#来源19)。

#### 3.5.3 突破的智能体挑战

- **长程任务可靠性 / 工具使用**：K3.1 Pro 在编码智能体基准 Terminal-Bench 4.0 得分 65.7%（高于 GPT-6 Astra 的 58.2%，略低于 Claude Opus 5.5 的 66.4%）；在内部长程基准 Kimi Code Bench 3.0 Long-horizon 得分 61.2%（高于 K3 的 55.95%），该基准测试编码智能体的多步执行、工具使用与端到端问题求解。来源 [[8]](#来源8)。
- **记忆/上下文**：1M 上下文窗口支撑超长任务；在「人类步态动力学模拟器」内部长程测试中，K3.1 Pro 跨 167 个任务迭代训练控制器，主动定位并修正 36 处肩部肌肉力矩臂计算错误，展示出长程自主调试能力。来源 [[8]](#来源8)。
- **安全与对齐**：为降低开放权重误用风险，K3.1 Pro 在中训练与 RL 两阶段识别并移除网络相关数据，xdev-bench-hard 由未清洗样本的 90.5% 降至最终 81.0%（pass@3）。来源 [[8]](#来源8)。

#### 3.5.4 商业化与生态

- K3.1 Pro 通过 Kimi 全产品族免费/会员分发：Kimi Agents（App）、Kimi Work（桌面端 3.1.0+）、Kimi Code（`/model` 切换）、Kimi API（`kimi-k3.1-pro` / `kimi-k3.1-pro-highspeed`，支持零数据保留）。企业管理员默认关闭、可手动开启。来源 [[8]](#来源8)。
- Kimi Researcher 本窗口内未见新的公开动态。

### 3.6 DeepSeek

#### 3.6.1 智能体产品发布与更新

- **Super-agent 架构公开（10-31 晚）**：DeepSeek Harness 团队发布技术文章《Super-agent 设计探索：迈向更自主的 Agent 系统》，公开一套面向自主智能体的新架构。来源 [[1]](#来源1)、[[20]](#来源20)。
- **`dsh-superagent-prototype` 开源（10-31，MIT）**：同日将原型代码发布到官方 GitHub 组织，仓库明文标注「研究原型，仅供参考，非官方产品」，绝大部分工程由编码智能体完成。原型为面向单个 GitHub 仓库的主动编码智能体，监听 GitHub 及（可选）飞书群聊，当被允许时接活、在自有会话与目录中工作，并回复如 PR。来源 [[2]](#来源2)。

#### 3.6.2 产品形态与能力

- **双层 Router-Worker 架构**：Super-agent 采用「上层单个 Router 模型 + 下层多个执行任务的 Worker 模型」两层结构，Router 负责调度、Worker 负责干活，实现「AI 指挥 AI」。来源 [[1]](#来源1)、[[20]](#来源20)。
- **被动→主动范式**：原型强调「尽可能少占用人类注意力、尽可能多产出价值」的哲学——只在被明确要求或团队规则允许时行动，只在必须有人决策时发声；作者在群聊中反馈软件问题时即使无人 @AI，系统也能自主识别缺陷、后台复现并寻找修复方案（来源 [[1]](#来源1)、[[20]](#来源20)，第三方转述）。

#### 3.6.3 突破的智能体挑战

- **长程任务可靠性 / 多智能体协作**：Router-Worker 分层实现任务编排与自主执行的分工，是长程、多智能体系统的架构性探索（来源 [[1]](#来源1)、[[20]](#来源20)）。
- **权限控制/安全对齐**：原型自带 Authorization（授权）文档（docs/002-authorization），设计了「谁可以要求智能体干活」的授权边界与「最低注意力」行为原则（来源 [[2]](#来源2)）。

#### 3.6.4 商业化与生态

- 本次为工程架构与开源原型公开，非商业产品发布；官方文档明确「非 DeepSeek 产品」「非生产就绪」，需自行评审后使用。来源 [[2]](#来源2)。
- 参考官方智能体集成文档（[api-docs.deepseek.com](https://api-docs.deepseek.com/quick_start/agent_integrations/)），本窗口内无第三方集成新增的官方公告。

## 4. 智能体挑战突破对照

| 挑战维度 | Anthropic | OpenAI | Google | 智谱 GLM | Kimi | DeepSeek |
| --- | --- | --- | --- | --- | --- | --- |
| 长程任务可靠性 | idle compaction 持续优化 [3] | faster steering 提升纠偏实时性 [12] | — | — | Terminal-Bench 4.0 达 65.7% [8] | Router-Worker 分层面向长程自主 [1][20] |
| 工具使用 | Monitor 工具扩展 Bedrock/Vertex/Foundry [3] | 浏览器 Work 模式接管标签页操作 [5] | ADK 五语言原生 MCP/A2A [17] | — | Kimi Code Bench 3.0 Long-horizon 61.2% [8] | 监听 GitHub/飞书自动接活 [2] |
| 记忆 | autoCompactWindow / 空闲压缩修复 [3] | dot 判别「续线程 vs 新线程」[13] | — | — | 1M 上下文支撑长任务 [8] | — |
| 多智能体协作 | forked subagents 默认开启 + SUBAGENT_EFFORT [3] | — | ADK 经 A2A 跨语言互操作 [17] | — | — | Router-Worker 双层多 Worker [1][20] |
| 安全与对齐 | 订阅额度解禁政策（生态开放）[4] | Chat/Work 双模式授权边界 [5] | Jules 关停聚焦 Antigravity（产品治理）[6][7] | — | 网络数据主动移除降风险 [8] | 授权文档 + 最低注意力原则 [2] |

> 说明：表格「—」表示本期窗口内该厂商未发现公开可核实的对应维度动态；矩阵内容均与第 3 节事实一致。

## 5. 本月趋势观察

1. **自主智能体从「被动应答」走向「主动值守」**：DeepSeek 10-31 开源 dsh-superagent，明确「尽量少占人类注意力」的行为哲学（来源 [[2]](#来源2)）——识别无人 @AI 也能自主复现缺陷（来源 [[20]](#来源20)）；OpenAI 的 dot 同样获得「改写已排程自动化」的主动能力（来源 [[13]](#来源13)）。自主性提升的同时，「何时行动、何时发声」的授权与注意力管理成为新焦点。
2. **编码智能体治理进入团队精细化阶段**：Anthropic 在 2.1.316 引入 pooled group budgets 与子代理 effort 级设置（来源 [[3]](#来源3)），从「个人工具」走向「团队预算+权限」的治理工具；Google 则以 Jules 关停、聚焦 Antigravity 的方式收拢产品线（来源 [[6]](#来源6)、[[7]](#来源7)）。
3. **「订阅额度解锁第三方智能体」成为生态竞争新杠杆**：Anthropic 约 10-07 解禁订阅额度接入第三方 App/Agent SDK（来源 [[4]](#来源4)），打破双重收费，与 OpenAI 收缩 AgentKit（来源 [[15]](#来源15)、[[16]](#来源16)）形成「开放生态 vs 收拢整合」的路线对照。
4. **模型层持续为智能体任务下移成本与提升能力下限**：Kimi K3.1 Pro 以开放权重在 Terminal-Bench 4.0 逼近最强闭源模型（来源 [[8]](#来源8)），Claude Code 默认模型切换至更快的 Haiku 5.5（来源 [[3]](#来源3)），编码智能体任务的成本与能力曲线同时改善。
5. **浏览器操作（computer use）进入大众化**：OpenAI 将 ChatGPT 扩展升级为可接管标签页的浏览器智能体并向所有套餐开放（来源 [[5]](#来源5)、[[14]](#来源14)），浏览器智能体从实验走向普及。

## 附录 A：参考来源

1. <a id="来源1"></a>[DeepSeek 发布全新 Agent 架构（环球网科技，10-31 晚官方公众号文章转述）](https://m.sohu.com/coo/zmtq/1095634733_99900743) — 环球网科技 / 搜狐，2026-11-01（事件日期 2026-10-31）
2. <a id="来源2"></a>[deepseek-ai/dsh-superagent-prototype（GitHub）](https://github.com/deepseek-ai/dsh-superagent-prototype) — DeepSeek AI（GitHub），2026-10-31
3. <a id="来源3"></a>[Claude Code Changelog（Havoptic 版本追踪汇总）](https://www.havoptic.com/tools/claude-code) — Havoptic，2026-10（最新 2.1.319）
4. <a id="来源4"></a>[刚刚，Claude彻底解禁第三方应用](https://36kr.com/p/4026370532790145?f=rss) — 36氪（新智元授权），2026-10-15（事件约 2026-10-07）
5. <a id="来源5"></a>[Inside OpenAI's Chrome update（含官方 X 帖）](https://me.mashable.com/tech/77297/inside-openais-chrome-update-web-tab-context-automation-and-privacy-risks) — Mashable，2026-10-16
6. <a id="来源6"></a>[Google is sunsetting its AI coding agent, Jules](https://www.theverge.com/tech/1022729/google-is-sunsetting-its-ai-coding-agent-jules) — The Verge，2026-10-29
7. <a id="来源7"></a>[Google Jules Shutdown Dec 31: Export Guide + Alternatives](https://explainx.ai/blog/google-jules-shutdown-december-31-antigravity-export-guide-2026) — ExplainX，2026-10-30
8. <a id="来源8"></a>[Introducing Kimi K3.1 Pro（官方技术博客）](https://www.kimi.com/en/blog/kimi-k3-1-pro) — Moonshot AI，2026-10-24
9. <a id="来源9"></a>[Claude Agent SDK Changelog (October 2026)](https://www.gradually.ai/en/changelogs/claude-agent-sdk/) — Gradually，2026-10（至 10-07 条目）
10. <a id="来源10"></a>[Codex now writes your next message for you（Composer predictions）](https://mixed-news.com/en/codex-composer-predictions-beta-on-by-default-tab-to-accept/) — MIXED，2026-10-11（事件 2026-10-09）
11. <a id="来源11"></a>[Notas de lançamento | OpenAI（官方 Release Notes）](https://openai.com/pt-BR/products/release-notes/) — OpenAI，2026-10（Codex 9 de out. 条目）
12. <a id="来源12"></a>[OpenAI 官方 Release Notes — Faster steering in Codex（8 de out.）](https://openai.com/pt-BR/products/release-notes/) — OpenAI，2026-10-08
13. <a id="来源13"></a>[Your ChatGPT dot can now edit the automations you scheduled, and start your Codex work](https://mixed-news.com/en/chatgpt-dots-mobile-app-codex-threads-work-automations/) — MIXED，2026-10-11（事件 10-05~10-09）
14. <a id="来源14"></a>[ChatGPT Can Now Control Your Browser: Fill Forms, Send Messages, and Take Over Your Tabs](https://tech.yahoo.com/ai/chatgpt/articles/chatgpt-now-control-browser-fill-185017541.html) — Yahoo Tech，2026-10-20
15. <a id="来源15"></a>[OpenAI Agents API vs Responses API vs Agents SDK vs AgentKit](https://apidog.com/blog/openai-agents-api-vs-responses-api-vs-agents-sdk/) — Apidog，2026-10-02
16. <a id="来源16"></a>[OpenAI AgentKit Has Fragmented（Agent Builder/Evals 关停时间线）](https://devio2025-ecs-main-v3.developers.io/en/articles/openai-agentkit-workspace-agents-claude-cowork-nocode-agent-comparison/) — DevelopersIO，2026-07-13（停用公告时间线）
17. <a id="来源17"></a>[One Agent Development Kit, five languages](https://cloud.google.com/blog/topics/developers-practitioners/one-agent-development-kit-five-languages/?hl=en) — Google Cloud Blog，2026-10-14
18. <a id="来源18"></a>[Gemini CLI changelogs（latest / v0.63.0 / v0.64.0 / v0.65.0）](https://geminicli.com/docs/changelogs/latest) — Google，2026-10
19. <a id="来源19"></a>[月之暗面发布新一代开源模型 Kimi K3.1 Pro（北京市科委转载）](https://kw.beijing.gov.cn/xwdt/kcyx/xwdtyqqy/202610/t20261026_4918451.html) — 北京市科学技术委员会，2026-10-26
20. <a id="来源20"></a>[DeepSeek 发布全新 Agent 架构「Super-agent」，让 AI 调度 AI](https://finance.sina.com.cn/wm/2026-10-31/doc-inixcwwm7197135.shtml) — 新浪财经，2026-10-31

---

**生成说明**：本报告基于 keyword.md 第二部分「智能体厂商发展报告」关键字与厂商清单联网检索，优先采用官方公告、技术文档与企业原始案例；覆盖窗口内事件均标注事件日期与来源。智谱 GLM 本窗口内未发现可核实的智能体产品新动态，各小节已按规范标注「检索未发现可核实动态/案例」；AutoGLM 2.0 为 2025-08 发布的历史产品，未纳入本期。旧报告中未发现以「> **用户观点**」标记的原文，故本期无用户观点块需要延续。
