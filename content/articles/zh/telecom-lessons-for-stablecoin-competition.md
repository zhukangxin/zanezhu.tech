---
title: "从程控交换到稳定币：电信竞争史对稳定币格局的启示与预测"
date: 2026-11-20
description: "2026年的稳定币行业，相当于1984–1991年的电信业。本文对照程控交换、移动制式和AT&T拆分的历程，分析稳定币竞争的异同，给出五条预测，并逐条列出先决条件、判断依据和证伪信号。"
tags: ["稳定币", "电信", "竞争格局", "GENIUS法案", "MiCA", "支付基础设施"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_zh_telecom-stablecoin-competition.png"
draft: false
---

> 相关文章：[支付可以向电信业学什么](/zh/articles/payments-learn-from-telecom/) · [跨境支付不需要区块链](/zh/articles/cross-border-payments-dont-need-blockchain/)
>
> 数据截至 2026 年 11 月。本文不构成投资建议。

## 摘要

**核心结论**：2026 年的稳定币行业，相当于 1984–1991 年的电信业：监管框架刚落地，方案林立，技术路线未收敛。电信业用了约 20 年，从“七国八制”走到“5 家设备商 + 1 个全球标准”。按此历程推演，稳定币会经历三步：**发行方洗牌 → 互联互通导致产品同质化 → 利润流向分发和应用层**。但两者的经济结构有六处根本差异，类比只能用于推演方向，不能套用细节。

**五条预测一览**（详见第六节，每条均列出先决条件和证伪信号）：

| # | 预测 | 电信对照 | 时间窗口 | 置信度 |
| --- | --- | --- | --- | --- |
| 1 | 发行层收敛为 2–3 家全球美元发行方 + 各货币区 1–2 家本地冠军 | 交换机厂商从十余家收敛到 5 家 | 2027–2032 | 中高 |
| 2 | 离岸 USDT 像“小灵通”：长期存在，但在受监管通道中份额持续下降 | 小灵通在 3G 牌照发放后退出 | 2027–2030 | 中 |
| 3 | 稳定币专用链“制式战”收敛，或被互操作/“漫游”层抽象掉 | GSM/CDMA 之争 → LTE 统一 | 2028–2032 | 中 |
| 4 | 受监管稳定币之间实现平价互通后，发行方变“管道”，价值流向分发和应用层 | AT&T 拆分后长途竞争；价值从设备商迁往运营商和应用 | 2029 年以后 | 中低（依赖监管） |
| 5 | 非美元货币区扶持本地发行方，形成“货币区冠军” | 中国“以市场换技术” → 巨大中华 | 2026–2030 | 中高 |

## 一、研究框架：两个行业的分层对应

本文把两个行业都拆成五层逐层对照：哪一层先竞争、哪一层先收敛、利润最后停在哪一层。

| 层级 | 电信（1980–2010） | 稳定币（2014–今） | 对应逻辑 |
| --- | --- | --- | --- |
| 核心产品/设备 | 程控交换机厂商：爱立信、阿尔卡特、北电、NEC、西门子、AT&T/朗讯 | 发行方：Tether、Circle、银行联盟、PayPal、汇丰 | 提供被使用的“东西” |
| 技术标准 | 移动制式：GSM、CDMA、TDMA → 3G → LTE | 公链/结算层：Ethereum、Tron、Solana、Tempo、Arc | 决定兼容性与规模效应 |
| 互联与清算 | 运营商互联、GSM 漫游结算 | 跨链协议、卡组织稳定币结算（Visa） | 让不同网络的用户互通 |
| 分发渠道 | 运营商（AT&T、区域 Bell、中国邮电） | 交易所、钱包、收单方（Coinbase、Stripe） | 接触最终用户 |
| 监管与主权 | AT&T 拆分、欧洲强制 GSM、中国产业政策 | GENIUS 法案、MiCA、香港《稳定币条例》 | 重塑市场结构 |

对应的前提是：两者都是**具有网络效应的基础设施**，都在从封闭、分散走向标准化，都被主权国家视为战略产业。类比失效的地方在第五节单独讨论。

## 二、电信竞争史回顾（1982–2016）

电信业的竞争按“碎片化 → 监管重塑 → 标准收敛 → 厂商整合 → 价值迁移”的顺序展开，前后约 30 年。

### 2.1 关键事件

| 时间 | 事件 | 意义 | 来源 |
| --- | --- | --- | --- |
| 1982 | 中国第一部万门程控交换机在福州启用（日本 F-150） | 中国程控化起点 | [新民周刊](https://img1.xinmin.cn/xmzk/2020-01-06/830106.pdf) |
| 1980 年代 | 各省自行引进，形成“七国八制”：NEC、富士通、朗讯、北电、爱立信、西门子、BTM、阿尔卡特 | 碎片化，但建设速度快 | [IT之家](https://www.ithome.com/0/533/645.htm) |
| 1984-01-01 | AT&T 拆分为长途公司 + 7 家区域 Bell 公司，长途市场对 MCI、Sprint 开放 | 监管把垄断环节与竞争环节分开 | [Wikipedia](https://en.wikipedia.org/wiki/Breakup_of_the_Bell_System)、[EBSCO](https://www.ebsco.com/research-starters/history/att-undergoes-divestiture) |
| 1986–1991 | 邮电部一所、十所先后研制 DS-2000、HJD-1024、DS-30 等国产程控机 | 国产替代起步 | [IT之家](https://www.ithome.com/0/616/767.htm) |
| 1980 年代末 | 中国模拟移动网分 A 网（摩托罗拉）、B 网（爱立信），两网差异极大 | 移动“制式之争”的雏形 | [虎嗅](https://www.huxiu.com/article/2794258.html) |
| 1990 年代初 | 巨龙 HJD04、华为 C&C08 等自主万门机出现 | “巨大中华”崛起 | [IT之家](https://www.ithome.com/0/522/054.htm) |
| 1990 年代中期 | 全球交换机淘汰赛基本结束，爱立信、阿尔卡特、西门子、北电、AT&T 胜出；中国计划合并八家国有厂组建巨龙 | 研发固定成本推动集中 | [Tech Monitor](https://www.techmonitor.ai/?p=160397) |
| 1990 年代 | 欧洲强制 GSM；美国不指定标准，三种技术并存 | 强制标准 vs 市场选择 | [Curwen 2004](https://emeraldinsight.com/insight/content/doi/10.1108/info.2004.27206aab.001/full/html)、[eWeek](https://www.eweek.com/mobile/winner-take-all/) |
| 1996 | AT&T 分拆出朗讯（设备业务） | 运营与设备分离 | [Wikipedia](https://en.wikipedia.org/wiki/Alcatel-Lucent) |
| 2007 | GSM 占 2G 市场约 80–85%，CDMA（IS-95）约 10–15% | 强制标准赢得规模 | [Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_mobile_phone_standards) |
| 2009 | 北电在加美申请破产保护，资产被爱立信、诺西等分拍 | 旧巨头出局 | [Wikipedia](https://en.wikipedia.org/wiki/Nortel)、[telecoms.com](https://www.telecoms.com/digital-ecosystem/end-of-an-era) |
| 2010 前后 | CDMA 阵营运营商转向 LTE，4G 基本统一 | 标准收敛 | 行业通史 |
| 2016 | 诺基亚收购阿尔卡特-朗讯（2006 年由两者合并而成） | 整合完成 | [Wikipedia](https://en.wikipedia.org/wiki/Alcatel-Lucent) |

### 2.2 三条规律

1. **固定成本决定厂商数量。** 只有拿到足够全球份额的厂商，才能负担下一代产品的研发（[Tech Monitor](https://www.techmonitor.ai/?p=160397)）。任正非当年也指出，中国交换机厂家太多、各自为政，整体水平难以提高（[IT之家](https://www.ithome.com/0/522/054.htm)）。
2. **标准之争由规模和监管共同决定，而非单纯技术优劣。** 美国不强制标准，设备商只能把研发预算拆给三种技术，进展变慢（[eWeek](https://www.eweek.com/pt/mobile/winner-take-all/)）。输掉制式的一方未必输掉利润：高通同时从 CDMA 和 GSM 3G 标准收取专利费（[eWeek](https://www.eweek.com/fr/mobile/winner-take-all/)）。
3. **监管强制互联后，价值向用户侧迁移。** AT&T 拆分后，长途市场引入竞争，消费者选择变多、价格下降，但本地服务因交叉补贴取消而涨价（[EBSCO](https://www.ebsco.com/research-starters/history/att-undergoes-divestiture)）。此后价值又从设备商转向运营商，再转向应用层（行业通史）。

## 三、稳定币竞争现状（2026 年 11 月）

稳定币市场约 2870 亿美元，双寡头占约 85%；美、欧、港三套监管已经把市场切成不同的合规区。

### 3.1 市场结构

- 截至 2026 年 11 月 12 日，稳定币总市值 2868.85 亿美元，其中 USDT 1756.6 亿、USDC 698.81 亿、USDS 53.57 亿（[DefiLlama](https://defillama.com/stablecoins)）。
- USDT 与 USDC 合计占约 85%（[Crypto Briefing](https://cryptobriefing.com/tether-circle-stablecoin-dominance/)）。
- 增速差异：2025 年 USDC 市值增长约 73%，USDT 约 36%（[DEXTools](https://www.dextools.io/news/stablecoin-market-tops-320-billion-usdc-usdt-june-2026)）。按链上转账量，2025 年 USDC 约 18.3 万亿美元，高于 USDT 的约 13.3 万亿（[CoinPaprika](https://coinpaprika.com/cs/education/stablecoin-wars)）。即：USDT 赢存量，USDC 赢流量。

### 3.2 监管：三套体系

| 辖区 | 框架 | 关键状态 | 对竞争的影响 | 来源 |
| --- | --- | --- | --- | --- |
| 美国 | GENIUS 法案（2025 年 7 月签署） | 2027 年 1 月 18 日生效；监管机构错过 2026 年 7 月的一年期限；OCC 于 2026 年 10 月率先发布最终规则 | 只管发行资质，不指定技术路线；禁止发行方向持有人付息 | [The Block](https://www.theblock.co/post/408843/us-regulators-miss-genius-acts-one-year-deadline-for-final-stablecoin-rules)、[The Block · OCC](https://theblock.co/news/regulation/2026-10-21-occ-final-rule-implementing-trump-signed-genius-act-421470)、[Latham & Watkins](https://www.lw.com/en/insights/2025/07/the-genius-act-of-2025-stablecoin-legislation-adopted-in-the-us) |
| 欧盟 | MiCA | 2026 年 7 月 1 日过渡期结束；Tether 未申请授权，USDT 退出受监管交易所 | 强制合规的“GSM 模式”；USDC、EURC 成为主流 | [The Paypers](https://thepaypers.com/crypto-web3-and-cbdc/news/tether-exits-eu-market-as-mica-rules-block-usdt-from-exchanges)、[Cryptopolitan](https://cryptopolitan.com/mica-pushes-usdt-out-leaves-usdc-in) |
| 香港 | 《稳定币条例》（2025 年 8 月生效） | 2026 年 4 月 10 日首发牌照给汇丰和 Anchorpoint（渣打 + 香港电讯 + Animoca） | 极少数、银行优先的“牌照制” | [HKMA](https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/04/20260410-4/)、[Caixin Global](https://www.caixinglobal.com/2026-04-10/hong-kong-grants-first-stablecoin-licenses-to-hsbc-standard-charteredbacked-venture-102432744.html) |

美国草案已经显示门槛方向：新联邦发行方最低资本 500 万美元、当日流动性缓冲、两个工作日内赎回；FinCEN 估计初期约 50 家发行方受约束（[Finance Magnates](https://www.financemagnates.com/cryptocurrency/regulation/ten-days-to-the-genius-act-deadline-what-the-draft-rules-already-reveal/)）。香港初批 2 张牌照来自 36 家申请者（[Caixin Global](https://www.caixinglobal.com/2026-04-10/hong-kong-grants-first-stablecoin-licenses-to-hsbc-standard-charteredbacked-venture-102432744.html)）。

### 3.3 主要玩家的战略动作

| 玩家 | 动作 | 战略含义 | 来源 |
| --- | --- | --- | --- |
| Tether | 2026 年 1 月推出美国合规的 USAT，由 Anchorage Digital 发行；欧盟则选择退出 | “离岸 + 合规”双轨 | [Yahoo Finance](https://finance.yahoo.com/news/tether-launches-us-regulated-usat-161314419.html) |
| Circle | 持有 MiCA 授权；自建 Arc 链（测试网 2025 年 10 月上线）；与 Coinbase 的分成协议续签至 2029 年 | 抢合规位置，向结算层延伸 | [Everstake](https://everstake.one/resources/blog/tempo-vs-arc-stablechains-the-next-generation-of-finance)、[KuCoin](https://www.kucoin.com/blog/in-circle-renews-usdc-revenue-sharing-agreement-with-coinbase-through-2029) |
| 21 家银行联盟 | 美银、花旗、高盛、德银、瑞银、三菱日联等计划 2027 年上半年发行美元稳定币，之后拓展到欧元等 G7 货币 | 在位者联合入场 | [CoinMarketCap](https://coinmarketcap.com/academy/article/21-banks-stablecoin-venture-usd-token-launch-2027) |
| Qivalis（欧洲） | 含 BBVA 在内的 37 家机构联盟，计划发行欧元稳定币 | 货币区冠军 | [Financial News](https://en.fnnews.com/news/202609020839433776) |
| 摩根大通 | 未加入联盟，据报道在评估自建 | 大型玩家保留自有“制式” | [Banking Dive](https://www.bankingdive.com/news/bofa-wells-fargo-citi-back-upcoming-stablecoin/829318/) |
| Stripe + Paradigm | Tempo 主网 2026 年 3 月 18 日上线，手续费用稳定币支付，强调“稳定币中立” | 分发方向下整合结算层 | [Everstake](https://everstake.one/resources/blog/tempo-vs-arc-stablechains-the-next-generation-of-finance)、[CryptoSlate](https://cryptoslate.com/stripe-and-paradigm-reveal-tempo-layer-1-blockchain-for-stablecoin-payments-infrastructure/) |
| Visa | 年化稳定币结算规模超过 250 亿美元，约为一年前的十倍；支持 5 种稳定币、10 条链 | “漫游结算中心”角色 | [crypto.news](https://crypto.news/visa-stablecoin-settlement-volume-25-billion-2026/) |

## 四、相同点：五个维度的对照

两个行业在竞争早期的五个特征高度一致，这是用电信史推演稳定币的基础。

| 维度 | 电信 | 稳定币 | 证据强度 |
| --- | --- | --- | --- |
| 1. 先碎片化，后快速集中 | 七国八制 → 5 家全球厂商胜出 | 数百种稳定币，但前两名已占约 85% | 强 |
| 2. 监管分两条路：强制 vs 放任 | 欧洲强制 GSM；美国不指定标准 | MiCA 强制授权、强制下架；GENIUS 只管资质不管技术 | 强 |
| 3. 固定成本门槛淘汰中小玩家 | 交换机研发成本 | 合规成本：资本、流动性、反洗钱、牌照 | 中强 |
| 4. 在位巨头以联盟形式入场 | 欧洲设备商和运营商联合推 GSM | 21 家银行联盟、37 家机构的 Qivalis | 中（尚未上线） |
| 5. 底层“制式”之争 | A 网/B 网；GSM/CDMA/TDMA | Ethereum、Tron、Solana、Tempo、Arc、Plasma | 强 |

**维度 1 的依据**：全球交换机市场经过一轮淘汰后，只剩下五家能拿到足够份额养活下一代研发的厂商（[Tech Monitor](https://www.techmonitor.ai/?p=160397)）。稳定币尚在早期，集中度却已高于当年的交换机市场（[Crypto Briefing](https://cryptobriefing.com/tether-circle-stablecoin-dominance/)）。

**维度 2 的依据**：美国政府没有强制全国标准，三种移动技术并存（[Curwen 2004](https://emeraldinsight.com/insight/content/doi/10.1108/info.2004.27206aab.001/full/html)）。欧盟则用 MiCA 把 USDT 挤出受监管交易所，USDC 和 EURC 接管空位（[The Paypers](https://thepaypers.com/crypto-web3-and-cbdc/news/tether-exits-eu-market-as-mica-rules-block-usdt-from-exchanges)）。

**维度 5 的依据**：Tempo、Arc、Plasma、Stable 是同一批专为稳定币设计的 Layer 1（[Fortune](https://fortune.com/crypto/2025/09/04/stripe-paradigm-tempo-blockchain-stablecoins-matt-huang-payments/)）。这与 80 年代末 A 网、B 网并存、差异极大的局面相似（[虎嗅](https://www.huxiu.com/article/2794258.html)）。

## 五、关键差异：类比失效之处

最大的差异在互联互通：稳定币之间没有强制互通，头部玩家也没有互通的动力。这决定了第六节哪些预测成立、哪些需要附加条件。

| 差异 | 电信 | 稳定币 | 对推演的影响 |
| --- | --- | --- | --- |
| 1. 互联互通 | 监管很早强制运营商互联，网络效应落在“标准”层 | 发行方之间无法定平价兑换；USDT 与 USDC 是不同主体的负债，网络效应锁在单一代币的流动性上 | 预测 4 必须以“出现互通机制”为前提 |
| 2. 收入来源 | 卖设备，利润来自产品 | 主要靠储备资产利息，对利率高度敏感 | 降息会加速洗牌，这是电信没有的宏观变量 |
| 3. 入场壁垒 | 重资产：铺网、频谱，带天然垄断属性 | 轻资产：可直接运行在公链上；壁垒是信任、牌照、流动性 | 后来者入场更快，格局变化周期更短 |
| 4. 主权敏感度 | 产业政策问题 | 货币主权问题：美元稳定币影响他国货币政策和资本管制 | 监管分裂更深，“货币区冠军”更可能出现 |
| 5. 替换成本 | 交换机部署后锁定 10–20 年 | 换链、换币是软件层面的事 | “制式战”未必需要有人胜出，可能被抽象层化解 |
| 6. 互联动机 | 物理覆盖和地区竞争使没有一家能覆盖所有用户，有强烈的合作和制定互通标准的意愿 | 依托全球一体的互联网，单一发行方可覆盖全球，头部倾向赢家通吃 | 互通只会来自监管或挑战者联合 |

**差异 1 的依据**：MiCA 下的研究发现，USDT 被下架后，全球 USDT 与 USDC 的份额几乎没变，只是欧盟交易所内的交易转向 USDC（[Cryptopolitan，引 Borri & Shakhnov 2026](https://cryptopolitan.com/mica-pushes-usdt-out-leaves-usdc-in)）。USDT 的流动性网络效应不依赖单一辖区，电信运营商从未有过这种跨辖区的产品锁定。

**差异 2 的依据**：GENIUS 第 4 节禁止发行方向持有人支付任何形式的利息或收益，但并未明确禁止交易所向客户发放奖励（[美国国会研究服务处 CRS](https://www.everycrsreport.com/reports/IF13174.html)）。据报道，Circle 二季度储备收益率已降至约 3.5%（[KuCoin](https://www.kucoin.com/blog/in-circle-renews-usdc-revenue-sharing-agreement-with-coinbase-through-2029)，二手来源）。

### 差异 6 展开：互联互通的动机

电信厂商受制于物理覆盖投入和地区竞争，没有一家能独自覆盖所有用户，因此有强烈的互联合作倾向，愿意共同制定互通标准，如 GSM 国际漫游、联合制定 3G 标准。稳定币依托全球一体的互联网，单一发行方理论上可以覆盖全球，头部玩家倾向“一家独大”，只有在竞争中无法取胜时才会寻求互通。

但需要补充一点：电信的合作倾向主要出现在跨国漫游和设备标准层面。在单一市场内，占支配地位的运营商同样拒绝互联。贝尔专利到期后，AT&T 一边收购独立电话公司、一边拒绝连接剩余对手，直到 1913 年在反垄断压力下才有 Kingsbury Commitment（[Broadband Breakfast](https://broadbandbreakfast.com/the-kingsbury-commitment-promised-competition-at-t-got-98-of-long-distance/)）。该承诺只开放长途网络，不包括本地互联（[Wikipedia](https://en.wikipedia.org/wiki/Kingsbury_Commitment)）。1980 年 MCI 还需要通过诉讼才赢得长途竞争权（[RCR Wireless](https://www.rcrwireless.com/20010212/carriers/breaking-ma-bell)）。

**综合后的规律**：在两个行业里，支配者都排斥互联。互联只有三种来源：

1. 物理或地域限制使没有人能独占，如电信国际漫游；
2. 监管强制，如 Kingsbury Commitment 和 1984 年 AT&T 拆分；
3. 处于劣势的挑战者联合。

稳定币缺少第 1 种驱动力，只剩第 2 种和第 3 种。现实也印证了这一点：份额第一的 Tether 宁可退出欧盟受监管市场，也不接受 MiCA 规则（[The Paypers](https://thepaypers.com/crypto-web3-and-cbdc/news/tether-exits-eu-market-as-mica-rules-block-usdt-from-exchanges)）；主动推动“中立”和多币种兼容的，是自身不发行主流稳定币的 Stripe/Tempo 和 Visa。

## 六、预测、先决条件与判断依据

五条预测中，预测 1 和预测 5 的证据最充分；预测 4 依赖一个尚不存在的互通机制，不确定性最高。每条均按“电信对照 → 先决条件 → 判断依据 → 证伪信号”列出。

**时间坐标**：电信从 1982 年中国首部万门程控机到设备商格局定型、从 1990 年代 GSM 商用到 2010 年前后 LTE 统一，各约 20 年。稳定币始于 2014 年，2025–2027 年的监管落地相当于电信的 1984 年（AT&T 拆分）。考虑到软件的替换成本更低，本文假设稳定币节奏是电信的一半到三分之二。这是判断，不是数据。

### 预测 1：发行层收敛为“2–3 家全球美元发行方 + 各货币区本地冠军”（2027–2032）

- **电信对照**：交换机厂商从十余家收敛到 5 家；北电 2009 年破产，阿尔卡特-朗讯 2016 年并入诺基亚。
- **先决条件**：
    1. GENIUS 实施规则在 2027 年 1 月 18 日前后大体按草案落地并执行，资本和流动性门槛不被大幅放宽。
    2. MiCA 和香港的严格牌照制维持不变。
    3. 利率维持或下行，压缩中小发行方的利差。
    4. 头部发行方不发生重大脱锚或储备危机。
- **判断依据**：
    - 集中度已经很高：双寡头合计约 85%（[Crypto Briefing](https://cryptobriefing.com/tether-circle-stablecoin-dominance/)）。
    - 合规门槛正在抬高：美国草案规定最低资本 500 万美元、两个工作日内赎回（[Finance Magnates](https://www.financemagnates.com/cryptocurrency/regulation/ten-days-to-the-genius-act-deadline-what-the-draft-rules-already-reveal/)）；香港 36 家申请者只发了 2 张牌照（[Caixin Global](https://www.caixinglobal.com/2026-04-10/hong-kong-grants-first-stablecoin-licenses-to-hsbc-standard-charteredbacked-venture-102432744.html)）。
    - 分发成本很高：2024 年 Circle 付给 Coinbase 约 9.08 亿美元，约占相关收入的 54%（[KuCoin](https://www.kucoin.com/blog/in-circle-renews-usdc-revenue-sharing-agreement-with-coinbase-through-2029)，二手来源）。规模不足的发行方付不起这类渠道费。
    - 在位者以联盟形式入场：21 家银行计划 2027 年上半年发行美元稳定币（[CoinMarketCap](https://coinmarketcap.com/academy/article/21-banks-stablecoin-venture-usd-token-launch-2027)）。
- **证伪信号**：到 2030 年，流通量超 10 亿美元的受监管美元发行方超过 10 家；或前两名合计份额跌破 70%。

### 预测 2：离岸 USDT 走“小灵通”路径——长期存在，但在受监管通道中份额下降（2027–2030）

- **电信对照**：小灵通靠低价和政策缝隙服务大量用户，3G 牌照发放后逐步退出（行业通史）。
- **先决条件**：
    1. 美国执行 GENIUS 对境外发行方的限制，且 USDT 未获得“可比监管体系”认定。
    2. Tether 不申请 MiCA 授权。
    3. 新兴市场的美元需求和离岸衍生品交易需求保持，这是 USDT 不会消失的前提。
- **判断依据**：
    - GENIUS 禁止数字资产服务商在美国提供境外发行方的支付稳定币（有例外条件）（[Latham & Watkins](https://www.lw.com/en/insights/genius-act-of-2025-stablecoin-legislation-adopted)）。
    - Tether 已用 USAT 走“双轨”：离岸 USDT + 由 Anchorage Digital 发行的合规 USAT（[Yahoo Finance](https://finance.yahoo.com/news/tether-launches-us-regulated-usat-161314419.html)）。
    - USDT 的需求主要来自新兴市场和离岸衍生品交易所（[KuCoin](https://www.kucoin.com/blog/stablecoins-stall-300-billion-tether-usdt-leads)）。
    - USDC 增速快于 USDT：2025 年约 73% 对 36%（[DEXTools](https://www.dextools.io/news/stablecoin-market-tops-320-billion-usdc-usdt-june-2026)）。
- **证伪信号**：USDT 获得美国可比监管认定或 MiCA 授权；或 USDT 全球份额重回 65% 以上。

### 预测 3：专用链“制式战”收敛，或被互操作层抽象掉（2028–2032）

- **电信对照**：GSM/CDMA 之争在 4G 时代统一到 LTE（行业通史）；输掉制式的高通仍靠专利收费获利（[eWeek](https://www.eweek.com/fr/mobile/winner-take-all/)）。
- **先决条件**：
    1. 跨链互操作标准成熟，安全性被受监管机构接受。
    2. 监管机构不指定某一条链（目前美欧都未指定）。
    3. 银行和卡组织持续承受多链运营成本，形成收敛压力。
- **判断依据**：
    - Visa 在扩大的多链结算试点中，用统一接口隐藏底层链的差异（[Visa 新闻稿](https://investor.visa.com/news/news-details/2026/Visa-Accelerates-Stablecoin-Momentum-Adding-Five-Blockchains-for-Settlement/default.aspx)）。这正是 GSM 漫游结算的角色。
    - Tempo 主打“稳定币中立”，允许任何稳定币支付手续费（[CryptoSlate](https://cryptoslate.com/stripe-and-paradigm-reveal-tempo-layer-1-blockchain-for-stablecoin-payments-infrastructure/)），说明链本身在向“管道”定位。
    - 电信史显示，多标准并存会分散研发、拖慢进展（[eWeek](https://www.eweek.com/pt/mobile/winner-take-all/)）。
- **证伪信号**：到 2032 年，受监管稳定币的结算仍均匀分布在 5 条以上的链上，且没有公认的互操作标准。

### 预测 4：互通机制出现后，发行方沉为“管道”，价值流向分发与应用层（2029 年以后）

- **电信对照**：AT&T 拆分后长途竞争加剧；此后价值从设备商转向运营商，再转向应用层。
- **先决条件**（本条依赖性最强）：
    1. **关键**：受监管稳定币之间出现平价互换机制，可以是监管要求、银行间清算安排或行业协议。目前这种机制尚不存在。推动者预计是监管机构或处于劣势的挑战者联盟，而非份额第一的发行方（见第五节差异 6）。
    2. GENIUS 的发行方付息禁令维持，而分发方发放奖励的空间不被关闭。
    3. 利率下行，储备利差缩小。
- **判断依据**：
    - 分发方已经拿走大部分利润：Coinbase 拿走其平台上 USDC 的全部储备利息，另加剩余收入的 50%（[KuCoin](https://www.kucoin.com/blog/in-circle-renews-usdc-revenue-sharing-agreement-with-coinbase-through-2029)）；50% 分成最早披露于 Circle 的 S-1 招股书（[Decrypt](https://decrypt.co/312757/coinbase-circles-residual-usdc-reserve-revenue-sharing-filing)）。
    - 法律禁止发行方付息，但未明确禁止交易所发放奖励（[CRS](https://www.everycrsreport.com/reports/R49351.html)），结构上偏向掌握用户的一方。
    - Stripe 自建 Tempo，是为了在交易双方不是 Stripe 客户时也能收费（[eMarketer](https://www.emarketer.com/content/stripe-makes-payments-infrastructure-stablecoin-blockchain)）。
- **证伪信号**：到 2030 年仍无任何平价互通机制；或发行方的分发成本占比持续下降。

### 预测 5：非美元货币区扶持本地冠军（2026–2030）

- **电信对照**：中国“以市场换技术”，在引进七国八制的过程中培养人才，最终崛起巨大中华（[虎嗅](https://www.huxiu.com/article/2794258.html)）。
- **先决条件**：
    1. 欧盟、香港等辖区继续发牌并保护本币稳定币。
    2. 本币稳定币找到真实用途：跨境贸易、代币化资产结算。
    3. CBDC（数字欧元等）不完全挤占私人发行方的空间。
- **判断依据**：
    - 香港首批持牌方计划发行港元稳定币（[FinTech Futures](https://www.fintechfutures.com/blockchain-crypto-digital-assets/hkma-grants-first-hong-kong-stablecoin-licences-to-hsbc-and-standard-chartered)）。
    - MiCA 下欧元稳定币于 2026 年年中创约 9 亿美元的新高，EURC 占约一半（[Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/euro-stablecoins-hit-record-highs-101822466.html)）。
    - 银行联盟计划在美元后扩展到欧元等 G7 货币，Qivalis 另设欧元方案（[Financial News](https://en.fnnews.com/news/202609020839433776)）。
    - 反向证据：欧元稳定币仍不到全球稳定币市场的 1%（[CoinStats，引 Token Terminal](https://coinstats.app/news/3585a5c32c264b62d97d531ee0252738215765c3af60e22608e936331e14f3f6_MiCA-pushes-USDT-out-leaves-USDC-in-the-spotlight)）。本条预测的是“出现冠军”，不是“挑战美元”。
- **证伪信号**：到 2030 年非美元稳定币合计仍低于市场的 2%，且没有任何一种流通量超过 50 亿美元。

## 七、风险与反例

以下五种情况一旦出现，本文的类比就会在相应环节失效。

1. **监管长期不要求互通。** USDT 的流动性网络效应可能比任何电信运营商都持久，预测 4 将不成立。MiCA 下架 USDT 后，全球份额几乎未变，已是一个警示（[Cryptopolitan](https://cryptopolitan.com/mica-pushes-usdt-out-leaves-usdc-in)）。
2. **CBDC 变量。** 电信业没有“政府直接发行电话”的对应物。数字欧元、数字人民币可能从顶层改写非美元区格局；分析师已把数字欧元视为 Visa 的中期监管压力（[The Block](https://www.theblock.co/amp/post/399405/visa-stablecoin-settlement-hits-7-billion-run-rate-pilot-expands-nine-blockchains)）。
3. **银行联盟可能重蹈巨龙的覆辙。** 中国曾计划合并八家国有厂组建巨龙（[Tech Monitor](https://www.techmonitor.ai/?p=160397)），但巨龙因股东多、治理内耗最早没落（[IT之家](https://www.ithome.com/0/533/645.htm)）。真正胜出的是在市场中自主研发的华为、中兴。21 家银行的联合公司可能面临同样的决策速度问题；其发行仍受成立条件限制，2027 年上半年只是目标（[KuCoin](https://www.kucoin.com/blog/21-financial-institutions-usd-stablecoin-2027)）。
4. **监管实施延误或反复。** 美国监管机构已经错过一年期限，发行方只能按可能变动的草案准备（[The Block](https://www.theblock.co/post/408843/us-regulators-miss-genius-acts-one-year-deadline-for-final-stablecoin-rules)）。若规则大幅放松，预测 1 的洗牌会变慢。
5. **加密币高光退去，引流失效。** 比特币 2026 年 11 月中旬较 2025 年 10 月高点下跌近 47%（[Crypto Briefing](https://cryptobriefing.com/bitcoin-selloff-tests-committed-investors/)），主要稳定币供应 30 天减少 142 亿美元，为 2022 年以来最大收缩（[The Block](https://theblock.co/news/ecosystems/2026-11-11-stablecoin-supply-drops-14-2-billion-largest-contraction-since-2022-bear-market-437907)）。若行情持续下行，靠加密交易引流的发行方增长放缓，预测 1 的洗牌会加快，银行发行方和支付型链相对受益。不过到目前为止，这次收缩只占稳定币总量的约 5%，“一泻千里”的是加密币价格，而不是稳定币供应。详细分析见[《稳定币的本质：无需清算所牌照的企业私有清算所》第十节](/zh/articles/stablecoin-private-clearing-house/)。

**方法论局限**：历史类比只能提示方向，不能提供概率。文中的“置信度”和时间窗口是作者判断，应按证伪信号定期复核。

## 参考资料

**可靠性说明**：监管机构公告、律所分析、美国国会研究服务处（CRS）报告和公司新闻稿为一手或权威来源；KuCoin、CoinPaprika 等交易所/数据平台博客为二手来源，相关数字已在正文中标注。标为“行业通史”的内容（小灵通退出、LTE 统一、价值向应用层迁移）为公认史实，未单独引用。

**电信史**

1. [IT之家：巨龙通信的成与败](https://www.ithome.com/0/533/645.htm)
2. [IT之家：大唐电信的沧桑往事](https://www.ithome.com/0/616/767.htm)
3. [IT之家：华为 08 机往事](https://www.ithome.com/0/522/054.htm)
4. [虎嗅：七国八制与移动通信的选择](https://www.huxiu.com/article/2794258.html)
5. [新民周刊：上海电信史](https://img1.xinmin.cn/xmzk/2020-01-06/830106.pdf)
6. [Tech Monitor：全球交换机厂商整合与中国巨龙计划](https://www.techmonitor.ai/?p=160397)
7. [Wikipedia：Breakup of the Bell System](https://en.wikipedia.org/wiki/Breakup_of_the_Bell_System)
8. [EBSCO：AT&T Undergoes Divestiture](https://www.ebsco.com/research-starters/history/att-undergoes-divestiture)
9. [Wikipedia：Kingsbury Commitment](https://en.wikipedia.org/wiki/Kingsbury_Commitment)
10. [Broadband Breakfast：The Kingsbury Commitment Promised Competition](https://broadbandbreakfast.com/the-kingsbury-commitment-promised-competition-at-t-got-98-of-long-distance/)
11. [RCR Wireless：Breaking Ma Bell](https://www.rcrwireless.com/20010212/carriers/breaking-ma-bell)
12. [Curwen (2004), Has GSM won the technology war?, *info* 6(1)](https://emeraldinsight.com/insight/content/doi/10.1108/info.2004.27206aab.001/full/html)
13. [eWeek：Winner Take All](https://www.eweek.com/mobile/winner-take-all/)
14. [Wikipedia：Comparison of mobile phone standards](https://en.wikipedia.org/wiki/Comparison_of_mobile_phone_standards)
15. [Wikipedia：Nortel](https://en.wikipedia.org/wiki/Nortel)
16. [Wikipedia：Alcatel-Lucent](https://en.wikipedia.org/wiki/Alcatel-Lucent)
17. [telecoms.com：End of an era](https://www.telecoms.com/digital-ecosystem/end-of-an-era)

**稳定币市场**

18. [DefiLlama：Stablecoins](https://defillama.com/stablecoins)
19. [Crypto Briefing：Tether and Circle control 85% of stablecoin supply](https://cryptobriefing.com/tether-circle-stablecoin-dominance/)
20. [DEXTools：Stablecoin Market Tops $320 Billion](https://www.dextools.io/news/stablecoin-market-tops-320-billion-usdc-usdt-june-2026)
21. [CoinPaprika：The Stablecoin Wars](https://coinpaprika.com/cs/education/stablecoin-wars)
22. [KuCoin：Why Stablecoin Growth Stalls at $300 Billion](https://www.kucoin.com/blog/stablecoins-stall-300-billion-tether-usdt-leads)
23. [Yahoo Finance：Euro Stablecoins Hit Record Highs Under MiCA](https://finance.yahoo.com/markets/crypto/articles/euro-stablecoins-hit-record-highs-101822466.html)

**监管**

24. [Latham & Watkins：The GENIUS Act of 2025](https://www.lw.com/en/insights/2025/07/the-genius-act-of-2025-stablecoin-legislation-adopted-in-the-us)
25. [CRS：The Stablecoin Yield Debate (IF13174)](https://www.everycrsreport.com/reports/IF13174.html)
26. [CRS：GENIUS Act (P.L. 119-27) (R49351)](https://www.everycrsreport.com/reports/R49351.html)
27. [The Block：US regulators miss GENIUS Act's one-year deadline](https://www.theblock.co/post/408843/us-regulators-miss-genius-acts-one-year-deadline-for-final-stablecoin-rules)
28. [The Block：OCC debuts final rule implementing GENIUS Act](https://theblock.co/news/regulation/2026-10-21-occ-final-rule-implementing-trump-signed-genius-act-421470)
29. [Finance Magnates：What the draft GENIUS rules reveal](https://www.financemagnates.com/cryptocurrency/regulation/ten-days-to-the-genius-act-deadline-what-the-draft-rules-already-reveal/)
30. [HKMA：Granting of stablecoin issuer licences（2026-04-10）](https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/04/20260410-4/)
31. [Caixin Global：香港首批稳定币牌照](https://www.caixinglobal.com/2026-04-10/hong-kong-grants-first-stablecoin-licenses-to-hsbc-standard-charteredbacked-venture-102432744.html)
32. [FinTech Futures：HKMA grants first licences](https://www.fintechfutures.com/blockchain-crypto-digital-assets/hkma-grants-first-hong-kong-stablecoin-licences-to-hsbc-and-standard-chartered)
33. [The Paypers：Tether exits EU market as MiCA rules block USDT](https://thepaypers.com/crypto-web3-and-cbdc/news/tether-exits-eu-market-as-mica-rules-block-usdt-from-exchanges)
34. [Cryptopolitan：MiCA pushes USDT out, leaves USDC in the spotlight](https://cryptopolitan.com/mica-pushes-usdt-out-leaves-usdc-in)

**主要玩家**

35. [Yahoo Finance：Tether Launches US-Regulated USAT](https://finance.yahoo.com/news/tether-launches-us-regulated-usat-161314419.html)
36. [Decrypt：Coinbase Takes 50% Share of Circle's Residual USDC Reserve Revenue](https://decrypt.co/312757/coinbase-circles-residual-usdc-reserve-revenue-sharing-filing)
37. [KuCoin：Circle Renews USDC Revenue-Sharing Agreement Through 2029](https://www.kucoin.com/blog/in-circle-renews-usdc-revenue-sharing-agreement-with-coinbase-through-2029)
38. [CoinMarketCap：21 Major Banks Plan Stablecoin Venture](https://coinmarketcap.com/academy/article/21-banks-stablecoin-venture-usd-token-launch-2027)
39. [KuCoin：21 Global Financial Institutions Back a Joint USD Stablecoin](https://www.kucoin.com/blog/21-financial-institutions-usd-stablecoin-2027)
40. [Banking Dive：BofA, Wells Fargo, Citi back upcoming stablecoin](https://www.bankingdive.com/news/bofa-wells-fargo-citi-back-upcoming-stablecoin/829318/)
41. [Financial News（韩国）：21 家机构联合发行美元稳定币](https://en.fnnews.com/news/202609020839433776)
42. [Fortune：Stripe and Paradigm announce Tempo](https://fortune.com/crypto/2025/09/04/stripe-paradigm-tempo-blockchain-stablecoins-matt-huang-payments/)
43. [Everstake：Tempo vs Arc](https://everstake.one/resources/blog/tempo-vs-arc-stablechains-the-next-generation-of-finance)
44. [CryptoSlate：Tempo layer-1 for stablecoin payments](https://cryptoslate.com/stripe-and-paradigm-reveal-tempo-layer-1-blockchain-for-stablecoin-payments-infrastructure/)
45. [eMarketer：Stripe makes payments infrastructure play](https://www.emarketer.com/content/stripe-makes-payments-infrastructure-stablecoin-blockchain)
46. [Visa 新闻稿：Adding Five Blockchains for Settlement（2026-04-29）](https://investor.visa.com/news/news-details/2026/Visa-Accelerates-Stablecoin-Momentum-Adding-Five-Blockchains-for-Settlement/default.aspx)
47. [crypto.news：Visa stablecoin settlement surpasses $25B](https://crypto.news/visa-stablecoin-settlement-volume-25-billion-2026/)
48. [The Block：Visa stablecoin settlement hits $7 billion run rate](https://www.theblock.co/amp/post/399405/visa-stablecoin-settlement-hits-7-billion-run-rate-pilot-expands-nine-blockchains)
49. [CoinStats：MiCA pushes USDT out, leaves USDC in the spotlight](https://coinstats.app/news/3585a5c32c264b62d97d531ee0252738215765c3af60e22608e936331e14f3f6_MiCA-pushes-USDT-out-leaves-USDC-in-the-spotlight)
