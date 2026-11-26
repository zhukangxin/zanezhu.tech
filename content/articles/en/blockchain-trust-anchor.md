---
title: "Blockchain: A Trust Anchor, Not a Business Container"
date: 2026-11-25
description: "Cross-border payment and stablecoin platforms are held back by blockchain's tight coupling. This article compares three evolution paths and argues that blockchain's edge comes from three automated, preset capabilities, which a distributed database with automated protocols can also deliver once regulators step in."
tags: ["Blockchain","Stablecoins","Cross-Border Payments","Regulation","Architecture"]
publication: "zanezhu.tech"
external_url: "https://zanezhu.tech/articles/blockchain-trust-anchor/"
cover: "/images/uploads/cover_en_blockchain-trust-anchor.png"
draft: false
---

## Introduction: The Problem Is Placement, Not Blockchain

The way forward for cross-border payment and stablecoin platforms is neither to abandon blockchain entirely nor to keep piling every function onto the chain. It is to shrink blockchain into a trust anchor and hand the business to systems built for it.

Over the past few years, many cross-border payment companies and stablecoin issuers built their core business on blockchain. They now share the same problem. A monolithic chain binds consensus, execution, storage and settlement tightly together, so it scales poorly and new features ship slowly.

Layer-2 networks, sidechains and state channels ease throughput pressure, but they do not resolve the underlying tension. A global payment platform must keep adding currencies, corridors, compliance rules and product forms. A monolithic chain architecture cannot keep pace.

Companies already on blockchain therefore have to decide what comes next. Three paths are commonly discussed: rebuild the platform on a distributed database; replace blockchain with a distributed file system; or minimize the blockchain and add layered capabilities on top. This article assesses each path's feasibility, strengths and weaknesses, and offers a simple decision rule.

The core thesis fits in one sentence: **blockchain should be a trust anchor, not a business container.** Going further, blockchain's advantages come mainly from three capabilities it presets in an automated way: open interoperability, transparent auditability and multi-party writing. Once regulators step in, a distributed database with automated protocols can preset the same capabilities, and blockchain's competitive edge is severely weakened.

## What Blockchain Uniquely Offers

Before assessing any alternative, break blockchain's capabilities apart. Many projects confuse "we use blockchain" with "we need blockchain."

| Capability | Unique to blockchain? | Notes |
| --- | --- | --- |
| A shared ledger among parties who don't trust each other | In name, yes | Technically guaranteed by consensus and cryptography; real trust depends on the companies that design and run the chain |
| Bearer-like assets that circulate freely (holding is owning) | In name, yes | On-chain records move freely; whether they match real assets depends on the issuing and operating companies |
| 24/7 atomic settlement with immediate finality | Partly | Centralized systems can do this too, but it is hard across institutions |
| Programmability (smart contracts) | No | Traditional systems can do this, just less openly |
| High throughput, low latency, massive storage | No, these are weaknesses | Exactly what should move off-chain |
| Privacy, and the ability to correct or delete data | No, conflicts with chain design | Data protection laws require deletion; public chains are immutable by design |

Blockchain offers only two capabilities that are technically distinctive: **multi-party trust** and **asset circulation**. Both are guarantees in name only; real trust depends on the companies that design and run the chain (see the next section). Databases, messaging systems and traditional clearing have delivered everything else for decades, and done it better.

So the key question for any platform is: **does your business depend on these two capabilities?** If it does, replacing blockchain outright loses its core value. If it doesn't, using blockchain in the first place may have been over-engineering.

## Multi-Party Trust and Asset Circulation: What Blockchain Can and Cannot Guarantee

Blockchain provides trust that is technically verifiable, not trust that is legally enforceable. It guarantees circulation within one chain, not across systems or jurisdictions. These two points determine how much value it keeps once regulators step in.

### Why blockchain can provide multi-party trust

Traditional systems ask you to trust the operator. Blockchain replaces that with trust in cryptography plus an honest majority of participants. Four mechanisms make this work:

1. **Every party holds a full copy of the ledger**: there is no single master ledger, so no party can change it unilaterally without others noticing
2. **Consensus tolerates malicious nodes**: Byzantine fault-tolerant consensus reaches agreement even when a minority of nodes (usually up to one-third) act maliciously. An ordinary distributed database only tolerates crashes, not malice
3. **Digital signatures define ownership**: only the private-key holder can move an asset; even the operator cannot sign on their behalf
4. **Hash chaining makes history verifiable**: altering any past record breaks the hashes of every later block, and any participant can recompute and check

This trust is conditional. It depends on an honest majority of validators, secure keys and correct contract code. More importantly, **it can only guarantee that on-chain data is consistent, not that off-chain facts are true**. Whether a stablecoin's on-chain supply is backed by an equal amount of dollars in a bank cannot be proven by the chain itself. Only audits and regulation can do that.

### Once regulators step in, is blockchain's multi-party trust still needed?

Regulation provides a different kind of trust: licensing, audits, capital requirements, enforcement and liability. It works after the fact and rests on legal force. Blockchain's trust works up front and can be verified in real time. They are not substitutes, but the stronger regulation becomes, the weaker blockchain's role as a trust replacement.

**Within a single jurisdiction, it is largely unnecessary.** Regulated centralized systems (central-bank RTGS, card networks, domestic instant-payment systems) have long let mutually distrustful banks cooperate. That is why domestic payments do not need blockchain.

**Regulation itself is eroding the "trustless" narrative.** The US GENIUS Act requires payment stablecoin issuers, including foreign issuers whose coins trade on US secondary markets, to maintain the technical ability to freeze and burn wallets in order to comply with lawful orders ([Senate Banking Committee fact sheet](https://banking.senate.gov/imo/media/doc/genius_fact_sheet_-_national_securitypdf.pdf)). This freezing power reaches holders with no relationship to the issuer, whether the tokens sit in custodial or non-custodial wallets ([Steptoe analysis](https://www.steptoe.com/en/news-publications/blockchain-blog/the-genius-act-and-financial-crimes-compliance-a-detailed-guide.html)). Ultimate control of a regulated stablecoin therefore sits with the issuer and the regulator. Holders are really trusting the issuer and the law, not just the algorithm.

**Across jurisdictions, it still has value, but the value changes.** In cross-border payments no single regulator covers every party, and countries may not want to hand their ledger to another. A settlement layer jointly maintained by several parties still makes sense here. But its role shifts from "replacing trust" to "lowering the cost of verification and reconciliation": regulated institutions share one verifiable record of facts instead of reconciling separately. And this role is not unique to blockchain. A neutral international clearing body plus common standards can do the same; international telecom settlement is the precedent.

### Blockchain alone cannot guarantee multi-party trust: who keeps the builders honest?

Whether a blockchain solution can be trusted depends not only on technology but on the **capability** and **intent** of its builders. A blockchain alone cannot guarantee multi-party trust.

The same blockchain technology can produce a system with widely distributed power or one fully controlled by a single company. The difference lies in the builders, not the chain:

- **Capability** determines whether trust fails by accident: sound key management, audited contracts, secure bridges, truly independent validators. Most of the largest bridge hacks in history were failures of capability, not of blockchain principles
- **Intent** determines whether trust fails on purpose: whether builders keep admin keys, can upgrade contract rules unilaterally, hand-pick validators they control, or misuse off-chain reserves. These powers are written into the system design; the chain will faithfully execute them, not stop them

Blockchain makes **covert misconduct** hard: secretly editing the ledger, forging transactions or rewriting history will be caught by every node. But it cannot stop **open misconduct**, because those actions are powers the system grants its builders.

| Who could misbehave | How | Can blockchain prevent it? |
| --- | --- | --- |
| Stablecoin issuer | Minting without reserves; misusing reserves; abusing freeze powers | Over-minting is visible on-chain, but reserves are off-chain and the chain cannot prove them; freezing is a legal feature |
| Validators / node operators | Colluding to censor transactions; permissioned nodes jointly changing rules | Harder to prevent the fewer and more concentrated the nodes |
| Protocol developers | Changing rules through contract-upgrade permissions | No: the code is written that way |
| Rollup sequencer | Refusing to include or reordering transactions | Partly, depending on whether forced exit exists |
| Bridge operators | Multisig keys stolen or colluding | No: historically the largest source of losses |
| Exchanges / custodians | Misappropriating customer assets (e.g., FTX) | Unrelated: the assets were never in users' own on-chain addresses |

Constraining builders requires four layers working together:

1. **Technical constraints**: reduce builders' privileges. Diverse, independent validators; multisig and timelocks on admin powers so users can exit before upgrades; open source, audits and formal verification
2. **Economic constraints**: slashing of stakes, reputational loss, and users' ability to switch to competitors
3. **Legal and regulatory constraints**: licensing, reserve requirements, periodic disclosure, independent audits and segregation of customer assets. For example, under the GENIUS Act, stablecoin holders have priority claims on reserves if the issuer goes bankrupt ([Orrick analysis](https://www.orrick.com/en/insights/2025/07/stablecoin-framework-signed-into-law))
4. **Governance constraints**: issuance, block production, custody and development handled by separate entities that check each other, so no single company holds every key

The mechanisms that keep regulated blockchain companies honest are essentially the same as those for banks and clearing houses. Blockchain's contribution is to make builders' behavior **visible and verifiable**, so regulators and users spot problems sooner, not to make misconduct impossible. **The chain is the technical anchor; regulation and law are the institutional anchor; the builders' capability and intent decide whether either holds.**

### Asset circulation: systems move information, not money

**Whether in a traditional information system or on a blockchain, what moves is a record, not the money itself.** For a fiat-backed stablecoin, an on-chain token is just a piece of information representing the holder's claim on the issuer's reserves. The actual dollars stay in the issuer's bank and custody accounts and do not move with the token.

Whether information and money match one-to-one depends not on blockchain but on whether the operator holds full reserves and can redeem at par. **Trust risk is therefore concentrated in the operating company.** This is exactly like a bank deposit or a mobile-wallet balance: when users pay each other, they transfer claims on the bank or platform, while the underlying central-bank money does not move.

**An information system can guarantee the transfer of records within the system; whether those records convert into real money depends on the operator and the regulator.** Moving records across systems requires the operator's cooperation plus integration and reconciliation with the other side. Telecom has shown that common standards, interconnection agreements and a clearing house let thousands of carriers worldwide interoperate without a shared ledger. The cost is high onboarding barriers and lengthy agreement negotiations.

**Blockchain can guarantee the transfer of records within one chain, but it cannot guarantee the money behind them either.** Native on-chain assets such as bitcoin are the only exception: the token is the asset, with no off-chain counterpart. Stablecoins, tokenized deposits and other on-chain fiat assets are all liabilities of their issuers; the chain only keeps the books. Blockchain's real edge over information systems is that, on the same chain, anyone with a wallet can receive and send the record without bilateral integration. Beyond the fundamental off-chain limit, there are four more boundaries:

- **No free movement across chains**: leaving a chain requires a bridge, the biggest security risk; more chains mean more fragmented liquidity
- **Assets can be frozen**: as noted above, circulation of regulated stablecoins can be halted by the issuer at any time
- **On- and off-ramps depend on banks**: converting back to local currency still passes through traditional banking and foreign-exchange controls
- **Technical finality is not legal finality**: on-chain transfers are irreversible, yet courts can still order assets returned; holding a private key does not automatically mean legal ownership

| Question | Information system (database + clearing agreements) | Blockchain |
| --- | --- | --- |
| Joint record-keeping among distrustful parties | Relies on a regulated central operator | Relies on consensus + cryptography; holds conditionally |
| Do records match real money? | Depends on operator + audit + regulation | Equally depends on issuer + audit + regulation |
| Transfer of records (claims) within the system | Guaranteed | Guaranteed |
| Transfer across systems | Standards + interconnection agreements + clearing house | No integration needed within one chain; across chains relies on bridges, high risk |
| Where trust risk sits | The operator | The issuer and the companies running the chain |
| Legal enforceability | Strong | Depends on the issuer and regulation, not the chain |
| Role once regulators step in | Unchanged | Shifts from "replacing trust" to "shared facts, lower reconciliation cost" |

**Conclusion: blockchain alone can only guarantee trust in name.** The risk to multi-party trust sits with the companies that design and build the chain; the risk to asset circulation sits in matching on-chain information to real assets, which also depends on the operator.

Blockchain does not eliminate trust risk. It moves that risk away from the business parties and concentrates it in the companies that design and run the chain. Blockchain alone cannot guarantee real multi-party trust or asset circulation.

To earn real trust, a blockchain solution therefore needs the same technical, regulatory and governance constraints as banks and clearing houses. That is why blockchain can only serve as an anchor and cannot carry trust on its own.

## Blockchain's Advantages Come from Three Automated, Preset Capabilities

Blockchain's advantages rest mainly on three capabilities it presets in an automated way. Once regulators step in, a distributed database can preset similar capabilities through automated protocols. Against that alternative, blockchain's competitiveness is severely weakened.

### Distributed databases can deliver all three preset capabilities

Blockchain is essentially a preset package: it fixes open interoperability, transparent auditability and multi-party writing into its protocol through automation. Once equivalent protocols are defined and made admission requirements, a distributed database can deliver the same.

| Preset capability | Blockchain's automated implementation | Distributed-database equivalent |
| --- | --- | --- |
| Open interoperability | Common address and token standards; any wallet can connect | Common APIs and messaging standards (e.g., ISO 20022) + admission rules. Brazil's Pix, India's UPI, open banking and telecom interconnection are precedents |
| Transparency and real-time auditability | Fully public ledger | Read-only nodes connected to the regulator + tamper-evident ledger tables + verifiable logs + periodic publication of ledger hashes |
| Multi-party writing: no single party controls writes | Consensus algorithm hard-coded into the chain | Byzantine fault-tolerant replication (e.g., PBFT, HotStuff, which predate blockchain) + k-of-N institutional threshold signatures + regulator-held witness replicas with automatic comparison + trusted execution environments |

The third capability is the most important and the one most often assumed to be unique to blockchain. In fact, Byzantine fault-tolerant protocols are general distributed-systems technology, not a blockchain invention. Regulators can write them into admission conditions, for example: "The settlement ledger must be maintained jointly by at least N independent institutions; every write requires k-of-N signatures; the regulator holds a full real-time replica." Dual control in banking and the Consolidated Audit Trail (CAT) in US securities markets are existing automated controls mandated by regulators.

This approach rests on two conditions:

- **Independent operators are the prerequisite**: if one company controls every node, no automated protocol means anything. This is equally true for blockchain and databases; both come down to governance
- **Keep the cost in the settlement layer**: Byzantine fault tolerance needs at least 3f+1 nodes to tolerate f malicious ones, so latency and cost are higher. Use it only for settlement and leave the business layer to ordinary distributed databases

At that point, a database jointly maintained by several regulated institutions and running a Byzantine fault-tolerant protocol is no different in capability from a permissioned blockchain. The only remaining difference is packaging: blockchain bundles the three capabilities with tokens, public addresses and crypto-economic incentives, while a database solution can take only what it needs.

### Under regulation, blockchain's competitiveness is severely weakened

| Dimension | Blockchain solution | Distributed database + automated protocols |
| --- | --- | --- |
| Ultimate source of trust | Issuer, operating companies and regulators | Operator, participating institutions and regulators |
| Open interoperability | Preset | Achieved through protocols + admission rules |
| Transparency and real-time auditability | Public by default; conflicts with privacy requirements | Direct regulator access with tiered disclosure; better fits privacy requirements |
| Multi-party writing | Preset | Achieved through BFT protocols + threshold signatures + regulatory admission |
| Regulatory complexity | High: many accountable parties across jurisdictions, code as rules, assets can flow to any wallet or protocol | Low: clear accountable parties, mature supervisory frameworks |
| Scaling and iteration | Three capabilities bundled; tightly coupled; hard to scale | Three capabilities defined separately; each evolves independently |
| Remaining unique advantage | Cross-jurisdiction networking without any lead party, which regulated stablecoins give up | — |

In an unregulated open environment, presetting is blockchain's advantage: participants get a ready-made set of trust, interoperability and transparency rules without negotiation or admission. Once regulators step in, the situation reverses:

1. **Preset trust gives way to regulation**: issuers must keep freeze powers, validators converge on regulated institutions, and the ultimate source of trust becomes the same as for a database solution
2. **Preset capabilities are no longer unique**: all three can be delivered by distributed databases through protocols and enforced as regulatory admission requirements
3. **The cost of presetting remains**: the tight coupling and poor scalability that come from bundling, plus higher regulatory complexity, do not disappear under regulation

This brings us back to the problem this article began with: the scalability dilemma facing cross-border payment companies stems precisely from blockchain presetting and bundling these capabilities together.

For regulators, the sensible approach is therefore **capability-based and technology-neutral**: require open interoperability, transparent auditability and the inability of any single party to misbehave, without mandating blockchain as the technology. Blockchain is just one preset way to meet those requirements, and in regulated environments it is often neither the cheapest nor the most flexible.

## Three Evolution Paths

The three paths differ in kind: the first exits blockchain, the second is a category mismatch, and the third is where the industry is heading.

### Path 1: Drop the narrow use case and rebuild on a distributed database

**Feasibility: fully feasible technically; commercially, it depends on positioning.**

Distributed databases (such as Spanner, CockroachDB, TiDB and OceanBase) are mature. Most of the world's largest payment systems run on centralized, distributed data architectures of this kind.

Strengths:

- Orders of magnitude faster: tens to hundreds of thousands of TPS, millisecond latency, strongly consistent transactions
- Fast feature development: schema changes, new services and microservice splits are mature engineering with a deep talent pool
- Compliance-friendly: data can be corrected and deleted, privacy controls are simple, audit trails are clear
- Predictable cost: no gas fees, no on-chain congestion

Weaknesses:

- **The trust model changes**: a distributed database is "physically distributed, logically centralized." Nodes trust each other by default and tolerate crashes, not malice. The ledger's credibility comes entirely from the operator
- **Stablecoins degrade**: a "stablecoin" in a private database is essentially e-money or a prepaid balance, losing its circulation in external ecosystems
- **Cross-institution connectivity must be renegotiated**: each new partner needs bilateral integration and reconciliation, back to the correspondent-banking model
- High migration cost: on-chain assets must be redeemed or mapped, and users and partners must migrate

Best fit: companies that are essentially remittance or acquiring businesses and use the chain only for internal bookkeeping. For them, returning to a database is a sensible way to cut the hype.

Note that the two weaknesses above, "the trust model changes" and "stablecoins degrade," apply to ordinary distributed databases. Add automated multi-party writing protocols as described in the previous chapter, and make them a regulatory admission requirement, and both weaknesses largely disappear. In regulated settings, this path then extends to stablecoin issuers and payment networks.

### Path 2: Replace blockchain with a distributed file system

**Feasibility: essentially infeasible as a replacement; valuable as a supporting component.**

Distributed file systems (IPFS, HDFS, Ceph, Filecoin, Arweave and others) answer "how do we store and retrieve large files." A payment system's core question is "how does state change, in what order, and how do we prevent double-spending." The two operate at different levels.

- **No global ordering or consensus**: a file system does not decide which of two transfers came first, so it cannot prevent double-spending
- **No state machine**: there is no notion of balances, accounts or transaction validation. All of that must be rebuilt on top, and you end up building a database or a blockchain anyway
- **Content addressing is not ledger integrity**: IPFS only guarantees that file contents have not changed, not that transaction records are complete, ordered and undeleted
- Higher privacy risk: file systems on public networks are unsuitable for KYC data or transaction details

Its proper place in the architecture: storing invoices, trade documents, contracts and audit reports, with only their hashes on-chain as proof; serving as part of a data-availability (DA) layer; archiving historical data. It should not be proposed as a "blockchain replacement" but as a data-layer component within Path 3.

### Path 3: Minimize blockchain infrastructure and add layered capabilities

**Feasibility: highest, and the industry's mainstream direction (modular architecture).**

The idea is to shrink blockchain to what it alone does, namely settlement, finality and proof of asset ownership, and move every other capability into separate layers.

Strengths:

- Keeps blockchain's core value (multi-party trust, asset circulation) while moving performance bottlenecks out
- Each layer upgrades independently: change the execution environment, add privacy modules, adopt new compliance rules, all without touching the base
- Gradual migration: existing on-chain assets need no rebuild
- Regional differentiation: some markets can use permissioned chains or private execution layers to meet local rules, with settlement unified on the base layer

Weaknesses and risks:

- **System complexity rises sharply**: more layers mean more points of failure; cross-layer consistency and security audits get harder
- **Bridges and cross-layer messaging are the biggest security risk**: most of the largest crypto thefts in history happened on bridges
- **Fragmented trust assumptions**: sequencers, DA layers, oracles and bridges each carry their own trust assumptions, and overall security is only as strong as the weakest layer
- **Fragmented liquidity**: multiple execution chains or app-chains split stablecoin liquidity
- High demands on the team: it must understand both blockchain and traditional financial systems architecture

## Comparing the Three Paths

Path 1 buys performance; in regulated settings, adding automated protocols also recovers multi-party trust. Path 2 does not stand up. Path 3 keeps blockchain's nominal value at the cost of complexity.

| Dimension | Path 1: Distributed database | Path 2: Distributed file system | Path 3: Minimal chain + layers |
| --- | --- | --- | --- |
| Technical feasibility | High | Low (category mismatch) | High |
| Performance scaling | Strongest | N/A | Strong |
| Speed of feature iteration | Fastest | N/A | Fast (layers upgrade independently) |
| Multi-party trust and asset circulation | Lost with an ordinary database; achievable with automated multi-party writing protocols + regulatory admission | Lost | Kept in name; in practice depends on the operating companies |
| Compliance and privacy | Easiest | Weak | Designable, but complex |
| Regulatory complexity | Low | — | High |
| Migration cost | High (rebuild) | — | Medium (gradual) |
| System complexity | Low to medium | — | High |
| Main risk | Losing differentiation if no protocols are added | The approach does not work | Bridge and cross-layer security; risk concentrated in operators |
| Best fit | Firms using the chain only for internal bookkeeping; in regulated settings, with protocols added, also issuers and payment networks | Document notarization and archiving only | Unregulated or cross-jurisdiction open settings; firms relying on on-chain liquidity |

The likeliest winner in practice is not one of the three but a hybrid: Path 3 as the skeleton, Path 1 as the body, Path 2 as a component.

## Recommended Architecture: A Layered Structure

The chain stays at the bottom for settlement and proof; the business runs in databases at the top; the layers in between are added as needed and upgraded independently.

[![Blockchain does only settlement; everything else moves up. Application and business services (distributed database + microservices) form the business container; compliance, execution, data and interoperability layers are added as needed; the settlement layer (minimal blockchain) is the trust anchor](/images/articles/trust-anchor-architecture-en.png)](/images/articles/trust-anchor-architecture-en.png)

Read from the top: users and partners start business in the application layer; the business services layer records it in real time in databases; after compliance screening, the execution layer processes it in batches; final settlement happens in the settlement layer. The settlement layer changes least, while the application and business layers iterate fastest.

This structure combines the strengths of all three paths: Path 3 provides the skeleton (a minimal settlement layer), Path 1 provides the body (distributed databases carry the business), and Path 2 provides a component (file storage in the data layer).

## Decision Rule and Migration Path

To decide which layer a function belongs in, ask one question: **does this function need confirmation from multiple parties who don't trust each other?** If yes, put it on-chain. If not, put it in the database.

Applying that rule to common functions:

| Function | Needs multi-party confirmation? | Where it belongs |
| --- | --- | --- |
| Stablecoin issuance and redemption | Yes | Settlement layer (on-chain) |
| Final settlement between institutions | Yes | Settlement layer (on-chain) |
| Proof of reserves | Yes | Settlement layer (on-chain) |
| Document notarization | Yes, but only the hash | Hash on-chain; originals in distributed storage |
| Orders, routing, FX quotes | No | Business services layer (database) |
| Risk and AML screening | No | Compliance layer + database |
| Customer data and KYC files | No, and must be deletable | Database (never on-chain) |
| Internal reconciliation and reporting | No | Database |

For companies that have already built their business on-chain, migrate in four steps:

1. **Inventory functions**: classify every on-chain function with the table above, and find those that sit on-chain without needing multi-party confirmation
2. **Move the business off-chain first**: migrate orders, routing, risk and reconciliation to a distributed database, keeping only settlement and assets on-chain
3. **Switch to batch settlement**: record high-frequency transactions in real time in the database, then submit periodic net settlements to the chain
4. **Add layers only when needed**: add execution layers, privacy modules or cross-chain channels only for a clear need, and assess each layer's trust assumptions and security risks separately

## Historical Analogies and Industry Trends

"Real-time recording plus periodic net settlement" is not new. Telecom and bank clearing have used it for decades, and the new generation of payment-focused chains is converging on the same model.

**How telecom does it.** In international roaming, every call and data session is first recorded in real time in each carrier's own billing system. Carriers do not settle call by call. Through clearing houses they periodically exchange records, reconcile differences, then net-settle. The business runs in each carrier's own container; only settlement needs multi-party confirmation.

**How bank clearing does it.** Each bank's core system records transactions in real time, while interbank funds reach final settlement through real-time gross settlement (RTGS) or net clearing systems. The clearing systems rarely change, while banks' products and business systems keep evolving. That is "a stable anchor, a flexible container."

In this model, blockchain's role is to turn the clearing house into a settlement layer that several parties maintain jointly and no single party owns. It replaces the clearing house, not each participant's billing or core systems.

**Industry trends.** New payment-focused chains are narrowing the chain's role and strengthening the capabilities around it:

- [Tempo, incubated by Stripe](https://fortune.com/2026/03/18/stripe-tempo-paradigm-mpp-ai-payments-protocol/), launched its mainnet in March 2026. [Stripe's documentation](https://docs.stripe.com/stablecoins/ecosystem/tempo) positions it as a chain built for stablecoin payments, with built-in privacy, account-level controls and reconciliation
- [Circle's Arc](https://www.theblock.co/news/ecosystems/2026-09-16-circle-launches-arc-mainnet-blackrock-and-visa-among-validators-mints-10-billion-arc-tokens-415250) opened its public mainnet on September 16, 2026, using USDC for fees and integrating its payments network and FX settlement service into the chain
- Notably, [Arc's blocks are produced by a fixed set of regulated financial institutions](https://thedefiant.io/news/blockchains/circle-launches-arc-mainnet-with-blackrock-dtcc-and-visa-producing-blocks) rather than an open validator market. Trust is anchored in a small number of accountable participants, a governance structure very close to traditional clearing

These chains all move in the same direction: the chain handles only settlement and trust, while compliance, privacy and reconciliation are offered as modules.

## Conclusion

The scalability problem facing cross-border payment and stablecoin platforms does not come from blockchain technology itself. It comes from using blockchain in the wrong place: asking a system designed for multi-party trust to carry high-frequency, complex, privacy-sensitive business.

Going further, blockchain alone cannot guarantee real multi-party trust or asset circulation. It guarantees trust only in name, and the real risk ends up concentrated in the companies that design and run the chain.

Of the three paths, replacing blockchain with a distributed file system does not work technically. In unregulated open settings, a minimized blockchain with layered extensions still has the edge. In regulated settings, a distributed database with automated protocols can deliver blockchain's three preset capabilities with lower regulatory complexity and more flexible scaling, making it clearly more competitive than a blockchain solution.

One line for architects and product leaders: **let the chain be the anchor, and let the database be the container.** Separate the two, and each does its own job well.

In your platform, which functions truly need to be on-chain?

**Further reading:** [Cross-Border Payments Without a Shared Ledger](/articles/cross-border-payments-dont-need-blockchain/), [Blockchain Through the Lens of Database History (Part 1)](/articles/blockchain-as-file-system/), [The Economics of Stablecoins](/articles/stablecoin-private-clearing-house/)
