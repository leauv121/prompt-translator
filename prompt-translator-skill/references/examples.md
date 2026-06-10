# Before/After Examples

**Purpose:** Concrete examples of prompt transformation. Load when users want to see how the skill improves prompts, or as reference during optimization.

---

## Example 1: Data Analysis

### User's Original Request
> "帮我分析一下这个季度的销售数据"

### What's Missing
- What decision does the analysis drive?
- What specific aspect of sales?
- What format should the output take?
- Who reads it?

### Optimized Prompt

```
你是一位零售行业的数据分析师，有10年经验。请帮我分析附件中的Q2销售数据。

**目标：** 判断营收同比增长仅2%的主要原因是客流下降还是客单价下降，以便CFO决定Q3是在引流还是提价上加大投入。

**数据说明：**
- 包含每日销售额、客流量、客单价、退货率
- 覆盖全国12个门店
- 去年同期数据作为对比

**输出格式：**
1. 总体结论 (2-3句话，结论先行)
2. 关键指标对比 (Q2 vs 去年同期，表格呈现)
   - 总营收、客流量、客单价、退货率
3. 下滑归因分析
   - 客流因素 vs 客单价因素的量化占比
4. 门店表现排名 (按营收增长率)
5. Q3建议 (按优先级排列，每条建议标注预期影响)

**约束：**
- 面向CFO和CEO，用商业语言，不要统计学术语
- 如果某天数据异常请标注
- 如果两个因素影响程度接近（差异<10%），请明确说明，不要强行归因
- 结论必须基于数据，不要引入外部假设
```

### What Improved
| Dimension | Before | After |
|-----------|--------|-------|
| Role | None | 零售数据分析师，10年经验 |
| Goal | 模糊的"分析" | 具体决策：引流还是提价 |
| Audience | Unknown | CFO & CEO |
| Structure | None | 5段式结构化输出 |
| Constraints | None | 商业语言、标注异常、不强行归因 |

---

## Example 2: Content Creation

### User's Original Request
> "帮我写一篇公众号文章，关于远程办公的"

### What's Missing
- Target audience
- Article angle/perspective
- Length and tone
- Call to action

### Optimized Prompt

```
你是一位关注未来工作方式的科技编辑，擅长用数据和故事结合的方式写作。

**任务：** 撰写一篇面向中国互联网从业者的公众号文章，讨论远程办公的未来趋势。

**受众：** 25-35岁的互联网从业者，对远程办公有兴趣但担心效率问题，希望看到客观分析而非一边倒的鼓吹。

**文章要求：**
- 标题：提供3个候选标题（信息量高，不标题党）
- 长度：2500-3500字
- 结构：
  1. 开篇以一个真实远程工作者的故事引入
  2. 国内外远程办公数据对比（请基于你的知识提供数据）
  3. 远程办公的3个真问题和3个被夸大的问题
  4. 适合/不适合远程的工作类型分析
  5. 给管理者和员工的可操作建议（各3条）
- 风格：理性、数据驱动、有温度但不煽情

**约束：**
- 不要用"未来已来""新常态"等陈词滥调
- 数据引用请标注来源和时间
- 如果某观点业内存在争议，请呈现双方观点
- 结尾不要用"你怎么看？欢迎留言"这种模板话术
```

### What Improved
| Dimension | Before | After |
|-----------|--------|-------|
| Role | None | 科技编辑，数据+故事风格 |
| Audience | None | 25-35岁互联网从业者 |
| Structure | None | 5段式结构 + 标题候选 |
| Constraints | None | 禁用陈词滥调、标注来源、呈现争议 |
| Length | Not specified | 2500-3500字 |

---

## Example 3: Code Generation

### User's Original Request
> "帮我写一个Python脚本处理Excel文件"

### What's Missing
- What processing exactly?
- Input/output format
- Error handling expectations
- Edge cases

### Optimized Prompt

```
你是一位Python后端工程师，擅长数据处理。请写一个Python脚本来处理销售Excel报表。

**功能：** 读取多个Excel文件，合并、清洗、输出汇总报表。

**输入：**
- 文件夹中包含多个.xlsx文件，每个文件的sheet名和列结构相同
- 列：日期 | 门店 | 商品SKU | 销量 | 销售额 | 退货数
- 文件名格式：sales_[门店名]_[年月].xlsx（如 sales_北京_202606.xlsx）

**处理逻辑：**
1. 读取文件夹中所有匹配的.xlsx文件
2. 合并为一个DataFrame
3. 清洗：日期列统一为datetime、缺失值标记为NaN不删除、销售额=销量*单价且在合理范围内(±3σ)不过滤
4. 按门店汇总：总销量、总销售额、退货率
5. 按商品SKU汇总：同上
6. 输出两个汇总表到新Excel文件

**技术要求：**
- 使用 pandas 和 openpyxl
- 包含完整的错误处理（文件不存在、sheet名不匹配、列名变化）
- 添加日志记录每一步的处理条数和异常条数
- 类型提示 (type hints)
- 用 argparse 接受输入/输出路径
- 结果文件命名为 summary_[日期].xlsx

**不要：**
- 使用全局变量
- 硬编码路径
- 忽略警告
```

### What Improved
| Dimension | Before | After |
|-----------|--------|-------|
| Input | "Excel文件" | 具体格式、列名、文件名规则 |
| Processing | "处理" | 6步具体逻辑，每步有明确规则 |
| Error handling | None | 文件、格式、内容三重异常处理 |
| Output | None | 两个汇总表，具体列和文件名 |
| Technical | None | 库选择、日志、类型提示、argparse |

---

## Example 4: Prompt Optimization (Existing Prompt)

### User's Existing Prompt
> "你是一个专业的助手，请帮我分析市场趋势。请全面深入地分析，给出有价值的建议。要专业。谢谢。"

### Problems Identified
1. "专业助手" — too generic
2. "市场" — which market?
3. "全面深入" — scope is impossibly broad
4. "有价值的建议" — by whose standards?
5. "要专业" — what does "professional" mean in context?
6. "谢谢" — polite but unnecessary, takes token space

### Optimized Prompt

```
你是一位专注于中国新能源汽车市场的行业分析师。请分析2026年Q2的市场竞争格局。

**分析维度：**
1. 市场份额变化 (TOP5品牌，与Q1对比)
2. 价格带竞争 (10-20万、20-30万、30万+三个区间的主要玩家和策略)
3. 技术趋势 (电池、智驾、座舱三个维度的最新进展)
4. 关键变量 (锂价、政策变化、新进入者的影响预判)

**受众：** 一家二线新能源车企的战略部，正在制定2026下半年的产品定价和营销策略。

**输出格式：**
1. 执行摘要 (5句话，每条一个关键判断)
2. 分维度的详细分析
3. 机会与威胁矩阵
4. 可执行的战略建议 (每条建议标注置信度：高/中/低)

**约束：**
- 数据截至2026年5月，请标注数据来源和时间
- 如果某判断缺乏数据支持，请说明"基于行业经验推断"而非暗示有数据
- 避免过度关注头部企业（比亚迪），更多关注腰部品牌的竞争动态
- 建议必须是"下周可以在会上讨论"的具体方案，而非笼统的方向
```

### What Improved
| Dimension | Before | After |
|-----------|--------|-------|
| Role | "专业助手" | 新能源汽车行业分析师 |
| Scope | "市场趋势" (infinite) | 4个具体分析维度 |
| Audience | Unknown | 二线车企战略部 |
| Actionability | "有价值的建议" | "下周可以在会上讨论的具体方案" |
| Constraints | "要专业" | 标注来源、置信度、避免过度关注头部企业 |

---

## Pattern Summary

Every optimized prompt follows the same transformation pattern:

```
模糊描述 → 具体任务 + 角色设定 + 受众 + 输出格式 + 约束 + 示例

"帮我分析X" → "作为[角色]，分析[X数据]，目的是[驱动Y决策]，
               面向[Z受众]。请按[结构]输出。注意[约束]。例如：[示例]"
```
