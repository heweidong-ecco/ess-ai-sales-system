# 工商业储能海外业务 · AI 系统

需求驱动产品开发 + superpowers 工作流。**重启入口:读 `CLAUDE.md`** → 读 `docs/ROADMAP.md` 接续。

## 文档入口

| 文件 | 说明 |
|---|---|
| `CLAUDE.md` | **启动锚点/接续规约**(新会话先读这个) |
| `简介.txt` | 公司原始需求(招聘文档,事实源) |
| `系统总纲.md` | 总纲:业务边界、飞轮、闭环 L1~L5、路线图 P0~P3 |
| `docs/ROADMAP.md` | **主执行图**:全系统模块/步骤/MVP 节点 + 实时状态 |
| `docs/superpowers/specs/` | 各闭环 spec(每闭环一个) |
| `docs/superpowers/plans/` | 各闭环实现计划 |
| `docs/decisions/` | 决策记录 |

## 现状(实时状态以 ROADMAP 为准)

- [x] 安装 superpowers 插件(project 作用域)
- [x] git 初始化 + 脚手架 + 分支统一到 main
- [x] 系统总纲 v0.1 评审通过
- [x] 主执行图摊平(模块/步骤/MVP 节点)定稿
- [x] 决策记录 DEC-001(L1 默认值)
- [ ] 首个节点开工(见 `docs/ROADMAP.md` 当前指针)

## 重启流程(3 步)

1. `cd` 进本目录,启动 Claude Code(superpowers 自动加载)
2. 读完 `CLAUDE.md` → 看 `docs/ROADMAP.md` 的 in_progress / 下一个 ⬜ 节点
3. 读该节点 spec/plan → 按流程入口(`br→spec→plan→build`)继续
