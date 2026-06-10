# Clarification Question Bank

**Purpose:** Structured question templates organized by domain and signal. Use when the user's input is too vague to directly generate a quality prompt.

---

## When to Ask Questions

**Ask when:**
- The goal is ambiguous ("帮我分析" — analyze what? For what decision?)
- The audience is unclear (self-use? Boss? Client? Public?)
- The format is unspecified
- The scope is too broad ("全面分析" is infinite scope)
- Constraints are missing

**Don't ask when:**
- The user already provided goal + audience + format + constraints
- The missing information is minor and you can make reasonable assumptions
- The user explicitly said "just give me a template, I'll fill in details"

---

## Question Bank by Signal

### Signal: Ambiguous Goal

User says: "帮我分析一下这个数据" / "帮我写个方案" / "给我一些建议"

Ask:
1. "这个分析/方案/建议最终要驱动什么决策或行动？" (What decision will this drive?)
2. "你希望得到什么类型的结果？一份报告？一个数字？一个方案？还是一个清单？"
3. "有没有你觉得很好的类似案例可以参考？"

### Signal: Missing Audience

User says: "帮我写一个报告" (no mention of reader)

Ask:
1. "这个报告给谁看？你自己看还是给领导/客户/团队看？"
2. "读者对这个话题的了解程度大概如何？需要解释基础概念还是可以直接深入？"
3. "读者最关心什么？成本？效率？风险？还是创新？"

### Signal: Missing Format

User says: "帮我整理这些信息"

Ask:
1. "你希望最终产出什么格式？Word文档？PPT？Excel表格？还是纯文本？"
2. "有没有公司或团队固定的模板需要遵循？"
3. "你希望多长？一句话总结还是一份完整报告？"

### Signal: Scope Too Broad

User says: "帮我全面分析市场" / "给我一个完整的方案"

Ask:
1. "我们能不能缩小范围？你最关心的2-3个方面是什么？"
2. "有没有时间、地域、人群等限制？比如只看中国市场还是全球？"
3. "如果只能回答一个最关键的问题，那个问题是什么？"

### Signal: Existing Prompt to Fix

User pastes an existing prompt and says it doesn't work well

Ask:
1. "这个prompt目前的输出有什么不满意的地方？"
2. "你期望的理想输出是什么样的？"
3. "你用的是哪个AI？(Claude/ChatGPT/DeepSeek/Gemini/其他)"

---

## Domain-Specific Questions

### Data Analysis
- "数据大概多少行/列？什么格式(Excel/CSV/数据库)？"
- "你更关心趋势变化还是单点异常？"
- "需要可视化图表吗？什么类型？"

### Content Creation
- "目标读者看到这篇文章后，你希望他们做什么？(转发/购买/关注/思考)"
- "有没有竞品或你喜欢的内容风格可以参考？"
- "品牌调性是什么？严肃专业还是轻松幽默？"

### Business/Strategy
- "这个决策的时间范围是什么？(本月/本季度/今年)"
- "预算/资源有限制吗？要不要考虑成本约束？"
- "失败的最大代价是什么？我们在多大程度上可以冒险？"

### Code/Technical
- "现有的技术栈是什么？语言、框架、版本？"
- "这个代码会被集成到现有项目中吗？如果是，上下文是什么？"
- "更看重开发速度还是代码质量？"

### Translation/Localization
- "目标读者是哪里人？(中国大陆/台湾/香港/海外华人/外国人)"
- "有没有术语表或品牌词需要保持一致？"
- "原文中有文化梗需要本地化处理吗？"

---

## Question Principles

1. **Max 3-4 at a time** — Don't overwhelm the user with 10 questions
2. **Priority-ordered** — Most impactful question first
3. **Provide defaults** — "你希望多长？比如500字简短分析还是2000字深度报告？" (hint at reasonable options)
4. **Explain why** — "我需要了解[这个信息]，因为[它对prompt质量的影响]"
5. **Skip obvious ones** — If context makes something clear, don't ask
6. **One round only** — After one round of clarification, generate the prompt with reasonable defaults for anything still unclear

---

## Default Assumptions (When User Skips Clarification)

If the user doesn't answer your clarifying questions, use these defaults:

| Dimension | Default |
|-----------|---------|
| Audience | The user themselves |
| Format | Markdown text |
| Length | 500-1500 words (medium) |
| Tone | Professional but not academic |
| Platform | Claude (universal-friendly) |
| Uncertainty | "请指出不确定的地方" |
| Language | Match the user's language |
