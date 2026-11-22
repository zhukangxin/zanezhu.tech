---
title: "Where Blockchain Earns Its Place: Answers to Eight Objections (Part 2)"
date: 2026-11-19
description: "Last time I argued that blockchain is likely to be unbundled into layers, as databases were. This issue tests that view against the eight strongest objections: trust, redundancy, evolution, adoption, programmability, network effects, censorship resistance and monolithic scaling."
tags: ["Blockchain","Stablecoins","Cross-border payments","Trust","Security"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_en_blockchain-counterarguments.png"
draft: false
---

[Last time](/articles/blockchain-as-file-system/) I argued that a blockchain is, at heart, a log file system that ties data and code together, and that, like the file systems of the 1960s, it is likely to be unbundled into layers [1].

Not everyone will agree, and some objections show where blockchain does earn its place. In this issue I list the eight strongest objections I can think of and answer each one. The first two matter most, so I spend more time on them.

## Objection 1: "The point of blockchain is that you don't have to trust anyone"

**The argument:** A database always has an operator who can change data, freeze accounts or shut the system down. A blockchain has no operator, so no one can control it.

**My view:** Blockchain doesn't remove the operator. It replaces the operator with builders. And when builders fail, it is harder to notice and harder to hold anyone accountable.

**Who are the builders?** Behind every "decentralized" chain is a group of people with real power: core developers who write the code and decide when to upgrade; miners and validators who decide which transactions get in; foundations that control funding and the roadmap; whoever holds the keys to bridges and multisig wallets; the companies that build wallets and front-end interfaces; and stablecoin issuers. Law professor Angela Walch pointed out years ago that these people act much like fiduciaries: they hold power, but no one holds them to account [2].

**Why is it harder to notice?** Four real examples.

The first is Zcash. In 2018 one of its cryptographers found a bug that would have let anyone create unlimited coins out of thin air, and because of the system's privacy design, no outsider could have seen it happen. Four insiders fixed it quietly and disclosed it almost a year later. The team admitted it could not be completely sure the bug had never been used [3]. Only a handful of insiders could find, exploit or fix it. Had they chosen to cheat, the ledger would have shown nothing unusual.

The second is the Ronin bridge. In 2022, four of its nine validators were run by the same company. Attackers got hold of five keys, moved out about US$600 million, and the theft went unnoticed for six days [4].

The third is Bybit. In 2025 the exchange lost about US$1.5 billion after a developer's computer at its wallet provider was hacked and malicious code was slipped into the web front end [5].

The last two were outside attacks, not builders cheating. But they show the same thing: the builder layer is concentrated, opaque, and the weakest point in the system. The blockchain recorded the attackers' transactions as perfectly valid, word for word, forever.

The fourth is censorship. After the U.S. sanctioned Tornado Cash in 2022, about 80% of Ethereum blocks were at one point being built by relays that filtered out related transactions [6]. Whether your transaction gets on-chain was being decided by a few companies, and most users had no idea.

**Who do you call when things go wrong?** When a bank fails you, there are licenses, regulators, auditors and courts. When a blockchain fails you, "code is law" usually shifts the blame to the user. Yet when losses are big enough, builders can rewrite the ledger with a hard fork, as they did after The DAO. Who can change the rules, and when, has never been written down.

**To be fair:** once a transaction is on-chain, the money trail is public and traceable, which is why stolen funds can be followed. The accurate statement is: **blockchain is more transparent at the transaction layer and less transparent at the builder layer.** And the biggest risks in payments sit at the builder layer: code, keys, upgrades, front ends and issuers.

I also accept that getting strangers to agree is blockchain's real contribution. But that capability can stand on its own. Transparency logs [7] and mathematical proofs [8] also make records publicly verifiable.

**One last point on stablecoins:** the U.S. GENIUS Act requires stablecoin issuers to be technically able to freeze and seize tokens when the law requires it [9]. So stablecoin users must trust both the issuer and the builders. That is two layers of trust, not zero.

## Objection 2: "Full replication is deliberate. It is where the security comes from"

**The argument:** Every machine keeps a full copy of the ledger. It's slow, but it's safe, and slowness is the price of safety.

**My view:** That price keeps rising, and sooner or later it stops being worth paying. And replication is only one security tool, and not the most cost-effective one.

**Why does the price keep rising?** Three bills.

The first is history. The ledger only grows, and every new node must download and verify all of it. Bitcoin's ledger is now about 768 GB and grows by 60 to 80 GB a year [10]. Disks are cheap, but "keep it forever, everyone keeps a copy, every newcomer replays it" doesn't get cheaper over time.

The second is the security bill. A database's security cost is mostly a one-time build plus ongoing operations. Bitcoin's security is paid for block by block, to miners, forever. The block subsidy halves every four years, and fees were supposed to take over. But a Cambridge report from October 2026 found that fees made up only 0.67% of miner revenue over the previous 90 days and have rarely exceeded 5% since 2010, while block production is becoming more concentrated [11]. The model of paying for a feeling of security has not yet found a sustainable source of income.

The third is the number of copies. In theory, tolerating f bad actors takes only 3f+1 copies [12]. Tens of thousands of machines each holding the full ledger is far more than security requires.

**Even Ethereum has stopped doing it.** In July 2025, all Ethereum clients began supporting deletion of history from before 2022, saving each node 300 to 500 GB [13]. In December 2025, Ethereum launched PeerDAS, which uses erasure coding (the same idea behind RAID disk arrays) to split data so each node keeps only part of it. No single node has to store everything anymore [14]. Distributed storage has used this technique for decades.

**Security is more than copies.** Security covers at least three things: confidentiality, integrity and availability. Full replication helps with the last two and does nothing for confidentiality, since the ledger is public. Even integrity doesn't need tens of thousands of copies; hash chains plus digital signatures are enough, which is exactly how database ledger tables work [15]. Banks rely on a whole set of measures: access control, separation of duties, auditing, hardware key management, off-site disaster recovery and external audits.

**Replication didn't stop the big losses.** Ronin and Bybit together cost more than US$2 billion, and both happened at the keys, front end and bridge level. Not one word of the ledger was altered. Tens of thousands of copies did nothing against these risks.

**"But Bitcoin has pruned nodes that don't keep full history."** Pruning has two limits. First, a pruned node joining the network still has to download and verify the entire history before deleting the old parts, so it saves disk, not time or bandwidth. Second, a pruned node can only serve roughly the last two days of blocks to others [16]; full history still depends on a small number of archive nodes. Pruning just shifts the cost from everyone to a few. Databases have long had the same split, with hot data online and history archived, but with a clear owner and audits. Blockchain reinvented that split in a way no one is responsible for.

## Objection 3: "Blockchain is evolving, not being displaced"

**My view:** That is my prediction in different words. From moving execution to layer 2 in 2020 [17] to verifying proofs on the main chain in 2026 [18], Ethereum's direction has always been to separate execution from verification. Follow that path and the "chain" ends up as an ordering log. Whether we still call it a blockchain is just a question of naming.

## Objection 4: "Stablecoin usage keeps growing, so blockchain must be useful"

**My view:** The demand is real, but what people want is access to dollars, 24/7 settlement and low fees, not blockchain itself. The BIS finds that stablecoins fall short as money [19], and that public chains face scalability problems [20]. Instant payment systems already settle around the clock, and the BIS Nexus project is linking them across borders [21], much as telecom networks were once interconnected.

## Objection 5: "Programmable, composable smart contracts made DeFi possible"

**My view:** Composability is tight coupling, and there is a long record of attacks that exploit it [22]. Programmable money can also be built with APIs, ISO 20022 messages, or "unified ledgers" run jointly by banks [23], and more safely.

## Objection 6: "Bitcoin has survived fifteen years; its value is as money"

**My view:** Agreed, but that isn't my question. I'm talking about how payment and data systems should be designed, not predicting any coin's price.

## Objection 7: "Censorship resistance matters to people living under capital controls"

**My view:** That is a legitimate need, and it falls exactly in the narrow space where blockchain truly fits [24]. It supports my point that blockchain's scope is narrow. And regulated stablecoins can already be frozen [9], so they have given up censorship resistance anyway.

## Objection 8: "Chains like Solana are already fast"

**My view:** These chains get faster mainly by raising hardware requirements for nodes, trading many machines for fewer, more powerful ones. That looks more and more like a controlled database cluster, and it weakens the very decentralization they emphasize. As for Ethereum's new direction [18], its core is verifying proofs on the main chain, which is itself a way of separating execution from verification.

## Closing thought

Put the eight answers together and they come down to three points:

- Blockchain doesn't remove trust. It hands trust to people who are harder to hold accountable.
- The cost of full replication only grows, and even Ethereum is looking for ways to store less.
- Every step blockchain takes to scale is a step toward taking itself apart.

These three points support the conclusion of [Part 1](/articles/blockchain-as-file-system/). They do not say blockchain is useless. They say it is a specialized tool: worth its cost where parties share no common operator and need public verifiability, and usually not worth it inside regulated institutional networks.

If you have an objection that isn't on this list, please write to me. You'll find my contact details on the About page.

**Further reading:**

- [Cross-Border Payments Without a Shared Ledger: What Telecom Already Solved](/articles/cross-border-payments-dont-need-blockchain/) (which answers ten further objections)
- [When Do You Actually Need a Blockchain? Lessons from mBridge](/articles/blockchain-boundaries-mbridge/) (which discusses vendor risk)

## References

1. [Zane Zhu, "Blockchain Is an Old Problem (Part 1)"](/articles/blockchain-as-file-system/)
2. [A. Walch, In Code(rs) We Trust: Software Developers as Fiduciaries in Public Blockchains (2019)](https://papers.ssrn.com/abstract=3203198)
3. [Zcash discloses vulnerability that could have allowed "infinite counterfeit" cryptocurrency (Fortune, 2019)](https://fortune.com/2019/02/05/zcash-vulnerability-cryptocurrency)
4. [Back to Building: Ronin Security Breach Postmortem (Ronin, 2022)](https://roninchain.com/blog/posts/back-to-building-ronin-security-breach-6513cc78a5edc1001b03c364)
5. [Lazarus hacked Bybit via breached Safe{Wallet} developer machine (BleepingComputer, 2025)](https://www.bleepingcomputer.com/news/security/lazarus-hacked-bybit-via-a-breached-safe-wallet-developer-machine/)
6. [Ethereum's OFAC-compliant blocks fall to 27% (The Block, 2023)](https://www.theblock.co/post/230179/ethereums-ofac-compliant-blocks-fall-to-27-marking-a-drop-in-protocol-level-censorship)
7. [IETF RFC 6962: Certificate Transparency](https://www.rfc-editor.org/rfc/rfc6962)
8. [E. Ben-Sasson et al., the STARK paper (2018)](https://eprint.iacr.org/2018/046)
9. [GENIUS Act, Public Law 119-27 (2025)](https://www.congress.gov/119/plaws/publ27/PLAW-119publ27.htm)
10. [Bitcoin blockchain size (YCharts)](https://ycharts.com/indicators/bitcoin_blockchain_size)
11. [Cambridge Centre for Alternative Finance, Funding Bitcoin's Future (2026)](https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/publications/funding-bitcoins-future-paying-for-security-as-the-block-subsidy-fades/)
12. [M. Castro & B. Liskov, Practical Byzantine Fault Tolerance (OSDI 1999)](https://pmg.csail.mit.edu/papers/osdi99.pdf)
13. [Partial history expiry announcement (Ethereum Foundation, 2025)](https://blog.ethereum.org/2025/07/08/partial-history-exp)
14. [PeerDAS (ethereum.org)](https://ethereum.org/en/roadmap/fusaka/peerdas/)
15. P. Antonopoulos et al., "SQL Ledger: Cryptographically Verifiable Data in Azure SQL Database," SIGMOD 2021.
16. [BIP 159: NODE_NETWORK_LIMITED](https://github.com/bitcoin/bips/blob/master/bip-0159.mediawiki)
17. [V. Buterin, A Rollup-Centric Ethereum Roadmap (2020)](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698)
18. [Vitalik Buterin reevaluates Ethereum's rollup-centric roadmap (The Block, 2026)](https://www.theblock.co/post/388285/vitalik-buterin-reevaluates-rollup-centric-roadmap-arguing-l2s-decentralized-far-slower-while-ethereum-base-layer-advanced)
19. [BIS Annual Economic Report 2025, Chapter III](https://www.bis.org/publ/arpdf/ar2025e3.htm)
20. [BIS Annual Economic Report 2026, Chapter III](https://www.bis.org/publications/aer-2026/anchoring-trust-money)
21. [BIS Project Nexus](https://www.bis.org/project/nexus)
22. [N. Atzei et al., A Survey of Attacks on Ethereum Smart Contracts (POST 2017)](https://eprint.iacr.org/2016/1007)
23. BIS Annual Economic Report 2023, Chapter III: Blueprint for the future monetary system.
24. [K. Wüst & A. Gervais, Do You Need a Blockchain? (CVCBT 2018)](https://eprint.iacr.org/2017/375)
