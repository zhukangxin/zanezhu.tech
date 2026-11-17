---
title: "What Banks Can Learn from Telecom: Layering, Not Coupling"
date: 2026-11-16
description: "Telecom evolved for half a century through layering. Banking suffers from coupled layers: SWIFT mixes customer messages with fund movement, and blockchain squeezes trust, business, resources and messages into one ledger. A layered architecture and five lessons for banks."
tags: ["Banking architecture", "Telecom", "SWIFT", "Blockchain", "Digital strategy"]
---

> Series: *What Banks and Payments Can Learn from Telecom*
>
> - Part 1: What Banks Can Learn from Telecom (this article)
> - [Part 2: What Payments Can Learn from Telecom](/articles/payments-learn-from-telecom/)

## Introduction: Telecom has already walked this road

Telecom networks move signals and messages; the banking system moves value and trust. They look very different, but at their core they solve the same problem: how to let a large number of independent institutions interact reliably, quickly and cheaply, while each of them remains free to evolve on its own.

Telecom spent more than half a century finding the answer: **layering**. From the OSI seven-layer model and the TCP/IP stack, to Signaling System No. 7 separating "control" from the voice circuit, to softswitches and IMS fully separating "services" from "transport", telecom networks evolved from analog telephony all the way to 4G, 5G and the Internet — while the services on top were largely unaffected by each change of underlying technology.

This is exactly what banking lacks. Core banking systems inside banks, the SWIFT network between banks, and blockchain solutions that many people pin their hopes on all share the same structural problem: **they mix functions from different layers together, creating deep coupling.**

## 1. What telecom layering really means

Layering is not just "splitting a system into pieces". It rests on three principles:

1. **Each layer has a single responsibility.** The physical layer only moves bits, the network layer only handles addressing and routing, the application layer only deals with business meaning. No layer does another layer's job.
2. **Layers connect through standard interfaces.** An upper layer only needs to know *what service* the lower layer provides, not *how* it is implemented. This makes each layer independently replaceable: copper becomes fiber and phone calls still work; IPv4 becomes IPv6 and web pages still load.
3. **Control is separated from transport.** SS7 moved call setup, billing and routing — the "control messages" — onto a separate signaling network, leaving voice circuits to carry only voice. Softswitches, IMS and SDN all continued this idea.

The result of layering: **complexity is isolated, evolution can happen locally, and interconnection relies on protocols rather than on a central hub.**

## 2. The problem in banking: two classic cases of mixed layers

### SWIFT: one network carrying two kinds of messages that should be separate

SWIFT is essentially a **point-to-point financial messaging network**; it does not move money itself. The problem is that it carries two completely different kinds of messages:

- **Customer business messages**: customer credit transfers (e.g. MT103 / pacs.008), containing payer, payee, purpose, remittance information and other business content;
- **Institutional fund-movement messages**: interbank position transfers and correspondent account movements (e.g. MT202 / MT202COV), which are in essence settlement operations between institutions.

In the correspondent banking model, every hop of a cross-border transfer both passes along the customer's business information and triggers interbank fund movement. Each intermediary bank is at once a "message forwarder", a "fund mover" and a compliance checkpoint. Business, clearing and settlement layers are bundled onto one chain — producing the familiar problems: long chains, slow speed, stacked fees, opaque status and repeated compliance checks. ISO 20022 improves the structure of messages, but it does not change this **architecture of coupled layers**.

### Blockchain: five things squeezed into one ledger

Blockchain is often promoted as an alternative to the banking system, but from a layering perspective it is even more tightly coupled than SWIFT. A public chain uses one mechanism to handle all of the following at once:

- **Operational trust**: consensus to guarantee that "bookkeeping operations were executed correctly";
- **Business trust**: who owns what, whether a transaction is valid, what the contract rules are;
- **Business operations**: transfers, issuance, exchange, smart-contract execution;
- **Resources**: the tokens and on-chain assets themselves;
- **Messages**: broadcasting and propagating transactions.

A single on-chain transaction is simultaneously a message, a business instruction, a ledger update and final settlement. Conceptually this looks "elegant"; in engineering terms it means any change in one layer pulls on everything, performance is bound by consensus, privacy is bound by a public ledger, and governance is bound by network-wide coordination. This is precisely the design telecom deliberately avoided decades ago — **binding trust, business, resources and messages to a single technical mechanism.**

## 3. How banking should be layered

Following telecom's approach, the banking system — both a single bank's internal architecture and the interbank architecture — can be divided into clear layers:

| Layer | Responsibility | Telecom analogy |
|---|---|---|
| Business / product | Deposits, loans, payments, wealth management; product rules and customer relationships | Application layer / IMS service layer |
| Compliance & trust | KYC, AML, sanctions screening, counterparty credit, legal constraints | Authentication, authorization and charging control |
| Clearing | Instruction confirmation between institutions, position calculation, netting | Signaling / control plane |
| Settlement | Final transfer of funds across settlement accounts | Transport plane / voice circuits |
| Ledger | Booking, posting, balances; guaranteeing correct operations | Switching and transmission equipment |
| Messaging / communication | Secure transport of standardized messages over general-purpose networks | Transport network / IP network |

The most important point is **layering trust itself**:

- **Operational trust** — "did the system execute the bookkeeping correctly?" — is solved by technology: database transactions, audit logs, reconciliation, cryptographic signatures. Mature databases and accounting systems already do this reliably, without network-wide consensus.
- **Business trust** — "is the counterparty reliable, is the transaction lawful, are the funds real?" — is solved by institutions: licensing, regulation, law, and the finality of central bank money.

Blockchain tries to solve both kinds of trust with one technical mechanism and ends up solving neither well. Telecom's experience tells us to let each kind of trust be provided by the mechanism best suited to it.

## 4. Five lessons banks can take from telecom

**1. Break the monolithic core into layered services.** Split the traditional "big core" into independent components — ledger service, product engine, clearing interface, channel access — connected by standard interfaces. Just as telecom split the switch into control and transport, banks can let product innovation proceed without touching the accounting kernel.

**2. Decouple message standards from transport networks.** A message standard such as ISO 20022 should be a *protocol*, not a *product* tied to one private network. Telecom protocols run over any transport; bank messages should likewise be deliverable over any secure network — including the Internet with PKI-based identity.

**3. Separate business information from fund movement.** The customer's business information (payment purpose, invoices, remittance details, compliance data) can travel end-to-end directly to the beneficiary's bank, while intermediaries handle only the minimum information needed to move funds. Intermediary banks no longer need to "understand" the customer's business, and no longer need to repeat compliance checks.

**4. Interconnect through protocols, not through a center.** The global telephone network has no "global switch"; national operators interconnect under ITU standards and bilateral agreements. Interbank connectivity should likewise center on open protocols that any licensed institution can join according to the standard, rather than depending on one centralized platform or one chain.

**5. Let every layer evolve independently.** Settlement can upgrade from correspondent banking to direct central bank access; messaging can move from private networks to the Internet; the business layer can keep launching new products — and as long as interfaces between layers stay stable, none of them disturbs the others. This is the fundamental reason telecom has kept evolving for decades, and it is the capability banking modernization needs most.

## Conclusion

Banks do not lack technology; they lack architectural discipline: **don't let one system, one network or one chain carry every responsibility.** SWIFT mixes customer business messages with institutional fund-movement messages; blockchain squeezes operational trust, business trust, business operations, resources and messages into one ledger. They go in different directions, but they make the same mistake.

Telecom has proven that layering, standard interfaces and the separation of control from transport are a reliable path for a global, multi-party network to interconnect and keep evolving. Banks can borrow this thinking directly, without reinventing a "chain".

In the [next article](/articles/payments-learn-from-telecom/), we turn to payments: how to borrow the design of SS7 to separate the clearing control network from the settlement funds network, and how to make full use of the Internet for direct point-to-point payment messaging.
