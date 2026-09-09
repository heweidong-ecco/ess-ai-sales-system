# SOP · 选题卡(brief)生成与排期(brief-creation)

- 适用:L1 M2.1 起;内容执行者(AI + 人)按本流程产出一张可选用的选题卡。
- 关联:`content/pipeline/_brief-template.md`、`content/keywords/`、G2 facts、外部调研附录 A1。
- 红线:**选题 ≠ 成稿**。brief 只定位"给谁、解决什么、用什么角度、需要哪些 Facts";成稿前必须 facts_required 就绪(见事实卡 SOP `sop/facts-record.md`)且人审(总纲红线1/3)。

## 输入(三选一即可开题)

- **人设 + 市场 + 意图**:例"欧洲 C&I 集成商 + DE 市场 + 评估" → 由下到上按意图落漏斗。
- **回流问题/一线反馈**:销售/客户反复问的问题(M4 回流、L1 选题来源)。
- **选题种子库**:外部调研附录 A1(T1~T8)或 `content/keywords/` 对应行。

## 五步产出 brief

1. **定人设/市场/意图** → 写清 persona、market、intent、funnel(顶/中/底);同意图多篇时排优先级。
2. **定关键词** → 从 `content/keywords/` 取 1~3 个词(EN 主稿词,DE 二期词);无合适词可新增,按 keywords README 纪律标注。
3. **列 Facts 需求** → 写出该选题会引用的卡片方向(F-CERT-*/F-PRODUCT-*/F-COMPANY-*/F-CASE-*);**未录的明确标"待 O3/O4"**,禁止假定事实已存在。
4. **填 brief** → 复制 `_brief-template.md` 到 `content/pipeline/<slug>/brief.md`,逐字段填;编号 B-<nnn> 顺序递增。
5. **评审与排期** → 与业务负责人过一遍角度与 CTA;定 priority 与 status(草稿→在用);进入渠道模板(M2.2)产出草稿。

## 断点纪律

- brief 中出现"尚无 Facts 支撑的技术/合规表述"→ 阻断,退回步骤 3,不得带病进成稿。
- 引用外部研究(市场数字/行业趋势)仅作文档语境定位;对外的具体数字由公司市场部核验后再用。
- 单篇完整链路(选题→成稿→人审→发布→登记)见 L1-MVP 验收。

## 速查

| 文件 | 用 |
|---|---|
| `content/pipeline/_brief-template.md` | 复制成新选题卡 |
| `content/keywords/seeds-2026-09-08.md` | 首批关键词种子(T1~T8) |
| `docs/discovery/2026-09-08-research-ci-ess-external.md` | 外部语境(A1 选题 / A/B/C 深度) |
| `sop/facts-record.md` | 事实卡就绪后引用 |
