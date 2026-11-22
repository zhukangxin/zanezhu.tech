---
title: "Cross-Border Payments Without a Shared Ledger: What Telecom Already Solved"
date: 2026-11-14
description: "An architecture comparison: today's institutional stablecoin and consortium settlement networks could also run on the telecom model: protocols agreed in advance, each party keeping its own ledger, and neutral clearing. A layer-by-layer case, a look at Partior, Tempo, Arc and Visa, and answers to ten objections."
tags: ["Cross-border payments","Stablecoins","Blockchain","Telecom","Payments infrastructure"]
publication: "LinkedIn"
external_url: ""
cover: "/images/uploads/cover_en_cross-border-blockchain.png"
draft: false
---

## The claim

I spent years building telecom platforms on telecommunication protocol standards, then nearly eight years on cross-border payments at Citi China. When I look at today's stablecoin payment networks, I keep seeing a problem telecom solved decades ago, without a shared ledger.

My claim is about architecture choice, not about whether these projects have merit. For institutional flows, today's stablecoin and consortium settlement networks, including Partior, Kinexys, mBridge, Tempo, Arc and multi-chain programs such as Visa's, could also be built without a shared blockchain ledger. Telecom has run a proven alternative for decades: protocols agreed in advance and executed by machines, each party keeping its own ledger, and a neutral clearinghouse or shared database where one is needed. For regulated institutional payments, that model is mature, efficient and easy to fit to regulation, so it deserves a place in every architecture review. Where blockchain does add something that model cannot, I say so at the end.

One clarification. The alternative I mean is a distributed database, not a distributed file system. File systems such as HDFS, Ceph or IPFS don't support transactions or strongly consistent balance updates, so they can't serve as a ledger. They are fine for documents, message archives and audit snapshots.

## Split the problem into three layers

Blockchain advocates bundle three different kinds of problems together and hand all of them to "consensus." Pulled apart, they look like this:

- **Business layer.** Who participates, what are their rights and duties, and how are disputes resolved? The right tool: multilateral agreements, regulation and licenses.
- **Operations layer.** How is data written and changed, and which state changes are valid? The right tool: protocols agreed in advance and executed automatically.
- **Storage layer.** How does each party keep its books fast and reliably? The right tool: mature distributed databases.

In today's solutions, trust actually comes from the business layer. Issuers can freeze addresses and stand behind redemption. Reserves are audited and regulated. Participants are known institutions bound by legal agreements. Once law and institutions provide the trust, a consensus mechanism is just extra cost.

## How telecom works: global cooperation without a shared ledger

Hundreds of independent operators, many of them competitors, connect calls across networks, support international roaming, and settle charges accurately every period. The mainstream model has no shared ledger. It rests on six pieces.

**1. Real-time signaling: protocols define every step [1][2][5][6].** SS7 (ITU-T Q.700 series) and MAP (3GPP TS 29.002) define location updates, authentication and call routing for roaming. Diameter (IETF RFC 6733) and SIP (IETF RFC 3261) handle authentication, charging control and session setup in 4G/5G and IP networks. Every state change is written into the standard as a state machine, so interactions between operators complete automatically in milliseconds, with no manual steps.

**2. Separate books: each operator keeps its own [3][4].** Each operator generates call detail records (CDRs) in its own systems under 3GPP charging standards (TS 32.240 for the architecture, TS 32.298 for record fields). No party can rewrite another party's books.

**3. Standard reconciliation and clearing [7][8][9].** GSMA's TAP3 standard (TD.57) defines how roaming records are exchanged, and RAP (TD.32) handles returns, rejections and disputes. The visited operator sends TAP files to a clearing house, which forwards them to the home operator. The home operator then pays based on the usage in the records and the rates in the roaming agreement. Any unilateral change to the records surfaces at reconciliation.

**4. Business agreements: disputes go to contract [10].** GSMA's standard international roaming agreement (AA.12/AA.13) sets out each party's rights and duties, charging, settlement and dispute handling.

**5. Shared data goes to a neutral operator [11].** US number portability runs on the Number Portability Administration Center (NPAC). It is a central database run by a neutral third party, currently iconectiv, and used by every competing carrier. Competitors share critical data through a neutral operator and regulation, not a blockchain.

**6. Open interconnection.** Any phone can call any phone, and any mailbox can email any other, with no central approval. Public standards are enough.

## Mapping the model to cross-border payments

- SS7 / MAP / SIP real-time signaling → ISO 20022 real-time payment messages and APIs
- Each operator's own billing system → Each bank's or payment firm's own ledger (a distributed database)
- TAP/RAP record exchange and dispute process → Real-time reconciliation, return and dispute protocols
- Roaming clearing house → Clearing institutions and neutral hubs for net settlement
- NPAC, a neutral shared database → Neutrally operated shared directories, routing tables and limit registries
- GSMA roaming agreement → Multilateral payment scheme rules and agreements

This model is already being built:

- **BIS Project Nexus [14][15][16].** Nexus aims to connect domestic instant payment systems in a standard way, making cross-border payments faster, cheaper, more transparent and more accessible. In most cases, funds should reach the payee within 60 seconds. It uses ISO 20022 and purpose-built APIs. Its operator, Nexus Global Payments, is a non-profit set up in March 2025 by the central banks and instant-payment operators of India, Malaysia, the Philippines, Singapore and Thailand. A PayNet–NETS joint venture is the technical operator, working with AWS and Endava; development began in early 2026, with launch targeted for 2027. There is no blockchain in it. It is close to the telecom roaming model, applied to payments.
- **Interledger Protocol (ILP) [17].** ILP was proposed by Stefan Thomas and Evan Schwartz while they were at Ripple. Their paper says the protocol needs neither a global coordinating system nor a blockchain, and that its security borrows from two-phase commit. Conditional locks and timeouts move value atomically across ledgers that don't talk to each other. In effect, it is a signaling protocol for payments.
- **Pix (Brazil) and UPI (India).** Both run in real time, around the clock, on conventional database architectures, at a scale far beyond any chain today.

## A look at today's solutions

- **Partior, a bank consortium [20][21].** Technically, it is a permissioned ledger built on ConsenSys Quorum and run by Partior Pte Ltd. It has no public token and settles commercial bank money. The participants are licensed banks, and there is a dedicated operating company. That is exactly the "neutral operator plus multilateral agreements" structure. The blockchain is an implementation choice that could be swapped out.
- **Tempo and Arc, payment-focused chains [23].** Stripe incubated Tempo with Paradigm, and Circle created Arc. Visa joined Tempo as an early validator in April 2026, alongside Stripe and Zodia Custody, and MoneyGram joined in May 2026. A few named institutions taking turns to keep the books is, in substance, a consortium database.
- **Visa's multi-chain approach [24][25].** In April 2026, Visa expanded its stablecoin settlement pilot to nine chains, including Tempo and Arc. When USDC arrives, Visa updates its internal ledger and then credits the acquirer. The chain covers only the settlement leg, while core accounting stays in Visa's own systems. If nine chains are interchangeable, the chain is a pipe. The value isn't in the chain itself.
- **USDT and USDC on public chains.** Issuers can freeze addresses and decide on redemption, so trust anchors on the issuer and its regulators. Flows between institutions could run entirely on the issuer's ledger plus standard protocols.

## Ten objections, and my answers

**1. "Blockchain is tamper-proof and trustless."** The telecom model doesn't require trusting the other side either. Each party keeps its own books, protocols define which state changes are valid, and any mismatch shows up in real-time checks or at reconciliation. Where needed, a hash-chained, append-only log lets each party verify independently. And today's solutions already rely on trusting issuers and licensed institutions, so "trustless" doesn't really apply here.

**2. "With no single operator, blockchain avoids the question of who's in charge."** A blockchain still has to decide who writes the code, who approves upgrades, who can validate, who fixes bugs, and whether to fork. Stripe and Paradigm incubated Tempo, Circle created Arc, and mBridge's central banks still negotiate rules and access. Blockchain doesn't remove governance; it moves it into code and foundations. Telecom has handled governance for decades through GSMA, 3GPP and neutral operators.

**3. "Blockchain guarantees no single party can rewrite history."** How parties relate to each other is a business question. How data is written and changed is an operations question, and protocols agreed in advance answer it: only state changes the protocol allows are executed, and each side validates them in its own systems. Operators never needed to co-edit one ledger. Each ledger only accepts messages that follow the protocol.

**4. "Money isn't phone calls. You must prevent double spending and guarantee finality."** That's a protocol design problem, with proven answers. Lock, confirm, then commit, the same idea as two-phase commit. Use conditional payments with timeout rollback, as ILP does. Settle finally in central bank money, or back it with prefunding and credit lines. A committed database transaction is final, unlike the probabilistic finality of some public chains.

**5. "Blockchain runs 24/7; legacy systems keep business hours."** Business hours are an operating and liquidity choice, not a property of ledger technology. UPI, Pix and telecom networks all run 24/7. Partior is working with LSEG DiSH on out-of-hours settlement liquidity [22], which shows the hard part of 24/7 is liquidity, not the chain.

**6. "Smart contracts make money programmable."** Conditional payments, payment splits and escrow releases can all be built with stored procedures, workflow engines and rules engines. Better still, write common conditional payments into the standard protocol, as telecom signaling does. Every party then implements them the same way, audits are easier, and there are no losses from smart-contract bugs.

**7. "Public chains are open and composable; databases aren't."** Openness comes from public standards, not from a shared ledger. Phone and email networks are open worldwide, with no common ledger and no central approval. With public interfaces and message standards (ISO 20022 plus open APIs), any licensed institution can connect and combine services.

**8. "Visa, Stripe, MoneyGram and Western Union are all investing in blockchain. The market has spoken."** Look at what they actually value. Visa connecting nine interchangeable chains shows it values stablecoins as a liquid settlement asset and a distribution channel, not any particular consensus mechanism. Funding narratives, a seat at the standards table and regulatory pilot windows are business motives. They don't prove blockchain is the best technical answer. The counterexample is the Australian Securities Exchange [18][19]. After about seven years on its blockchain-based CHESS replacement, ASX abandoned the project in 2022, writing off A$245–255 million before tax. It moved to a platform built by Tata Consultancy Services, and the first release, clearing, went live in April 2026. BIS's Nexus also chose a path without blockchain.

**9. "Isn't this just slow correspondent banking again?"** Correspondent banking is slow because of batch messages, manual compliance review, layers of intermediaries and business hours, not because each bank keeps its own books. The key in telecom is real-time signaling: protocols execute automatically, with confirmation in milliseconds. That is what cross-border payments should borrow, not batch reconciliation.

**10. "GSMA itself built a blockchain network for roaming settlement." [12][13]** True. In 2021, GSMA announced that its industry-wide private, permissioned blockchain network, the GSMA eBusiness Network, was commercially available. But note three things. First, it is a permissioned chain of known operators, exactly the kind this article argues could be replaced by protocols plus databases. Second, GSMA's main improvement is the BCE specification (Billing and Charging Evolution). Unlike TAP, BCE exchanges aggregated data and allows more flexible exchange and settlement cycles. That is a process and protocol change that doesn't depend on blockchain. Third, GSMA acknowledges that most roaming clearing and settlement still runs on TAP, and operators expect TAP and blockchain/BCE to coexist for a long time. Even in telecom, blockchain is one optional implementation, not a replacement for standard protocols.

## The one thing blockchain can't replace

There is exactly one thing the protocol model cannot do: bearer self-custody. On a public chain, anyone can hold dollar value without an account at any licensed institution and send it directly to someone else. In the protocol model, both ends are always institutions.

But that is not the problem these networks set out to solve. They serve cross-border flows between institutions, and they actively meet KYC/AML, sanctions and freeze-list requirements. Bearer self-custody is a separate policy question, unrelated to the efficiency of institutional cross-border payments.

## Conclusion

Institutional cross-border payments can be rebuilt on the telecom model: multilateral agreements at the business layer, automated protocols agreed in advance at the operations layer, mature distributed databases at the storage layer, and neutral operators for any data that must be shared. This architecture has decades of engineering behind it, and for institutional flows it compares well with blockchain on performance, privacy, data sovereignty and regulatory fit. Blockchain remains the stronger choice where bearer self-custody or open, permissionless access is the goal.

In today's stablecoin networks, the blockchain plays two roles: a carrier for the settlement asset, and a distribution channel. An issuer's ledger plus standard protocols can play both.

Where do you think a shared ledger is truly necessary in institutional payments? I'd like to hear the strongest counterexample.

## References

**Telecom standards and practice**

1. [ITU-T Q.700, Introduction to Signalling System No. 7](https://www.itu.int/rec/T-REC-Q.700-199303-I/en)
2. [3GPP TS 29.002 (MAP)](https://www.3gpp.org/dynareport/29002.htm)
3. [3GPP TS 32.240 (Charging architecture and principles)](https://www.3gpp.org/dynareport/32240.htm)
4. [3GPP TS 32.298 (CDR parameter description)](https://www.3gpp.org/dynareport/32298.htm)
5. [IETF RFC 6733 (Diameter)](https://www.rfc-editor.org/rfc/rfc6733)
6. [IETF RFC 3261 (SIP)](https://www.rfc-editor.org/rfc/rfc3261)
7. [GSMA open standards (TD.57 TAP3, TD.58, TD.32 RAP)](https://www.gsma.com/about-us/open-standards-specifications/)
8. [GSMA TD.58 TAP3.12 implementation handbook (Sep 2026)](https://www.gsma.com/get-involved/working-groups/wp-content/uploads/2026/09/TD.58-TAP3.12.pdf)
9. [GSMA, International Roaming Explained](https://www.gsma.com/publicpolicy/wp-content/uploads/2012/09/Africa-International-roaming-explained-English.pdf)
10. [Operator agreement citing AA.12/AA.13 (Wind Hellas)](https://www.wind.gr/files/1/Etaireia/PDFs/2012%2011%20DIRECT%20WHOLESALE%20ROAMING%20ACCESS%20REFERENCE%20OFFER_final%20version_02_2013.pdf)
11. [NPAC, operated by iconectiv](https://iconectiv.com/NPAC); [FAQ](https://numberportability.com/general)
12. [Light Reading: GSMA announces blockchain network for roaming and settlement](https://www.lightreading.com/ai-machine-learning/gsma-announces-blockchain-network-for-roaming-and-settlement)
13. [GSMA on TAP, BCE and blockchain](https://www.gsma.com/solutions-and-impact/industry-services/?p=4849)

**Payments**

14. [BIS Project Nexus](https://www.bis.org/project/nexus)
15. [Business Wire: Nexus Global Payments appoints technical operator](https://www.businesswire.com/news/home/20260209818123/en/Nexus-Global-Payments-Appoints-Technical-Operator)
16. [Payments Industry Intelligence: Nexus adopts ISO 20022 and APIs](https://paymentsindustryintelligence.com/?p=56050)
17. [Interledger white paper](https://interledger.org/interledger.pdf); [protocol spec](https://interledger.org/developers/rfcs/interledger-protocol/)
18. [Finextra: ASX scraps DLT-based CHESS replacement](https://finextra.com/newsarticle/41337/asx-takes-a250m-hit-after-scrapping-dlt-based-chess-replacement-project)
19. [ShareCafe: ASX moves to TCS platform](https://www.sharecafe.com.au/?p=173794); [btw.media: Release 1 live](https://btw.media/en/asx-chess-replacement-market-infrastructure-assurance-accountability)
20. [Partior technical architecture](https://wiki.private.law/en/partior)
21. [Eco: What is Partior](https://eco.com/support/en/articles/17272672-what-is-partior-bank-owned-settlement-network)
22. [Payment Expert: Partior and LSEG DiSH on 24/7 settlement](https://paymentexpert.com/2026/09/17/partior-lseg-dish-247-settlement/)
23. [Tempo: Stripe, Visa and Zodia join as validators](https://tempo.xyz/blog/stripe-visa-zodia-join-as-validators/); [Cointelegraph: MoneyGram joins Tempo](https://cointelegraph.com/news/moneygram-joins-tempo-validator-network-as-stablecoin-settlement-push-expands)
24. [Visa press release, Apr 29, 2026](https://corporate.visa.com/en/sites/visa-perspectives/press-releases/visa-expands-stablecoin-settlement-adds-five-blockchains.html); [AMBCrypto](https://ambcrypto.com/viable-complement-visa-expands-stablecoin-rails-as-demand-grows-50/)
25. [BlockEden: Visa and Mastercard stablecoin settlement rails](https://blockeden.xyz/blog/2026/02/28/visa-mastercard-stablecoin-settlement-rails/)
