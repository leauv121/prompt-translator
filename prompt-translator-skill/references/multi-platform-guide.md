# Multi-Platform Prompt Adaptation Guide

**Purpose:** Detailed reference for adapting prompts across different AI platforms. Load when users specify a target platform.

---

## Platform Characteristics

### Claude (Anthropic)

**Strengths:** Long-form reasoning, nuanced analysis, detailed instructions, creative writing, code generation
**Prompt style:** Detailed, contextual, structured
**Key features:** Extended thinking (Opus), long context window, strong tool use

**Adaptation rules:**
- Provide rich context — Claude thrives on detail
- Use XML-like tags for structure: `<role>`, `<task>`, `<constraints>`
- Chain reasoning explicitly: "First think through X, then do Y, then verify Z"
- Long prompts are fine — Claude handles up to 200K context
- Use `Human:` and `Assistant:` separation for multi-turn patterns

**Template:**
```
Human: 你是[角色]。请[任务]。

背景：[上下文]

请按以下步骤思考：
1. [推理步骤1]
2. [推理步骤2]
3. [给出最终答案]

约束：
- [约束1]
- [约束2]

Assistant: 我来逐步分析...
```

### ChatGPT (OpenAI)

**Strengths:** Fast generation, broad knowledge, strong at following format instructions
**Prompt style:** Concise, system/user separation, markdown-heavy output
**Key features:** System message, function calling, JSON mode

**Adaptation rules:**
- Separate system-level instructions from user messages
- Be more concise than Claude — ChatGPT prefers focused prompts
- Use markdown formatting heavily — ChatGPT excels at markdown output
- For structured output, specify "Respond in JSON format"
- Avoid overly long prompts — break into conversation turns

**Template:**
```
System: 你是[角色]。输出格式：[格式要求]。约束：[关键约束]。

User: [具体任务]
[输入数据]
[期望的输出格式]
```

### DeepSeek

**Strengths:** Reasoning (R1), cost-effective, strong at math and code
**Prompt style:** Chain-of-thought markers, explicit step instructions
**Key features:** Reasoning mode, Chinese-optimized, cost-efficient

**Adaptation rules:**
- Chinese prompts work natively and often better
- Use explicit reasoning markers: "请逐步思考"，"第一步...第二步..."
- Keep system prompts minimal — DeepSeek prefers direct instructions
- For V3: straightforward instructions work best
- For R1: lean into chain-of-thought with explicit thinking steps
- Avoid overly creative or ambiguous instructions

**Template:**
```
请一步一步地完成以下任务：

任务：[具体描述]

第1步：[第一步做什么]
第2步：[第二步做什么]
第3步：[给出最终答案]

注意：
- [约束1]
- [约束2]

输出格式：[具体格式]
```

### Gemini (Google)

**Strengths:** Multi-modal, large context, Google ecosystem integration
**Prompt style:** Concise, multi-modal aware, structured
**Key features:** Multi-modal input, grounding, very long context

**Adaptation rules:**
- Keep it concise — Gemini prefers shorter, clearer instructions
- Mention if multi-modal inputs are involved
- Use numbered lists for structure
- Avoid role-play heavy setups
- Leverage grounding when relevant ("use Google Search knowledge")

**Template:**
```
Task: [specific task description]

Role: [short role definition]

Output requirements:
1. [requirement 1]
2. [requirement 2]

Constraints:
- [constraint]
```

---

## Decision Matrix

| Factor | Claude | ChatGPT | DeepSeek | Gemini |
|--------|--------|---------|----------|--------|
| Prompt length | Long OK | Medium | Medium | Short |
| Role detail | High | Medium | Low-Medium | Low |
| Chinese quality | Excellent | Good | Excellent | Good |
| Reasoning tasks | ★★★★★ | ★★★★ | ★★★★★ | ★★★★ |
| Creative tasks | ★★★★★ | ★★★★ | ★★★ | ★★★★ |
| Code generation | ★★★★★ | ★★★★ | ★★★★★ | ★★★★ |
| Format adherence | ★★★★ | ★★★★★ | ★★★★ | ★★★★ |
| Context needed | Rich | Moderate | Minimal | Minimal |

---

## Platform-Specific Anti-Patterns

### Claude
- ❌ One-line prompts — wastes reasoning capability
- ❌ "你是专家" without context — be specific about what kind of expert
- ✅ "你是[具体领域]专家，有[X年]经验，擅长[Y]"

### ChatGPT
- ❌ Overly long system messages — keep it focused
- ❌ Mixing system and user instructions redundantly
- ✅ Clear separation: system = who you are + format; user = what to do

### DeepSeek
- ❌ Vague role assignments — prefers direct task descriptions
- ❌ Creative ambiguity — prefers explicit, structured instructions
- ✅ "请按以下步骤：1. ... 2. ... 3. ..."

### Gemini
- ❌ Multi-paragraph role descriptions
- ❌ Heavy XML/HTML tagging in prompts
- ✅ Short role + numbered requirements

---

## Universal Prompt (Cross-Platform Safe)

When the user doesn't specify a platform, use the universal template that works well everywhere:

```
你是[具体角色]。

任务：[清晰的任务描述]

输出格式：
1. [部分1]
2. [部分2]

要求：
- [约束1]
- [约束2]

示例输入：[如有]
示例输出：[如有，这是最有效的提高准确率的方式]
```

This template is:
- Short enough for any platform
- Structured enough for consistent results
- Has role, task, format, constraints — the essentials
- Includes example when possible (highest ROI technique across all platforms)
