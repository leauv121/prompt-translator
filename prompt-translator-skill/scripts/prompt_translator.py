#!/usr/bin/env python3
"""
Prompt Translator — Natural Language to Optimized AI Prompt Converter.

This script provides the underlying prompt analysis and optimization
logic used by the prompt-translator-skill. It can be used standalone
or as a library.

Usage:
    python prompt_translator.py translate "我需要分析销售数据"
    python prompt_translator.py optimize existing_prompt.txt
    python prompt_translator.py template --type analysis
"""

import argparse
import sys
import json
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# SPACES Framework
# ---------------------------------------------------------------------------

SPACES_ELEMENTS = {
    "S": {
        "name": "System/Role",
        "zh": "角色设定",
        "description": "Who the AI should be — identity, expertise, context, audience",
        "example": "你是一位有10年经验的电商数据分析师，擅长从GMV、客单价、复购率等指标中识别增长瓶颈。",
    },
    "P": {
        "name": "Problem/Task",
        "zh": "任务描述",
        "description": "What needs to be done — specific, measurable, decision-driven",
        "example": "分析Q3销售数据，判断营收下滑是由客流量下降还是客单价下降导致。",
    },
    "A": {
        "name": "Audience",
        "zh": "受众设定",
        "description": "Who the output is for — determines language, depth, format",
        "example": "你的报告面向CEO和CFO，需要结论先行，使用商业语言。",
    },
    "C": {
        "name": "Constraints",
        "zh": "约束条件",
        "description": "Rules, limits, do's and don'ts, uncertainty handling",
        "example": "不要使用专业术语；如果数据不足以得出结论，请明确指出，不要猜测。",
    },
    "E": {
        "name": "Examples",
        "zh": "示例参考",
        "description": "Few-shot examples — the highest-ROI prompt technique",
        "example": "参考这个格式：[提供一个具体的输入/输出示例]",
    },
    "S": {
        "name": "Structure",
        "zh": "输出结构",
        "description": "Output format specification — sections, order, length",
        "example": "输出结构：1. 核心结论 2. 数据支撑 3. 可执行建议",
    },
}


# ---------------------------------------------------------------------------
# Prompt Analysis
# ---------------------------------------------------------------------------

def analyze_prompt(prompt: str) -> dict:
    """Analyze a prompt for missing SPACES elements.

    Args:
        prompt: The user's raw prompt text.

    Returns:
        A dict with scores and recommendations for each SPACES dimension.
    """
    analysis = {
        "original": prompt,
        "length": len(prompt),
        "elements": {},
        "overall_score": 0.0,
        "recommendations": [],
    }

    # Heuristic checks for each SPACES element
    checks = {
        "S_Role": _has_role(prompt),
        "P_Specificity": _is_specific(prompt),
        "A_Audience": _has_audience(prompt),
        "C_Constraints": _has_constraints(prompt),
        "E_Examples": _has_examples(prompt),
        "S_Structure": _has_structure(prompt),
    }

    for key, score in checks.items():
        analysis["elements"][key] = score
        if score < 0.5:
            analysis["recommendations"].append(_get_recommendation(key))

    scores = list(checks.values())
    analysis["overall_score"] = sum(scores) / len(scores) if scores else 0.0

    return analysis


def _has_role(text: str) -> float:
    """Check if the prompt assigns a role to the AI."""
    role_keywords = [
        "你是", "你是一位", "你是", "作为", "acting as", "you are a",
        "你是我的", "假设你是", "请扮演", "你是一名", "资深", "专家",
        "分析师", "工程师", "顾问", "教练", "编辑", "设计师",
    ]
    matches = sum(1 for kw in role_keywords if kw.lower() in text.lower())
    return min(matches / 2.0, 1.0)


def _is_specific(text: str) -> float:
    """Check if the prompt has specific task instructions."""
    vague_patterns = ["分析", "帮我", "写一个", "给建议", "整理"]
    specific_indicators = [
        "找出", "判断", "对比", "排名", "计算", "生成",
        "具体", "数字", "%", "表格", "步骤", "原因",
        "输出", "格式", "结构",
    ]
    vague_count = sum(1 for p in vague_patterns if p in text and len(text) < 50)
    specific_count = sum(1 for p in specific_indicators if p.lower() in text.lower())
    base = min(specific_count / 3.0, 1.0)
    penalty = vague_count * 0.2
    return max(base - penalty, 0.0)


def _has_audience(text: str) -> float:
    """Check if the prompt specifies an audience."""
    audience_keywords = [
        "面向", "给.*看", "读者", "受众", "领导", "老板",
        "CEO", "客户", "团队", "用户", "学生", "新手",
        "专业人士", "技术", "非技术",
    ]
    matches = sum(1 for kw in audience_keywords if kw.lower() in text.lower())
    return min(matches / 1.0, 1.0)


def _has_constraints(text: str) -> float:
    """Check if the prompt includes constraints."""
    constraint_keywords = [
        "不要", "禁止", "避免", "限制", "不超过", "不少于",
        "必须", "确保", "注意", "约束", "要求",
        "如果.*请", "不确定", "不要猜测",
    ]
    matches = sum(1 for kw in constraint_keywords if kw.lower() in text.lower())
    return min(matches / 2.0, 1.0)


def _has_examples(text: str) -> float:
    """Check if the prompt includes examples."""
    example_keywords = [
        "例如", "比如", "示例", "参考", "样例",
        "输入：", "输出：", "样本", "像这样",
    ]
    matches = sum(1 for kw in example_keywords if kw.lower() in text.lower())
    return min(matches / 1.0, 1.0)


def _has_structure(text: str) -> float:
    """Check if the prompt specifies output structure."""
    structure_keywords = [
        "按.*格式", "输出结构", "分为", "包含以下", "请按",
        "第1", "第2", "首先", "然后", "最后",
        "表格", "列表", "markdown", "json",
        "1.", "2.", "3.", "第一部分", "第二部分",
    ]
    matches = sum(1 for kw in structure_keywords if kw.lower() in text.lower())
    return min(matches / 2.0, 1.0)


def _get_recommendation(key: str) -> str:
    """Get a human-readable recommendation for a missing element."""
    recommendations = {
        "S_Role": "添加角色设定：告诉AI它是谁、擅长什么、为谁服务",
        "P_Specificity": "具体化任务：说明要做什么、目标是什么、产出什么",
        "A_Audience": "明确受众：谁会看这个输出？他们对话题了解多少？",
        "C_Constraints": "添加约束：格式、长度、风格、禁止事项、不确定时的处理",
        "E_Examples": "提供示例：一个具体的输入/输出示例胜过很多描述",
        "S_Structure": "指定输出结构：告诉AI按什么格式组织回答",
    }
    return recommendations.get(key, f"Improve element: {key}")


# ---------------------------------------------------------------------------
# Prompt Template Generation
# ---------------------------------------------------------------------------

TEMPLATES = {
    "analysis": {
        "label": "数据分析",
        "template": """你是{role}。请分析以下数据。

**目标：** {goal}

**数据：**
{data}

**输出格式：**
1. 核心发现 (2-3条)
2. 数据支撑 (表格)
3. 可执行建议 (按优先级)

**约束：**
- {constraints}
- 如果数据不足以得出结论，请明确指出""",
    },
    "writing": {
        "label": "内容创作",
        "template": """你是{role}。请写一篇关于{topic}的{content_type}。

**受众：** {audience}
**字数：** {length}
**风格：** {tone}

**结构：**
{structure}

**约束：**
- {constraints}""",
    },
    "coding": {
        "label": "代码生成",
        "template": """你是{role}。请用{language}实现以下功能。

**功能描述：** {goal}

**技术要求：**
- {tech_requirements}
- 包含完整的错误处理
- 添加类型提示

**不要：**
- {donts}""",
    },
    "decision": {
        "label": "决策支持",
        "template": """你是{role}。请帮我做以下决策。

**决策问题：** {goal}

**背景：** {context}

**可选方案：**
{options}

**评估维度：**
{evaluation_dimensions}

**输出格式：**
1. 各方案对比 (表格)
2. 推荐方案及理由
3. 风险提示
4. 下一步行动""",
    },
    "general": {
        "label": "通用模板",
        "template": """你是{role}。

**任务：** {goal}

**受众：** {audience}

**输出格式：**
{structure}

**约束：**
- {constraints}

**示例：**
{examples}""",
    },
}


def generate_template(template_type: str, **kwargs) -> str:
    """Generate a filled prompt template.

    Args:
        template_type: One of 'analysis', 'writing', 'coding', 'decision', 'general'.
        **kwargs: Values to fill into the template placeholders.

    Returns:
        A filled prompt string.
    """
    if template_type not in TEMPLATES:
        available = ", ".join(TEMPLATES.keys())
        raise ValueError(f"Unknown template type '{template_type}'. Available: {available}")

    template = TEMPLATES[template_type]["template"]
    label = TEMPLATES[template_type]["label"]

    # Fill with defaults for any missing kwargs
    defaults = {
        "role": "[角色 — 描述AI应该扮演的专业身份]",
        "goal": "[任务目标 — 具体要完成什么]",
        "data": "[待分析的数据]",
        "audience": "[受众 — 谁会使用这个输出]",
        "length": "[字数范围]",
        "tone": "[风格 — 正式/口语/专业/轻松]",
        "content_type": "[内容类型 — 文章/报告/邮件/帖子]",
        "topic": "[主题]",
        "language": "[编程语言]",
        "context": "[决策背景 — 相关信息和约束]",
        "options": "- [方案A]\n- [方案B]\n- [方案C]",
        "evaluation_dimensions": "- [维度1: 如成本]\n- [维度2: 如风险]",
        "structure": "1. [部分1]\n2. [部分2]\n3. [部分3]",
        "constraints": "[格式/长度/风格要求]",
        "examples": "[输入示例]\n→ [期望输出示例]",
        "tech_requirements": "- [如：使用pandas处理数据]",
        "donts": "- [不要做的事情]",
    }
    defaults.update(kwargs)

    try:
        filled = template.format(**defaults)
    except KeyError as e:
        filled = template.format(**defaults)  # Retry with all defaults
        filled = filled.replace("{" + str(e).strip("'") + "}", defaults.get(str(e).strip("'"), "[...]"))

    return f"## {label}模板\n\n{filled}"


# ---------------------------------------------------------------------------
# CLI Interface
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Prompt Translator — Natural Language to Optimized Prompt Converter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python prompt_translator.py analyze "帮我分析销售数据"
  python prompt_translator.py template --type analysis
  python prompt_translator.py template --type writing --role "科技编辑" --topic "远程办公"
  python prompt_translator.py optimize prompt.txt
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze a prompt for completeness")
    analyze_parser.add_argument("prompt", nargs="?", help="The prompt to analyze (or use --file)")
    analyze_parser.add_argument("--file", type=str, help="Read prompt from file")
    analyze_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # template command
    template_parser = subparsers.add_parser("template", help="Generate a prompt template")
    template_parser.add_argument("--type", type=str, default="general",
                                choices=list(TEMPLATES.keys()),
                                help="Template type")
    template_parser.add_argument("--role", type=str, help="Role to fill in")
    template_parser.add_argument("--goal", type=str, help="Task goal")
    template_parser.add_argument("--topic", type=str, help="Topic (for writing)")
    template_parser.add_argument("--audience", type=str, help="Target audience")
    template_parser.add_argument("--structure", type=str, help="Output structure")
    template_parser.add_argument("--constraints", type=str, help="Constraints")

    args = parser.parse_args()

    if args.command == "analyze":
        prompt_text = args.prompt
        if args.file:
            prompt_text = Path(args.file).read_text(encoding="utf-8")
        if not prompt_text:
            print("Error: No prompt provided. Use --file or pass prompt directly.", file=sys.stderr)
            sys.exit(1)

        result = analyze_prompt(prompt_text)

        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"\n{'='*60}")
            print(f"📊 Prompt Analysis")
            print(f"{'='*60}")
            print(f"Length: {result['length']} chars")
            print(f"Overall Score: {result['overall_score']:.1%}")
            print(f"\nElement Scores:")
            for key, score in result["elements"].items():
                bar = "█" * int(score * 10) + "░" * (10 - int(score * 10))
                print(f"  {key:20s} [{bar}] {score:.0%}")
            if result["recommendations"]:
                print(f"\n💡 Recommendations:")
                for i, rec in enumerate(result["recommendations"], 1):
                    print(f"  {i}. {rec}")
            print()

    elif args.command == "template":
        kwargs = {k: v for k, v in vars(args).items()
                  if k not in ("command", "type") and v is not None}
        template = generate_template(args.type, **kwargs)
        print(template)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
