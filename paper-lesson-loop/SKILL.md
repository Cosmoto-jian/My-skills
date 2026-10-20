# 论文解读经验闭环（Lesson Loop）

> 配套 skill：`../local-paper-interpretation/`。本 skill 管"迭代闭环"——每次写作前读一遍历史经验再动笔，写完后把新经验写回去。经验库存在 Notion 的 Memory Log 数据库里。

## 为什么需要这个闭环

单篇解读的质量靠 skill 里的硬规则兜底，但"忠实度""易读性"这类软能力只能靠一篇篇积累。闭环让每一篇的教训（抓错的数字、踩过的排版坑、被用户纠正的表述）都沉淀为下一条可执行的规则，而不是散在聊天记录里。

## 两个步骤

### 0. 动笔前：读经验

```bash
python3 scripts/read_lessons.py
```

读最近 8 条"经验"类型条目，重点看：数字核对时踩过的坑、排版硬规则的新增项、用户纠正过的表述。读完再开始写。

### 6. 写完后：写经验

```bash
python3 write_lesson.py --title "一句话标题" --content "2-5句：是什么+为什么+关键细节"
```

从四个方面总结（每次至少覆盖一条）：

1. **理解**：对论文机制/结论的理解是否有偏差，如何纠正的。
2. **忠实原文献**：数字、引用、图表描述是否全部可回溯；踩过的"凭印象写"坑。
3. **读者易读性**：结构、节奏、术语解释是否对非专业读者友好。
4. **文字写作表达**：去提示词痕迹、中英混杂、口语化过头等文字问题。

一条经验只记一件事，写清楚"是什么+为什么+关键细节"，方便下次直接执行。

## 配置

两个脚本通过环境变量连接 Notion（标准 Notion API，无私有依赖）：

| 环境变量 | 说明 |
|---|---|
| `NOTION_API_KEY` | Notion internal integration token |
| `NOTION_MEMLOG_DATA_SOURCE_ID` | Memory Log 数据库的 data source id |
| `NOTION_PROJECT_ID` | 论文解读项目的 page id（用于关联过滤）|

```bash
export NOTION_API_KEY="secret_..."
export NOTION_MEMLOG_DATA_SOURCE_ID="..."
export NOTION_PROJECT_ID="..."
```

`write_lesson.py` 还支持 `--type`（决策/架构/发布/里程碑/经验/弃用/失败/约束/偏好/待办，默认"经验"）和 `--keywords`（默认"论文解读"）。

## 在流程中的位置

```
读经验（本 skill 步骤 0）
  → 抓全文（local-paper-interpretation：按出版商分流）
  → 数字核对表
  → 按七节成文
  → 自检
  → 交稿前终审（用户过目）
  → 上传发布
  → 写经验（本 skill 步骤 6）
```
