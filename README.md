# Intelligent_Report

每月产出三份 AI 行业月度报告（PDF 为交付格式，同时保留 Markdown 源文件），每期覆盖一个自然月的公开信息：

- **报告1「模型发展报告」**：Anthropic、OpenAI、Google（美国）与智谱 GLM、Kimi、DeepSeek（中国）当月模型变化与模型特性发布。
- **报告2「智能体发展报告」**：同样六家厂商当月智能体产品发布与突破的智能体挑战。
- **报告3「行业智能化发展报告」**：金融、制造、互联网、电信、电力、医疗、交通、教育八大行业当月智能化落地实践与方案。

## 目录约定

```
reports/
  templates/                      # 模板源头，只在此维护，每月复制后填充
    report1-model-development.md
    report2-agent-development.md
    report3-industry-adoption.md
  YYYY-MM/                        # 每月一个目录，如 reports/2026-10/
    report1-model-development.md
    report2-agent-development.md
    report3-industry-adoption.md
keyword.md                        # 检索关键字配置（用户维护，见下节）
```

## 月度产出流程

1. **读关键字**：以 `keyword.md` 当前内容为检索/提取依据（中英文混检）；用户可随时修改，下次制作报告直接生效。
2. **检索**：按关键字逐厂商（报告 1/2）、逐行业（报告 3）检索覆盖窗口内的公开动态与案例。
3. **填充**：把 `reports/templates/` 的对应模板复制到 `reports/YYYY-MM/` 后逐节填充；每条动态/案例必须在正文标注来源（标题链接 + 日期），无动态/案例的小节写「本期无公开动态」（报告 3 写「本期无公开案例」），不留空白。
4. **融入用户观点**：用户输入的观点/总结按主题归入正文对应小节，以「> **用户观点**：…」标记块呈现，保留原意不改写，与来源事实区分。
5. **汇总来源**：全部来源在报告末尾「附录 A：参考来源」统一汇总。

## 关键字配置（keyword.md）

`keyword.md` 分三部分对应三份报告：厂商/行业等固定词、通用与维度词、排除词。**内容由用户维护**，制作报告前以文件当前内容为准。

## GitHub Actions 自动生成

按以下时间（北京时间 09:17）分别生成上个自然月的报告：每月 5 日生成 模型发展报告，15 日生成 智能体发展报告，25 日生成行业智能化发展报告（PDF 和 Markdown 源文件），保存到 `reports/YYYY-MM/` 并提交到仓库。GitHub 定时任务可能延迟；工作流须位于默认分支。

配置步骤：

1. 在仓库 Settings → Secrets and variables → Actions 添加 Secret `DEEPSEEK_API_KEY`，使用有 API 额度的 DeepSeek 密钥。
2. 可选添加 Repository Variable `DEEPSEEK_MODEL`，默认 `deepseek-v4-pro`；所选模型必须支持 Responses API 的 `web_search` 工具；当前官方文档仅列明 `deepseek-v4-pro` 支持，`deepseek-flash` 会忽略该工具。接口依据：[DeepSeek 官方文档](https://api-docs.deepseek.com/guides/responses_api/)。
3. 确保仓库允许 Actions 写入内容；分支保护可能阻止自动提交，生成文件仍可从成功上传的 Artifact 下载。
4. 手动生成：Actions → Generate monthly reports → Run workflow，选择报告类型（`model` 模型、`agent` 智能体、`industry` 行业、`all` 全部），填写 `YYYY-MM`；留空生成上月，指定当月则生成截至当天的初稿。重复运行会重新生成该月文件，并将旧报告中的用户观点提供给模型保留。

每次运行读取所选分支最新检出的 `keyword.md` 与模板，不使用缓存关键词。调用 DeepSeek 联网搜索会产生 API 费用。本次所选报告全部生成且通过基本格式检查后才写入文件；检索覆盖和事实准确性仍需人工审阅。`generation-<报告类型>.json` 记录窗口、模型和关键词摘要，便于追踪配置版本。

本地运行（Python 3.12，无第三方依赖）：`python scripts/generate_reports.py --month 2026-10`，需通过环境变量提供密钥。测试：`python -m unittest discover -s tests`。

PDF 使用 Chromium 排版，支持中文字体、可点击来源链接、跨页表格与页码。生成成功后在当月目录保存 `模型发展报告.pdf`、`智能体发展报告.pdf`、`行业智能化发展报告.pdf`，Actions 附件同时包含 PDF。PDF 导出依赖见 `requirements.txt`，工作流自动安装。

### PushPlus 推送

在 Actions Secrets 添加 `PUSHPLUS_TOKEN`（从 PushPlus 官网获取）。每次报告归档后，通过 PushPlus 默认渠道推送本次所选 PDF 的 GitHub 链接及 Actions 附件下载入口。无需 SMTP 配置，不发送邮件。

推送为报告链接通知，PDF 保存在 GitHub；私有仓库需登录有权限的账号访问。缺少 Token 或接口拒绝请求会使推送步骤失败，但已归档报告仍保留。接口接受请求不等于最终送达，请在 PushPlus 查看送达状态。[官方接口文档](https://www.pushplus.plus/doc/guide/api.html)。
