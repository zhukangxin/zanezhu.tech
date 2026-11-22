---
title: "稳定币的经济学：发行方为什么像一家私有跨境清算所"
date: 2026-11-20
description: "从经济实质看，稳定币发行方像一家企业私有的跨境清算所：把用户的法币归拢成资金池，在自己的负债账本上转移价值，赚取浮存金利差。本文拆解其运作、牌照、获客和盈利模式，分析加密市场低迷时格局可能的变化，并列出它确实不同于清算所的地方。目的是看清支付型和银行型稳定币将在什么样的商业模式上竞争。"
tags: ["稳定币", "清算所", "浮存金", "支付监管", "跨境支付"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_zh_stablecoin-clearing-house.png"
draft: false
---

> 相关文章：[跨境支付不一定需要共享账本](/zh/articles/cross-border-payments-dont-need-blockchain/) · [从程控交换到稳定币](/zh/articles/telecom-lessons-for-stablecoin-competition/)
>
> 数据截至 2026 年 11 月。本文不构成投资建议，也不是法律意见。

## 一、论点

**从经济实质看，稳定币发行方像一家企业私有的跨境清算所。** 它做的很多是清算所的事，但持有的是发行人和汇款类牌照，而不是清算所牌照；它的增长主要来自加密交易和公链的覆盖面；它把用户的法币归拢成资金池，主要收入来自资金池的利息。看清这个模式，对做稳定币产品的人很重要，因为监管正在把它拉向支付基础设施的标准。

把这句话拆开，是五个要素，外加一个推论：

| 要素 | 含义 | 本文对应章节 |
| --- | --- | --- |
| 企业私有清算所 | 资金集中到一家公司，转账在它的负债账本上完成 | 二、三 |
| 不同的牌照体系 | 以汇款、数字资产服务或新设的发行人牌照经营，而不是按金融市场基础设施监管 | 四 |
| 借区块链分发 | 钱包接入降低获客成本，但用户需要评估的是发行方的信用，而不是链 | 五 |
| 增长与加密交易挂钩 | 很多用户为买卖加密币而来，资金池随加密行情涨落 | 六 |
| 构建资金池 | 无息吸收法币，储备投向国债，利差归发行方 | 七、八 |
| 加密市场低迷时 | 加密币价格下跌，交易驱动的需求减弱，格局重排 | 十 |

## 二、拆开一笔稳定币跨境支付

以一家美国企业通过 USDC 向墨西哥供应商付款为例：

| 步骤 | 表面上 | 实际上 |
| --- | --- | --- |
| ① 入金 | 买入 USDC | 企业通过电汇、ACH 等传统银行网络，把美元打进发行方的银行账户 |
| ② 铸币 | 链上生成代币 | 发行方在自己的负债账本上记一笔：欠该企业 X 美元 |
| ③ 链上转账 | “去中心化点对点支付” | 发行方对企业的负债，转记为对供应商的负债；资金仍在发行方的银行账户和国债里 |
| ④ 出金 | 卖出 USDC 换比索 | 供应商通过交易所或做市商，再经墨西哥本地银行网络收到比索 |

三点结论：

1. **两端都离不开传统支付网络。** 真正的法币流动只发生在入金和出金时。
2. **中间的“支付”是债权转让。** 持有人 A 对发行方的债权变成持有人 B 的债权，经济上与同一家银行内部转账相同。
3. **链上转账再快，也只是所内记账的速度。** 跨境法币结算被推到出金端的外汇和本地银行环节。

## 三、为什么说它是清算所

清算所的核心特征是：参与者把资金集中存放在一个中心机构，机构在内部账本上完成划转，只在必要时与外部系统做最终结算。稳定币发行方几乎完全符合：

| 维度 | 传统清算所 / 代理行 | 稳定币发行方 |
| --- | --- | --- |
| 资金存放 | 会员在清算所或代理行存放资金 | 用户把法币交给发行方 |
| 内部划转 | 清算所账本上的记账 | 链上代币转账，即发行方负债的转让 |
| 控制权 | 可暂停、拒绝会员 | 可冻结、拉黑地址，销毁后重新发行 |
| 最终结算 | 央行或商业银行账户 | 发行方的银行账户 |
| 主要收入 | 交易手续费 | 储备资产的利息 |

国际标准制定者也是这样看的。2022 年，国际清算银行支付与市场基础设施委员会（CPMI）和国际证监会组织（IOSCO）发布最终指引，确认具有系统重要性的稳定币安排应遵守《金融市场基础设施原则》（PFMI），即支付、清算和结算系统的国际标准，理由是“同样的风险，同样的监管”（[BIS 新闻稿](https://www.bis.org/media-releases/20220713-cpmi-and-iosco-publish-final-guidance-stablecoin-arrangements-confirming-application-principles)；[IOSCO 新闻稿](https://www.iosco.org/news/pdf/IOSCONEWS651.pdf)）。指引明确，稳定币安排的转账功能就是一项金融市场基础设施功能（[CPMI-IOSCO 报告](https://www.bis.org/cpmi/publ/d198.pdf)）。

区块链在这里更像一块公开显示屏和报文层，而不是独立的货币体系。

## 四、牌照：以发行人牌照承担清算所的功能

一家受监管的清算机构，要按 PFMI 满足治理、全面风险管理、结算最终性等一整套要求（[FSB 摘要](https://www.fsb.org/2022/07/application-of-the-principles-for-financial-market-infrastructures-to-stablecoin-arrangements/)）。稳定币发行方大多在其他框架下取得牌照：

- **Tether 的注册地选择。** Tether 原注册于英属维尔京群岛，2025 年 1 月在萨尔瓦多拿到数字资产服务商（DASP）和稳定币发行人牌照后，宣布把总部和子公司迁往萨尔瓦多（[Cointelegraph](https://cointelegraph.com/news/tether-el-salvador-securing-license-property)）。这些是数字资产类牌照，不是清算机构或银行牌照。
- **纽约州的认定。** 2021 年纽约州总检察长与 Bitfinex 和 Tether 和解，和解协议指控二者在储备问题上误导市场，同时在纽约州开展业务却没有相应牌照，双方支付 1850 万美元（[Hunton 律所摘要](https://www.hunton.com/blockchain-legal-resource/2021/03/new-york-attorney-general-announces-settlement-with-bitfinex/)）。
- **Circle 的联邦牌照来得很晚。** USDC 自 2018 年发行，Circle 直到 2026 年 7 月才获得美国货币监理署（OCC）的全国性信托银行牌照，而且首先用于数字资产托管；USDC 的发行将转到一家纽约有限目的信托公司（[The Block](https://www.theblock.co/news/regulation/2026-07-10-stablecoin-firm-circle-wins-final-occ-approval-to-open-national-trust-bank-407876)）。
- **新法设立的是“发行人牌照”，不是清算所牌照。** 美国 GENIUS 法案为“许可支付稳定币发行人”设立了新的牌照类别；按目前的草案，新联邦发行人的最低资本只有 500 万美元（[Finance Magnates](https://www.financemagnates.com/cryptocurrency/regulation/ten-days-to-the-genius-act-deadline-what-the-draft-rules-already-reveal/)），且这些规则要到 2027 年 1 月 18 日才生效（[The Block](https://www.theblock.co/post/408843/us-regulators-miss-genius-acts-one-year-deadline-for-final-stablecoin-rules)）。

结论：USDT 自 2014 年、USDC 自 2018 年起，这两家最大的稳定币多年来都在清算所以外的牌照体系下运营。监管正在通过新设的发行人牌照补上这一块；具有系统重要性的发行方是否也会按金融市场基础设施来监管，仍是一个开放问题。

## 五、借区块链分发：覆盖面带来的信用问题

持有稳定币，意味着持有一家私营公司的无息债权。公链在四个方面帮助了发行方：

1. **信任框架。** 用户看到的常常是“链上美元”，而不是对发行方的债权，因此对发行方本身信用的审视往往不够。
2. **低成本分发。** 有钱包就能接入，无需开户和面签，获客成本远低于银行。
3. **监管定性空白。** 早期在“它是证券、存款、电子货币还是支付工具”的定性空白中运营，避开了银行和清算机构的牌照、资本金和存款保险要求（见第四节）。
4. **生态绑定。** 交易所和 DeFi 协议把稳定币作为基础结算资产，形成网络效应。

换句话说，**对发行方来说，区块链主要是分发渠道和公共展示账本；核心的经济逻辑在储备资产上。**

## 六、增长与加密交易挂钩：资金池随行情涨落

大多数稳定币用户最初不是为了跨境支付而来，而是为了买卖加密币，稳定币成了进出加密市场的主要工具。证据有四条：

1. **主要用途是加密交易。** 国际清算银行（BIS）2026 年指出，稳定币年交易额约 35 万亿美元，但用于实体经济的交易有限，主要用于加密生态内的链上交易（[BIS 演讲](https://www.bis.org/speeches/20260420-stablecoins-framing-debate)）。BIS 2026 年年报也认为，稳定币的主要用途是加密交易，其次才是新兴市场的离岸美元储值（[Bitcoin Foundation 报道](https://bitcoinfoundation.org/?p=7882)）。
2. **资金随牛市流入。** 摩根大通测算，2020–2021 年约有 1650 亿美元通过新铸稳定币进入加密市场（[CoinDesk](https://www.coindesk.com/markets/2022/11/17/jpmorgan-the-shrinking-stablecoin-market-is-another-sign-of-investors-exodus-from-crypto/)）。
3. **资金随熊市流出。** 同一报告显示，最大几种稳定币合计市值在 2022 年 5 月达到 1860 亿美元峰值，此后下降 410 亿美元，其中近一半来自 Terra 崩盘（[CoinDesk](https://www.coindesk.com/markets/2022/11/17/jpmorgan-the-shrinking-stablecoin-market-is-another-sign-of-investors-exodus-from-crypto/)）。2026 年 11 月，主要稳定币 30 天内供应减少 142 亿美元，是 2022 年熊市以来最大的一次收缩（[The Block](https://theblock.co/news/ecosystems/2026-11-11-stablecoin-supply-drops-14-2-billion-largest-contraction-since-2022-bear-market-437907)）。
4. **引流渠道要分成。** 交易所是主要入口，发行方因此要把利息分给交易所：Coinbase 拿走其平台上 USDC 的全部储备利息，另加剩余储备收入的 50%（[Decrypt，据 Circle 招股书](https://decrypt.co/312757/coinbase-circles-residual-usdc-reserve-revenue-sharing-filing)）。

所以获客链条一直是：**加密交易需求 → 用户进入交易所 → 用法币换稳定币当交易筹码 → 法币沉淀在发行方的资金池 → 利息由发行方和交易所分享。** 到目前为止，资金池的规模更多跟着加密行情走，而不是跟着跨境支付需求走。支付用途的增长才是值得关注的部分。

## 七、构建资金池：浮存金生意

发行方的核心商业模式是浮存金（float）：

- 用户交出法币，换到无息的代币；
- 发行方把储备投到短期美国国债、回购和银行存款上，利息归发行方；
- GENIUS 法案禁止发行方向持有人支付任何利息或收益，但没有明确禁止交易所向客户发放奖励（[美国国会研究服务处 CRS](https://www.everycrsreport.com/reports/IF13174.html)）。制度上等于确认了“无息吸储、利差归发行方和渠道”。

这门生意的利润很高。Tether 2024 年净利润超过 130 亿美元，2025 年约 101 亿美元，主要来自美国国债利息（[CoinPaprika](https://coinpaprika.com/news/tether-reports-10b-profit-2025-usdt-supply-hits-186b-record/)；[Tether 公告](https://tether.io/news/tether-delivers-10b-profits-in-2025-6-3b-in-excess-reserves-and-record-141-billion-exposure-in-u-s-treasury-holdings/)）。

**中国已经处理过同一种模式。** 支付宝、微信支付早期的客户备付金存放在商业银行，利息归支付机构。中国人民银行的做法是两步：

1. **收回清算。** 2018 年 6 月 30 日起，支付机构涉及银行账户的网络支付业务全部通过网联平台处理（[每日经济新闻](https://www.nbd.com.cn/articles/2018-06-30/1230579.html)）。
2. **收回资金池。** 2017 年起按比例集中交存备付金，2019 年 1 月 14 日实现 100% 集中存管，规模超过 1.2 万亿元（[界面新闻](https://www.jiemian.com/article/2791123.html)；[新华社](https://www.rmzxw.com.cn/c/2019-01-09/2259805.shtml)）。支付机构由此失去备付金沉淀的收益（[第一财经](https://www.yicai.com/news/100094905.html)）。

这正是把“企业私有清算所 + 浮存金”拿回监管体系的做法。

**关于“集资”一词。** 法律意义上的“集资”，尤其是中国语境下的“非法集资”，通常以承诺回报为特征；稳定币恰恰不承诺回报，只承诺 1:1 兑付。所以更准确的说法是“无息吸储”或“储值归集”，经济上更接近电子货币和预付价值。不过二者的风险结构是相通的（见第八节）。

## 八、资金池的老问题：挤兑与透明度

- **挤兑风险。** 2023 年 3 月硅谷银行倒闭，Circle 有 33 亿美元储备（约占 8%）存在该行，USDC 一度跌破 0.87 美元（[CNBC](https://www.cnbc.com/amp/2023/03/11/stablecoin-usdc-breaks-dollar-peg-after-firm-reveals-it-has-3point3-billion-in-svb-exposure.html)；[美联储 FEDS Notes](https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html)）。持有人承担的是发行方及其开户银行的信用风险。
- **透明度风险。** 2021 年 10 月，美国商品期货交易委员会（CFTC）认定 Tether 在 2016–2019 年间就“完全由美元支持”做出不实陈述，处以 4100 万美元罚款（[CFTC 新闻稿](https://www.cftc.gov/PressRoom/pressReleases/8450-21)）；按 CFTC 的认定，2016–2018 年间 Tether 只有 27.6% 的时间有足够储备覆盖流通代币（[Advisor.ca](https://www.advisor.ca/industry-news/industry/cftc-sanctions-tether-bitfinex/)）。同年 2 月，Tether 和 Bitfinex 还与纽约州总检察长以 1850 万美元和解（[CNBC](https://www.cnbc.com/amp/2021/02/23/tether-bitfinex-reach-settlement-with-new-york-attorney-general.html)）。

这些都是资金池模式的典型风险，也正是清算所和银行牌照要防范的风险。

## 九、公平地说：稳定币确实不同于传统清算所的地方

1. **持有人之间的转让无需发行方逐笔批准。** 链上可以 7×24 小时流转，发行方只保留事后冻结的权力。
2. **账本公开可验证。** 发行方不能单方面篡改历史交易，任何人都能审计链上流通量。
3. **可编程、可组合。** 智能合约能把支付和交割、托管、条件触发绑定在一起。
4. **对部分人群有真实价值。** 对高通胀国家的居民和没有银行账户的人，它提供了可得的美元工具；BIS 也承认这是它的第二大用途（[Bitcoin Foundation 报道](https://bitcoinfoundation.org/?p=7882)）。
5. **监管正在把它“银行化”。** GENIUS 法案、欧盟 MiCA 都要求足额储备、定期披露、持牌经营。这从侧面印证了本文的论点：监管者事实上把它当作一类支付机构或准银行来管理，而不是“去中心化货币”。

## 十、加密市场低迷时：交易需求减弱与格局重排

稳定币是随着加密市场的势头成长起来的。势头放缓时，交易驱动的余额先缩，格局随之重排。本节是基于现有数据的推演，不是价格预测。

### 10.1 低迷的数据

- **比特币价格约腰斩。** 比特币 2025 年 10 月创下约 12.6 万美元的历史高点；2026 年 11 月中旬跌至约 6.2 万美元，较高点低近 47%。11 月 5 日至 13 日，美国现货比特币 ETF 连续 7 个交易日净流出约 19.1 亿美元（[Crypto Briefing](https://cryptobriefing.com/bitcoin-selloff-tests-committed-investors/)）。
- **稳定币资金池同步收缩。** 主要稳定币供应 30 天内减少 142 亿美元，是 2022 年熊市以来最大的一次收缩，总量回落到略低于 2800 亿美元，即 2025 年 9 月的水平；USDT 在截至 11 月 7 日的 60 天内减少 66 亿美元，是 FTX 倒闭后同期降幅的两倍多（[The Block](https://theblock.co/news/ecosystems/2026-11-11-stablecoin-supply-drops-14-2-billion-largest-contraction-since-2022-bear-market-437907)）。
- **2022 年的先例。** 2022 年 6 月，稳定币 30 天降幅接近 300 亿美元，约 5 个月后比特币才见到 1.55 万美元的熊市底部（同上）。

### 10.2 传导机制：引流失效的四个环节

1. **获客停滞。** 赚钱效应消失，新用户不再进场，新铸稳定币减少。
2. **存量赎回。** 持有人把稳定币兑回美元离场，资金池缩小。Glassnode 的解读是：供应收缩意味着现金正在离开市场（[The Block](https://theblock.co/news/ecosystems/2026-11-11-stablecoin-supply-drops-14-2-billion-largest-contraction-since-2022-bear-market-437907)）。
3. **利润双重挤压。** 发行方收入约等于“资金池规模 × 利率”。降息已经让 Tether 2025 年净利润同比下降 23%，至约 101 亿美元（[MEXC 转载](https://www.mexc.com/news/602839)）；如果资金池再随行情收缩，两个因子会同时下降。
4. **挤兑与抛售风险。** BIS 指出，稳定币挤兑会引发储备资产的抛售，可能损害市场运行（[BIS 演讲幻灯片](https://www.bis.org/speeches/sp260420_slides.pdf)）。资金池越依赖加密交易，越容易在行情急跌时集中赎回。

### 10.3 对格局的影响：谁受伤最重，谁相对受益

| 玩家类型 | 对加密交易引流的依赖 | 市场低迷的影响 | 判断 |
| --- | --- | --- | --- |
| 收益型、小型发行方 | 很高 | 收益和规模同时萎缩；例如 2025 年 11 月收益下降时，USDe 市值一个月内减半（[ForkLog](https://forklog.com/en/top-ten-dollar-stablecoins-from-would-be-monopolists-to-those-on-the-brink/)） | 最脆弱，加速出清 |
| 离岸 USDT | 高（离岸交易所、衍生品），但有新兴市场美元储值需求缓冲 | 规模收缩最直接；份额未必下降，目前约占 62.8%（[The Block](https://theblock.co/news/ecosystems/2026-11-11-stablecoin-supply-drops-14-2-billion-largest-contraction-since-2022-bear-market-437907)） | 规模承压，地位短期稳固 |
| 合规型 USDC | 中（交易所、机构、DeFi） | 受交易萎缩影响；但避险时合规属性可能吸引份额，2022 年熊市中 USDC 市值仍增长了 100 多亿美元（[NewsBTC](https://www.newsbtc.com/news/domino-effect-on-stablecoins-leads-to-reversal-of-growth-trend/)） | 相对抗跌 |
| 银行发行（21 家银行联盟、汇丰港元稳定币） | 低，客户来自银行存量 | 不靠加密引流，竞争回到信用和分发，这是银行的强项 | 相对受益 |
| 支付型链与卡组织（Tempo、Visa 稳定币结算） | 低，需求来自 B2B 支付和跨境付款 | 叙事从“交易筹码”转向“支付工具” | 相对受益 |

**格局推论：** 加密市场降温，会削弱靠加密引流起家的发行方的增长引擎，同时抬高不依赖这条引流渠道的银行和支付机构的相对位置。行业重心会从“谁的交易对多”转向“谁的信用好、谁的分发渠道深”。

### 10.4 价值主张转向支付

加密牛市里，稳定币的需求很大一部分来自交易；市场低迷时，长期的价值主张是合规、信用质量和支付效率。换言之，**稳定币会越来越多地被当作支付基础设施来评判，并在信用和分发上与银行和支付网络竞争。** 这对行业是健康的转变，也印证了本文的视角。

电信业有类似先例：2000 年前后电信泡沫破裂。北电鼎盛时市值占多伦多证券交易所全部上市公司总市值的三分之一以上，后来于 2009 年破产（[Wikipedia](https://en.wikipedia.org/wiki/Nortel)）。泡沫退去后，留下来的是有真实客户和现金流的企业。

### 10.5 反方证据与观察指标

**反方证据：**

- BIS 指出，在近期加密市场下跌中，稳定币市场表现得相当有韧性（[BIS 演讲](https://www.bis.org/speeches/20260420-stablecoins-framing-debate)）。到目前为止，30 天 142 亿美元的收缩只占总量的约 5%，远不是“一泻千里”。“一泻千里”更多发生在加密币价格上，而不是稳定币供应上。
- 2022 年的收缩是周期性的：稳定币供应此后恢复，并在 2025–2026 年创出新高。新兴市场的美元储值需求和机构支付需求，构成不依赖加密行情的底盘。

**观察指标：**

1. 稳定币 30 天供应变化是否持续为负；
2. USDT 与 USDC 的份额此消彼长；
3. BIS 等机构统计的非交易用途占比是否上升；
4. 银行联盟稳定币能否按 2027 年上半年的目标上线。

## 十一、结论

从经济实质看，稳定币发行方是一家**持发行人牌照、通过公链分发、主要靠加密交易成长、以资金池利差盈利的企业私有清算所**。它通过传统支付网络归拢法币，以无息负债的形式发行代币，在自己的账本上完成“支付”，再通过传统网络兑付出去。

由此得出四个推论：

1. **稳定币之间的竞争，本质上是吸储能力和分发渠道的竞争，而不是技术竞争。**
2. **它与银行、Visa、Mastercard、SWIFT 的关系不是“颠覆”，而是争夺跨境清算环节的浮存金和中间费用。**
3. **加密市场低迷，会把焦点转向支付。** 靠加密交易做大资金池的发行方可能放缓，以支付场景为基础的发行方，以及银行和支付机构，相对位置上升（见第十节）。
4. **监管越完善，稳定币越像一家“窄银行 + 清算所”。** 最终的问题会回到三点：这类机构由谁发牌，受谁监管，利息归谁所有。中国用网联和备付金集中存管给出了一种答案。

## 参考资料

**国际标准与研究**

1. [CPMI-IOSCO：Application of the PFMI to stablecoin arrangements（2022）](https://www.bis.org/cpmi/publ/d198.pdf)
2. [BIS 新闻稿：CPMI 和 IOSCO 发布稳定币安排最终指引（2022-07-13）](https://www.bis.org/media-releases/20220713-cpmi-and-iosco-publish-final-guidance-stablecoin-arrangements-confirming-application-principles)
3. [IOSCO 新闻稿（2022-07-13）](https://www.iosco.org/news/pdf/IOSCONEWS651.pdf)
4. [FSB：Application of the PFMI to stablecoin arrangements](https://www.fsb.org/2022/07/application-of-the-principles-for-financial-market-infrastructures-to-stablecoin-arrangements/)
5. [BIS 演讲：Stablecoins – framing the debate（2026-04-20）](https://www.bis.org/speeches/20260420-stablecoins-framing-debate)
6. [Bitcoin Foundation：BIS 年报称稳定币主要服务加密交易](https://bitcoinfoundation.org/?p=7882)
7. [美联储 FEDS Notes：硅谷银行倒闭对稳定币的影响（2025-12-17）](https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html)
8. [美国国会研究服务处 CRS：The Stablecoin Yield Debate](https://www.everycrsreport.com/reports/IF13174.html)

**牌照与监管**

9. [Cointelegraph：Tether 获萨尔瓦多牌照并迁址](https://cointelegraph.com/news/tether-el-salvador-securing-license-property)
10. [Hunton：纽约州总检察长与 Bitfinex/Tether 和解](https://www.hunton.com/blockchain-legal-resource/2021/03/new-york-attorney-general-announces-settlement-with-bitfinex/)
11. [The Block：Circle 获 OCC 全国性信托银行最终批准](https://www.theblock.co/news/regulation/2026-07-10-stablecoin-firm-circle-wins-final-occ-approval-to-open-national-trust-bank-407876)
12. [Finance Magnates：GENIUS 规则草案要点](https://www.financemagnates.com/cryptocurrency/regulation/ten-days-to-the-genius-act-deadline-what-the-draft-rules-already-reveal/)
13. [The Block：美国监管机构错过 GENIUS 一年期限](https://www.theblock.co/post/408843/us-regulators-miss-genius-acts-one-year-deadline-for-final-stablecoin-rules)
14. [CFTC 新闻稿 8450-21：Tether 罚款 4100 万美元](https://www.cftc.gov/PressRoom/pressReleases/8450-21)
15. [Advisor.ca：CFTC 制裁 Tether 与 Bitfinex](https://www.advisor.ca/industry-news/industry/cftc-sanctions-tether-bitfinex/)
16. [CNBC：Tether 与 Bitfinex 以 1850 万美元和解纽约州调查](https://www.cnbc.com/amp/2021/02/23/tether-bitfinex-reach-settlement-with-new-york-attorney-general.html)

**市场与盈利**

17. [CoinDesk：摩根大通称稳定币市场收缩是资金撤离加密市场的信号](https://www.coindesk.com/markets/2022/11/17/jpmorgan-the-shrinking-stablecoin-market-is-another-sign-of-investors-exodus-from-crypto/)
18. [The Block：稳定币供应 30 天减少 142 亿美元（2026-11-11）](https://theblock.co/news/ecosystems/2026-11-11-stablecoin-supply-drops-14-2-billion-largest-contraction-since-2022-bear-market-437907)
19. [Decrypt：Coinbase 分得 Circle 剩余储备收入的 50%](https://decrypt.co/312757/coinbase-circles-residual-usdc-reserve-revenue-sharing-filing)
20. [Tether 公告：2025 年利润超过 100 亿美元](https://tether.io/news/tether-delivers-10b-profits-in-2025-6-3b-in-excess-reserves-and-record-141-billion-exposure-in-u-s-treasury-holdings/)
21. [CoinPaprika：Tether 2025 年利润与 2024 年对比](https://coinpaprika.com/news/tether-reports-10b-profit-2025-usdt-supply-hits-186b-record/)
22. [CNBC：USDC 因硅谷银行敞口脱锚](https://www.cnbc.com/amp/2023/03/11/stablecoin-usdc-breaks-dollar-peg-after-firm-reveals-it-has-3point3-billion-in-svb-exposure.html)

**中国备付金与网联**

23. [每日经济新闻：备付金集中交存比例提高至 100%（2018-06-30）](https://www.nbd.com.cn/articles/2018-06-30/1230579.html)
24. [界面新闻：备付金超 1.2 万亿元完成集中存管](https://www.jiemian.com/article/2791123.html)
25. [新华社（人民政协网转载）：备付金全部集中央行存管](https://www.rmzxw.com.cn/c/2019-01-09/2259805.shtml)
26. [第一财经：备付金账户撤销与支付机构收益变化](https://www.yicai.com/news/100094905.html)

**加密行情与格局变化**

27. [Crypto Briefing：比特币抛售考验长期投资者（2026-11）](https://cryptobriefing.com/bitcoin-selloff-tests-committed-investors/)
28. [MEXC 转载：Tether 2025 年利润同比下降 23%](https://www.mexc.com/news/602839)
29. [BIS 演讲幻灯片（2026-04-20）](https://www.bis.org/speeches/sp260420_slides.pdf)
30. [ForkLog：十大美元稳定币](https://forklog.com/en/top-ten-dollar-stablecoins-from-would-be-monopolists-to-those-on-the-brink/)
31. [NewsBTC：2022 年熊市中的稳定币](https://www.newsbtc.com/news/domino-effect-on-stablecoins-leads-to-reversal-of-growth-trend/)
32. [Wikipedia：Nortel](https://en.wikipedia.org/wiki/Nortel)
