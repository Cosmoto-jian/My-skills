---
name: writing
description: Nature 风格科研写作统一技能（润色/翻译为 Nature 英文、起草手稿章节与摘要、模拟审稿报告、审稿回复信与 cover letter、开题与研究方案）。触发词：润色, polish, Nature style, 论文英文, 写摘要, 写引言, manuscript draft, 论文写作, Nature reviewer, 审稿人视角, reviewer report, 预投稿评审, rebuttal, 返修邮件, 审稿意见回复, response to reviewers, cover letter, proposal, 开题报告, 研究方案。
---

# Nature Writing Suite（合并技能）

本技能是 5 个 nature-skills 写作类技能的统一入口。按任务路由到对应子工作流：**读取该子技能的 SKILL.md 并严格遵循其流程**，本文件不替代它。

| 任务特征 | 子工作流（相对本目录） |
|---|---|
| 学术文本润色、重构、翻译为 Nature 风格英文；全文术语/单位/数值精度/声称漂移扫描 | `nature-polishing/SKILL.md` |
| 起草 Nature 风格手稿章节（摘要、引言、结果、讨论）、重建论文论证 | `nature-writing/SKILL.md` |
| 审稿人视角模拟评审：三份互盲 reviewer reports、Major/Minor 分级、手稿内部一致性检查 | `nature-reviewer/SKILL.md` |
| 解析返修邮件、为各审稿人分别生成回复、cover letter、标红稿、LaTeX 返修包 | `nature-response/SKILL.md` |
| proposal-first 写作状态机：先立证据/论证/章节契约，再起草或审查（开题报告、研究方案） | `nature-proposal-writer/SKILL.md` |

路由规则：

- 单一任务只走一个子工作流，不要混用多家的流程步骤；用户要求多个阶段（如先润色、再写回复信）时按顺序分别执行。
- 子技能内部引用的资源路径（含 `../nature-shared/core/...`、`../nature-shared/journal-formats/...`）均相对该子技能目录解析，`nature-shared/` 与五个子技能平级，直接按原路径读取即可。
- 子技能 SKILL.md 顶部的 YAML frontmatter 仅作来源标识，执行时以正文流程为准。
