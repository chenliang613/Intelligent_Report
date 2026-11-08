# 关键字配置（keyword.md）

> **维护人**：陈亮，三个部分分别对应三份月度报告的信息提取关键字，**内容由你配置**
>
> **使用约定**：
> - 每月制作报告前，以本文件**当前内容**为提取/检索依据（中英文混检）。
> - 用户修改本文件后无需通知任何流程；下次制作报告时直接读取最新内容。
> - 「固定词」建议保持厂商/产品名准确；「通用词」「维度词」「排除词」按需增删。

---

## 第一部分：报告1 「Top 模型厂商模型发展报告」 关键字

### 1.1 厂商与模型名

以下为检索种子词，并非完整在售清单。每次检索须从官方目录补充新型号，区分正式可用、预览、受限访问和退役状态。

- **Anthropic**：Claude Mythos, Claude Fable, Claude Opus, Claude Sonnet, Claude Haiku；以[官网模型信息](https://www.anthropic.com/claude/mythos)与[生命周期文档](https://docs.anthropic.com/en/docs/about-claude/model-deprecations)为准。Mythos 属于受限访问模型，不能视为全面开放。
- **OpenAI**：GPT 系列、o 系列，以及图像、音频、实时等专用模型；逐次读取[官方模型目录](https://developers.openai.com/api/docs/models)补全具体型号。o3、o4-mini 保留为历史检索词；不将“o4”泛称视为已核实型号，区分 ChatGPT 名称与 API 模型 ID。
- **Google / Google DeepMind**：Gemini, Gemma；同时关注 Veo, Lyria, Genie, Gemini Robotics 等官网模型系列。来源：[Gemini 模型目录](https://ai.google.dev/gemini-api/docs/models)、[DeepMind 模型入口](https://deepmind.google/models/gemma/)。Gemma 为开放模型系列，具体许可须另行核实。
- **智谱 / Z.ai**：GLM；ChatGLM 保留作历史检索词。[官方概览](https://docs.z.ai/guides/overview/overview)目前列有 GLM-5.3、GLM-5.3-Flash 等，不限于 GLM-4 / GLM-5。
- **Kimi（月之暗面 Moonshot AI）**：Kimi 及官方完整型号；[官方文档](https://platform.kimi.ai/docs/get-your-api-key)目前列有 Kimi K3.1 Pro、Kimi K3、Kimi K2.7 Code、Kimi K2.6。K2 保留作历史检索词；不以未核实的“K1”简称替代具体型号。
- **DeepSeek**：DeepSeek 及官方完整型号，V3、R1 保留作历史检索词；[官方 API 文档](https://api-docs.deepseek.com/quick_start/pricing)目前列有 deepseek-flash、deepseek-v4-pro。API 别名与实际承载模型分别记录，不能永久绑定旧型号。

### 1.2 通用关键词（示例可修改）

- 中文：模型发布, 新模型的能力, 版本更新, 升级, 开源, 开放权重, 上下文长度, 长文本, 多模态, 推理模型, 混合推理, API 定价, 降价, 价格调整, 基准测试, 跑分, 评测, 榜单
- 英文：model release, new model, launch, update, benchmark, pricing, context window, open weights, open source, reasoning model, multimodal, API

### 1.3 评测维度词（示例可修改）

- SWE-bench, AIME, GPQA, MMLU, HumanEval, LMArena, 大模型竞技场, 编程评测, 数学评测

#### 其他关注维度（非评测）

- 融资动态, 收购信息, 高管讲话

### 1.4 排除词
招聘, 广告类的信息

---

## 第二部分：报告2「Top 智能体厂商发展报告」关键字

### 2.1 厂商与产品名（固定词，示例可修改）

- **Anthropic**：Claude Code, Claude Agent SDK；computer use（能力词，非独立产品名）
- **OpenAI**：ChatGPT agent, Codex, AgentKit；Operator（历史产品检索词，需核实当期状态）
- **Google**：Jules, Gemini CLI, Project Mariner
- **智谱 GLM**：AutoGLM；Z.ai（品牌与平台检索词，非单一智能体产品名）
- **Kimi（月之暗面）**：Kimi Researcher, Kimi Code CLI
- **DeepSeek**：用 2.2 通用词 + DeepSeek 检索，并查看[官方智能体集成文档](https://api-docs.deepseek.com/quick_start/agent_integrations/)；区分官方能力、工具与第三方集成，不预设无产品

### 2.2 通用关键词（示例可修改）

- 中文：智能体, AI Agent, 编码智能体, 编程智能体, 通用智能体, 浏览器智能体, 计算机操作, 多智能体, 工具调用, 自主执行, 任务编排, 数字员工, 智能体平台
- 英文：agent, agentic, coding agent, computer use, browser agent, multi-agent, tool use, tool calling, autonomous, orchestration

### 2.3 挑战维度词（示例可修改，用于「突破的智能体挑战」归类）

- 长程任务, 长期规划, 任务可靠性, 幻觉, 记忆, 上下文记忆, 多智能体协作, 协作, 安全对齐, 权限控制, 沙箱
- 评测：SWE-bench Verified, Terminal-Bench, OSWorld, WebArena, GAIA, TAU-bench, ARC-AGI

### 2.4 排除词（示例可修改）

- 招聘, 市场营销稿件

---

## 第三部分：报告3「行业智能化发展报告」关键字

### 3.1 行业词（固定词，示例可修改）

- 金融（银行, 证券, 保险, 支付）, 制造（工业, 汽车, 半导体）, 医疗健康（医院, 药企）, 零售电商, 消费品, 政务, 公共服务, 能源（电力, 石油）, 交通物流, 教育, 电信, 建筑地产, 农业

### 3.2 场景与方案词（示例可修改）

- 中文：智能化, 数字化转型, 大模型落地, AI 落地, 落地案例, 解决方案, 行业大模型, 企业知识库, 知识问答, 智能客服, 代码助手, 研发提效, 智能营销, 数字员工, RAG, 智能体应用, 降本增效
- 英文：enterprise AI, AI adoption, case study, deployment, production use, AI transformation, LLM application

### 3.3 主体词（可选，用于筛选案例企业量级，示例可修改）

- 央企, 国企, 世界500强, 头部企业, 独角兽

### 3.4 排除词（示例可修改）

- 概念炒作, PPT 产品, 招投标预告

---

## 官方核对说明

- 核对日期：2026-11-08。具体版本是核对时的检索示例，不代表完整清单；每次检索继续查阅官网最新信息。
- 补充来源：[Jules 官方更新记录](https://jules.google/docs/changelog/)、[Google Jules 与 Gemini CLI](https://developers.googleblog.com/en/meet-jules-tools-a-command-line-companion-for-googles-async-coding-agent/)、[Moonshot 官方 Kimi K2 / Researcher 说明](https://moonshotai.github.io/Kimi-K2/)、[AutoGLM 团队论文](https://arxiv.org/abs/2411.00820)。历史产品词不表示当前仍独立提供。
- 通用词、评测词、行业词及排除词属于用户检索偏好，保留原有关注范围；行业扩展词用于检索，报告3章节仍按 README 与模板组织。
