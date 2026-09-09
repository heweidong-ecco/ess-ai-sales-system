# 渠道模板(channel-templates)

- 适用:M2.2 起。把一张已批准的选题卡(brief,`content/pipeline/<slug>/brief.md`)产出为某渠道草稿。
- 四类:`blog`(SEO 博客)/ `linkedin`(专业短帖)/ `ali-detail`(阿里国际站多语言详情页文案)/ `video-script`(短视频脚本)。
- 使用方式:内容执行者(AI)读对应模板 + 该 brief → 按模板结构填,技术/合规表述**只引用 approved 事实卡**(`[F-…]`),产出放 `content/pipeline/<slug>/`(草稿/变体/发布记录)。
- 红线(所有模板强制):只引用 `content/facts/` 中 `status: approved` 的卡;`draft/obsolete` 卡不引用;对外发布前必经人审(红线1/3)。演示产物在文首标 `DEMO`。
- 语言:EN 主稿;DE 译制按 M2.3(术语表+人工终校)。

| 模板 | 文件 | 典型长度 |
|---|---|---|
| SEO 博客 | `blog.md` | EN 1,200~1,800 词 |
| LinkedIn 专业帖 | `linkedin.md` | 150~250 词(可带长文链接) |
| 阿里详情页文案 | `ali-detail.md` | 分节,含参数表/FAQ |
| 短视频脚本 | `video-script.md` | 60~90 秒口播+画面 |
