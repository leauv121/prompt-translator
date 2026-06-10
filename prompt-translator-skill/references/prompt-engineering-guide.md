# Prompt Engineering Deep Dive

**Purpose:** Comprehensive reference for prompt engineering techniques. Load this when the user asks "why" a certain structure was used, or when you need to explain optimization decisions.

---

## 1. The SPACES Framework (Detailed)

### S — System/Role Assignment

Role assignment is the single highest-leverage prompt technique. It:
- Primes the model's knowledge base to the right domain
- Sets the appropriate level of technical depth
- Establishes perspective and bias consciously

**Weak:** "分析这个数据"
**Strong:** "你是一位有10年经验的电商数据分析师，擅长从GMV、客单价、复购率等指标中识别增长瓶颈。你的分析报告通常会被CEO直接阅读。"

**Role components:**
1. **Identity** — 谁？(职业、资历)
2. **Expertise** — 擅长什么？
3. **Context** — 在什么场景下工作？
4. **Audience** — 为谁产出？

### P — Problem/Task Specification

Vague tasks produce vague outputs. Specificity drives quality.

**Levels of specificity:**

| Level | Example | When to Use |
|-------|---------|------------|
| **L1: Vague** | "分析销售数据" | Never — this is what you're fixing |
| **L2: Specific** | "分析Q3销售数据，找出营收下滑3%的原因" | Quick exploratory queries |
| **L3: Decision-driven** | "分析Q3销售数据，判断下滑是由客流量减少还是客单价下降导致的，以便决定是加大引流还是做促销" | Professional use |
| **L4: Full context** | L3 + "数据包含每日销售额、客流量、客单价、退货率。如果某天数据异常，请标注。如果两个因素都有影响，请量化各自的贡献比例。" | Production-grade prompts |

### A — Audience Specification

Knowing the audience changes everything:
- **CEO**: Conclusion first, big picture, financial impact
- **Technical peer**: Methodology matters, assumptions stated, data sources cited
- **Client**: Professional, no jargon, actionable recommendations
- **Yourself**: Raw data, edge cases highlighted, exploration encouraged

### C — Constraints

Constraints prevent common failure modes:

| Constraint Type | Example |
|----------------|---------|
| Format | "用markdown表格呈现" |
| Length | "不超过500字" |
| Style | "用口语化的中文，不要学术腔" |
| Scope | "只关注营收，不涉及成本" |
| Negative | "不要使用任何专业术语" |
| Uncertainty | "如果数据不足以得出结论，请明确指出，不要猜测" |
| Attribution | "引用来源时请标注页码" |
| Language | "中英文混合时，关键术语保留英文" |

### E — Examples (Few-Shot)

Examples are the most underused powerful technique. A single well-chosen example often outperforms a page of instructions.

**Patterns:**
1. **Input-output pair**: Show the model what you provide and what you expect back
2. **Graded examples**: Show both good and bad outputs, explain why
3. **Edge case examples**: Show how to handle unusual inputs

### S — Structure Specification

Tell the model exactly how to organize output:

```
请按以下结构输出：
1. 核心结论 (1-2句)
2. 关键发现 (3-5条，每条不超过50字)
3. 数据支撑 (表格)
4. 风险提示 (如有)
5. 可执行建议 (按优先级排列)
```

---

## 2. Advanced Techniques

### Chain of Thought (CoT)

For reasoning tasks, explicitly request step-by-step thinking:

"请一步一步思考。先列出所有可能的原因，然后逐一分析数据检验，最后给出结论。"

### Self-Consistency

For important decisions, ask the model to approach from multiple angles:

"请分别从市场角度、财务角度、用户角度分析这个问题，然后综合三个视角给出最终建议。"

### Negative Prompting

Sometimes telling the model what NOT to do is more effective than telling it what to do:

"不要在报告中写'根据数据显示'这种废话。不要给出模棱两可的建议。如果两个方案优劣不明显，直接说'无法判断'。"

### Context Windowing Awareness

Put the most important information at the beginning and end of your prompt — models pay most attention to these positions:

```
[最重要：角色 + 任务 + 受众]
[中间：背景信息、数据、细节]
[最后：输出格式要求 + 示例 + 约束]
```

### Dealing with Hallucination

Structure prompts to reduce fabrication:

1. "如果不确定，请说'我不确定'，不要编造"
2. "请只基于我提供的数据进行分析，不要引入外部假设"
3. "对于每个结论，请在括号中标注所依据的数据来源"
4. "如果数据中存在矛盾，请指出而不是试图调和"

---

## 3. Domain-Specific Patterns

### Data Analysis Prompts

```
你是[领域]分析师。分析我提供的[数据类型]。
目标：判断[具体决策问题]。
方法：[具体分析方法]。
输出：[结论 -> 证据 -> 建议]。
注意：[约束，如"不要用统计术语"、"标注数据异常点"]。
```

### Content Creation Prompts

```
你是[角色]，为[受众]创作[内容类型]。
主题：[具体主题]。
风格：[调性、字数、格式]。
必须包含：[要点1, 2, 3]。
避免：[禁忌1, 2]。
参考示例：[样例]。
```

### Code Generation Prompts

```
用[语言/框架]实现[功能]。
技术栈：[版本、依赖]。
输入：[参数格式]。
输出：[返回值格式]。
要求：[性能/可读性/测试/错误处理]。
不要：[过度设计/使用废弃API]。
上下文：[现有代码库信息]。
```

### Translation/Localization Prompts

```
将以下内容从[源语言]翻译成[目标语言]。
受众：[具体描述，如"中国大陆的00后用户"]。
风格：[正式/口语/营销/技术]。
术语约定：[术语表]。
保留：[品牌名/商标/代码]。
本地化要求：[文化适配说明，如"英文笑话替换为中文梗"]。
```

---

## 4. Common Mistakes and Fixes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| "帮我写个方案" | 不知道什么方案、给谁看、什么格式 | 加上角色、受众、目标、约束 |
| 过长的prompt | 模型注意力分散，抓不住重点 | 结构化、优先最重要的信息 |
| 多个不相关任务 | 模型在一个任务上表现好，多个任务混淆 | 拆分成多次对话 |
| 矛盾的要求 | "详细但简洁" — 模型无法同时满足 | 明确优先级 |
| 缺少输出格式 | 模型自由发挥，产出可能不符合需求 | 指定结构 |
| 角色太泛 | "你是一个专家" — 什么专家？ | 具体化身份和专业领域 |
| 不提约束 | 模型可能产出不该出现的内容 | 明确限制 |
| 没有示例 | 抽象描述不如一个具体例子 | 至少给一个输入/输出示例 |

---

## 5. Testing Your Prompt

Before delivering a prompt to the user, mentally test it:

1. **Ambiguity check**: Could a reasonable person interpret this prompt in multiple ways?
2. **Missing context check**: Is there information the model needs but wasn't provided?
3. **Hallucination risk**: Could the model fabricate information to fulfill this prompt?
4. **Format compliance**: Will the output definitely match the expected format?
5. **Edge case resilience**: What happens with empty input, contradictory data, or impossible requests?
