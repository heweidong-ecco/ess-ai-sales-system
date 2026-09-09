# DEMO 交付说明 · 工商业储能出海 AI 营销系统(需求驱动演示)

- 日期:2026-09-09
- 定位:本仓库为一套**需求驱动产品开发 + superpowers 工作流**的方法论演示,用虚构演示数据(MiraSol)把 L1 内容获客闭环的工具与流程完整跑通;**不含任何真实公司/业务/素材**。
- 关联:`系统总纲.md`、`docs/ROADMAP.md`(指针)、`需求文档.md`(需求基线)、`content/demo-kit.md`。

## 一、演示了什么(模块 → 位置)

| 层 | 交付物 | 位置 | 状态 |
|---|---|---|---|
| 治理与需求 | 需求基线化(无招牌内容)、DEC-001~005、G1~G3 决策 | 根 + `docs/decisions/` | ✔ |
| 事实卡工具 | facts_tool:new/validate/index/search(28 测试) | `tools/facts_tool.py`、`tests/` | ✔ |
| 演示事实库 | 34 张 MiraSol 虚构卡(validate 通过+索引) | `content/facts/` | ✔ demo |
| 选题体系 | brief 模板 + keywords 首批种子 + SOP | `content/pipeline/_brief-template.md`、`content/keywords/`、`sop/brief-creation.md` | ✔ |
| 渠道模板 | blog / linkedin / ali-detail / video-script | `sop/channel-templates/` | ✔ |
| 端到端切片 | B-001 认证主题:brief→EN blog→DE 译制→变体→发布记录 | `content/pipeline/demo-b001-certifications-blog/` | ✔ demo |
| 发布看板 | tracker 状态流(草稿→审校→待发→已发) | `content/tracker.md` | ✔ demo |
| 回流登记 | 周回流模板 + 演示周报 | `content/reflux/` | ✔ demo |
| 多语言 | EN↔DE 演示术语表 | `content/glossary/_glossary-demo.md` | ✔ demo |

## 二、怎么复现
1. 事实卡校验/索引:`python3 tools/facts_tool.py validate` / `index`;全量测试 `python3 -m unittest discover -s tests`(28)。
2. 走一遍链路:看 `content/pipeline/demo-b001-certifications-blog/brief.md` → `draft.en.md` → `draft.de.md` → `variants/` → `publish-log.md` → 回 `content/tracker.md` 看状态。
3. 想体验"1 张卡 <3 步":`python3 tools/facts_tool.py new <class>` 按 SOP `sop/facts-record.md`。

## 三、红线边界(演示数据不是公司事实)
- 全部演示内容标 `> DEMO · 虚构(MiraSol)`;**不对外发布、不冒充任何真实公司技术/合规声明**。
- 生产红线仍有效(红线1~5):真实对外内容只引公司真实 Facts、人审后发、挂指标验收。

## 四、生产就绪清单(下一步要真实数据才解锁)
| 输入(缺) | 解锁 |
|---|---|
| O3 在售主力产品线+认证(真实) | M1.1 → M1.3 首批真实事实卡 |
| O4 素材文件与语言覆盖 | M1.1 译制量定 |
| O1 CRM/ERP 与 API | L2.1 起(线索自动化) |
| O2 渠道账号/导出能力 | L1 回流自动化 + L2 |
| O5 询盘主力渠道排名 | 发布优先级校准 |
| O6 北极星(量 vs 转化) | L3 目标口径 |

> 生产推进时:读 `docs/ROADMAP.md` 当前指针 → 以真实数据重跑已 demo 过的节点,再按依赖推进 L2~L4。

## 变更历史
- 2026-09-09 建立(demo 收口交付说明;M3.1 看板 + M4.1 回流 demo 已含)
