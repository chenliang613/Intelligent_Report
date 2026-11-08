# 2026年10月 模型发展报告

- **期数**：2026-10
- **覆盖窗口**：2026-10-01 ~ 2026-10-31
- **生成日期**：2026-11-08

## 1. 本期摘要

1. **月之暗面（Kimi）**：10-24 发布 3 万亿级参数开源模型 Kimi K3.1 Pro，官方称其为「迄今能力最强的 3 万亿级参数模型」，智能指数逼近最强闭源模型，并同步推出高速版 Highspeed（来源：[Kimi K3.1 Pro 发布报道](https://www.cnstock.com/commonDetail/808507)，2026-10-24）——中国开源权重模型首次把与闭源前沿的智能差距压缩到约 3 分，标杆意义显著。
2. **OpenAI**：10-26 发布中档模型 GPT-6.1 Terra，标准 API 定价输入 $1 / 输出 $5 每百万 token，为 GPT-5.6 Terra 与 GPT-6.1 Sol 的一半，聚焦计算机操作、视觉理解与日常办公自动化（来源：[Dataconomy 报道](https://www.dataconomy.com/2026/10/27/openai-gpt-6-1-terra-api-50-percent-cheaper-sol/)，2026-10-27）——「以价换量」路线从旗舰延伸至中档模型。
3. **DeepSeek**：10-17 发布 DeepSeek-V4.1-Flash-1017，在基准、运行速度与输出长度上实现「性能-成本的帕累托改进」，权重以 MIT 协议在 Hugging Face / ModelScope 开源，并同步向所有开发者开放自研 Search & Fetch API（来源：[DeepSeek 官方公告](https://api-docs.deepseek.com/news/news261017.md)，2026-10-17）——单次更新同时覆盖模型升级、开源与搜索基础设施。
4. **Google**：旗舰 Gemini 4 Argon 于 10-13 在 Gemini API 正式可用（9-30 首发），推广价 $2/$10 每百万 token；同月 10-06 发布端侧多模态嵌入模型 EmbeddingGemma 2（来源：[Gemini 4 Argon](https://china.googleblog.com/2026/10/gemini-4-argon_0397895399.html)，2026-10-14；[Gemma releases](https://ai.google.dev/gemma/docs/releases)，2026-10-06）——旗舰落地与端侧轻量模型并行推进。
5. **Anthropic**：10-07 发布 Claude Haiku 5.5，补齐 5.5 家族，官方称其为「迄今最快、最强的小型模型」，≤100K token 请求输入价降至 $0.10 每百万（来源：[Claude release notes](https://support.claude.com/en/articles/12138966-release-notes)，2026-10-07）——小型模型以价换量承接高频与智能体任务。

## 2. 月度总览

| 厂商 | 动态类型 | 动态简述 | 日期 |
| --- | --- | --- | --- |
| Anthropic | 发布 | Claude Haiku 5.5 发布，补齐 5.5 家族；Max/Team 订阅新增每月 API 额度 | 10-07 |
| Anthropic | 产品 | Claude Duet 研究预览上线（Pro/Max，属智能体产品） | 10-21 |
| OpenAI | 发布/下线 | GPT-6 Sol/Luna 全量开放；GPT-5.5 退役 | 10-07 / 10-14 |
| OpenAI | 发布 | GPT-6.1 Terra 发布，API 定价减半 | 10-26 |
| Google | 发布 | Gemini 4 Argon 在 Gemini API 正式可用 | 10-13 |
| Google | 发布 | EmbeddingGemma 2（740M 开放权重）发布 | 10-06 |
| Google | 定价/分层 | Gemini 应用免费档仅保留 Flash-Lite，AI Plus 失去 Pro | 10-09 起 |
| 智谱 GLM | 灰度/第三方 | GLM-5.3-Highspeed 在 ZCode 灰度测试；Cursor 上线 GLM-5.3/5.3-Flash | 10-12 / 10-05 |
| 智谱 GLM | 传闻 | 市场传闻 GLM-5.5 将发布（非官方，未证实） | 10-22 |
| Kimi（月之暗面） | 发布 | Kimi K3.1 Pro 及 Highspeed 版发布 | 10-24 |
| DeepSeek | 更新/开源 | DeepSeek-V4.1-Flash-1017 更新，MIT 开源；开放 Search & Fetch API | 10-17 |

## 3. 分厂商详情

### 3.1 Anthropic

#### 3.1.1 模型发布与版本更新

- **Claude Haiku 5.5**（10-07）：Claude 5.5 家族第三款、也是补齐版本（Opus 5.5 于 9-22、Sonnet 5.5 于 9-28 发布）。官方将其定位为「迄今最便宜、最快、最强的小型模型」，面向高吞吐、成本敏感任务（来源：[Claude release notes](https://support.claude.com/en/articles/12138966-release-notes)，2026-10-07）。

#### 3.1.2 能力与特性

- Haiku 5.5 相对 Haiku 4.5 在编码、工具使用、computer use 与智能体（agentic）任务上有显著提升，官方称其为「首个可信的 Haiku 智能体」（来源：[Claude Haiku 5.5 发布](https://www.anthropic.com/claude-haiku-5-5)，2026-10-07；[LLM-Stats 技术解析](https://llm-stats.com/blog/research/claude-haiku-5-5-launch)，2026-10-07）。

#### 3.1.3 价格与开放策略

- **Haiku 5.5 定价**：≤100K token 请求输入 $0.10、输出 $0.50 每百万 token；>100K 请求输入 $0.50、输出 $2.50（来源：[NSTL 转载报道](http://portal.nstl.gov.cn/choiceness/getChoicenessDetail.htm?serverId=42&uuid=6bff1a494cd7b0a962af0ecfab1ec091&recommendId=192656&controlType=openhome)，2026-10-08）。社区跟踪报道称 Haiku 5.5 对齐 GPT-6 Luna 的定价（$0.10/$0.50）（来源：[OrcaRouter 分析](https://www.orcarouter.ai/blog/claude-haiku-5-5-75-percent-claim)，2026-10-08）。
- **Max/Team 订阅每月 API 额度**（10-07）：Max 和 Team 订阅现包含每月 API 额度，用于在 Claude Platform 上运行自有应用与智能体（来源：[Claude release notes](https://support.claude.com/en/articles/12138966-release-notes)，2026-10-07）。

#### 3.1.4 基准与评测

本期窗口内检索未发现 Anthropic 官方就 Haiku 5.5 发布的具体跑分数据；官方立场为「以更低成本承接高频任务」，具体基准数字以官网模型介绍页为准。

#### 3.1.5 其他相关动态

- **Claude Duet 研究预览**（10-21）：面向 Pro 和 Max 用户开放，Claude 作为主动式智能体运行于新应用。此属智能体产品（详见报告2），此处仅作模型生态相关动态记录（来源：[Claude release notes](https://support.claude.com/en/articles/12138966-release-notes)，2026-10-21）。
- 窗口内检索未发现 Anthropic 在融资、收购或高管讲话方面的可核实公开动态。

### 3.2 OpenAI

#### 3.2.1 模型发布与版本更新

- **GPT-6 Sol / GPT-6 Luna 全量开放**（10-07）：面向全部 ChatGPT 用户开放，替换 GPT-5.6 Sol 与 GPT-5.6 Luna（来源：[KBS 报道](https://mobile.kbs.co.kr/news/pc/view/view.do?ncd=8680581)，2026-10-08）。
- **GPT-5.5 退役**（10-14）：官方「模型发布说明」确认 GPT-5.5 退役（来源：[OpenAI Model Release Notes](https://help.openai.com/en/articles/9624314-model-release-notes)，2026-10-14）。
- **GPT-6.1 Terra 发布**（10-26）：新增通用模型中档型号，API 模型 ID 为 `gpt-6.1-terra`，接替 GPT-5.6 Terra（来源：[AWS 公告](https://aws.amazon.com/cn/about-aws/whats-new/2026/10/openai-gpt-6-1-terra-on-amazon-bedrock/)，2026-10-26；[Dataconomy 报道](https://www.dataconomy.com/2026/10/27/openai-gpt-6-1-terra-api-50-percent-cheaper-sol/)，2026-10-27）。

#### 3.2.2 能力与特性

- **GPT-6.1 Terra** 主打计算机操作（computer use）、视觉理解、编程与日常办公任务，如读取屏幕上内容、点击应用、撰写回复提纲等（来源：[DigitalToday 报道](https://www.digitaltoday.co.kr/en/view/119717/openai-unveils-gpt-6-1-terra-cuts-prices-boosts-coding-performance)，2026-10-27）。知识截止日期为 2026-06-01，是 GPT-6 家族中最新的型号（来源：[Dataconomy](https://www.dataconomy.com/2026/10/27/openai-gpt-6-1-terra-api-50-percent-cheaper-sol/)，2026-10-27）。

#### 3.2.3 价格与开放策略

- **GPT-6.1 Terra API 定价**：标准价为输入 $1 / 输出 $5 每百万 token（缓存输入 $0.05），较 GPT-5.6 Terra 与 GPT-6.1 Sol 低 50%（来源：[Dataconomy](https://www.dataconomy.com/2026/10/27/openai-gpt-6-1-terra-api-50-percent-cheaper-sol/)，2026-10-27）。OpenAI 通用产品线由此形成四档：Luna（$0.10/$0.50）、Terra（$1/$5）、Sol（$2/$10）、Astra（$10/$50）。

#### 3.2.4 基准与评测

- **Terminal-Bench 4.0**：GPT-6.1 Terra 在 maximum 推理档下解决 50.3% 任务，对比 GPT-5.6 Terra 的 21.5%，提升超过一倍（来源：[Digit 报道](https://www.digit.in/features/general/gpt-61-terra-explained-what-openais-newest-computer-use-model-can-do.html)，2026-10-27；[The Next Web](https://thenextweb.com/news/openai-gpt-6-1-terra-computer-use)，2026-10-26）。
- **OSWorld 2.1**：官方称 Terra 在 medium effort 下超过 GPT-5.6 Terra 最佳成绩（来源：[Omniakey 对比](https://omniakey.com/blog/gpt-6-1-terra-vs-sol)，2026-10-27）。

#### 3.2.5 其他相关动态

- GPT-6.1 Terra 同日（10-26）在 Amazon Bedrock 上正式可用（来源：[AWS 公告](https://aws.amazon.com/cn/about-aws/whats-new/2026/10/openai-gpt-6-1-terra-on-amazon-bedrock/)，2026-10-26）。
- 窗口内检索未发现 OpenAI 在融资、收购或高管讲话方面的可核实公开动态。

### 3.3 Google（Gemini）

#### 3.3.1 模型发布与版本更新

- **Gemini 4 Argon**（9-30 首发，10-13 GA）：10-13 起在 Gemini API 正式可用，定位面向真实世界软件工程、企业知识工作（法律、金融）与网络安全防御的旗舰模型（来源：[Gemini 4 Argon 官方博客](https://china.googleblog.com/2026/10/gemini-4-argon_0397895399.html)，2026-10-14）。
- **EmbeddingGemma 2**（10-06）：740M 参数的开放权重多模态嵌入模型，将文本、代码、图像、视频、音频映射到统一嵌入空间，面向端侧/本地 RAG 检索（来源：[Gemma releases](https://ai.google.dev/gemma/docs/releases)，2026-10-06；[TechRepublic 报道](https://www.techrepublic.com/de/article/news-google-embeddinggemma-2-on-device-multimodal-search/)，2026-10-07）。

#### 3.3.2 能力与特性

- Argon 主打三个方向：real-world coding、enterprise knowledge work、cyber defense（来源：[Gemini 4 Argon 官方博客](https://china.googleblog.com/2026/10/gemini-4-argon_0397895399.html)，2026-10-14）。
- EmbeddingGemma 2 是 Google 首个「原生多模态」开放权重嵌入模型，无需联网即可在手机、笔记本电脑本地处理多模态数据，数据不离开终端（来源：[TechRepublic](https://www.techrepublic.com/de/article/news-google-embeddinggemma-2-on-device-multimodal-search/)，2026-10-07）。

#### 3.3.3 价格与开放策略

- **Argon API 推广价**：每百万输入 token $2、输出 $10（缓存输入享 95% 折扣），优惠至 2026-11-30；此后输入标准价 $4、输出 $20（来源：[Gemini 4 Argon 官方博客](https://china.googleblog.com/2026/10/gemini-4-argon_0397895399.html)，2026-10-14）。
- **Gemini 应用分层调整**（10-09 起）：免费档（无 Google AI 订阅）仅保留 Flash-Lite；Google AI Plus（约 $4.99/月）保留 Flash-Lite 与 Flash、失去 Pro；AI Pro（$19.99/月）与 AI Ultra 保留全部三档（来源：[Google 支持文档](https://support.google.com/gemini/answer/17004136)，2026-10；[TechRepublic](https://www.techrepublic.com/article/news-google-gemini-free-flash-lite-access/)，2026-10-06）。
- **EmbeddingGemma 2**：开放权重模型（开放许可，具体条款以官方模型卡为准）（来源：[Gemma releases](https://ai.google.dev/gemma/docs/releases)，2026-10-06）。

#### 3.3.4 基准与评测

- **DeepSWE v1.1**：Gemini 4 Argon 得 77.9%，官方称刷新纪录，高于 Claude Opus 5.5 的 74.2% 与 GPT-6 Astra 的 74.1%（来源：[IT之家](https://www.ithome.com/1/008/953.htm)，2026-10-01；[The Next Web](https://thenextweb.com/news/google-gemini-4-argon-cyber-defenders-fairwind)，2026-09-30）。
- **Vibe Code Bench**：91.9%（来源：[LLM-Stats 技术解析](https://llm-stats.com/blog/research/gemini-4-argon-launch)，2026-10-07）。
- **CWE-bench**：68%，并列第一（来源：[The Next Web](https://thenextweb.com/news/google-gemini-4-argon-cyber-defenders-fairwind)，2026-09-30）。

#### 3.3.5 其他相关动态

- 窗口内检索未发现 Google/Google DeepMind 在 Gemma、Veo、Lyria、Gemini Robotics 等领域有覆盖窗口内（10-01~10-31）的其他可核实模型发布动态。

### 3.4 智谱 GLM

#### 3.4.1 模型发布与版本更新

- **GLM-5.3-Highspeed 灰度测试**（10-12 报道）：智谱在其 AI 编程工具 ZCode 3.15.1 中向订阅用户随机开放 GLM-5.3-Highspeed 体验，属灰度测试，官方尚未发布正式公告（来源：[量子位](https://www.qbitai.com/2026/10/502649.html)，2026-10-12；[Pandaily](https://pandaily.com/zhipu-glm-5-3-highspeed-zcode-gray-release-490-tokens-per-second-user-test)，2026-10-12）。
- **GLM-5.5 传闻**（10-22 报道）：网上流传的「智谱专家交流纪要」称 GLM-5.5 或于 10 月底/11 月初发布、参数规模 2.5 万亿~3.5 万亿，属非官方传闻，本报告不视为已核实发布（来源：[EET-China](https://www.eet-china.com/mp/a533099.html)，2026-10-22）。

#### 3.4.2 能力与特性

- 社区用户实测 GLM-5.3-Highspeed 生成速度接近约 490 tokens/s，明显高于上月 GLM-5.3-FlashX 的最高 200 tokens/s（来源：[量子位](https://www.qbitai.com/2026/10/502649.html)，2026-10-12；[36氪](https://www.36kr.com/p/4022354401104000)，2026-10-12）。

#### 3.4.3 价格与开放策略

- 窗口内检索未发现智谱在 10 月有新的 API 定价调整或开源/权重开放的官方公告。当月背景：GLM-5.3-Flash（及 FlashX）为 GLM-5 系列首个原生多模态模型，最新旗舰仍为 GLM-5.3（来源：[智谱开放文档](https://docs.bigmodel.cn/cn/guide/models/text/glm-5.3)，2026-11-05 检索）。

#### 3.4.4 基准与评测

- **CursorBench 4.0**（第三方）：AI 编程工具 Cursor 10 月上线 GLM-5.3 及 GLM-5.3-Flash，并称 GLM-5.3 在 Max 推理设置下取得其自有编程评测 CursorBench 4.0 中开放权重模型最高分（来源：[证券时报](https://www.stcn.com/article/detail/4206401.html)，2026-10-05；[澎湃](https://www.thepaper.cn/newsdetail_forward_34202193)，2026-10-05）。

#### 3.4.5 其他相关动态

- 清华大学与智谱唐杰团队 10-15 在 arXiv 发布 GLM-Omni 技术底座相关论文，市场据此猜测 GLM-5.5 即将发布，但论文未披露版本对应关系（来源：[证券之星](https://wap.stockstar.com/detail/IG2026102800019536)，2026-10-28）。
- 窗口内检索未发现智谱在融资、收购方面的可核实公开动态。

### 3.5 Kimi（月之暗面）

#### 3.5.1 模型发布与版本更新

- **Kimi K3.1 Pro 发布**（10-24）：K3.1 系列首个模型，官方称其为「迄今能力最强的 3 万亿级参数模型」，支持 100 万（1,048,576 token）上下文窗口。同日 10 月 24 日为「1024 程序员节」（来源：[上海证券报/中国证券网](https://www.cnstock.com/commonDetail/808507)，2026-10-24；[北京日报](https://kw.beijing.gov.cn/xwdt/kcyx/xwdtyqqy/202610/t20261026_4918451.html)，2026-10-26）。
- **Kimi K3.1 Pro Highspeed**：同步推出的高速版，官方称「同等智能，输出速度约 2-3 倍」（来源：[上海证券报](https://www.cnstock.com/commonDetail/808507)，2026-10-24）。

#### 3.5.2 能力与特性

- K3.1 Pro 在代码、3D 创作、金融研究和其他长程 Agent 能力上提升明显；擅长参数化建模，可直接编写并运行 Blender、CAD 等专业工具脚本，端到端完成机械零件、建筑、多参数产品建模（来源：[上海证券报](https://www.cnstock.com/commonDetail/808507)，2026-10-24）。
- 金融领域：官方称 K3.1 Pro 能端到端交付完整金融工作流，提供的案例包括英伟达财务模型、宁德时代投委会报告、量子计算行业研究等（来源：[上海证券报](https://www.cnstock.com/commonDetail/808507)，2026-10-24）。
- 官网同步上线 3D Make 功能，支持在线预览与编辑、导出 3D 打印、视频或实况照片（来源：[上海证券报](https://www.cnstock.com/commonDetail/808507)，2026-10-24）。

#### 3.5.3 价格与开放策略

- **Kimi K3.1 Pro API 定价**：输入 $2.00 / 输出 $10.00 / 缓存输入 $0.20 每百万 token（同时提供人民币价 ¥13/¥68），与 GPT-6.1 Sol 相同，约为 Claude Opus 5.5 的一半（来源：[Kimi API 定价页](https://platform.kimi.com/docs/pricing/chat)，2026-10-30；[Simon Willison](https://simonwillison.net/2026/Oct/23/kimi-k31-pro/)，2026-10-24）。
- **开源权重**：10-24 发布时定为开源模型，权重于 11 月在 Hugging Face 开放（模型卡显示约 2.8 万亿总参数、104B 激活参数，采用 Kimi K3.1 Pro License）。**注**：权重开放动作发生在覆盖窗口之外（11 月），此处仅作定位说明，不作为本期事件（来源：[Hugging Face 模型卡](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)，2026-11-06）。

#### 3.5.4 基准与评测

- **OfficeQA Pro v2**：K3.1 Pro 得分 64.4，官方称取得当前最优（SoTA）成绩；该基准考察基于真实金融文档的复杂财务数据分析（来源：[上海证券报](https://www.cnstock.com/commonDetail/808507)，2026-10-24）。
- **Artificial Analysis 智能指数**：K3.1 Pro 排名第 4，位居全球开源模型之首，官方称综合智能水平接近全球领先闭源模型，价格约为 GPT-6 Astra 的五分之一（来源：[Artificial Analysis](https://artificialanalysis.ai/ko/articles/kimi-k3-1-pro-launch-benchmarks)，2026-10-23；[北京日报](https://kw.beijing.gov.cn/xwdt/kcyx/xwdtyqqy/202610/t20261026_4918451.html)，2026-10-26）。
- **Frontier Finance**：K3.1 Pro 较 K3 进一步提升（来源：[上海证券报](https://www.cnstock.com/commonDetail/808507)，2026-10-24）。

#### 3.5.5 其他相关动态

- 窗口内检索未发现月之暗面在融资、收购方面的可核实公开动态。海外媒体 VentureBeat 于 10-25 报道 K3.1 Pro 之际提及「付费网红争议指控」，属第三方报道，未获官方证实，此处仅作事实记录（来源：[VentureBeat](https://venturebeat.com/technology/moonshots-kimi-k3-1-pro-flirts-with-open-weights-leadership-amid-paid-influencer-scandal-allegations)，2026-10-25）。

### 3.6 DeepSeek

#### 3.6.1 模型发布与版本更新

- **DeepSeek-V4.1-Flash-1017 更新**（10-17）：将 DeepSeek V4.1 Flash 升级至 V4.1-Flash-1017，官方网页端、App 与 API 同步更新；API 调用方式与定价不变，使用 `deepseek-flash` 即可调用最新版本（来源：[DeepSeek 官方公告](https://api-docs.deepseek.com/news/news261017.md)，2026-10-17；[Change Log](https://api-docs.deepseek.com/updates/)，2026-10-17）。

#### 3.6.2 能力与特性

- 官方称新版本在「多种基准上性能提升、任务处理更快、输出更短」，实现性能与成本的帕累托改进（Pareto improvement）（来源：[DeepSeek 官方公告](https://api-docs.deepseek.com/news/news261017.md)，2026-10-17）。
- 采用带自反馈（self-feedback）的强化学习，提升端到端项目开发能力，覆盖从游戏创作到 3D 建模（来源：[DeepSeek 官方公告](https://api-docs.deepseek.com/news/news261017.md)，2026-10-17）。
- 针对 DeepSeek Harness、腾讯 CodeBuddy、WorkBuddy 等平台优化；建议升级至 DeepSeek Harness 0.2.1-rc.1 或更高版本（来源：[DeepSeek 官方公告](https://api-docs.deepseek.com/news/news261017.md)，2026-10-17）。

#### 3.6.3 价格与开放策略

- **开源权重**：DeepSeek-V4.1-Flash-1017 权重以 MIT 协议在 Hugging Face（deepseek-ai/DeepSeek-V4.1-Flash-1017）与 ModelScope 开源（来源：[DeepSeek 官方公告](https://api-docs.deepseek.com/news/news261017.md)，2026-10-17；[Mistral 文档转载](https://docs.mistral.ai/models/deepseek-v4-flash-1017.md)，2026-10-28）。模型参数约 763B 总参数、37B 激活参数（来源：[Mistral 文档](https://docs.mistral.ai/models/deepseek-v4-flash-1017.md)，2026-10-28）。
- **Search & Fetch API 开放**（10-17）：基于自研搜索引擎，向所有开发者开放，每端点 $0.75 / 千次调用；经 DeepSeek Harness、Claude Code、Codex 的服务端工具调用目前免费，2026-10-31 16:00 UTC 起计费（来源：[DeepSeek 官方公告](https://api-docs.deepseek.com/news/news261017.md)，2026-10-17）。

#### 3.6.4 基准与评测

以下为官方公布的 V4.1-Flash-1017 基准成绩（来源：[DeepSeek Change Log](https://api-docs.deepseek.com/updates/)，2026-10-17）：

- HLE (w/o tools)：42.6（纯文本子集 44.0*）
- Terminal-Bench 4.0：42.3（Claude Code 框架测试）
- DeepSWE v1.1：77.0（Mini-SWE-V2 框架测试）
- ProgramBench：29.1
- NL2Repo-Bench：68.2
- Automation-Bench v1.0.6：60.5
- Agents' Last Exam：35.4
- Apex Bench v1.1：72.1
- Chartography (w/tools)：83.0
- BabyVision (w/tools)：92.5
- ZeroBench-main (w/tools)：51.0（Pass@5）

#### 3.6.5 其他相关动态

- 官方表示自研 DeepSeek 搜索引擎指数级覆盖数千亿网页，每日可靠处理数亿搜索请求，支持多语言、过滤 SEO 垃圾与低质 AIGC（来源：[DeepSeek Change Log](https://api-docs.deepseek.com/updates/)，2026-10-17）。
- 窗口内检索未发现 DeepSeek 在融资、收购方面的可核实公开动态。

## 4. 横向对比与趋势

### 4.1 旗舰模型对比

| 厂商 | 旗舰模型 | 上下文长度 | API 定价档 | 开放程度 |
| --- | --- | --- | --- | --- |
| Anthropic | Claude Opus 5.5（Fable/Mythos 为前沿/受限） | 1M | Haiku 5.5 $0.10/$0.50（≤100K）回归小型 | 闭源（Mythos 受限访问） |
| OpenAI | GPT-6 Astra（GPT-6.1 Sol/Terra 已上市） | 1.05M（Astra） | Terra $1/$5、Sol $2/$10、Astra $10/$50 | 闭源 |
| Google | Gemini 4 Argon | 1M | 推广价 $2/$10（至 11-30），后 $4/$20 | 闭源（EmbeddingGemma 2 开放权重） |
| 智谱 GLM | GLM-5.3（GLM-5.5 传闻未证实） | 1M | 本期无新调整 | 开放权重（GLM 系列） |
| Kimi（月之暗面） | Kimi K3.1 Pro | 1M | $2/$10/$0.20 | 开放权重（11 月开放，本期发布） |
| DeepSeek | DeepSeek-V4.1 系列（V4-Pro / V4.1-Flash-1017） | 1M（V4 系列） | V4.1-Flash-1017 定价不变；Search/Fetch $0.75/千次 | 开放权重（MIT） |

<!-- — 表示本期来源未给出可核验数据；空白不填。 -->

### 4.2 本月趋势观察

1. **中国开放权重模型逼近闭源前沿**：Kimi K3.1 Pro 在 Artificial Analysis 智能指数排名第 4、居开源之首，官方称与最强闭源模型智能差距压缩到约 3 分（来源：[Artificial Analysis](https://artificialanalysis.ai/ko/articles/kimi-k3-1-pro-launch-benchmarks)，2026-10-23）；DeepSeek-V4.1-Flash-1017 以 MIT 开源并同步开放搜索基础设施（来源：[DeepSeek 官方公告](https://api-docs.deepseek.com/news/news261017.md)，2026-10-17）——中国厂商同时在高智能上限与低成本开放两条路径上推进。
2. **「以价换量」从旗舰扩展至中档与小型模型**：OpenAI 用 Terra 将中档模型价格减半（来源：[Dataconomy](https://www.dataconomy.com/2026/10/27/openai-gpt-6-1-terra-api-50-percent-cheaper-sol/)，2026-10-27）；Anthropic 以 Haiku 5.5 大幅降价承接高频任务（来源：[Claude release notes](https://support.claude.com/en/articles/12138966-release-notes)，2026-10-07）——旗舰之外的价格战全面展开。
3. **C 端与 API 分层同步收紧/分化**：Google 自 10-09 起把免费档压缩至 Flash-Lite、AI Plus 失去 Pro（来源：[Google 支持文档](https://support.google.com/gemini/answer/17004136)，2026-10），而 Argon 以限时推广价 $2/$10 吸引开发者（来源：[Gemini 4 Argon 官方博客](https://china.googleblog.com/2026/10/gemini-4-argon_0397895399.html)，2026-10-14）——旗舰推理成本向订阅分层传导，「免费可用模型」门槛在提高。
4. **端侧与多模态嵌入成新焦点**：Google 发布 EmbeddingGemma 2 推动本地 RAG 与隐私友好型检索（来源：[Gemma releases](https://ai.google.dev/gemma/docs/releases)，2026-10-06）——端侧轻量模型成为旗舰之外的第二战场。

## 附录 A：参考来源

1. [Claude release notes](https://support.claude.com/en/articles/12138966-release-notes) — Anthropic Help Center，2026-10-30（含 10-07/10-21 发布记录）
2. [Introducing Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5) — Anthropic，2026-10-07
3. [Claude Haiku 5.5: The First Credible Haiku Agent](https://llm-stats.com/blog/research/claude-haiku-5-5-launch) — LLM-Stats，2026-10-07
4. [Claude Haiku 5.5 平均运行成本较前代下降约75%](http://portal.nstl.gov.cn/choiceness/getChoicenessDetail.htm?serverId=42&uuid=6bff1a494cd7b0a962af0ecfab1ec091&recommendId=192656&controlType=openhome) — 国家科技图书文献中心，2026-10-08
5. [Claude Haiku 5.5: the 75% Claim](https://www.orcarouter.ai/blog/claude-haiku-5-5-75-percent-claim) — OrcaRouter，2026-10-08
6. [OpenAI Model Release Notes](https://help.openai.com/en/articles/9624314-model-release-notes) — OpenAI Help Center，2026-10-14（GPT-5.5 退役）
7. [오픈AI·앤트로픽 같은 날 새 모델](https://mobile.kbs.co.kr/news/pc/view/view.do?ncd=8680581) — KBS，2026-10-08
8. [OpenAI GPT-6.1 Terra 现已在 Amazon Bedrock 上正式推出](https://aws.amazon.com/cn/about-aws/whats-new/2026/10/openai-gpt-6-1-terra-on-amazon-bedrock/) — AWS，2026-10-26
9. [OpenAI launches GPT-6.1 Terra at half the API cost of Sol](https://www.dataconomy.com/2026/10/27/openai-gpt-6-1-terra-api-50-percent-cheaper-sol/) — Dataconomy，2026-10-27
10. [OpenAI GPT-6.1 Terra cuts prices and boosts coding performance](https://www.digitaltoday.co.kr/en/view/119717/openai-unveils-gpt-6-1-terra-cuts-prices-boosts-coding-performance) — DigitalToday，2026-10-27
11. [GPT-6.1 Terra explained](https://www.digit.in/features/general/gpt-61-terra-explained-what-openais-newest-computer-use-model-can-do.html) — Digit，2026-10-27
12. [OpenAI launches GPT-6.1 Terra, a cheaper model for everyday computer work](https://thenextweb.com/news/openai-gpt-6-1-terra-computer-use) — The Next Web，2026-10-26
13. [GPT-6.1 Terra vs GPT-6.1 Sol: Benchmarks](https://omniakey.com/blog/gpt-6-1-terra-vs-sol) — Omniakey，2026-10-27
14. [Gemini 4 Argon：为您解决最棘手的问题](https://china.googleblog.com/2026/10/gemini-4-argon_0397895399.html) — Google 黑板报，2026-10-14
15. [Gemma releases](https://ai.google.dev/gemma/docs/releases) — Google AI for Developers，2026-10-06（EmbeddingGemma 2）
16. [Google Shrinks Multimodal AI Search for Phones and Laptops](https://www.techrepublic.com/de/article/news-google-embeddinggemma-2-on-device-multimodal-search/) — TechRepublic，2026-10-07
17. [Gemini 模型访问与限额变更](https://support.google.com/gemini/answer/17004136) — Google 支持文档，2026-10
18. [Google Limits Free Gemini to Flash-Lite Starting Oct. 9](https://www.techrepublic.com/article/news-google-gemini-free-flash-lite-access/) — TechRepublic，2026-10-06
19. [谷歌最前沿 AI 模型：Gemini 4 Argon 登场](https://www.ithome.com/1/008/953.htm) — IT之家，2026-10-01
20. [Gemini 4 Argon: Google's new flagship reaches cyber defenders first](https://thenextweb.com/news/google-gemini-4-argon-cyber-defenders-fairwind) — The Next Web，2026-09-30
21. [Gemini 4 Argon: Breadth Leader, Fairwind-Gated Access](https://llm-stats.com/blog/research/gemini-4-argon-launch) — LLM-Stats，2026-10-07
22. [智谱新模型，490 tokens/s！](https://www.qbitai.com/2026/10/502649.html) — 量子位，2026-10-12
23. [每秒狂喷近500个token，智谱GLM-5.3高速版悄悄亮相](https://www.36kr.com/p/4022354401104000) — 36氪，2026-10-12
24. [Zhipu's GLM-5.3-Highspeed Appears in ZCode Gray Release](https://pandaily.com/zhipu-glm-5-3-highspeed-zcode-gray-release-490-tokens-per-second-user-test) — Pandaily，2026-10-12
25. [国产最大、最强大模型有望月底发布](https://www.eet-china.com/mp/a533099.html) — EET-China，2026-10-22
26. [智谱股价涨近5% GLM-5.3海外走红](https://www.stcn.com/article/detail/4206401.html) — 证券时报，2026-10-05
27. [智谱收盘涨超6%，Cursor宣布上线GLM-5.3及GLM-5.3-Flash](https://www.thepaper.cn/newsdetail_forward_34202193) — 澎湃新闻，2026-10-05
28. [港股异动 | 智谱(02513)早盘涨近7%](https://wap.stockstar.com/detail/IG2026102800019536) — 证券之星，2026-10-28
29. [GLM-5.3 - 智谱AI开放文档](https://docs.bigmodel.cn/cn/guide/models/text/glm-5.3) — 智谱AI开放文档，2026-11-05 检索
30. [智能、便宜、能打，月之暗面发布Kimi K3.1 Pro](https://www.cnstock.com/commonDetail/808507) — 上海证券报·中国证券网，2026-10-24
31. [月之暗面发布新一代开源模型Kimi K3.1 Pro](https://kw.beijing.gov.cn/xwdt/kcyx/xwdtyqqy/202610/t20261026_4918451.html) — 北京日报（北京科委），2026-10-26
32. [Kimi K3.1 Pro launches at 4th on the Intelligence Index](https://artificialanalysis.ai/ko/articles/kimi-k3-1-pro-launch-benchmarks) — Artificial Analysis，2026-10-23
33. [Model Inference Pricing - Kimi API Platform](https://platform.kimi.com/docs/pricing/chat) — Kimi API 开放平台，2026-10-30
34. [Introducing Kimi K3.1 Pro](https://simonwillison.net/2026/Oct/23/kimi-k31-pro/) — Simon Willison，2026-10-24
35. [moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) — Hugging Face，2026-11-06
36. [Moonshot's Kimi K3.1 Pro flirts with open weights leadership](https://venturebeat.com/technology/moonshots-kimi-k3-1-pro-flirts-with-open-weights-leadership-amid-paid-influencer-scandal-allegations) — VentureBeat，2026-10-25
37. [DeepSeek-V4.1-Flash-1017: Wish-Driven Programming Made Real](https://api-docs.deepseek.com/news/news261017.md) — DeepSeek 官方公告，2026-10-17
38. [Change Log | DeepSeek API Docs](https://api-docs.deepseek.com/updates/) — DeepSeek API 文档，2026-10-17
39. [DeepSeek V4.1 Flash 1017（Mistral 文档转载）](https://docs.mistral.ai/models/deepseek-v4-flash-1017.md) — Mistral AI 文档，2026-10-28
40. [DeepSeek 发布 V4.1-Flash-1017](https://news.iresearch.cn/content/202610/569960.shtml) — 艾瑞，2026-10-19
41. [DeepSeek launches Search, Fetch APIs](https://www.digitaltoday.co.kr/en/view/116485/deepseek-launches-search-fetch-apis-at-0-75-per-1-000-successful-requests) — DigitalToday，2026-10-19

---

> **说明**：本报告所有事实均基于覆盖窗口（2026-10-01 ~ 2026-10-31）内检索到的公开来源，并区分了「事件日期」与「报道日期」。旧报告中"GPT-6 Sol/Luna 全量开放（10-07）""GPT-6.2 退役（10-14）""Gemini 4 Argon API 正式可用（10-13）""Gemini 免费档仅保留 Flash-Lite（10-09 起）"等动态经本期重新核实，均已更新来源链接与日期。旧报告未含「用户观点」标记块，故本期无需要保留的用户观点原文。
