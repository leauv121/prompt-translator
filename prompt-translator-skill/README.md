# /prompt-translator-skill — 自然语言转最佳AI提示词

> 你说需求，我生成最佳提示词。不用学提示词工程，说人话就行。

## 这是什么？

一个AI技能，可以把你的自然语言需求自动转化为结构化的、高质量AI提示词。

**痛点**: 很多人知道想要什么，但不会写prompt，导致AI产出质量差。

**解决**: 你只需要描述你的需求（哪怕很模糊），这个技能会：
1. 分析你的需求
2. 追问关键信息（受众、格式、约束等）
3. 生成一个专业的、结构化的提示词
4. 解释它做了什么优化及为什么

## 快速开始

### 安装

**方式一：自动安装（推荐）**
```bash
git clone https://github.com/YOUR_USER/prompt-translator-skill.git
cd prompt-translator-skill
./install.sh
```

安装到特定平台：
```bash
./install.sh --platform cursor    # Cursor
./install.sh --platform claude    # Claude Code
./install.sh --platform copilot   # GitHub Copilot
./install.sh --all                # 所有检测到的平台
```

**方式二：手动复制**

| 平台 | 安装位置 |
|------|---------|
| **Claude Code** | `~/.claude/skills/prompt-translator-skill/` |
| **GitHub Copilot** | `.github/skills/prompt-translator-skill/` |
| **Cursor** | `.cursor/rules/prompt-translator-skill/` |
| **Windsurf** | `.windsurf/rules/prompt-translator-skill/` |
| **Cline** | `.clinerules/prompt-translator-skill/` |
| **Gemini CLI** | `~/.gemini/skills/prompt-translator-skill/` |
| **Codex CLI** | `~/.agents/skills/prompt-translator-skill/` |
| **Universal** | `~/.agents/skills/prompt-translator-skill/` |

### 使用

在任意支持的AI工具中输入：

```
/prompt-translator-skill 我需要做一个竞品分析报告，但不知道怎么写prompt
```

或者自然地：
```
帮我把这个需求转化为提示词：我想分析我们公司过去一年的销售数据，找出增长瓶颈
```

优化现有的prompt：
```
帮我优化这个提示词：[粘贴你现有的prompt]
```

## 示例

### 输入（你说的话）
> "帮我写个提示词，我要分析一下销售数据"

### 技能会追问
- 这个分析要驱动什么决策？
- 报告给谁看？
- 数据大概什么格式？

### 输出（优化后的提示词）

```
你是一位零售行业的数据分析师，有10年经验。请分析附件中的Q2销售数据。

目标：判断营收同比增长仅2%的主要原因是客流下降还是客单价下降，
      以便CFO决定Q3是在引流还是提价上加大投入。

数据说明：
- 包含每日销售额、客流量、客单价、退货率
- 覆盖全国12个门店
- 去年同期数据作为对比

输出格式：
1. 总体结论 (2-3句话，结论先行)
2. 关键指标对比 (表格)
3. 下滑归因分析
4. 门店表现排名
5. Q3建议 (按优先级)

约束：
- 面向CFO和CEO，用商业语言
- 如果某天数据异常请标注
- 结论必须基于数据，不要引入外部假设
```

## 功能列表

| 功能 | 说明 |
|------|------|
| **需求转提示词** | 自然语言 → 结构化prompt |
| **追问澄清** | 模糊需求自动追问关键信息 |
| **提示词优化** | 改进现有prompt的质量 |
| **多平台适配** | Claude / ChatGPT / DeepSeek / Gemini |
| **模板生成** | 常见场景的prompt模板 |
| **教育性输出** | 解释优化了什么及为什么 |

## 文件结构

```
prompt-translator-skill/
├── SKILL.md                              # 主技能文件
├── scripts/
│   └── prompt_translator.py              # Python脚本（分析/模板生成）
├── references/
│   ├── prompt-engineering-guide.md       # 提示词工程深入指南
│   ├── examples.md                       # 优化前后对比示例
│   └── multi-platform-guide.md           # 多平台适配详细指南
├── assets/
│   ├── prompt-template.md                # SPACES框架模板
│   └── clarify-questions.md              # 追问问题库
├── install.sh                            # 跨平台安装脚本
└── README.md                             # 本文件
```

## SPACES 框架

这个技能使用的核心方法论：

| 元素 | 说明 | 示例 |
|------|------|------|
| **S**ystem | 角色设定 | "你是一位资深战略分析师..." |
| **P**roblem | 任务描述 | "分析Q3销售下滑的原因..." |
| **A**udience | 受众设定 | "报告面向CEO..." |
| **C**onstraints | 约束条件 | "不要使用专业术语..." |
| **E**xamples | 示例参考 | "参考这个格式：[示例]" |
| **S**tructure | 输出结构 | "1. 核心发现 2. 数据支撑 3. 建议" |

## 贡献

欢迎提交Issue和Pull Request。

## 许可

MIT License
