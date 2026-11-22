---
title: "从数据库发展史看区块链（上）：数据和程序绑在一起的代价"
date: 2026-11-19
description: "从数据库发展史看区块链：数据和程序绑死的设计，行业已经淘汰过两次。区块链本质上是一个专用的、紧耦合的日志文件，智能合约就是跑在日志上的存储过程。我的判断是：它会像数据库一样走向分层，共享账本留在真正需要它的地方。"
tags: ["区块链","数据库","智能合约","稳定币","跨境支付"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_zh_blockchain-as-file-system.png"
draft: false
---

科技圈每隔几年就会出现一个“这次不一样”的技术，区块链就是其中之一。

但我越研究稳定币和跨境支付，越觉得区块链一点也不新。如果你经历过数据库的发展史，会发现区块链面对的设计取舍，计算机行业五十年前遇到过一次，三十年前又遇到过一次。两次的解法都一样：分层。

**本期要点：**

- 区块链本质上是一本“所有人共用、只能往后写的账本”，再把程序直接挂在账本上；
- 这种“数据和程序绑死”的设计，行业已经淘汰过两次；
- 我的判断是：区块链很可能走同样的路，逐步分层，共享账本留在真正需要它的地方。

这一期讲我的论证。[下期](/zh/articles/blockchain-counterarguments/)专门回应八个常见的反驳 [1]。

## 一、先讲个老故事：文件时代

六十年代的企业系统，每个程序都有自己的数据文件，文件长什么样、怎么读写，全写在程序里。

这样做很快就出了问题。同一个客户的地址，工资系统存一份，销售系统存一份，发货系统又存一份，改了一处，另外两处不会跟着变。文件里多加一个字段，所有读这个文件的程序都得重写。想出一张新报表，就得再写一个新程序。

一句话总结：**数据和程序绑在一起，系统越大越难改。**

## 二、关系数据库为什么赢了

1970 年，IBM 的 Codd 提出了关系模型 [2]。核心思想很简单：**你只说要什么数据，不用管数据怎么存、怎么取。**

这就是“数据独立性”。存储方式可以随便换，应用程序不用改；想查什么，写一句 SQL 就行。

有个细节后面会用到：数据库内部其实也有一本“流水账”（日志），每笔修改都先记在里面。但这本账是藏起来的，用户看不到，系统还会定期清理旧的部分。

早期的关系数据库其实比老系统慢。它能赢，靠的不是速度，而是“改起来便宜”。速度后来慢慢追上了。

一句话总结：**把数据和程序拆开，系统才能长期演化。**

## 三、存储过程：逻辑放进数据库，后来又搬了出来

八十年代末，数据库开始支持“存储过程”和“触发器”，也就是把业务逻辑直接写进数据库里运行。当时网络慢，这样做能少传几次数据，规则也能集中管理，看起来很合理。

可是到了九十年代末，行业又开始把逻辑往外搬，从三层架构一路到后来的微服务。原因也不复杂：数据库是整个系统里最难扩容的一环，往里面塞计算，就是让最贵的资源干最多的活；数据库里的代码难测试、难调试，还会把你锁死在某个厂商身上；触发器在后台自动执行，出了问题很难查清楚是哪一步引起的。

最后，存储过程没有消失，但只留在审计、数据校验这类小角色上。

一句话总结：**把逻辑和数据绑在一起，行业已经试过一次，结果是又拆开了。**

## 四、把区块链拆开看

如果不谈币价，只把区块链当成一个数据系统，它由四样东西组成：

1. 一本只能往后写、每页都用哈希值连起来的账本。这个想法最早来自 1991 年的一种文档时间戳方案 [3]；
2. 每个节点都保存一份完整的账本；
3. 一套让互不信任的人对账本内容达成一致的规则，也就是“共识” [4]；
4. 用代币奖励维护账本的人。

问题在于，这四样被焊死成了一个整体。和数据库对比一下：

| | 数据库 | 区块链 |
|---|---|---|
| 流水账 | 藏在内部，可以清理 | 账本本身就是产品，永久保存，新节点要从头读一遍 |
| 改数据格式 | 改表结构就行 | 要“硬分叉”，全网一起升级 |
| 查询 | 写 SQL | 没有查询功能，得在链外另建一个数据库 |
| 扩容 | 加机器就加容量 | 每台机器存全部、算全部，加机器只是多一份备份 |
| 隐私 | 可以设权限，可以删除 | 默认全公开，删不掉 |

看出来了吗？文件时代的毛病全回来了。不同的链之间互不相通，就像当年各系统之间的文件格式不兼容；要在链之间转资产，就得靠“跨链桥”，相当于当年的格式转换程序。而跨链桥恰恰是被黑客盗得最多的地方：光是 2022 年，跨链桥就被盗了约 20 亿美元，占当年加密资产被盗总额的近七成 [5]。

一句话总结：**从数据管理的角度看，区块链就是一个“专用的、紧耦合的日志文件”。**

## 五、智能合约：跑在文件上的存储过程

智能合约和存储过程很像：代码在账本旁边运行，由交易触发，和数据一起写入。

但它比存储过程的处境更糟。存储过程下面至少还有一个完整的数据库帮它把关，智能合约下面只有一棵存键值的树。合约部署后改不了，漏洞也就永远留在那里：2016 年 The DAO 被盗约 360 万 ETH，2017 年 Parity 钱包的漏洞冻结了约 51 万 ETH [6]。合约之间可以随意互相调用，听起来很灵活，其实就是紧耦合，很多攻击正是利用了这一点。

更关键的是，合约里的每一步计算都要全网所有节点重复执行一遍。当年把逻辑塞进数据库是“让最贵的资源干活”，现在是“让成千上万台机器同时干同一份活”。

一句话总结：**行业花了二十年把逻辑搬出数据库，智能合约又把它全搬了回去。**

## 六、证据：慢、窄，而且连自己人都在拆

**慢。** 比特币每秒大约处理 7 笔交易 [7]，以太坊主链每秒几十笔，而卡组织网络的设计容量是每秒几万笔。这不是优化一下就能解决的，因为“每台机器都做全部的事”这个设计本身就有上限。国际清算银行（BIS）在 2026 年的年报里也提到，稳定币所在的公链存在扩容难题 [8]。

**窄。** 有学者总结过 [9]：只有同时满足“多方都要写同一份数据、彼此不信任、又找不到大家都认可的第三方”这几个条件时，区块链才比数据库好用。大多数企业和支付场景都不满足。

**失败案例。** 马士基和 IBM 的区块链贸易平台 TradeLens 已经关停 [10]。澳大利亚证券交易所放弃了做了好几年的区块链结算系统，减记约 2.5 亿澳元 [11]，2026 年还因为当初对外宣称“进展顺利”被罚了 2050 万澳元 [12]。亚马逊的账本数据库 QLDB 也在 2025 年停止服务 [13]，而“防篡改”变成了普通数据库的一个功能，比如微软 Azure SQL 的账本表 [14]。

**自己人在拆。** 以太坊 2020 年提出把执行搬到“第二层” [15]；2026 年又调整路线，改为在主链上直接验证“证明” [16]。路线换了，方向却没变：把执行和验证分开，不再让每个节点都重算一遍。数据库当年拆分的过程，正在区块链内部重演。

## 七、我的判断，以及它的边界

我要说清楚：我的论点只针对“数据管理”这一面。区块链让互不认识的人达成共识，这是它真正的贡献。但我认为这个能力可以单独拿出来用，不必和存储、计算、查询绑在一起。

所以我的判断是：

- **不需要“无许可、去信任”的场景**（大多数企业内部系统和许多受监管的支付流程）：分层的普通数据系统通常是更简单的选择；
- **确实需要这一点的场景**（开放网络、没有共同运营方、需要公开可验证）：区块链会保有它的位置，并很可能瘦身为一层很薄的排序和结算层。

“那信任问题呢？”“冗余不就是为了安全吗？”这些反驳我都想过，[下期](/zh/articles/blockchain-counterarguments/)逐条回答 [1]。

## 八、不用区块链，用什么？

我看好下面五个方向。

1. **“算一次，大家验证”的证明技术。** 一个人负责计算并给出数学证明，其他人花几毫秒验证就够了，不用每个人都重算 [17]。这是最有可能承接区块链核心价值的技术。
2. **分布式数据库加防篡改账本。** 像 Google Spanner [18] 这样的数据库能做到全球一致、随时扩容，再加上账本表 [14]，定期把账本的“指纹”公开发布，第三方就能审计。对受监管的支付业务来说，这是最务实的方案。
3. **透明日志。** 我们每天上网用的 HTTPS 证书，背后就有一套“证书透明度”机制 [19]，用公开、可审计的日志防止证书被冒发，既不需要共识，也不需要代币。它证明了一件事：防篡改和公开可查，不一定非要用区块链。
4. **独立的日志系统。** 比如 Kafka [20]，把日志、数据、查询分开管理。大部分“需要留痕”的业务，用它就够了。
5. **支付专用的基础设施。** 包括各国的即时支付系统、ISO 20022 报文标准、BIS 的 Nexus 跨境互联项目 [21]，以及由央行和商业银行共同运营的“统一账本” [22]。这种统一账本更像一个多家机构共同维护的数据库，而不是公链。

## 写在最后

关系数据库赢了文件系统，不是因为文件不好，而是因为把东西拆开，系统才容易改、容易扩，也更值得信任。

所以，做稳定币和跨境支付，与其问“该用哪条链”，不如问：**我真正需要的是哪一种能力？能提供这种能力的、最便宜的组件是什么？**

[下期](/zh/articles/blockchain-counterarguments/)，我回应八个常见的反驳。

**延伸阅读：**

- [跨境支付不一定需要共享账本：电信的“协议加各自账本”模式能给稳定币方案什么启示](/zh/articles/cross-border-payments-dont-need-blockchain/)
- [什么时候真的需要区块链？从 mBridge 看分布式账本的适用边界](/zh/articles/blockchain-boundaries-mbridge/)
- [去中心化的区块链，为什么给跨境支付带来的是“中心化红利”](/zh/articles/blockchain-centralization-dividend/)

## 参考资料

1. [朱康辛：《区块链在哪里不可替代？我对八个反驳的回答（下）》](/zh/articles/blockchain-counterarguments/)
2. E. F. Codd, “A Relational Model of Data for Large Shared Data Banks,” *Communications of the ACM*, 13(6), 1970.
3. S. Haber & W. S. Stornetta, “How to Time-Stamp a Digital Document,” *Journal of Cryptology*, 3(2), 1991.
4. [S. Nakamoto, Bitcoin: A Peer-to-Peer Electronic Cash System（2008）](https://bitcoin.org/bitcoin.pdf)
5. [2022 年跨链桥被盗约 20 亿美元（Cointelegraph，引用 Chainalysis）](https://cointelegraph.com/news/2b-in-crypto-stolen-from-cross-chain-bridges-this-year-chainalysis)
6. [N. Atzei 等，以太坊智能合约攻击综述（POST 2017）](https://eprint.iacr.org/2016/1007)
7. K. Croman et al., “On Scaling Decentralized Blockchains,” FC 2016 Workshops.
8. [BIS 2026 年度经济报告第三章：Anchoring trust in money](https://www.bis.org/publications/aer-2026/anchoring-trust-money)
9. [K. Wüst & A. Gervais, Do You Need a Blockchain?（CVCBT 2018）](https://eprint.iacr.org/2017/375)
10. [马士基与 IBM 关停 TradeLens（Maersk，2022）](https://www.maersk.com/news/articles/2022/11/29/maersk-and-ibm-to-discontinue-tradelens)
11. [ASX 放弃区块链 CHESS 替换项目（iTnews，2022）](https://www.itnews.com.au/news/asx-axes-blockchain-based-core-replacement-587904)
12. [ASX 因项目进展误导市场被罚 2050 万澳元（iTnews，2026）](https://www.itnews.com.au/news/asx-faces-205m-penalty-for-failed-blockchain-based-system-replacement-626625)
13. [AWS 终止 QLDB（InfoQ，2024）](https://www.infoq.com/news/2024/07/aws-kill-qldb)
14. P. Antonopoulos et al., “SQL Ledger: Cryptographically Verifiable Data in Azure SQL Database,” SIGMOD 2021.
15. [V. Buterin, A Rollup-Centric Ethereum Roadmap（2020）](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698)
16. [Buterin 调整以 Rollup 为中心的路线（The Block，2026）](https://www.theblock.co/post/388285/vitalik-buterin-reevaluates-rollup-centric-roadmap-arguing-l2s-decentralized-far-slower-while-ethereum-base-layer-advanced)
17. [E. Ben-Sasson 等，STARK 论文（2018）](https://eprint.iacr.org/2018/046)
18. J. C. Corbett et al., “Spanner: Google's Globally-Distributed Database,” OSDI 2012.
19. [IETF RFC 6962：Certificate Transparency](https://www.rfc-editor.org/rfc/rfc6962)
20. J. Kreps, “The Log: What Every Software Engineer Should Know About Real-Time Data's Unifying Abstraction,” LinkedIn Engineering, 2013.
21. [BIS Nexus 项目页](https://www.bis.org/project/nexus)
22. BIS 2023 年度经济报告第三章：Blueprint for the future monetary system.
