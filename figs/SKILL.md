---
name: figs
description: Nature 风格科研绘图与论文汇报统一技能（投稿级 Python/R 多面板科研图、论文示意图、论文转中文文献汇报 PPT、幻灯片图片/扫描 PDF 还原为可编辑 PPT）。触发词：科研绘图, Nature figure, 投稿级图片, publication plot, scientific figure, figures4papers, 论文示意图, GPT Image 2, paper PPT, journal club, 论文汇报, 文献汇报, paper to slides, 图片转可编辑PPT, 截图还原PPT, 扫描PDF转PPTX, image to editable PowerPoint。
---

# Nature Figures Suite（合并技能）

本技能是 3 个 nature-skills 图表类技能的统一入口。按任务路由到对应子工作流：**读取该子技能的 SKILL.md 并严格遵循其流程**，本文件不替代它。

| 任务特征 | 子工作流（相对本目录） |
|---|---|
| 投稿级科研图：Python/R 多面板证据架构、模板复用、最终 PDF 文字/图形碰撞审计、AI 示意图草稿（OpenRouter GPT Image 2） | `nature-figure/SKILL.md` |
| 从科研论文生成中文 PPTX 文献汇报 deck（journal club / 组会汇报） | `nature-paper2ppt/SKILL.md` |
| 幻灯片图片、扫描 PDF、图片型 PPTX 重建为对象级可编辑 PowerPoint + 渲染 QA | `nature-image2ppt/SKILL.md` |

路由规则：

- 单一任务只走一个子工作流；用户要求多个阶段（如先作图、再进 PPT 汇报）时按顺序分别执行。
- 子技能内部引用的资源路径（含 `../nature-shared/core/...`、`../nature-shared/journal-formats/...`）均相对该子技能目录解析，`nature-shared/` 与三个子技能平级，直接按原路径读取。
- 子技能 SKILL.md 里若出现 `skills/nature-figure/scripts/...` 这类仓库根相对路径，实际脚本在本技能目录内的 `nature-figure/scripts/` 下，按实际路径执行。
- 子技能 SKILL.md 顶部的 YAML frontmatter 仅作来源标识，执行时以正文流程为准。
