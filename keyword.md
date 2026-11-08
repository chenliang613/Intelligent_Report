# 关键字配置（keyword.md）

> **维护人**：用户。三个部分分别对应三份月度报告的信息提取关键字，**内容由你（用户）配置**，当前为示例初稿。
>
> **使用约定**：
> - 每月制作报告前，以本文件**当前内容**为提取/检索依据（中英文混检）。
> - 用户修改本文件后无需通知任何流程；下次制作报告时直接读取最新内容。
> - 「固定词」建议保持厂商/产品名准确；「通用词」「维度词」「排除词」按需增删。

---

## 第一部分：报告1「Top 模型厂商模型发展报告」关键字

### 1.1 厂商与模型名（固定词，示例可修改）

- **Anthropic**：Claude, Opus, Sonnet, Haiku
- **OpenAI**：GPT, o 系列（o3/o4…）
- **Google**：Gemini, Gemma
- **智谱 GLM**：GLM, ChatGLM, GLM-4, GLM-5
- **Kimi（月之暗面 Moonshot AI）**：Kimi, K1, K2
- **DeepSeek**：DeepSeek, V3, R1

### 1.2 通用关键词（示例可修改）

- 中文：模型发布, 新模型, 版本更新, 升级, 开源, 开放权重, 上下文长度, 长文本, 多模态, 推理模型, 混合推理, API 定价, 降价, 价格调整, 基准测试, 跑分, 评测, 榜单
- 英文：model release, new model, launch, update, benchmark, pricing, context window, open weights, open source, reasoning model, multimodal, API

### 1.3 评测维度词（示例可修改）

- SWE-bench, AIME, GPQA, MMLU, HumanEval, LMArena, 大模型竞技场, 编程评测, 数学评测

### 1.4 排除词（示例可修改）

<!-- 命中这些词的动态默认不进报告1，除非同时命中 1.1/1.2 -->
- 融资, 收购传闻, 高管离职

---

## 第二部分：报告2「Top 智能体厂商发展报告」关键字

### 2.1 厂商与产品名（固定词，示例可修改）

- **Anthropic**：Claude Code, Claude Agent SDK, computer use
- **OpenAI**：ChatGPT Agent, Operator, Codex, AgentKit
- **Google**：Jules, Gemini CLI, Project Mariner
- **智谱 GLM**：AutoGLM, Z.ai
- **Kimi（月之暗面）**：Kimi Researcher
- **DeepSeek**：（当前无固定产品词，用 2.2 通用词 + DeepSeek 检索）

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
