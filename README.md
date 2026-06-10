# 🔮 Prompt Translator — 需求转最佳提示词

> 你说需求，AI 帮你转化为最佳提示词。不用学提示词工程，说人话就行。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/demo-live-brightgreen)](https://leauv121.github.io/prompt-translator/)

---

## 🎯 这是什么？

一个工具，把你的自然语言需求自动转化为结构化的、高质量 AI 提示词。

**痛点**：很多人知道想要什么，但不会写 prompt，导致 AI 产出质量差，反复对话浪费时间。

**解决**：你描述需求 → 工具分析 → 追问关键信息 → 生成最佳提示词 → 一键复制使用。

**两种形态**：

| 形态 | 怎么用 | 适合谁 |
|------|--------|--------|
| 🌐 **Web 应用** | 打开网址就行 | 任何人，发链接即可分享 |
| 🤖 **Agent Skill** | 在 Claude Code 里 `/prompt-translator-skill` | Claude Code 用户，深度集成 |

---

## 🚀 快速开始

### Web 应用（推荐）

直接打开：**[https://leauv121.github.io/prompt-translator/](https://leauv121.github.io/prompt-translator/)**

```
1. 打开网址
2. 点 ⚙️ → 选模型（DeepSeek/Claude/ChatGPT/Gemini）→ 填入 API Key → 保存
3. 在输入框描述你的需求，回车
4. AI 追问关键信息（如果需要），生成最佳提示词
5. 一键复制，粘贴到任何 AI 工具
```

**离线使用**：下载 `prompt-translator-web/index.html`，双击打开，手动模式不需要 API Key。

### Agent Skill（Claude Code 用户）

```bash
# 安装
cp -R prompt-translator-skill ~/.claude/skills/prompt-translator-skill

# 使用（在 Claude Code 中）
/prompt-translator-skill 帮我写一个分析销售数据的提示词
```

---

## 📁 项目结构

```
prompt-translator/
├── README.md                           # 本文件 — 项目总览
├── LICENSE                             # MIT License
├── .gitignore
│
├── prompt-translator-web/              # 🌐 Web 应用（单文件，零依赖）
│   ├── index.html                      #   完整应用（1214行，含CSS+JS）
│   └── README.md                       #   部署和使用说明
│
└── prompt-translator-skill/            # 🤖 Agent Skill（Claude Code 插件）
    ├── SKILL.md                        #   技能主文件（<500行，含完整工作流）
    ├── scripts/
    │   └── prompt_translator.py        #   Python CLI：分析/模板生成
    ├── references/
    │   ├── prompt-engineering-guide.md  # 提示词工程深入指南
    │   ├── examples.md                  # 优化前后对比示例
    │   └── multi-platform-guide.md      # 多平台适配详细指南
    ├── assets/
    │   ├── prompt-template.md           # SPACES 框架模板
    │   └── clarify-questions.md         # 追问问题库
    ├── install.sh                      #   跨平台自动安装脚本
    └── README.md                       #   安装说明
```

---

## 🔌 支持的 AI 模型

| 提供商 | Web | Skill | 获取 Key |
|--------|:---:|:-----:|----------|
| **DeepSeek** | ✅ | — | [platform.deepseek.com](https://platform.deepseek.com) |
| **Claude** (Anthropic) | ✅ | ✅ | [console.anthropic.com](https://console.anthropic.com) |
| **ChatGPT** (OpenAI) | ✅ | — | [platform.openai.com](https://platform.openai.com) |
| **Gemini** (Google) | ✅ | — | [aistudio.google.com](https://aistudio.google.com) |
| **自定义** (OpenAI 兼容) | ✅ | — | 你自己的服务 |

---

## 🧠 核心方法论：SPACES 框架

每个生成的高质量提示词都包含六个要素：

| 要素 | 含义 | 示例 |
|------|------|------|
| **S**ystem | 角色设定 — AI 扮演谁？ | "你是一位资深电商数据分析师，有10年经验" |
| **P**roblem | 任务描述 — 要完成什么？ | "分析Q3销售数据，判断营收下滑的主要原因是客流下降还是客单价下降" |
| **A**udience | 受众设定 — 给谁看的？ | "报告面向CEO和CFO，需要结论先行，使用商业语言" |
| **C**onstraints | 约束条件 — 限制和要求 | "不要使用专业术语；不确定的地方请明确指出，不要猜测" |
| **E**xamples | 示例参考 — 期望什么样？ | "参考这个格式：[提供一个输入/输出示例]" |
| **S**tructure | 输出结构 — 按什么格式？ | "1.核心结论 2.数据支撑 3.归因分析 4.可执行建议" |

---

## 📸 功能一览

### 🤖 AI 智能模式
- 自然语言描述需求
- AI 自动追问缺失的关键信息（受众、格式、约束）
- 生成面向特定平台优化的提示词
- 支持所有主流模型

### 📝 手动引导模式
- 按 SPACES 框架填表
- 实时预览生成的提示词
- 纯离线可用，不需要 API Key
- 支持5种平台风格输出

### 🛠 其他功能
- **一键复制**：生成后点复制，直接粘贴到任何 AI 工具
- **历史记录**：自动保存到浏览器 localStorage，随时回溯
- **暗色模式**：晚上用不刺眼
- **响应式设计**：手机、平板、电脑都能用
- **隐私安全**：API Key 只存在用户浏览器里，不上传任何服务器

---

## 🔧 本地开发

```bash
# 克隆项目
git clone https://github.com/leauv121/prompt-translator.git
cd prompt-translator

# Web 应用 — 直接打开
open prompt-translator-web/index.html

# 或用本地服务器
cd prompt-translator-web
python3 -m http.server 8080
# 访问 http://localhost:8080

# Agent Skill — 安装到 Claude Code
cp -R prompt-translator-skill ~/.claude/skills/

# Skill Python 脚本
python3 prompt-translator-skill/scripts/prompt_translator.py analyze "帮我分析数据"
python3 prompt-translator-skill/scripts/prompt_translator.py template --type analysis
```

---

## ❓ 常见问题

<details>
<summary><b>怎么获取 DeepSeek API Key？</b></summary>

1. 访问 [platform.deepseek.com](https://platform.deepseek.com)
2. 注册/登录
3. 在 API Keys 页面创建 Key
4. 复制粘贴到工具的 ⚙️ 设置中
5. DeepSeek 价格很便宜，约 ¥1/百万 token
</details>

<details>
<summary><b>API Key 安全吗？</b></summary>

完全安全。Key 只存在你浏览器的 localStorage 中，**绝不上传任何第三方服务器**。所有 API 调用直接从你的浏览器发送到对应 AI 厂商。
</details>

<details>
<summary><b>手动模式和 AI 模式有什么区别？</b></summary>

| | AI 模式 | 手动模式 |
|---|---|---|
| 怎么用 | 说人话，AI 自动处理 | 按表单填空 |
| 需要什么 | API Key | 无 |
| 追问 | AI 自动追问 | 你自己判断需要填什么 |
| 适合 | 需求不明确时 | 需求清晰时 |
</details>

<details>
<summary><b>能不能离线使用？</b></summary>

Web 应用的手动模式完全离线可用。AI 模式需要联网调用 API。

Agent Skill 完全离线可用（本身就是本地插件）。
</details>

<details>
<summary><b>怎么分享给同事？</b></summary>

最简单：发网址 `https://leauv121.github.io/prompt-translator/`

或发 `prompt-translator-web/index.html` 文件，对方保存后双击打开。
</details>

---

## 📄 开源协议

MIT License — 详见 [LICENSE](LICENSE)

---

## 🙏 致谢

本项目方法论融合了以下优秀开源项目的思想：

- [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills) — EARS 需求分析方法论
- [ndpvt-web/prompt-improver](https://github.com/ndpvt-web/prompt-improver) — 第一性原则追问机制
- [getsentry/skills](https://github.com/getsentry/skills) — 提示词工程最佳实践集合
- [ckanner/agent-skills](https://github.com/ckanner/agent-skills) — Agent Skill 设计参考
