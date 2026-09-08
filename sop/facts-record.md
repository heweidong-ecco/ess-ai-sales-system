# SOP · 事实卡录入(facts-record)

- 适用:L1 内容获客闭环 M1.2 起;任何人/AI 录入事实卡走本流程
- 关联:G2 spec §2(事实卡 schema)、`tools/facts_tool.py`
- 红线:技术/合规表述只准引用**approved** 事实卡(红线1);无来源引用不得成卡

## 一张卡 3 步

1. **建卡**:`python3 tools/facts_tool.py new <class>`(class∈product/advantage/certification/case/company/price)
   → 自动生成 `content/facts/<class>/F-<CLASS>-<nnn>.md`,给出下个可用编号。
2. **填内容**:打开该文件,补 frontmatter(`title/source/markets/keywords/…`)与正文 `zh`(+`en`,+`de` 按需);
   内容只从**权威来源**摘取,`source` 指向来源登记条目或文件+位置。
   → 定稿为可引用需改 `status: approved` 并填 `reviewer/reviewed_at`(业务负责人核验)。
3. **校验+入索引**:`python3 tools/facts_tool.py validate <该文件>`(通过应打印无 FAIL);再 `python3 tools/facts_tool.py index` 重建 `_index.md`。

## 命令速查

| 命令 | 作用 |
|---|---|
| `python3 tools/facts_tool.py new product` | 建新卡(自动编号) |
| `python3 tools/facts_tool.py validate` | 校验全部卡 |
| `python3 tools/facts_tool.py validate content/facts/product/F-PRODUCT-001.md` | 校验单卡 |
| `python3 tools/facts_tool.py index` | 重建可检索索引 |
| `python3 tools/facts_tool.py search <词>` | 检索(标题/关键词/正文,忽略大小写) |

## 校验会拦什么

- 必填缺失:`id/class/title/source`;`approved` 缺 `reviewer/reviewed_at`
- 编号非法 / 与类别目录不一致 / 跨卡 id 重复(作废不重号)
- `status`/`class` 不在枚举内;正文缺 `## zh`

## 纪律

- 编号由工具生成,人工不写死;作废卡改 `status: obsolete` 不删文件不重号。
- frontmatter 用 LF 换行、勿带行尾注释;编号由工具生成,勿手写/手抄(文件名 stem、`id`、所在目录 class 三者须一致)。
- 只有 `approved` 卡被正文引用;`obsolete` 停用。更新卡内容后必须重跑核验(改 `reviewed_at`)。
- 本 SOP 随卡片量增长可演进(如批量录入),但 schema 变更须回 G2 spec 评审后再改。
