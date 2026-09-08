# 外部调研:C&I ESS 出海营销真实数据(A/B/C)· 置信度标注

- 日期:2026-09-08
- 性质:**外部参考 · 非公司 Facts · 禁直接入事实卡/正文**
- 生成:deep-research 工作流(103 代理、多源抓取、3 票对抗核验)后整理归档
- 关联:`简介.txt`(公司需求)、DEC-003、G1《现状与对接清单》、L1 spec(选题/SEO 参考)

> **红线提示(强制)**:本文件全部内容来自公开网络,**不是公司的权威事实**。
> 依据红线1:技术/合规表述只准引用公司事实卡(Facts),**禁止把本文件的参数/认证/数据直接写入事实卡或对外正文**。
> 本文件仅用于:① 认证**外部对照基线**(供核对公司自家认证);② 内容选题/SEO 的行业语境参考;③ 了解真实产品的参数带与市场叙事。
> 任何引用前须由人核,并与公司 Facts 交叉验证(红线3)。厂商标称(效率/循环/节能/市占)含推广成分;实际 RTE 与装机通常更低。

## 方法与统计

- 抓取来源 21 个 · 提取 claim 40 · 经 3 票对抗核验 25 · 确认 21 · 剔除 4 · 综合后 10 条
- 置信度口径:高=一手/权威多源一致;中=多源但含二手或需限定;低=二手/内部矛盾,仅作方向参考。每条条目下给出**该条自己的来源 URL 列表**(不以统一清单为限),统一清单 S1~S21 仅作跨条目检索锚。

## 总体限定(Caveats)

总体定性:本调研全部内容为「外部参考、非公司 Facts」,禁止直接写入事实卡或正文;使用前需人核并与公司 Facts 交叉验证。逐条限定:(1) 多数产品参数(B、A 部分)与市占数字源自厂商自述/营销博客(IEA-PVPS、ENA/DNO 等机构来源除外),数字(如 Sungrow 90% RTE、FORTON 60% 节能、'routine >5MWh'、欧洲大储/ C&I GWh)含标称与推广成分,实际 RTE 与装机通常更低。(2) 来源分级参差:高置信结论主要落在 UK 并网框架、IEC/UL 伞形标准、EU 电池法规与两个具名厂商规格(多为一手/权威);中低置信集中在本块 C 市场数字与部分博客级参数趋势。(3) 需按原文修正的引用错误:UL 9540 '2022 版' 实际不存在(真实为 2020 第二版含 2022 修订 / ANSI/CAN 2023 第三版);IEA-PVPS '2025 年底欧洲标准统一' 的预期期限已过,应标注为 2025 年预期而非现状;IEA-PVPS 的 IEC 只覆盖电池安全标准,不覆盖 VDE-AR-N 4105/G99/AS/NZS 4777 等并网代码。(4) 多条候选结论在 3 票对抗复核中被否、未纳入本档:如 C&I 回收期 5–12+ 年(aforenergy,1-2)、全球储能电池市场 7.83bn→52.55bn 美元(aforenergy/mate-solar,1-2)、美关税 40.9%→82.4% + 2026 美 ~59GWh(aforenergy/mate-solar,1-2)、ihuapower 314Ah 柜线 8000 次/IP54/C3-M/FK-5-1-12 参数集(0-3)——若后续要用需重取证。(5) 时敏性:多数数据以 2025 年(实绩/预测)为基准,调研日 2026-09;标准版本(EN 50549、IEC、UL 9540 版次、G100 Issue 2 后 State-2 上限存在 111%/112% 内部口径差异)与法规执行节点需在落档前再核一遍。(6) 采集环境限制:若干厂商页与 PDF 因网络策略无法直连,部分逐字核验靠搜索快照与官方文档间接完成。(7) 置信度评级:high=多一手来源/一致票,medium=二手或分裂票,low=单一或博客级来源;与复核实效近似,非对现实趋势的绝对把握。落档应保留每条结论的原始来源 URL 与上述置信标注,便于后续升级为 Facts 前重验。


## A · 目标市场并网与安全合规认证框架(外部对照基线)

### UK 并网框架 — 置信度:高

英国并网标准按容量分层且现行口径稳定:G98(前 G83)覆盖单相每相≤3.68kW/16A 的发电+储能,connect-and-notify 免网研,三相系统可做成 3×3.68kW 单相机或单台≤11.04kW 三相系统;G99(前 G59)覆盖 >3.68kW(16A)/相,两条通道——G99 Form A1-1 用于单相≤17kW/三相≤50kW,G99 Standard Application Form(SAF)用于更大系统(典型 C&I BESS >50kW 三相走 SAF);G99 'Integrated Micro-Generation'(前 Fast track)通道用于装机≤7.36kW/32A、经 G100 限电方案(ELS)出口限制在≤3.68kW/16A 的户用级 PV+储能组合。G100 还用于在 tap change 后电压仍超限时把出口压到 253V 法定值以下,但无论限电器如何,装机总量不得超过 255.3V(253V+1%)以保护电网(防限电失效)。注:2020 年来源中个别 11.04kW 措辞混乱已被标准本体与其他 DNO 文档推翻,不影响该分层结论。

**该条来源**:
  - [S6] <https://www.enwl.co.uk/globalassets/get-connected/ice/ice-event-presentations/ice-event-slides-archive/2020/dg-lv-online-event-12-november-2020.pdf>
  - · <ENA EREC G99 Issue 1 Amendment 10 (2024)>
  - · <ENA G99 Issue 2 (Mar 2025)>
  - · <National Grid G99 连接页>
  - · <SSEN G99 SAF form>
  - · <SP Energy Networks electrical_energy_storage / export_limitation 文档>
  - · <Enphase / NIE Networks / SurgePV / Selectra G98-G99 指南>

> 核验注记:四条合并均为一手/权威来源:DNO(ENWL)工程演示 PPT 逐字支撑分界点 3.68kW/16A、A1-1 阈值、SAF 与 253V/255.3V 逻辑;ENA G99 Issue1 Amend10(2024)与 G99 Issue2(2025-03)确认阈值未变、仅表格措辞更新;SP Energy Networks 现行资料确认户储快轨放宽口径(合计装机≤7.36kW、单设备≤3.68kW、经 type-approved G100 设备出口≤3.68kW/相)。分界口径 2026 年仍现行,无反向证据。

---

### 北美并网安全 — 置信度:中

北美(美/加)固定式锂电 BESS 采用伞形标准组合:UL 1973:2022(固定/辅助动力电池)与 UL 9540(ESS 系统整机)+UL 9540A 热失控火蔓延测试(模块/单元/安装层级,由 AHJ/法规引用驱动而非联邦直接强制)。因果 UL 9540/9540A 对电池集装箱/机架给出比 IEC 62619 更细的结构(9540)与火蔓延(9540A)要求,故部分北美以外买家(及保险/消防顾问)也要求符合 UL 9540/9540A。

**该条来源**:
  - [S11] <https://iea-pvps.org/wp-content/uploads/2025/10/IEA-PVPS_T18-04-2025_REPORT_Li-Ion-Systems.pdf>
  - · <UL 1973:2022 (ANSI/CAN, 3rd ed, 2022-02)>
  - · <UL 9540 (2nd ed 2020 amended 2022 / ANSI/CAN 3rd ed 2023)>
  - · <UL 9540A 测试方法>
  - · <NFPA 855 / IFC / 2024 Canadian Electrical Code 引用 UL 9540>
  - · <pvb.com / howtostoreelectricity / erneuerbareenergien.de / Kiwa>

> 核验注记:框架层多源一致(UL Solutions、Intertek、ANSI webstore、SCC/CCN 及行业指南)。两点须修正/标注:(1)来源引文写 UL 9540:2022 并不存在——真实版本为 2016/2020 第二版(2022-07 Amend1)/2023 第三版,落档应按 UL 9540(2020,2022 修订)或 ANSI/CAN/UL 9540:2023 表述;(2)'must apply'实为 AHJ/法规采用口径,9540A 安装级测试通常针对较大/多机箱项目由 AHJ 触发,非无条件。'部分北美以外买家亦要求 UL'为 IEA-PVPS 原话转述,方向性获多源支持。

---

### 欧洲及全球其余伞形标准 — 置信度:高

美/加以外(欧洲及多数国家)固定式锂电 BESS 的伞形安全标准为 IEC 62619:2022(工业用锂电芯/电池安全)与 IEC 63056:2020(电化学储能用锂电安全,ESS 专属补充),IEC 62619:2022/63056:2020 至今仍为现行版本(2025 年出现的 INTE/IEC 62619:2025 为同一第二版内容的国别采用,非新修订)。IEA-PVPS T18-04:2025 报告并预期:欧洲标准化机构正统一(harmonize)上述 IEC 标准,预计 2025 年底各欧洲国家将适用同一标准(或带少量国家补充)——该'2025 年底'预期期限已过,落档应标为报告当年(2025)的预期而非现状事实;且此处指电池安全标准(IEC 62619/63056),不含并网代码(VDE-AR-N 4105、G99、AS/NZS 4777)。

**该条来源**:
  - [S11] <https://iea-pvps.org/wp-content/uploads/2025/10/IEA-PVPS_T18-04-2025_REPORT_Li-Ion-Systems.pdf>
  - · <IEC 62619:2022 (2nd ed)>
  - · <IEC 63056:2020>
  - · <EN IEC 62619:2022 / EN IEC 63056:2020 国别采用>
  - · <2025-06 TÜV Rheinland 集装箱 BESS 认证文章>
  - · <DIN/GSO/SN 采用记录>

> 核验注记:IEA-PVPS Task 18 技术报告为政府间权威来源;引文(含 '2025 年底全欧洲同一标准、或带小补充' 一句)在下载的 61 页 PDF 第 23 页逐字核实。标准标题与适用范围(62619=工业用途;63056=ESS 专属)与引文完全一致,EU 电池法规符合性评定及多家公告机构(DEKRA/TÜV)均把两标准作为欧洲固定式 BESS 安全基础。限注:两标准为电芯/电池级安全而非 UL 9540A 式火蔓延试验,后者正被欧洲保险业越来越多要求——限定而不否定该伞形结论。

---

### EU 电池法规与 CE — 置信度:高

欧盟《电池与废电池法规(EU)2023/1542》2023-07 获批(2023-08-17 生效),制造商自 2024-08-18 起须为电池加贴 CE 标记(第 38 章/第六章符合性评定当日适用);可加贴 CE 所需的技术要求与测试主要由 IEC 62619 与 IEC 63056 承载(工业/固定储能场景),固定式 BESS 依据第 12 条基础还并列列出 UN 38.3/UL 1973/UL 9540A 等标准(原文 'mainly' 措辞,未越界)。家用便携电池走 EN 62133-2,不否定本结论对 C&I/工业电池的适用。

**该条来源**:
  - [S11] <https://iea-pvps.org/wp-content/uploads/2025/10/IEA-PVPS_T18-04-2025_REPORT_Li-Ion-Systems.pdf>
  - · <Regulation (EU) 2023/1542>
  - · <adherent.com/blog/ask-our-experts-top-frequently-asked-questions-on-batteries-regulation-eu-20231542/>
  - · <reuschlaw.de/en/news/battery-regulation-commencement-of-further-obligations/>
  - · <prodlaw.eu/2024/08/eu-batteries-regulation-new-requirements-for-a-greener-market/>
  - · <DEKRA / TÜV 指南>

> 核验注记:三个要件独立核实:法规 2023-07 通过、CE 义务 2024-08-18 起适用、实施标准为 EN IEC 62619:2022/EN IEC 63056:2020(多家公告机构与法律快讯一致)。来源为 IEA-PVPS 制度性研究,2026 年现行有效。第 12 条另列 UN 38.3/UL 1973/9540A 系原出处即有的限定措辞,已保留。

---


## B · 真实厂商 C&I BESS 产品线与技术参数带(外部参考)

### Sungrow PowerStack 200CS 参数组 — 置信度:高

Sungrow(阳光电源)澳洲市场 C&I 一体化柜 PowerStack 200CS 型号 ST455kWh-110kW-4H(ST455CS-4H):额定交流输出 110kW、电池容量 458kWh、额定交流电压 400V,即约 4 小时放电(0.25C)的 ~100kW/400–500kWh 参数点(2024-06 发布,2025 澳洲 SA CSIP-AUS 社区储能部署仍在用,现行有效)。全系统 RTE 标称 90%,高效 PCS 最高效率 98.5%;液冷热管理,电芯温差≤2.5℃,官方称 'AI bionic thermal balance' 使全天系统热损失降 33%(注:该 33% 官方文案亦有一处表述为辅助功耗降 33%≈12kWh/天,营销措辞不一致,按产品页措辞引用);三级电气安全 PACK/RACK/PCS 过流保护 + 三级消防设计与 AI 电芯健康监控/热失控早期预警,支持文档另列 NFPA 68/69、UL 9540A、烟温气检测/通风/泄爆/水喷淋。

**该条来源**:
  - [S13] <https://www.sungrowpower.com/au/en/products/c-i-energy-storage-system/b-st455kwh-110kw-4h>
  - · <Sungrow 官方 EN_FS_PowerStack200CS_Factsheet_V1.0 (2025-03-11)>
  - · <ManualsLib PowerStack 200CS ST455CS-4H>
  - · <pv-magazine Australia (2025-09-05) ST455CS-4H 部署报道>
  - · <estg.eu / solarxin / tiansolar / vpsolar / woba-solar 分销数据表>
  - · <Sungrow support 三级消防设计文档 (NFPA 68/69, UL 9540A)>

> 核验注记:五条全票确认合并,数据与多区域官方页及独立分销数据表一致(系统 RTE 90%、PCS 98.5%、液冷、ST455kWh-110kW-4H)。作为厂商一手规格引用是恰当的(规格类主张非营销主张),但 90% RTE/33%/AI 仿生温控为厂商标称,实际运行 RTE 通常更低——本发现仅作厂商参数带数据点,不作事实卡。

---

### TESVOLT FORTON 参数组 — 置信度:高

TESVOLT FORTON 为可扩展 C&I 户外 BESS 柜线:储能 92–1,475kWh(可并联)、功率 90–1,500kW(基准单元 92kWh/1C/100% DoD)、充电/放电循环≤15,000 次、配最长 15 年质保(以约 11,000 次满循环为前提,2025-03 发布,现行);热设计为高温电芯 + 非液冷 'HYPEROX+' 方案(加热器加热 + 换热器冷却),官方称比液冷系统能耗低最多 60%,户外环境 -20~+55℃,最大噪音约 60 dB(A)(数据表为不含逆变器口径);消防/安全为三级防护概念(报警 + 气溶胶灭火 + 烟/热/燃气传感器)+ 集成网络安全(OTA 更新、直连服务);交流耦合、低压 400V 并网,符合 VDE-AR-N 4105,另配 TEC Pro S 控制器 + 兼容 Master EZA 电站控制器方可满足 VDE-AR-N 4110 并网(4110 属电站级证书,带条件性,未过度声明)。

**该条来源**:
  - [S15] <https://www.tesvolt.com/en/products/forton.html>
  - · <TESVOLT 官方数据表 (RD.TI.144.E.en-UK / TESVOLT_Forton_DE)>
  - · <TESVOLT 手册 RD.TI.160 / RD.TI.143(气溶胶灭火、烟温气传感器、两级报警联动 BMS/EMS)>
  - · <pv-magazine (2025-03-26) 15 年质保报道>
  - · <energidea FORTON/12-30 数据表页>
  - · <Photon / Solarserver (2025-03-25) / pv Europe / photovoltaik.eu 报道>

> 核验注记:四条全票确认合并。容量/功率/循环次数与官方数据表逐字一致(1.475 为德式千分位,即 1,475);15 年质保不在引用片段内但被 2025-03 贸易媒体独立证实。厂商直接页被网络策略拦截,靠官方 PDF 与多渠道搜索交叉核实。安全/寿命语言为厂商集成设计表述,不主张独立验证过的火险性能。

---

### 集装箱化参数趋势 — 置信度:中

20ft 集装箱储能能量密度由数年前的 2.5–3MWh/柜升至当前主流 >5MWh、旗舰设计向 6–7MWh 逼近;电芯容量由 280Ah 演进至 314Ah/588Ah/661Ah,液冷成为标配。具名示例:Sungrow PowerTitan 3.0(20ft 6.9MWh、661Ah 叠片 LFP、4h 93.6% RTE,2025-09 发布)、Tesla Megapack 3(约 5MWh)。

**该条来源**:
  - [S17] <https://www.mate-solar.com/2026-global-ci-and-containerized-energy-storage-a-scalable-policy-driven-market-enters-hyper-growth/>
  - · <pv-magazine-usa.com / solarpowerworldonline.com / powermag.com (PowerTitan 3.0)>
  - · <reneweconomy.com.au (Megapack 3)>
  - · <howtostoreelectricity.com / exliporcpower.com (电芯密度演进)>
  - · <KTH diva 论文>

> 核验注记:载荷事实经主流行业媒体独立核实(PowerTitan 3.0 6.9MWh/661Ah/93.6%;Megapack 3 ~5MWh;280→314Ah 使 20ft 密度由 ~3.7MWh 上探 5MWh+,2026 年 20ft 主流 5–6.25MWh)。三条限定不推翻但压低置信:(1)源头 mate-solar.com 为促销博客;(2)主流非旗舰 20ft 系统仍在 ~3.7–5MWh,'routinely >5MWh' 带推广色彩;(3)Megapack 3 用 ~28ft 机箱,5MWh 仅是松散的'每 20ft'口径。

---


## C · 市场数据与买家内容偏好(选题/SEO 外部参考)

### 欧洲大储与德国政策语境 — 置信度:中

欧洲大型公用事业储能(被本文献当作驱动 C&I 时代电网市场的主力)装机据称由 2024 年 8.8GWh 升至 2025 年 >16GWh(核数落在 SolarPower Europe 区间:2024 欧洲大储 +79% 约 8.8GWh、2025 预测约 16.2GWh +84%);德国 215GW-by-2030 光伏目标(EEG 2023/复活节一揽子)与 Solar Package I(2024-02 生效,放开商用光伏/储能)为 C&I 表后储能需求托底。2025 实绩(SPE:欧盟破纪录 27.1GWh,大储占新增 55%,英国 +5GWh)确认大储爆发方向。

**该条来源**:
  - [S17] <https://www.mate-solar.com/2026-global-ci-and-containerized-energy-storage-a-scalable-policy-driven-market-enters-hyper-growth/>
  - · <SolarPower Europe, European Market Outlook for Battery Storage 2025-2029>
  - · <SolarPower Europe EU Battery Storage Market Review 2025>

> 核验注记:核心数字由行业权威 SolarPower Europe 独立支撑(建议落档以 SPE 报告为主锚、博客为辅);德国 215GW/SPI 政策为真实现行事实。扣分点:mate-solar.com 系厂商营销博客且无法直连核验页内原文,主张本身已带 '据称/当作' 限定。作中置信外部参考。

---

### 欧洲 C&I 细分市场数字 — 置信度:低

某厂商白皮书博客称:欧洲 C&I 储能市场 2024–2029 CAGR 55%,2025 年欧洲 C&I 新增装机 3.6GWh(+62% YoY)。同文 'Table 2' 却给出 2025 欧洲 C&I 预测 6.5GWh,来源内部矛盾;而 SolarPower Europe 2026-01 实绩口径 EU C&I 2025 实际仅约 2.3GWh——3.6GWh 更接近'欧洲(EU+UK 等)范围'的偏乐观预测,且 2025 于本调研时点已成历史。55% CAGR 有分析师支持,方向性成立(欧洲 C&I 高增),但具体数字只宜作低置信外部预测引用。

**该条来源**:
  - [S18] <https://www.mate-solar.com/2025-commercial-and-industrial-energy-storage-investment-whitepaper-market-trends-technological-innovations-and-future-outlook/>
  - · <SolarPower Europe, European Market Outlook for Battery Storage 2025-2029 (2025-05)>
  - · <SolarPower Europe EU Battery Storage Market Review (2026-01)>
  - · <SPIR Research / Dongwu Securities / SPIR 报告>

> 核验注记:文字转述准确且自我标注内部矛盾(6.5 与 3.6GWh 并存);两端口均有外部支持(SPE ~3.5GWh 装机预测 / Dongwu ~6.17GWh、SPIR 6+GWh 出货),系装机-出货、EU-欧洲口径差。多重扣分:即期来源为厂商营销博客、同文矛盾、2026-01 实绩(约 2.3GWh)低于预测——故整条降为低置信方向性参考,不作精确指标引用。

---

### C&I BESS 买家决策链与售前技术问题 — 置信度:中

C&I BESS 采购/询价呈明确链条:先定义 use case → 将功率 kW(PCS)与容量 kWh(电芯/模块)作为两个独立决策分别量化 → 定硬件 → 再查认证(证书须精确到型号/列名编号,不接受笼统 certified)→ 电网并网要求 → 区分设备质保(warranty)与性能担保(performance guarantee)→ TCO → 按流程尽调厂商;招标/RFP 必须要求:在指定 DoD 下的可用 kWh(而非铭牌)、电芯厂商/等级披露(电芯溯源)、指定 SOH 终点下的循环寿命(如 6000–8000 次 @80% DoD 至 80% SOH)、按文件/列表编号出示的证书(IEC 62619、UN 38.3、UL 1973/9540、EN 50549/VDE-AR-N 4105)。这套链条直接映射出可反哺 L1 选题/SEO 的 B 端售前问题清单。

**该条来源**:
  - [S19] <https://www.ihuapower.com/blog/commercial-industrial-energy-storage/ci-bess-procurement-guide/>
  - · <hitekenergy.com C&I BESS RFQ Checklist>
  - · <pcenersys.com BESS Procurement Guide>
  - · <orytasolar.com International Buyers Checklist>
  - · <pvb.com 2026 C&I buyer guide / aforenergy.com / jhynewenergy.com>

> 核验注记:核心链条由引文直证,每个具体要素经多家非促销采购/RFQ 指南独立交叉证实(可用 vs 铭牌 kWh 及 DoD/SoC 窗口;循环寿命须带测试条件/DoD/EOL-SOH;电芯溯源;证书按型号列名编号;质保 vs 性能担保)。扣分:即期来源页无法直连,8 步措辞全貌未逐字核验,且'采购阶段映射为售前问题'含轻微编辑推断——均不损实质。

---

## 开放问题(未取证/待补,供后续调研)

- A:澳洲并网与合规的具体执行——AS/NZS 4777.2(2020)适用范围、逆变器/储能注册(CEC)、以及南澳 CSIP-AUS(如 PowerStack ST455CS-4H 已在做 CSIP-AUS 测试)等新兴要求的现行版本与认证路径,本次未获可票确认的一手结论。

- A:证书'有效期口径'与认证机构分工未被覆盖——VDE-AR-N 4105(≤135kW 分界与 4110 上位关系)在 2026 的更新状态、TÜV Rheinland/Süd/DEKRA 等机构的 C&I BESS 认证范围与周期、以及 UN 38.3/运输(ADR/IATA/IMDG 现行版本)要求均需另补取证。

- B:除 Sungrow 与 TESVOLT 外,比亚迪储能、宁德时代、华为、Fluence、Wärtsilä、Sonnen 等代表厂商在目标市场的具名 C&I 产品参数(尤其面向德/英/澳市场的柜级产品与认证)尚未系统取证,现仅有两条标杆数据点。

- C:买家'内容偏好/SEO 需求'维度只由采购决策链反推,缺一手数据——哪些内容类型(白皮书/对比页/认证解读/回收期计算器)与关键词在德/英/澳 C&I BESS 买家中表现最好,本次未获实证,需另做关键词与内容基准调研。


## 已剔除项(核验不通过/来源不可靠,勿采用)

- ~~The article projects the global solar energy storage battery market to grow from USD 7.83 billion in 2026 to over USD 52.55 billion by 2035, a CAGR exceeding 23.3% — an indicative (vendor-cited, non-primary) market-size figure for block C.~~

- ~~The article claims Chinese battery exporters to the US face a potential tariff increase from 40.9% to 82.4% in 2026 and must meet UL 9540 / UL 9540A certification requirements, with US storage additions estimated at ~59 GWh in 2026 despite FEOC component restrictions (relevant to block A certification + US market context).~~

- ~~Typical C&I BESS spec band: credible LFP cells are rated at least 6,000–8,000 cycles at 80% state of health; the vendor's own 3.2V/314Ah LiFePO4-based C&I cabinet line claims >=8,000 cycles @80% SOH, IP54 enclosures, C3-M corrosion protection, and aerosol/FK-5-1-12 fire suppression with IEC 62619 and UN 38.3 compliance — an example of a real China-based C&I vendor's publicly stated parameter set.~~

- ~~In developed markets the C&I (commercial/industrial) battery storage payback period typically lands around 5-12+ years, with shorter paybacks where demand charges, time-of-use spreads, incentives, export restrictions or resilience value are strong - supporting the buyer-economics framing (arbitrage/demand management/self-consumption/backup) in research block C.~~


## 附录 A1 · L1 选题候选表(C 条映射,外部参考)

> 用途:把本档 C 条(市场语境 C1/C2 + 买家决策链与售前问题 C3)映射成 **L1 选题种子**,供 L1 M2.1(选题卡模型 + SEO 关键词表)与首个端到端切片(L1-MVP)选用。
> **红线**:选题 ≠ 可写。任何成稿前须公司 Facts(O3/O4)入卡并由人审;本表关键词/角度**不做公司事实**。市场数字行(C1/C2)仅作方向与语境,发布引用前由公司市场部核验或省略;低置信(C2)行不做结论引用。

| # | 选题方向(EN 可用标题) | 买家/人设 | 意图·漏斗 | 渠道 | 关键词种子(EN / DE) | 依赖 Facts | 研究源 | 优 |
|---|---|---|---|---|---|---|---|---|
| T1 | kW vs kWh:工商业储能的功率与容量是两个独立决策(sizing 指南) | 业主 / EPC / 集成商 | 评估·中段 | 博客 + LinkedIn + 短视频脚本 | "C&I battery storage sizing" / "kW vs kWh BESS" · "Gewerbespeicher Dimensionierung" | 产品参数 + 项目案例 | C3 | P1 |
| T2 | 峰谷套利 / 需量管理 / 自用 / 备用:先定 use case 再谈产品 | 业主 / 工厂决策(CFO) | 认知→评估 | 博客 | "demand charge reduction battery" / "C&I BESS arbitrage" | 产品参数 + 报价政策(如有) | C3 | P1 |
| T3 | 招标 RFP 怎么读:可用 kWh@DoD、循环寿命@80% SOH、电芯溯源 | 采购 / 集成商 | 决策·末端 | 博客 + LinkedIn(专业向) | "BESS RFP requirements" / "warranty vs performance guarantee" | 产品参数 + 公司资质 | C3 | P2 |
| T4 | 一台 C&I BESS 出厂要带哪些证书;为何"certified"必须精确到型号 | 集成商 / 业主 | 评估 | 博客 + 阿里详情页 FAQ | "IEC 62619 BESS" / "UN38.3" · "CE Batterieverordnung" | 认证清单 | A + C3 | P1 |
| T5 | 并网路径科普:德国 VDE-AR-N 4105/4110 与英国 G99 怎么对 | 集成商 / EPC | 认知→评估 | 博客(EN/DE) | "VDE-AR-N 4105 Gewerbespeicher" / "G99 application BESS" | 认证清单 | A | P2 |
| T6 | 欧洲 C&I 储能为何加速:政策脉络(德国 215GW / Solar Package I、大储翻倍) | 公司决策层 / 集成商 | 认知·顶端 | LinkedIn 观点 + 短视频脚本 | "Europe C&I battery growth" · "Gewerbeenergiespeicher Markt" | 公司资质 + 项目案例 | C1 | P2 |
| T7 | 欧盟电池法规与 CE:2024-08 起对储能厂家的意义(gate 解读) | 集成商 / 合规 | 认知 | LinkedIn + 博客 | "EU Battery Regulation CE battery" · "Batterieverordnung CE 2024" | 认证清单 | A + C1 | P2 |
| T8 | 欧洲工商业储能上量的信号(方向性解读,不引具体数字) | 集成商 / 业主 | 认知 | LinkedIn + 短视频脚本 | "C&I ESS trend 2026" · "Trends Gewerbespeicher 2026" | 公司资质 + 案例 | C2(低,仅方向) | P3 |

注:表内 A 行(A 块认证)作深度扩展源;T8 因 C2 低置信,定位为语境/视频种子,禁止引具体 GWh/CAGR 结论。选题卡正式模板见 L1 spec §5 C2,本表仅给第一批候选与关键词方向。

## 统一来源清单(S1~S21,跨条目检索锚)

- [S1] <https://www.vde.com/de/fnn/themen/tar/tar-niederspannung/erzeugungsanlagen-am-niederspannungsnetz-vde-ar-n-4105-2018>

- [S2] <https://www.vde.com/en/press/press-releases/fnn-technical-connection-rules-low-voltage-niederspannungsnetze>

- [S3] <https://cleanenergycouncil.org.au/industry-programs/products-program/inverters/standards-change>

- [S4] <https://www.energynetworks.com.au/projects/national-grid-connection-guidelines/power-quality-response-mode-settings/>

- [S5] <https://www.energynetworks.org/industry/engineering-and-technical-programmes/energy-storage>

- [S6] <https://www.enwl.co.uk/globalassets/get-connected/ice/ice-event-presentations/ice-event-slides-archive/2020/dg-lv-online-event-12-november-2020.pdf>

- [S7] <https://www.ul.com/insights/industry-insights-eu-battery-regulation-20231542>

- [S8] <https://cms.law/en/ita/legal-updates/eu-sustainable-batteries-regulation-where-are-we-now>

- [S9] <https://www.tuvsud.com/en-ae/industries/mobility-and-automotive/automotive-and-oem/automotive-testing-solutions/battery-testing/testing-of-stationary-energy-storage-systems>

- [S10] <https://www.tuvsud.com/en-us/resource-centre/blogs/mobility-and-automotive/understanding-the-new-eu-battery-regulation>

- [S11] <https://iea-pvps.org/wp-content/uploads/2025/10/IEA-PVPS_T18-04-2025_REPORT_Li-Ion-Systems.pdf>

- [S12] <https://www.gefahrgut-online.de/themen/un-38-3-pruefzusammenfassung-die-pruefzusammenfassung-3614198.html>

- [S13] <https://www.sungrowpower.com/au/en/products/c-i-energy-storage-system/b-st455kwh-110kw-4h>

- [S14] <https://solar.huawei.cn/ke/professionals/all-products/LUNA2000-215-Series>

- [S15] <https://www.tesvolt.com/en/products/forton.html>

- [S16] <https://ebs.publicnow.com/view/34CCD4A6B34DD789F757E2F02D94A9F9118C27BA>

- [S17] <https://www.mate-solar.com/2026-global-ci-and-containerized-energy-storage-a-scalable-policy-driven-market-enters-hyper-growth/>

- [S18] <https://www.mate-solar.com/2025-commercial-and-industrial-energy-storage-investment-whitepaper-market-trends-technological-innovations-and-future-outlook/>

- [S19] <https://www.ihuapower.com/blog/commercial-industrial-energy-storage/ci-bess-procurement-guide/>

- [S20] <https://www.aforenergy.com/commercial-energy-storage-system-guide-for-epcs-installers-and-commercial-pv-decision-makers/>

- [S21] <https://www.aforenergy.com/battery-storage-payback-period-for-ci-pv-complete-guide-for-epcs-and-commercial-project-decision-makers/>


## 变更历史

- 2026-09-08 建立(deep-research 产出归档,A/B/C 三块)
- 2026-09-08 附录 A1:L1 选题候选表(C 条映射 8 项,外部参考,喂 M2.1)