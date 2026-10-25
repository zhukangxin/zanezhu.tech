---
title: "When Do You Actually Need a Blockchain? Lessons from mBridge"
date: 2026-10-25
description: "Most of what mBridge does could run on a conventional database. What it really buys is a political solution. That insight leads to four necessary conditions for blockchain, the difference between \"can use\" and \"must use\", and the vendor risk that public blockchain infrastructure often overlooks."
tags: ["Blockchain", "mBridge", "CBDC", "Cross-border payments", "Digital strategy"]
---

People often ask me whether mBridge could be built on a conventional database.

Technically, most of it could. But the question of *why it still uses a blockchain* is the best way to see where blockchain's real value lies — and why, in most cases, it isn't needed at all.

## 1. What mBridge is

mBridge (the Multiple CBDC Bridge) is a cross-border payment platform shared by several central banks. It lets their central bank digital currencies settle cross-border payments and foreign exchange in real time, peer to peer, on a single platform.

- **Origins:** Launched in 2021 by the BIS Innovation Hub Hong Kong Centre, the Hong Kong Monetary Authority, the Bank of Thailand, the Central Bank of the UAE and the People's Bank of China's Digital Currency Institute. It grew out of Project Inthanon-LionRock, a Hong Kong–Thailand collaboration.
- **Progress:** A pilot with real-value transactions ran in 2022, and the platform reached minimum viable product (MVP) stage in mid-2024.
- **BIS exit:** In October 2024 the BIS handed the project over to the participating central banks. Agustín Carstens, then its general manager, said the decision was not political.
- **Membership:** The Saudi Central Bank became a full participant in 2024, then stopped participating after completing its proof of concept in May 2025. The Monetary Authority of Macao joined in 2026 and opened trading for 11 local banks in June. The core members today are mainland China, Hong Kong, Thailand, the UAE and Macao.
- **Scale:** As of January 2026 the platform had reportedly processed more than 4,000 transactions worth about US$56 billion, most of them in digital yuan.

Under the hood, mBridge runs on a purpose-built permissioned blockchain, the **mBridge Ledger**, which is compatible with the Ethereum Virtual Machine (EVM). Each founding central bank runs its own validating node, located in and managed by its own jurisdiction. The code is visible to every participant and can be audited and tested. Transactions are validated by multiple central banks against smart-contract rules, which makes them unique, authentic and final.

## 2. Most of it could run on a database

mBridge's core business logic is not complicated: central banks issue and redeem their own digital currencies, execute atomic payment-versus-payment (PvP) FX swaps, and run compliance checks. A conventional distributed database can do all of this:

- Each central bank's currency balances are a table; issuance and redemption are controlled writes.
- PvP requires both legs to succeed or both to roll back — exactly what relational database transactions (ACID) guarantee. No smart contract needed.
- Permission management and audit logging are mature in traditional stacks.

If mBridge were one central bank's internal system, or if all participants fully trusted one another and cared only about uptime, a database would be enough. No blockchain required.

## 3. What a database can't provide: a political solution

In reality, mBridge's participants are sovereign states that answer to no one and remain wary of each other. What the permissioned-ledger design buys is not bookkeeping. It is this: **no single party controls the ledger, yet every party can verify that no one else is cheating.** Four things make that possible.

**1. "Who runs the central database?" has no answer among sovereigns.** A conventional design needs one party — or a neutral joint operator — to hold the master database and the final right to write. No central bank wants its currency balances hosted on servers another country controls, whatever promises are made. This is a matter of political trust, not technical trust. mBridge keeps each central bank's node physically and legally inside its own jurisdiction, so the hosting question never arises.

**2. Every party can verify the rules for itself.** Because the code is open to all participants, any central bank can confirm that the platform runs exactly the rules everyone agreed to, unmodified. With a central database, the logic runs on someone else's servers and you simply have to trust it.

**3. Privacy and compliance can coexist.** mBridge reportedly plans to add zero-knowledge proofs (ZKP), which can prove that a transaction is compliant and fully funded without revealing balances, timestamps or other sensitive details. The usual centralized answer — the operator sees everything and everyone else trusts the operator — leads straight back to trusting a single party.

**4. It defends against nodes that lie, not just nodes that crash.** Primary–replica databases are built for crash faults. Independent multi-party validation provides Byzantine fault tolerance: if one node tries to forge a transaction, the others reject it.

Put the other way round: for a database to offer the same guarantees, it would have to become "every party keeps a copy, every party verifies, and the code is open for audit" — which is, in essence, a permissioned blockchain.

## 4. The other path: the euro model

There is a more radical solution: participating countries create a supranational body that runs one centralized system. A database would then do the job, and the political complexity would disappear. That is the path European countries took over decades of negotiation to build the EU and the euro — and euro-area large-value payments are still settled on a centralized system run by the Eurosystem.

This carries a lesson for the internationalization of the renminbi. Solving the political-trust problem does not have to rely solely on growing the renminbi's market share; a euro-style model of regional cooperation is another option — though a longer and far less certain road to building trust.

## 5. The general test: four necessary conditions

Generalizing from mBridge, a use case truly needs a blockchain only if all four of these conditions hold at once:

1. There are two or more independent parties that don't fully trust each other.
2. Every party needs to keep the same history, and no party may alter or erase it unilaterally.
3. There is no natural, accepted central authority. (If there is one, trusting it plus an audit log is enough.)
4. The business benefit outweighs the added cost and risk of distributed governance, operations, auditing and smart-contract security.

Test a few common use cases:

- **Data sharing across government departments:** there is usually a supervising authority, so condition 3 fails.
- **Corporate supply-chain traceability:** often only the manufacturer submits data, with no independent verification, so condition 2 fails — and source fraud remains unsolved.
- **Intellectual-property evidence:** a notary is already a trusted authority, and a centralized timestamp service works; blockchain is an optional enhancement.

The key distinction is that **"can use" is not "must use."** Many showcase projects *can* run on a blockchain. Use cases that *cannot* meet their goals without one are very rare. In most cases, "centralized storage + file hashes + a trusted timestamp service + audit logs" delivers the same result at lower cost, with a smaller attack surface and more mature auditing.

mBridge is one of the few cases where all four conditions hold: multiple sovereign states, a need for a shared ledger, no supranational authority, and cross-border settlement benefits large enough to justify the governance cost.

## 6. Public blockchain infrastructure: value and risk

If genuine needs are so rare, why does China's 15th Five-Year Plan still call for building blockchain infrastructure? The realistic reasons fall into four groups:

1. **Strategic reserve:** cross-border collaboration (for example between domestic and overseas institutions) has no common superior, so a single central authority is hard to establish. These cases are small today but worth preparing for.
2. **Lower integration costs:** shared protocols and evidence interfaces spare every pair of institutions from building its own integration, signature checks and timestamps. That is the value of standardization, though — a centralized gateway could provide it too.
3. **Engineering capability:** multi-party key management, cross-institution identity and privacy-preserving computation carry over to data-sharing and data-market initiatives.
4. **Industrial and showcase goals:** some projects are driven by industry support and demonstration programs — "blockchain for blockchain's sake."

The real danger lies in how the infrastructure is delivered. If one company builds and hosts everything, and the client lacks independent technical capability and multi-party governance, a nominally distributed trust system becomes a vendor-controlled "pseudo-consortium chain":

- **The vendor holds the keys and consensus settings.** The "multi-party" nodes all run on the vendor's cloud, so the vendor can quietly change consensus thresholds or add nodes it controls.
- **The vendor controls the way in and the way out.** The gateway can swap data before it is written to the chain. The block explorer is the only window auditors and regulators use, so altering its back end can display false records while the ledger itself stays untouched.
- **Audits become a formality.** Development and auditing are done by the same or related parties, and the client cannot verify independently.
- **The label hides the risk.** People assume "blockchain = tamper-proof" and watch the vendor less closely than they would a traditional DBA.

An outsourced traditional database at least leaves the database instances and audit logs with the client, who can deploy a bastion host and independent log auditing. With vendor-hosted blockchain, the nature of the risk changes: **an incident is not necessarily more likely, but it is harder to detect, harder to prove and harder to assign responsibility for** — and "the blockchain is immutable" can even become a cover story.

## 7. Three questions and a checklist

To check whether a blockchain infrastructure has fallen into this trap, ask:

1. Are the consensus nodes' private keys held separately by different participating institutions, out of the vendor's reach?
2. Is the protocol fully published, so regulators and third parties can run their own full nodes and verify data without the vendor's explorer?
3. Does the original business data stay in each business owner's own systems?

If any answer is "no," the hidden risk of a single vendor rises sharply.

| Suitable for public blockchain infrastructure | Not suitable |
|---|---|
| Cross-institution electronic evidence (contracts, documents, IP) | Internal systems of a single organization (OA, HR, ERP) |
| Verifying licenses and credentials, and recording status changes, across agencies | High-frequency, high-throughput real-time transaction systems |
| Supply chains with independent records from multiple parties (does not solve source fraud) | Core business databases whose rules change often |
| Audit trails for public funds and subsidy approvals | Raw sensitive personal data (copied everywhere, hard to delete) |
| Tamper-evident logs for IoT device events | "Traceability" with a single data source and no cross-checks |

The suitable cases share one trait: the chain is only a trusted-history layer. It stores hashes, timestamps and event records; raw data and business logic stay in each party's own systems; and smart contracts are kept as simple as possible.

## Conclusion

Blockchain is not a universal tool. It is a costly multi-party trust mechanism with risks of its own, and its range of use is narrow by nature. mBridge needs it not because the technology is irreplaceable, but because its participants lack a center they are all willing to trust.

So the first question for any project is not "can the technology do it?" but **"is there a center everyone is willing to trust? If so, use a database. If not, check whether all four conditions hold."**

---

**References**

- [Project mBridge](https://www.bis.org/project/mbridge), Bank for International Settlements
- [Macao joins $56 billion central bank digital currency platform mBridge](https://www.caixinglobal.com/2026-06-03/macao-joins-56-billion-central-bank-digital-currency-platform-mbridge-102450306.html), Caixin Global, June 2026
- [Saudi Arabia ends public role in China-linked mBridge CBDC platform after completing trial](https://www.crowdfundinsider.com/2026/09/312023-saudi-arabia-ends-public-role-in-china-linked-mbridge-cbdc-platform-after-completing-trial/), Crowdfund Insider, September 2026
