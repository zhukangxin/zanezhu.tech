---
title: "From In-Band to Common-Channel Signaling: Why Cross-Border Payments Must Decouple"
date: 2026-11-17
description: "Cross-border payments are slow, expensive and opaque because messaging, FX, funds movement and storage are coupled along one correspondent chain. Through the lens of telecom's SS7: SWIFT's half-decoupling, blockchain's re-coupling, and why payments will decouple into layers."
tags: ["Cross-border payments", "SS7", "SWIFT", "Layered architecture", "Blockchain"]
cover: "/images/articles/in-band-to-common-channel-cover-en.jpg"
---

## Introduction

Cross-border payments are slow, expensive and opaque. The root cause is not a missing technology. It is that **messaging, FX conversion, funds movement and storage** have long been tightly coupled along a single chain of correspondent banks.

Telecom faced the same problem in the 1970s and 1980s. Its answer was Signaling System No. 7 (SS7): pull control signaling out of the voice path and run it on a separate signaling network. The Intelligent Network, mobile roaming, SMS and today's IMS all grew out of that single act of decoupling.

Payments are on the same road. SWIFT took the first step by separating messages from money. But funds movement, FX conversion and account storage are still bound to correspondent relationships. Blockchain goes the opposite way, bundling business logic, transaction execution and ledger storage back into one chain. This article argues that cross-border payments will inevitably move to **layered decoupling**.

## 1. The telecom lesson: from in-band signaling to SS7

The essence of SS7 is separating "control" from "payload", so that control becomes a layer that can evolve independently and be programmed.

In the era of **channel-associated signaling** (CAS), signaling and voice shared the same circuit. China's No. 1 signaling, the international R2 system and North America's 2600 Hz single-frequency signaling all belonged to this family. It had four built-in flaws:

- **Wasted resources**: trunks were seized hop by hop before the call was connected; even a busy callee meant seizing a line and then releasing it.
- **Poor information**: only a few digits, such as the dialed number, could be carried, and slowly.
- **Security holes**: control and content shared one channel. A 2600 Hz whistle or a "blue box" let a user impersonate a switch and make free long-distance calls.
- **Hard to innovate**: every new service required modifying every switch along the route.

**Common-channel signaling** (CCS) moved signaling onto a separate packet network. In May 1976, AT&T launched CCIS (based on Signaling System No. 6). Signaling now ran on dedicated links that users could not reach, and the blue box stopped working. CCITT published the SS7 recommendations (Q.701–Q.741) in its 1980 Yellow Book. Decoupling delivered three things:

1. **Signal first, seize later**: a trunk is assigned only after the callee is confirmed reachable.
2. **Protocol layering**: MTP handles transfer, SCCP handles addressing, TCAP handles transactions, and ISUP/MAP handle services, each evolving independently.
3. **Circuit-independent services**: the signaling network could query databases and run transactions, enabling 800-number translation, number portability, prepaid billing and mobile roaming. SMS itself was born in the signaling channel.

Even more important, the Intelligent Network then separated the Service Control Point (SCP) from the Service Switching Point (SSP). Softswitch, IMS and SDN all extend this idea.

| Dimension | In-band signaling | SS7 |
|---|---|---|
| Signaling channel | Same circuit as voice | Separate signaling network (via STPs) |
| Resource use | Trunk seized before connection | Trunk seized only after confirmation |
| Information capacity | A few digits | Rich, structured parameters |
| Security | Signals can be injected into the voice path | Users cannot reach the signaling network |
| New services | Modify switches one by one | Deploy centrally in the service layer |

Note that the SS7 network itself has three signaling modes: **associated** (signaling links run parallel to the trunk group between the same pair of switches), **quasi-associated** and **non-associated** (both routed via STPs; quasi-associated is the preferred SS7 mode). This distinction is used later to locate SWIFT.

## 2. The in-band era of payments

Before SWIFT, cross-border payment instructions always traveled along the "physical line" of the money itself. That is the in-band signaling of payments.

**Stage 1: the instrument is the instruction.** Bills of exchange, letters of credit and traveler's checks were both payment instructions and stores of value. Control information and the value carrier were the same piece of paper, fully coupled.

**Stage 2: telegraph and Telex.** Banks sent free-format payment instructions by telegraph and Telex, authenticated with bilaterally agreed test keys and read by humans. Every pair of banks had to set up its own test-key arrangement, just as every trunk carried its own in-band signaling.

**Stage 3: instructions hop along the account chain.** Money could only move across the nostro/vostro accounts between correspondent banks. So payment instructions had to be forwarded hop by hop along the chain of account relationships. At every hop, "read the message + post the entry + possibly convert currency + deduct a fee" happened at once. The longer the chain, the more delay, fees and inquiries.

The costs of this era map one-to-one onto in-band signaling. The best-known case is the failure of Bankhaus Herstatt on 26 June 1974. The two legs of FX trades settled separately, in different time zones and different systems, with no independent coordination layer: counterparties had paid, and Herstatt closed before paying them back. "Herstatt risk" has since become shorthand for coupling FX conversion to settlement.

| Telecom | Cross-border payments |
|---|---|
| Voice path (trunk circuits) | Chain of correspondent nostro/vostro accounts |
| In-band signals relayed hop by hop | Payment instructions relayed hop by hop along the account chain |
| Trunk seized before connection | Funds leave before the beneficiary is verified; errors fixed by returns |
| Signaling carries only a few digits | Free format or limited fields; remittance data truncated |
| Blue box forges signals in the voice path | Forged telegrams, leaked test keys |
| New services need every switch modified | New products need a string of bilateral agreements |

## 3. SWIFT: a common-channel network, only half decoupled

SWIFT separated messages from money, but it did not separate the routing of messages from the path of the money.

**1973–1977: the message layer becomes independent.** SWIFT was founded in Brussels in 1973 and went live in 1977. It replaced bilateral Telex and test keys with a shared, standardized, self-authenticating messaging network. SWIFT holds no funds and does no clearing; it only carries messages. It is the common-channel signaling network of payments, and MT messages are its signaling protocol.

**Traces of half-decoupling.** MT103 (customer transfers) and MT202 (bank-to-bank cover) are still routed along correspondent account chains. The messaging network is independent, but "who gets the message" is still decided by "whose books the money sits on". In SS7 terms, today's SWIFT resembles the **associated mode**: physically separate from the voice path, but logically still running parallel to the trunk group.

The MT202 COV, introduced in November 2009, is the clearest evidence. In cover payments, customer details were split from the bank-to-bank funding message, so intermediary banks could not see the originator, creating an AML blind spot. The fix was to carry the customer details "in band" again inside the interbank message, because there was no independent control layer to query centrally.

**2017: gpi adds observability.** gpi uses a Unique End-to-end Transaction Reference (UETR) and a central tracker so every payment can be traced. This is like adding a call-tracing database to the signaling network: real progress in the control layer, but it does not change the fact that money still hops along the correspondent chain.

**2023–2025: ISO 20022 upgrades the signaling language.** Cross-border payments migrated from MT to ISO 20022, and the MT/MX coexistence period ended in November 2025. Structured, extensible data fields are the equivalent of moving from a few in-band digits to the rich parameters of SS7. With a common language, the message layer can finally be routed independently of any specific account chain.

**SWIFT itself is moving toward the non-associated mode.** It has launched payment pre-validation and beneficiary account verification, i.e. "signal first, seize later". It is also testing its network as an interoperability layer linking traditional accounts, tokenized assets and central bank digital currencies. In September 2025, it announced that, together with more than 30 financial institutions and starting from a conceptual prototype by Consensys, it will add a blockchain-based shared ledger to its infrastructure, with real-time 24/7 cross-border payments as the first use case. SWIFT says the ledger will work alongside its existing messaging, APIs and ISO 20022 rather than replace the message layer. But it will also record, sequence and validate transactions directly. This is SWIFT's first step into the storage layer, and worth watching.

Three things SWIFT has not yet decoupled:

- **Funds movement** still depends on correspondent account chains, with large amounts of liquidity pre-funded in each country.
- **FX conversion** is hidden inside one hop of the chain, with opaque pricing and no default synchronized settlement.
- **Storage** (accounts) is scattered across banks, and addressing depends on bank codes and account numbers. There is no independent addressing layer like number portability.

## 4. Counter-example: blockchain as the new in-band signaling

Blockchain puts five things that a payment system should keep apart back into one system running on one clock:

- **Messaging**: broadcasting a transaction is passing the instruction;
- **Business logic**: smart contracts;
- **Execution and ordering**: the consensus mechanism;
- **Storage**: a ledger replicated on every full node;
- **The asset itself**: the token.

This puts control and payload back into the same channel. Each of the four flaws of in-band signaling has a counterpart on blockchain:

| Flaw of in-band signaling | Counterpart on blockchain |
|---|---|
| Wasted resources | Every node re-executes and re-stores every transaction; throughput is capped by the slowest link |
| Poor information | To keep on-chain data small, compliance and remittance data must stay off-chain or be heavily trimmed |
| Security holes | A contract bug is a loss of funds: in 2022, about $620 million was stolen from the Ronin bridge (March) and about $320 million from the Wormhole bridge (February), at market value when stolen |
| Hard to innovate | Changing one layer means upgrading the whole network; disagreement means a hard fork |

There are two further problems specific to payments. The first is privacy: on a public chain, message content and the ledger are visible to everyone, which conflicts with banking secrecy and data localization rules. The second is cross-chain transfer: different chains again need "bridges" and market makers relaying hop by hop, effectively reinventing the correspondent banking chain.

The most convincing evidence comes from the blockchain community itself. Ethereum's 2022 Merge split the consensus layer and the execution layer into two separate clients. Layer-2 rollups move execution off-chain. Dedicated data-availability layers split storage out as well. The so-called "modular blockchain" is decoupling layer by layer, which amounts to admitting that the monolithic design does not work.

The same is true of stablecoins. Their value comes from the bank deposits and government bonds held by the issuer, not from the chain. The chain is just one way of keeping their books, and it can sit in the storage layer of a layered architecture as one account form among many.

## 5. A layered framework for payments and FX

Following telecom's layering, cross-border payments can be split into five layers. Each layer does one job and talks to its neighbors through standard interfaces.

![Telecom layers vs. cross-border payment layers: service layer to orchestration, signaling to messaging, media gateway to FX, transport to funds movement, subscriber data to storage and accounts](/images/articles/payment-layers-en.svg)

The left column shows the layers telecom separated long ago; the right column shows the layers cross-border payments should form. Dashed lines mark the functional correspondence.

Each decoupling has concrete costs and benefits, and each has a precedent in telecom history:

| Layers to decouple | Problem when coupled | Benefit once decoupled | Telecom precedent |
|---|---|---|---|
| Messaging ↔ funds movement | Money leaves first; errors fixed by returns; inquiries sent bank by bank | Pre-validate and verify the payee, then move money; end-to-end tracking | Signal first, seize later |
| FX ↔ funds movement | Conversion hidden in one hop with opaque spreads; legs not synchronized, so Herstatt risk | Transparent, comparable quotes; PvP settlement | Media gateways transcode independently |
| Storage ↔ funds movement | Routes locked to account relationships; liquidity pre-funded abroad | Accounts can take any form; the movement layer connects through interfaces | HLR separated from switches, enabling roaming |
| Addressing ↔ account institution | Payee must give bank code and account number | Alias addressing: change institution, keep identifier | Number portability |
| Services ↔ infrastructure | New products need a string of bilateral agreements | Launch new services in the orchestration layer without touching the network | IN separates SCP from SSP |

The FX business itself also needs a three-way split. Quoting and dealing are messaging, settling the two currencies is funds movement, and the foreign-currency position is storage. Today a single correspondent bank often bundles all three and charges for the bundle. Once decoupled, quotes can come from competing FX providers, settlement can run through PvP or synchronized RTGS in both countries, and positions can be pooled in a few liquidity hubs instead of being held separately on every correspondent relationship.

## 6. Forecast: cross-border payments will decouple into layers

Telecom took about two decades to move from in-band to common-channel signaling and then to the Intelligent Network. Payments have completed the first step, and the rest of the path is clear.

**Public policy is already splitting things by layer.** In 2020 the G20 launched its Roadmap for Enhancing Cross-border Payments, with quantitative targets for speed, cost, transparency and access by 2027. The priority actions the FSB set in 2023 (harmonizing ISO 20022 data requirements, interlinking fast payment systems across borders, extending RTGS operating hours and widening access) each map onto one layer.

**Project Nexus is a textbook case of layered decoupling.** Nexus, initiated by the BIS Innovation Hub, handles only the "messaging, routing and message translation" layer. Funds settle in each country's domestic fast payment system, FX is quoted by independent FX providers, and accounts stay with their own banks. A country connects to Nexus once and can then reach every other connected country. That is exactly the logic of a signal transfer point (STP). In April 2025, the central banks of India, Malaysia, the Philippines, Singapore and Thailand incorporated Nexus Global Payments in Singapore to put it into operation.

**An addressing layer is taking shape.** Fast payment systems such as Brazil's Pix and India's UPI let users pay to aliases such as phone numbers and email addresses instead of account numbers, decoupling identity from the institution that holds the account. This is number portability for payments.

From this, five predictions for the next five to ten years:

1. **The message layer becomes a neutral public network.** SWIFT, Nexus and national payment gateways speak ISO 20022 as a common language, pre-validate and verify the beneficiary first, and only then move money.
2. **FX becomes an independent service layer.** Quotes are public and comparable, payment-versus-payment (PvP) settlement becomes the default, and spreads no longer hide inside one hop of the chain.
3. **The funds-movement layer runs many rails side by side.** RTGS, interlinked fast payment systems, correspondent banking and tokenized-deposit rails coexist, with the message layer choosing the route by cost, speed and risk, like least-cost routing in telecom.
4. **The storage layer diversifies.** Bank accounts, e-wallets, tokenized deposits, stablecoins and CBDCs coexist, interoperating through common addressing and messaging interfaces.
5. **Blockchain returns to its proper place.** Where it exists, it will be one implementation option for the storage or funds-movement layer, not a full-stack solution.

**The strongest counter-argument, and a reply.** Advocates of a "unified ledger", including Project Agorá, which the BIS is running with seven central banks and more than 40 financial institutions, argue that only putting messages, assets and logic on the same ledger can deliver atomic settlement and programmability. This is a serious argument. But atomicity is a coordination problem, not a co-location problem. Since 2002, CLS has used PvP to eliminate Herstatt risk without a shared ledger, and SS7 achieved consistent call setup without ever putting voice and signaling on the same circuit. Even where a unified ledger is adopted for some use cases, it is likely to become one storage/settlement node in a layered architecture rather than a replacement for layering. Agorá's own prototype reportedly uses a two-layer structure that records tokenized deposits separately from central bank reserves ([source](https://www.pulse.bot/currencies/video/project-agora-a-shared-programmable-platform-for-wholesale-cross-border-payments-157db9ef-b4f9-4549-8063-88889299f02e/)): even the unified-ledger camp is layering.

## Conclusion

One act of signaling decoupling took telecom from "making phone calls" to the mobile internet. The "SS7 moment" for cross-border payments is at hand. SWIFT proved that messaging can stand on its own; the next step is to let FX conversion, funds movement and storage each stand on their own too. Blockchain, which bundles everything back together, is in-band signaling dressed up as innovation, and history has already shown us how that ends.

This article extends the series *What Banks and Payments Can Learn from Telecom*. See also: [What Banks Can Learn from Telecom](/articles/banks-learn-from-telecom/) · [What Payments Can Learn from Telecom](/articles/payments-learn-from-telecom/).

## References

Sources checked one by one on 2026-11-17.

- Telecom: [Bell System Technical Journal: CCIS overview (1978)](https://nokia.com/bell-labs/publications-and-media/publications/common-channel-interoffice-signaling-an-overview) · [CCITT Yellow Book, SS7 recommendations (1980)](https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/4.258.43.en.1020.pdf) · [SS7 signaling modes (Patton)](https://www.patton.com/whitepapers/intro-to-ss7-tutorial/) · [History of SMS](https://webarchive.library.unt.edu/web/20161213140327/https://en.wikipedia.org/wiki/Short_message_service)
- SWIFT: [SWIFT history](https://www.swift.com/about-us/who-we-are/our-story) · [FDIC: MT202 COV (2009)](https://www.fdic.gov/news/financial-institution-letters/2009/fil09072b.pdf) · [gpi Tracker](https://www.swift.com/news-events/news/swift-introduces-universal-real-time-payment-tracking) · [ISO 20022 switch completed](https://www.swift.com/news-events/migrated-news/press-releases/global-financial-community-completes-switch-iso-20022-paving-way-new-levels-cross-border-payment-speed-and-innovation-around-world) · [Payment Pre-validation](https://www.swift.com/products/payment-pre-validation) · [Shared ledger announcement (2025)](https://www.swift.com/news-events/news/swift-add-blockchain-based-ledger)
- FX settlement: [ECB: the Herstatt case and settlement risk](https://ECB.eu/pub/financial-stability/fsr/focus/2007/pdf/ecb~ccda416def.fsrbox200712_19.pdf) · [Herstatt Bank and CLS (2002)](https://en.wikipedia.org/wiki/Herstatt_Bank)
- Blockchain: [Fortune: biggest crypto hacks of 2022](https://fortune.com/2022/12/30/5-biggest-crypto-hacks-2022/) · [ethereum.org: The Merge](https://ethereum.org/roadmap/merge)
- Public policy: [FSB: G20 Roadmap priority actions (2023)](https://www.fsb.org/2023/02/fsb-details-actions-for-the-next-phase-of-the-g20-roadmap-for-enhancing-cross-border-payments/) · [BIS: Project Nexus](https://www.bis.org/project/nexus) · [Bank of Thailand: NGP incorporated](https://www.bot.or.th/en/news-and-media/news/news-20250403.html) · [BIS: Project Agorá](https://www.bis.org/about/bisih/topics/fmis/agora.htm) · [Banco Central do Brasil: Pix](https://bcb.gov.br/en/financialstability/pix_en) · [Nexus: proxy addressing (incl. UPI)](https://docs.bis.org/nexus/addressing-and-proxy-resolution/overview-of-payment-addressing-in-nexus/addressing-via-proxies-aliases)
