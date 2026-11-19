---
title: "Blockchain Is an Old Problem (Part 1): Why It Will Be Replaced Like the File System"
date: 2026-11-19
description: "A look at blockchain through the history of databases. Tying data and code together is a design the industry has already abandoned twice. Blockchain is a special-purpose, tightly coupled log file, and smart contracts are stored procedures running on that file. It will be taken apart and replaced."
tags: ["Blockchain","Databases","Smart contracts","Stablecoins","Cross-border payments"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_en_blockchain-as-file-system.png"
draft: false
---

Every few years the tech world produces a technology that is supposed to be different this time. Blockchain is one of them.

But the more I study stablecoins and cross-border payments, the less new blockchain looks. If you know the history of databases, you will recognize its mistakes. The computer industry made them once fifty years ago, and again thirty years ago. Both times the outcome was the same.

**In this issue:**

- At its core, a blockchain is a shared, append-only ledger with programs attached directly to it.
- Tying data and code together is a design the industry has already abandoned twice.
- My view: blockchain will go the same way. It will be taken apart and replaced.

This issue makes the case. [Part 2](/articles/blockchain-counterarguments/) answers the eight strongest objections [1].

## 1. An old story: the file era

In the 1960s, every business program had its own data files. The file layout, and the code to read and write it, lived inside the program.

Problems showed up quickly. The same customer address sat in the payroll system, the sales system and the shipping system. Change one, and the other two did not follow. Add one field to a file, and every program that read it had to be rewritten. Every new report meant writing a new program.

The short version: **when data and code are tied together, the bigger the system, the harder it is to change.**

## 2. Why relational databases won

In 1970, Ted Codd at IBM proposed the relational model [2]. The core idea was simple: **say what data you want, and let the system worry about how it is stored and fetched.**

This is called data independence. You can change how data is stored without touching the applications. If you want to ask a new question, you write one line of SQL.

One detail matters later. A database also keeps a running log of every change. But that log is hidden. Users never see it, and the system regularly trims the old parts.

Early relational databases were actually slower than the systems they replaced. They won not on speed but because they were cheap to change. The speed caught up later.

The short version: **separate data from code, and a system can keep evolving.**

## 3. Stored procedures: logic moved into the database, then moved back out

In the late 1980s, databases began to support stored procedures and triggers, which let business logic run inside the database. Networks were slow then, so this saved round trips and kept rules in one place. It made sense.

By the late 1990s, the industry started moving that logic back out, first to three-tier architectures and later to microservices. The reasons were simple. The database is the hardest part of a system to scale, so putting computation there makes the most expensive resource do the most work. Code inside the database is hard to test and debug, and it locks you into one vendor. Triggers fire silently in the background, so when something breaks, it is hard to tell which step caused it.

Stored procedures did not disappear, but they shrank to small jobs like auditing and data checks.

The short version: **the industry already tried tying logic to data, and then took it apart again.**

## 4. Taking a blockchain apart

Set aside token prices and treat a blockchain as a data system. It has four parts:

1. A ledger you can only append to, with each page linked to the last by a hash. The idea goes back to a 1991 scheme for time-stamping documents [3].
2. Every node keeps a full copy of the ledger.
3. A set of rules that lets parties who don't trust each other agree on what the ledger says, known as consensus [4].
4. Tokens that reward the people who maintain the ledger.

The problem is that these four parts are welded into one. Compare it with a database:

| | Database | Blockchain |
|---|---|---|
| The log | Hidden inside, can be trimmed | The ledger is the product, kept forever; new nodes replay it from the start |
| Changing the data format | Alter the table | A hard fork, with the whole network upgrading together |
| Queries | Write SQL | No query feature; you build a separate database off-chain |
| Scaling | Add machines, add capacity | Every machine stores and computes everything; adding machines only adds copies |
| Privacy | Permissions, and data can be deleted | Public by default, nothing can be deleted |

See the pattern? The problems of the file era are back. Chains can't talk to each other, just as old systems couldn't read each other's file formats. Moving assets between chains requires a "bridge", which plays the role of the old format-conversion programs. Bridges are exactly where hackers have stolen the most: in 2022 alone, about US$2 billion was stolen from cross-chain bridges, close to 70% of all crypto stolen that year [5].

The short version: **from a data management point of view, a blockchain is a special-purpose, tightly coupled log file.**

## 5. Smart contracts: stored procedures running on a file

Smart contracts look a lot like stored procedures. The code runs next to the ledger, is triggered by transactions, and commits together with the data.

But smart contracts are in a worse position. A stored procedure at least has a full database underneath it. A smart contract has only a tree of keys and values. Once deployed, a contract can't be changed, so its bugs stay forever: The DAO lost about 3.6 million ETH in 2016, and a bug in the Parity wallet froze about 513,000 ETH in 2017 [6]. Contracts can call each other freely. That sounds flexible, but it is tight coupling, and many attacks exploit exactly that.

Worse, every step of a contract's computation is repeated by every node on the network. Putting logic in a database meant making the most expensive resource do the work. Smart contracts make thousands of machines do the same work at the same time.

The short version: **the industry spent twenty years moving logic out of the database, and smart contracts moved it all back in.**

## 6. The evidence: slow, narrow, and being taken apart from the inside

**Slow.** Bitcoin handles about 7 transactions per second [7] and Ethereum's main chain a few dozen, while card networks are built for tens of thousands. Tuning won't close that gap, because "every machine does everything" has a ceiling built in. The Bank for International Settlements (BIS) noted in its 2026 annual report that the public blockchains stablecoins run on face scalability challenges [8].

**Narrow.** Researchers have shown [9] that a blockchain beats a database only when several parties must write to the same data, they don't trust each other, and there is no third party they can all accept. Most business and payment use cases fail at least one of these tests.

**Failures.** Maersk and IBM shut down their blockchain trade platform, TradeLens [10]. The Australian Securities Exchange dropped its blockchain settlement project after years of work and wrote off about A$250 million [11]; in 2026 it was also fined A$20.5 million for having told the market the project was on track [12]. Amazon retired its ledger database, QLDB, in 2025 [13], while tamper-evidence became an ordinary database feature, such as ledger tables in Microsoft's Azure SQL [14].

**Taken apart from the inside.** In 2020, Ethereum proposed moving execution to "layer 2" [15]. In 2026 it changed course and moved toward verifying proofs directly on the main chain [16]. The route changed, but the direction didn't: separate execution from verification, so that not every node has to redo every computation. The way databases were taken apart is now playing out inside blockchain itself.

## 7. My view, and where it stops

To be clear, my argument covers only the data management side. Letting strangers reach agreement is blockchain's real contribution. But I think that capability can stand on its own. It doesn't need to be welded to storage, computation and queries.

So my view is:

- **Where permissionless, trustless operation isn't needed** (most businesses and all regulated payments): blockchain will be replaced by ordinary, decoupled data systems.
- **Where it truly is needed:** blockchain will be taken apart itself, until only a thin layer for ordering and settlement remains.

"What about trust?" "Isn't the redundancy there for security?" I've thought about these objections, and [Part 2](/articles/blockchain-counterarguments/) answers them one by one [1].

## 8. If not blockchain, then what?

Here are five directions I find promising.

1. **Compute once, verify everywhere.** One party does the computation and produces a mathematical proof; everyone else checks it in milliseconds instead of redoing it [17]. This is the technology most likely to replace blockchain's core value.
2. **Distributed databases with tamper-evident ledgers.** Databases like Google Spanner [18] offer global consistency and easy scaling. Add ledger tables [14], publish a fingerprint of the ledger regularly, and third parties can audit it. For regulated payments, this is the most practical option.
3. **Transparency logs.** The HTTPS certificates we use every day are protected by Certificate Transparency [19], a public, auditable log that stops certificates from being issued fraudulently. It needs no consensus and no token. It shows that tamper-evidence and public verifiability don't require a blockchain.
4. **Standalone log systems.** Kafka [20], for example, keeps the log, the data and the queries separate. For most businesses that need an audit trail, this is enough.
5. **Payment-specific infrastructure.** National instant payment systems, the ISO 20022 messaging standard, the BIS Nexus project for linking them across borders [21], and "unified ledgers" run jointly by central banks and commercial banks [22]. A unified ledger of this kind looks more like a database maintained by several institutions than a public chain.

## Closing thought

Relational databases didn't beat the file system because files were bad. They won because taking things apart makes a system easier to change, easier to scale, and easier to trust.

So for stablecoins and cross-border payments, the better question isn't "which chain should we use?" It is: **which capability do I actually need, and what is the cheapest component that provides it?**

In [Part 2](/articles/blockchain-counterarguments/), I answer eight common objections.

**Further reading:**

- [Cross-Border Payments Don't Need Blockchain: What Telecom Already Solved](/articles/cross-border-payments-dont-need-blockchain/)
- [When Do You Actually Need a Blockchain? Lessons from mBridge](/articles/blockchain-boundaries-mbridge/)
- [Why a Decentralized Technology Delivers a Centralization Dividend in Cross-border Payments](/articles/blockchain-centralization-dividend/)

## References

1. [Zane Zhu, "Is Blockchain Really Irreplaceable? Answers to Eight Objections (Part 2)"](/articles/blockchain-counterarguments/)
2. E. F. Codd, "A Relational Model of Data for Large Shared Data Banks," *Communications of the ACM*, 13(6), 1970.
3. S. Haber & W. S. Stornetta, "How to Time-Stamp a Digital Document," *Journal of Cryptology*, 3(2), 1991.
4. [S. Nakamoto, Bitcoin: A Peer-to-Peer Electronic Cash System (2008)](https://bitcoin.org/bitcoin.pdf)
5. [About $2B stolen from cross-chain bridges in 2022 (Cointelegraph, citing Chainalysis)](https://cointelegraph.com/news/2b-in-crypto-stolen-from-cross-chain-bridges-this-year-chainalysis)
6. [N. Atzei et al., A Survey of Attacks on Ethereum Smart Contracts (POST 2017)](https://eprint.iacr.org/2016/1007)
7. K. Croman et al., "On Scaling Decentralized Blockchains," FC 2016 Workshops.
8. [BIS Annual Economic Report 2026, Chapter III: Anchoring trust in money](https://www.bis.org/publications/aer-2026/anchoring-trust-money)
9. [K. Wüst & A. Gervais, Do You Need a Blockchain? (CVCBT 2018)](https://eprint.iacr.org/2017/375)
10. [Maersk and IBM to discontinue TradeLens (Maersk, 2022)](https://www.maersk.com/news/articles/2022/11/29/maersk-and-ibm-to-discontinue-tradelens)
11. [ASX axes blockchain-based core replacement (iTnews, 2022)](https://www.itnews.com.au/news/asx-axes-blockchain-based-core-replacement-587904)
12. [ASX faces $20.5m penalty for failed blockchain-based system replacement (iTnews, 2026)](https://www.itnews.com.au/news/asx-faces-205m-penalty-for-failed-blockchain-based-system-replacement-626625)
13. [AWS discontinues QLDB (InfoQ, 2024)](https://www.infoq.com/news/2024/07/aws-kill-qldb)
14. P. Antonopoulos et al., "SQL Ledger: Cryptographically Verifiable Data in Azure SQL Database," SIGMOD 2021.
15. [V. Buterin, A Rollup-Centric Ethereum Roadmap (2020)](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698)
16. [Vitalik Buterin reevaluates Ethereum's rollup-centric roadmap (The Block, 2026)](https://www.theblock.co/post/388285/vitalik-buterin-reevaluates-rollup-centric-roadmap-arguing-l2s-decentralized-far-slower-while-ethereum-base-layer-advanced)
17. [E. Ben-Sasson et al., the STARK paper (2018)](https://eprint.iacr.org/2018/046)
18. J. C. Corbett et al., "Spanner: Google's Globally-Distributed Database," OSDI 2012.
19. [IETF RFC 6962: Certificate Transparency](https://www.rfc-editor.org/rfc/rfc6962)
20. J. Kreps, "The Log: What Every Software Engineer Should Know About Real-Time Data's Unifying Abstraction," LinkedIn Engineering, 2013.
21. [BIS Project Nexus](https://www.bis.org/project/nexus)
22. BIS Annual Economic Report 2023, Chapter III: Blueprint for the future monetary system.
