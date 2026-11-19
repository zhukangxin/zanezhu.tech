---
title: "区块链真的不可替代吗？我对八个反驳的回答（下）"
date: 2026-11-19
description: "上期我说区块链会像文件系统一样被拆开、被替代。这期回应八个最有力的反驳：信任、冗余、进化、采用量、可编程性、网络效应、抗审查、单体链扩容。"
tags: ["区块链","稳定币","跨境支付","信任","安全"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_zh_blockchain-counterarguments.png"
draft: false
---

[上期](/zh/articles/blockchain-as-file-system/)我提出一个观点：区块链本质上是一个“数据和程序绑死”的日志文件系统，会像六十年代的文件系统一样被拆开、被替代 [1]。

这个观点肯定有人不同意。这一期，我把能想到的最有力的八个反驳列出来，逐条回答。前两条最重要，我多写一些。

## 反驳一：“区块链的价值在于不需要信任任何人”

**这个反驳是这么说的：** 数据库总有一个管理者，他可以改数据、封账户、关系统；区块链没有管理者，谁也控制不了。

**我的看法：** 区块链没有消除管理者，只是把“运营方”换成了“建设方”。而建设方出问题，比运营方更难发现，也更难追责。

**谁是建设方？** 一条“去中心化”的链背后，其实有一群握着实权的人：写代码、决定何时升级的核心开发者；决定哪些交易能上链的矿工和验证者；掌握资金和路线的基金会；管着跨链桥和多签钱包钥匙的人；做钱包、做前端界面的公司；还有稳定币的发行方。法学教授 Angela Walch 早就指出，这些人实际上扮演着“受托人”的角色，手里有权力，却没人追究他们的责任 [2]。

**为什么更难发现？** 我举四个真实的例子。

第一个是 Zcash。2018 年，它的密码学家发现了一个漏洞，可以无限制地凭空造币，而且因为系统的隐私设计，外人根本看不出来。四个内部人员悄悄修好了它，过了将近一年才公开，团队自己也承认无法完全确定漏洞有没有被人用过 [3]。能发现、能利用这个漏洞的，只有极少数内部人员。如果他们想作恶，账本上看不出任何痕迹。

第二个是 Ronin 跨链桥。2022 年，它的 9 个验证节点里有 4 个归同一家公司管。黑客拿到 5 把私钥，转走了约 6 亿美元，6 天后才被发现 [4]。

第三个是 Bybit。2025 年，这家交易所被盗约 15 亿美元，起因是一家钱包服务商的开发人员电脑被黑，网页前端被植入了恶意代码 [5]。

后两起是外部攻击，不是建设方自己作恶，但它们说明了同一件事：建设方这一环集中、不透明，是整个系统最薄弱的地方。区块链会把黑客发起的交易当作合法交易，一字不差、永久地记下来。

第四个是审查。2022 年美国制裁 Tornado Cash 之后，以太坊上一度有约 80% 的区块会自动过滤掉相关交易 [6]。决定“你的交易能不能上链”的，其实是少数几家公司，而大多数用户并不知道。

**出了事找谁？** 银行出问题，有牌照、有监管、有审计，还有法院可以找。区块链出问题，常常一句“代码即法律”，就把责任推给了用户。可是当损失足够大时，建设方又可以通过硬分叉把账本改掉，The DAO 事件就是这样。规则由谁来改、什么时候能改，从来没有写清楚。

**公平地说：** 交易一旦上链，资金流向确实是公开、可追踪的，所以黑客盗走的钱能被一路追查。准确的说法是：**区块链在交易层更透明，在建设层更不透明。** 而支付系统最大的风险，恰恰在建设层：代码、钥匙、升级、前端、发行方。

我也承认，让陌生人之间达成共识是区块链真正的贡献。但这个能力可以单独拿出来用，用透明日志 [7] 或数学证明 [8]，同样能做到公开可验证。

**最后说一句稳定币：** 美国的 GENIUS 法案要求稳定币发行方必须有能力按法律要求冻结、没收代币 [9]。也就是说，用稳定币的人既要信任发行方，又要信任建设方，是两层信任。

## 反驳二：“全网备份是故意的，这正是安全的来源”

**这个反驳是这么说的：** 每台机器都存一份完整账本，虽然慢，但很安全，慢是安全的代价。

**我的看法：** 这个代价会越来越贵，迟早会贵到不划算。而且备份只是安全措施的一种，还不是最划算的那一种。

**代价为什么越来越贵？** 有三笔账。

第一笔是历史数据。账本只增不减，每个新节点都要从头下载、从头验证一遍。比特币账本现在大约 768 GB，每年还在增加 60 到 80 GB [10]。硬盘确实便宜，但“永久保存、人人一份、新人重读一遍”这几件事，不会随着时间变便宜。

第二笔是安全费用。数据库的安全投入，主要是一次性建设加上日常维护；比特币的安全，靠的是每个区块都要付给矿工的报酬，永远停不下来。比特币的出块奖励每四年减半，原本设想由交易手续费接替。但剑桥大学 2026 年 10 月的报告显示，最近 90 天手续费只占矿工收入的 0.67%，2010 年以来很少超过 5%，同时出块越来越集中在少数矿池手里 [11]。为“安全感”付钱的这个模式，到现在还没找到可持续的收入来源。

第三笔是备份份数。理论上，要防住 f 个捣乱的节点，只需要 3f+1 份副本 [12]。让几万台机器各存一份全量账本，远远超过了安全所需。

**连以太坊自己都不这么做了。** 2025 年 7 月，以太坊的所有客户端都开始支持删除 2022 年以前的历史数据，每个节点能省下 300 到 500 GB [13]。同年 12 月，以太坊又上线了 PeerDAS，用一种叫“纠删编码”的技术（原理类似硬盘阵列 RAID）把数据切开、分散保存，每个节点只存一部分，不再要求谁都存全部 [14]。这项技术在分布式存储领域已经用了几十年。

**安全不只是备份。** 安全至少包括三件事：保密、不被篡改、随时可用。全网备份只管后两件，保密完全做不到，因为账本是公开的。就连防篡改，也用不着几万份备份，用哈希链加数字签名就够了，数据库的账本表就是这么做的 [15]。银行的安全靠的是一整套措施：权限控制、职责分离、审计、密钥硬件、异地灾备、外部审计。

**备份也没挡住真正的大案。** 前面提到的 Ronin 和 Bybit，加起来损失超过 20 亿美元，全都出在钥匙、前端、跨链桥这些环节，账本本身一个字都没被改过。几万份备份，对这类风险毫无作用。

**有人会说：“比特币有剪枝节点，不用存全部历史。”** 剪枝有两个问题。第一，剪枝节点加入网络时，照样要把全部历史下载下来、验证一遍，然后才删掉旧数据，省的只是硬盘，不省时间和带宽。第二，剪枝节点只能向别人提供最近两天左右的区块 [16]，完整的历史还是要靠少数“存档节点”来保存。所以剪枝只是把成本从“大家一起扛”变成了“少数人扛”。数据库早就有类似的分工，在线库放热数据，历史数据归档，而且有明确的负责人和审计。区块链则是用一种没人负责的方式，重新发明了这套分工。

## 反驳三：“区块链在进化，不是被取代”

**我的看法：** 这其实和我的预测是一回事，只是说法不同。以太坊从 2020 年把执行搬到第二层 [17]，到 2026 年改为在主链上验证证明 [18]，方向始终是把执行和验证分开。照这个方向走下去，“链”最后只剩一个负责排序的日志。到时候还叫不叫“区块链”，只是名字问题。

## 反驳四：“稳定币用的人越来越多，说明区块链有用”

**我的看法：** 需求是真的，但大家要的是“能用美元、全天候到账、费用低”，不是区块链本身。BIS 认为稳定币作为货币并不合格 [19]，而且公链存在扩容难题 [20]。全天候到账，即时支付系统早就能做到；BIS 的 Nexus 项目也在把各国的即时支付系统连起来 [21]，就像当年电信网络之间的互联互通。

## 反驳五：“智能合约能编程、能组合，带来了 DeFi 这样的创新”

**我的看法：** “能组合”说白了就是紧耦合，已经有大量攻击案例 [22]。可编程的钱，用 API、ISO 20022 报文，或者银行共同运营的“统一账本” [23] 一样能做到，而且更安全。

## 反驳六：“比特币活了十五年，价值在于货币属性”

**我的看法：** 同意，但这不是我讨论的问题。我谈的是支付和数据系统该怎么设计，不预测任何币的价格。

## 反驳七：“对资本管制地区的人来说，抗审查很重要”

**我的看法：** 这是正当的需求，而且正好是区块链真正适用的那个小范围 [24]。它说明的恰恰是“区块链适用范围很窄”。况且受监管的稳定币本身就可以冻结 [9]，早已放弃了抗审查。

## 反驳八：“Solana 这样的链也能做到很快”

**我的看法：** 这类链变快，主要靠提高节点的硬件门槛，用更少、更强的机器换速度。这其实越来越像一个“受控的数据库集群”，削弱的正是它最强调的去中心化。以太坊的新路线 [18] 核心是在主链上验证证明，这本身就是在拆分执行和验证。

## 写在最后

八条回答合在一起，其实就是三句话：

- 区块链没有消除信任，只是把信任交给了更难追责的人；
- 全网备份的成本只会越来越高，连以太坊都在想办法少存；
- 区块链为了扩容做的每一步，都是在把自己拆开。

这三点，正好支撑了[上期](/zh/articles/blockchain-as-file-system/)的判断。

如果你有不在这八条里的反驳，欢迎写信给我，联系方式在本站“关于”页面。

**延伸阅读：**

- [跨境支付不需要区块链：用电信的“协议加各自账本”模式重构稳定币方案](/zh/articles/cross-border-payments-dont-need-blockchain/)（文末回应了另外十个反对意见）
- [什么时候真的需要区块链？从 mBridge 看分布式账本的适用边界](/zh/articles/blockchain-boundaries-mbridge/)（其中讨论了承建商风险）

## 参考资料

1. [朱康辛：《区块链其实是个“老问题”（上）》](/zh/articles/blockchain-as-file-system/)
2. [A. Walch, In Code(rs) We Trust: Software Developers as Fiduciaries in Public Blockchains（2019）](https://papers.ssrn.com/abstract=3203198)
3. [Zcash 披露可无限伪造代币的漏洞（Fortune，2019）](https://fortune.com/2019/02/05/zcash-vulnerability-cryptocurrency)
4. [Ronin 安全事件复盘（Ronin，2022）](https://roninchain.com/blog/posts/back-to-building-ronin-security-breach-6513cc78a5edc1001b03c364)
5. [Lazarus 通过攻破 Safe{Wallet} 开发者电脑盗取 Bybit（BleepingComputer，2025）](https://www.bleepingcomputer.com/news/security/lazarus-hacked-bybit-via-a-breached-safe-wallet-developer-machine/)
6. [以太坊 OFAC 合规区块比例变化（The Block，2023）](https://www.theblock.co/post/230179/ethereums-ofac-compliant-blocks-fall-to-27-marking-a-drop-in-protocol-level-censorship)
7. [IETF RFC 6962：Certificate Transparency](https://www.rfc-editor.org/rfc/rfc6962)
8. [E. Ben-Sasson 等，STARK 论文（2018）](https://eprint.iacr.org/2018/046)
9. [GENIUS 法案全文（Public Law 119-27，2025）](https://www.congress.gov/119/plaws/publ27/PLAW-119publ27.htm)
10. [比特币账本大小（YCharts）](https://ycharts.com/indicators/bitcoin_blockchain_size)
11. [剑桥另类金融研究中心：Funding Bitcoin's Future（2026）](https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/publications/funding-bitcoins-future-paying-for-security-as-the-block-subsidy-fades/)
12. [M. Castro & B. Liskov, Practical Byzantine Fault Tolerance（OSDI 1999）](https://pmg.csail.mit.edu/papers/osdi99.pdf)
13. [以太坊部分历史过期公告（Ethereum Foundation，2025）](https://blog.ethereum.org/2025/07/08/partial-history-exp)
14. [PeerDAS 介绍（ethereum.org）](https://ethereum.org/en/roadmap/fusaka/peerdas/)
15. P. Antonopoulos et al., “SQL Ledger: Cryptographically Verifiable Data in Azure SQL Database,” SIGMOD 2021.
16. [BIP 159：NODE_NETWORK_LIMITED](https://github.com/bitcoin/bips/blob/master/bip-0159.mediawiki)
17. [V. Buterin, A Rollup-Centric Ethereum Roadmap（2020）](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698)
18. [Buterin 调整以 Rollup 为中心的路线（The Block，2026）](https://www.theblock.co/post/388285/vitalik-buterin-reevaluates-rollup-centric-roadmap-arguing-l2s-decentralized-far-slower-while-ethereum-base-layer-advanced)
19. [BIS 2025 年度经济报告第三章](https://www.bis.org/publ/arpdf/ar2025e3.htm)
20. [BIS 2026 年度经济报告第三章](https://www.bis.org/publications/aer-2026/anchoring-trust-money)
21. [BIS Nexus 项目页](https://www.bis.org/project/nexus)
22. [N. Atzei 等，以太坊智能合约攻击综述（POST 2017）](https://eprint.iacr.org/2016/1007)
23. BIS 2023 年度经济报告第三章：Blueprint for the future monetary system.
24. [K. Wüst & A. Gervais, Do You Need a Blockchain?（CVCBT 2018）](https://eprint.iacr.org/2017/375)
