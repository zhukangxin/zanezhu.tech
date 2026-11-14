---
title: "跨境支付不需要区块链：用电信的“协议加各自账本”模式重构稳定币方案"
date: 2026-11-14
description: "现有的稳定币和联盟链跨境方案，都可以改用电信业验证了几十年的模式：事先共同制定的自动化协议、各方各自的账本、中立的清算。本文分三层论证，逐一检视 Partior、Tempo、Arc 和 Visa，并回应十个反对意见。"
tags: ["跨境支付","稳定币","区块链","电信","支付基础设施"]
publication: "LinkedIn"
external_url: ""
cover: "/images/uploads/cover_zh_cross-border-blockchain.png"
draft: false
---

## 一、论点

我曾多年基于电信协议标准搭建电信平台，之后在花旗中国做了将近八年跨境支付。看今天的稳定币支付网络，我总会想起一个电信业几十年前就解决了的问题，而且没有用共享账本。

我的论点是：现有的稳定币跨境支付企业和联盟方案（Partior、Kinexys、mBridge、Tempo、Arc，以及接入多条链的 Visa 等）都可以不用区块链。改用电信业已经验证了几十年的方式就能实现，也就是“事先共同制定的自动化协议，加上各方各自的账本，再加上中立的清算或共享数据库”。这样做更成熟、更高效，也更容易满足监管要求。

需要先说明一点：这里的替代技术指分布式数据库。分布式文件系统（HDFS、Ceph、IPFS 等）不支持事务，也无法保证余额更新的强一致，不能用作账本，只适合存放单据、报文归档和审计快照。

## 二、核心逻辑：把问题分成三层

区块链的支持者把三类不同性质的问题混在一起，都交给“共识”去解决。拆开来看：

- **业务层。**谁参与、各方有什么权利义务、出了争议怎么办？合适的解决方式：多边协议、监管规则、牌照。
- **操作层。**数据怎么写、怎么改、什么样的状态变化才合法？合适的解决方式：事先共同制定、由机器自动执行的协议。
- **存储层。**每一方的账怎么记得又快又可靠？合适的解决方式：成熟的分布式数据库。

现有方案的信任其实来自业务层：发行人可以冻结地址、负责赎回；储备资产受审计和监管；参与机构身份已知，并签有法律协议。信任既然已经由法律和机构提供，共识机制就是多余的成本。

## 三、电信业的做法：没有共享账本的全球协作

全球几百家运营商互不隶属，很多还是竞争对手，却能让电话跨网接通、手机国际漫游、费用定期准确结算。这套体系的主流做法里没有共享账本。

**1. 实时信令：用协议规定每一步操作 [1][2][5][6]。**七号信令（SS7，ITU-T Q.700 系列）和移动应用部分（MAP，3GPP TS 29.002）定义了漫游时的位置登记、鉴权、呼叫路由。Diameter（IETF RFC 6733）和 SIP（IETF RFC 3261）用于 4G/5G 和 IP 网络中的认证、计费控制和会话建立。所有状态变化都用状态机写进标准，跨运营商的交互在毫秒级自动完成，不需要人工干预。

**2. 各自记账：每家只管自己的账 [3][4]。**每家运营商根据 3GPP 计费标准（TS 32.240 规定计费架构，TS 32.298 规定话单字段），在自己的系统里生成话单（CDR）。没有任何一方能改写对方的账。

**3. 标准化对账与清算 [7][8][9]。**GSMA 的 TAP3 标准（TD.57）规定了漫游话单的交换格式，RAP 标准（TD.32）规定了退回、拒付和争议处理的流程。拜访地运营商把 TAP 文件发给清算中心，清算中心再转给用户的归属运营商；归属运营商按话单里的用量和漫游协议约定的费率付费。哪一方擅自改账，都会在对账时暴露。

**4. 业务协议：争议靠合同解决 [10]。**GSMA 的标准国际漫游协议（AA.12/AA.13）规定了各方的权利义务、计费、结算和争议处理。

**5. 需要共享数据时，交给中立方运营的数据库 [11]。**美国的携号转网，靠的是号码可携带管理中心（NPAC）。这是一个由中立第三方运营（目前是 iconectiv）、所有相互竞争的运营商共同使用的中心数据库。互相竞争的运营商共享一份关键数据，靠的是中立运营方和监管规则，不是区块链。

**6. 开放互通。**任何手机都能打给任何手机，任何邮箱都能发给任何邮箱，不需要中心运营方批准，靠的只是公开标准。

## 四、映射到跨境支付

- SS7/MAP/SIP 实时信令 → ISO 20022 实时支付报文和 API
- 运营商各自的计费系统 → 银行和支付机构各自的账本（分布式数据库）
- TAP/RAP 话单交换和争议流程 → 实时对账、退回和争议协议
- 漫游清算中心 → 清算机构和中立的连接枢纽，做净额结算
- NPAC 中立共享数据库 → 中立运营的共享名录、路由表、额度登记库
- GSMA 漫游协议 → 多边支付规则和协议

已经在落地的例证：

- **BIS 的 Nexus 项目 [14][15][16]。**目标是以标准化的方式连接多个国家的即时支付系统，提升跨境支付的速度、成本、透明度和可得性，多数情况下可以在 60 秒内从付款人到达收款人。它采用 ISO 20022 标准和专门设计的 API。运营机构 Nexus Global Payments 是 2025 年 3 月成立的非营利组织，创始伙伴是印度、马来西亚、菲律宾、新加坡和泰国的央行和即时支付系统运营方。技术运营方由 PayNet 与 NETS 的合资公司担任，与 AWS 和 Endava 合作完成平台设计和开发，2026 年初开始开发，目标 2027 年上线。整个方案没有用区块链，几乎就是电信漫游模式在支付领域的翻版。
- **Interledger 协议（ILP）[17]。**由当时在 Ripple 工作的 Stefan Thomas 和 Evan Schwartz 提出。论文指出，这个协议不需要全局协调系统，也不需要区块链，安全机制借鉴了两阶段提交协议。它用条件锁定和超时规则，在互不相通的账本之间完成原子化的价值转移，相当于支付领域的“信令协议”。
- **巴西 Pix 和印度 UPI。**都运行在传统数据库架构上，全天候实时运行，规模远超目前任何一条链。

## 五、逐一检视现有方案

- **Partior（银行联盟）[20][21]。**在技术上是基于 ConsenSys Quorum 的许可账本，由 Partior Pte Ltd 运营，没有公开代币，结算的是商业银行货币。参与者都是持牌银行，又有专门的运营公司，这正是“中立运营方加多方协议”的结构。区块链在这里只是实现方式，可以替换。
- **Tempo、Arc（支付专用公链）[23]。**Tempo 由 Stripe 和 Paradigm 共同孵化，Arc 由 Circle 推出。2026 年 4 月，Visa 与 Stripe、Zodia Custody 一起成为 Tempo 的早期验证节点，MoneyGram 于 5 月加入。几家有名有姓的机构轮流记账，本质上就是联盟数据库。
- **Visa 的多链策略 [24][25]。**2026 年 4 月，Visa 把稳定币结算试点扩展到九条链，包括 Tempo 和 Arc。它的结算流程是：收到 USDC 后更新内部账本，再给收单行记账。链只承担结算这一段，核心账务仍在 Visa 自己的系统里。九条链可以随时互换，正说明链只是管道，价值不在链本身。
- **公链上的 USDT 和 USDC。**发行人可以冻结地址、决定赎回，信任锚定在发行人和监管上。机构之间的跨境流转，完全可以在发行人账本加标准协议的模式下完成。

## 六、反方可能的观点与回应

**1. “区块链防篡改，不需要信任任何一方。”**电信模式同样不需要信任对方。各方各记各的账，状态变化由协议规定，任何不一致都会在实时校验或对账时暴露，必要时再加上哈希链式的只追加日志供各方独立核验。何况现有方案本来就建立在对发行人和持牌机构的信任上，“去信任”在这里是个伪命题。

**2. “区块链没有单一运营者，能回避‘谁说了算’的治理难题。”**区块链同样要回答谁写代码、谁决定升级、谁能当验证节点、出了漏洞谁来修、要不要分叉。Tempo 由 Stripe 和 Paradigm 孵化，Arc 由 Circle 推出，mBridge 的各国央行同样要谈规则和准入。治理问题两边一样，区块链没有消除它，只是把它藏进了代码和基金会里。电信业用 GSMA、3GPP 加中立运营方，已经把这个问题处理了几十年。

**3. “区块链保证单方不能改写历史，这是权限设计上的优势。”**各方之间是什么关系，属于业务问题；数据怎么写、怎么改，属于操作问题。操作问题可以用事先共同制定的自动化协议解决：只有协议允许的状态变化才会被执行，双方系统各自校验。电信运营商之间从来不需要“共同改写同一本账”，各自的账本只接受符合协议的报文。

**4. “钱和电话不一样，必须防止双花，还要保证结算的最终性。”**这是协议设计问题，已经有成熟方案：先锁定、再确认、后提交（与两阶段提交思路相同）；ILP 那样的条件支付加超时回滚；最终结算用央行货币完成，或用事先存入的保证金、授信额度兜底。分布式数据库的事务一旦提交就是最终的，不像部分公链那样只有概率上的最终性。

**5. “区块链能 7×24 运行，传统系统有营业时间。”**营业时间是运营安排和流动性安排的问题，与账本技术无关。UPI、Pix 和电信网络都全天候运行。Partior 也在和 LSEG DiSH 合作解决非营业时间的结算流动性 [22]，说明 7×24 的难点在流动性，不在链。

**6. “智能合约提供可编程货币。”**条件支付、分账、托管释放，都可以用存储过程、工作流引擎、规则引擎实现。更好的做法是像电信信令那样，把常用的条件支付写进标准协议。这样各方实现一致，也更容易审计，避免智能合约漏洞造成的损失。

**7. “公链开放接入、可以自由组合，数据库做不到。”**开放互通靠的是公开标准，不是共享账本。全球电话网和电子邮件都是开放互通的，没有统一的账本，也不需要某个中心批准。只要接口和报文标准公开（ISO 20022 加开放 API），任何持牌机构都可以接入并组合服务。

**8. “Visa、Stripe、MoneyGram、Western Union 都在加码区块链，市场已经给出了答案。”**要分清它们看重的是什么。Visa 同时接入九条链并且可以互换，说明它看重的是稳定币作为结算资产的流动性和分发渠道，而不是哪种共识机制。融资叙事、抢占标准话语权、监管试点窗口，都是商业动机，不能证明区块链是技术上的最优解。反面的例子是澳大利亚证券交易所（ASX）[18][19]：它基于区块链的 CHESS 替换项目做了约七年，2022 年宣布放弃，税前核销 2.45 亿至 2.55 亿澳元；新方案改用塔塔咨询服务公司（TCS）的平台，第一阶段（清算）已于 2026 年 4 月上线。BIS 推动的 Nexus 也选择了不用区块链的路线。

**9. “这不就回到了慢的代理行模式吗？”**代理行慢，是因为批量报文、人工合规审查、多层中转和营业时间，不是因为各自记账。电信的关键在于实时信令：协议自动执行，毫秒级确认。跨境支付需要借鉴的正是这一点，而不是批量对账。

**10. “GSMA 自己都建了区块链网络来做漫游结算。”[12][13]**确实如此。2021 年，GSMA 宣布全行业的私有许可区块链网络“GSMA eBusiness Network”可以商用。但要看清三点：第一，这是私有许可链，参与者都是已知的运营商，正属于本文认为可以换成“协议加数据库”的那一类。第二，GSMA 的主要改进是 BCE 规范（Billing and Charging Evolution，计费结算演进）。它与 TAP 不同，改为交换汇总数据，交换频率和结算周期也更灵活。这是流程和协议层面的改进，本身不依赖区块链。第三，GSMA 自己也承认，目前大多数漫游清算结算仍然基于 TAP 规范；运营商的反馈也是 TAP 和区块链/BCE 会长期并存，并非所有运营商都会提早采用。可见即使在电信业，区块链也只是可选的实现方式之一，替代不了标准协议。

## 七、边界：区块链唯一不可替代的地方

区块链真正无法被协议模式替代的只有一点：无记名的个人自托管。任何人可以不在任何持牌机构开户，就自己持有美元价值，并直接转给别人。协议模式的两端总是机构，所以做不到这一点。

但这恰恰不是这些企业和联盟方案要解决的问题。它们服务的是机构之间的跨境资金流转，并且都在主动满足 KYC/AML 和冻结名单的监管要求。无记名自托管是另一个政策议题，与机构间跨境支付的效率无关。

## 八、结论

机构之间的跨境支付，可以完全按电信模式重构：业务层用多边协议，操作层用事先共同制定的自动化协议，存储层用成熟的分布式数据库，必要的共享数据交给中立运营方。这套架构有几十年的工程积累，性能、隐私、数据主权、合规适配都优于区块链。

现有稳定币跨境方案里的区块链，承担的是“结算资产的载体”和“分发渠道”的角色。这两个角色，用发行人账本加标准协议同样可以承担。

你认为在机构间支付里，哪个场景真正非共享账本不可？欢迎留言给出最有力的反例。

## 参考资料

**电信标准与实践**

1. [ITU-T Q.700，七号信令系统概述](https://www.itu.int/rec/T-REC-Q.700-199303-I/en)
2. [3GPP TS 29.002（MAP）](https://www.3gpp.org/dynareport/29002.htm)
3. [3GPP TS 32.240（计费架构与原则）](https://www.3gpp.org/dynareport/32240.htm)
4. [3GPP TS 32.298（话单字段说明）](https://www.3gpp.org/dynareport/32298.htm)
5. [IETF RFC 6733（Diameter）](https://www.rfc-editor.org/rfc/rfc6733)
6. [IETF RFC 3261（SIP）](https://www.rfc-editor.org/rfc/rfc3261)
7. [GSMA 开放标准页面（TD.57 TAP3、TD.58、TD.32 RAP）](https://www.gsma.com/about-us/open-standards-specifications/)
8. [GSMA TD.58 TAP3.12 实施手册（2026 年 9 月版）](https://www.gsma.com/get-involved/working-groups/wp-content/uploads/2026/09/TD.58-TAP3.12.pdf)
9. [GSMA《国际漫游详解》](https://www.gsma.com/publicpolicy/wp-content/uploads/2012/09/Africa-International-roaming-explained-English.pdf)
10. [引用 AA.12/AA.13 的运营商公开协议示例（Wind Hellas）](https://www.wind.gr/files/1/Etaireia/PDFs/2012%2011%20DIRECT%20WHOLESALE%20ROAMING%20ACCESS%20REFERENCE%20OFFER_final%20version_02_2013.pdf)
11. [美国携号转网中心 NPAC（iconectiv 运营）](https://iconectiv.com/NPAC)；[常见问题](https://numberportability.com/general)
12. [GSMA eBusiness Network 区块链网络（Light Reading）](https://www.lightreading.com/ai-machine-learning/gsma-announces-blockchain-network-for-roaming-and-settlement)
13. [GSMA 关于 TAP、BCE 与区块链的博客](https://www.gsma.com/solutions-and-impact/industry-services/?p=4849)

**支付相关**

14. [BIS Nexus 项目页](https://www.bis.org/project/nexus)
15. [Nexus Global Payments 任命技术运营方（Business Wire）](https://www.businesswire.com/news/home/20260209818123/en/Nexus-Global-Payments-Appoints-Technical-Operator)
16. [Nexus 采用 ISO 20022 与 API（Payments Industry Intelligence）](https://paymentsindustryintelligence.com/?p=56050)
17. [Interledger 白皮书](https://interledger.org/interledger.pdf)；[协议规范最新版](https://interledger.org/developers/rfcs/interledger-protocol/)
18. [ASX 放弃区块链项目（Finextra）](https://finextra.com/newsarticle/41337/asx-takes-a250m-hit-after-scrapping-dlt-based-chess-replacement-project)
19. [ASX 改用 TCS 平台（ShareCafe）](https://www.sharecafe.com.au/?p=173794)；[第一阶段上线（btw.media）](https://btw.media/en/asx-chess-replacement-market-infrastructure-assurance-accountability)
20. [Partior 技术架构](https://wiki.private.law/en/partior)
21. [Partior 的运营与定位（Eco）](https://eco.com/support/en/articles/17272672-what-is-partior-bank-owned-settlement-network)
22. [Partior 与 LSEG DiSH 合作（Payment Expert）](https://paymentexpert.com/2026/09/17/partior-lseg-dish-247-settlement/)
23. [Stripe、Visa、Zodia 成为 Tempo 验证节点（Tempo）](https://tempo.xyz/blog/stripe-visa-zodia-join-as-validators/)；[MoneyGram 加入（Cointelegraph）](https://cointelegraph.com/news/moneygram-joins-tempo-validator-network-as-stablecoin-settlement-push-expands)
24. [Visa 新闻稿（2026 年 4 月 29 日）](https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-expands-stablecoin-settlement-adds-five-blockchains.html)；[AMBCrypto](https://ambcrypto.com/viable-complement-visa-expands-stablecoin-rails-as-demand-grows-50/)
25. [Visa 的 USDC 结算流程（BlockEden）](https://blockeden.xyz/blog/2026/02/28/visa-mastercard-stablecoin-settlement-rails/)
