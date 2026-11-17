---
title: "What Payments Can Learn from Telecom: Layered Design and the Signaling Idea"
date: 2026-11-16
description: "A cross-border payment solves the same problems as an international phone call. Borrowing from SS7: separate the clearing control network from the settlement funds network, use the Internet for direct messaging, and let central banks run domestic-currency settlement and exchange houses."
tags: ["Cross-border payments", "Telecom", "SS7", "Central banks", "Payment architecture"]
---

> Series: *What Banks and Payments Can Learn from Telecom*
>
> - [Part 1: What Banks Can Learn from Telecom](/articles/banks-learn-from-telecom/)
> - Part 2: What Payments Can Learn from Telecom (this article)

## Introduction: Telecom has faced every problem payments face

The [previous article](/articles/banks-learn-from-telecom/) argued that banks should borrow telecom's layering principle and avoid mixing functions from different layers, as SWIFT and blockchain do. This article focuses on payments, especially cross-border payments.

The problems a cross-border payment must solve are strikingly similar to those of an international phone call: **how to find the other party (addressing), how to set up and control the interaction (control), how to actually deliver the content (transport), and how operators settle with each other afterwards (settlement).** Over decades, telecom built a complete layered design for these problems. Payments can borrow four key lessons from it.

## 1. Separate business content from underlying operations

In a phone call, "what you talked about" and "how the call was connected, billed and torn down" are two different things. The switch does not need to understand the conversation, and the callers do not need to care about routing details.

Payments should work the same way. Every payment contains two completely different kinds of information:

- **Business content**: payment purpose, invoice number, contract details, merchant information, remittance notes, payer and payee data required for compliance, and so on;
- **Underlying operations**: which account to debit and by how much, which account to credit and by how much, and through which settlement node the funds move.

Today's payment systems often pack both into the same message and pass it hop by hop along the same chain. As a result, every intermediary is forced to touch business content — causing privacy exposure, repeated compliance checks, and truncated or lost data.

Once separated: **business content is delivered end-to-end, directly from the payer's institution to the payee's institution; intermediary clearing and settlement steps handle only the minimum information needed for the funds operation.** The two are linked by a unique payment identifier, similar to a call identifier in a telephone network.

## 2. Like SS7: separate the clearing control network from the settlement funds network

Early telephone networks used "in-band signaling": dialing and control signals traveled through the same circuit as the voice. It was inefficient, vulnerable to interference and hard to extend with new services. **Signaling System No. 7 (SS7)**, widely deployed from the 1980s, switched to "common-channel signaling": a separate signaling network made up of Signaling Points (SPs) and Signal Transfer Points (STPs), dedicated to control messages such as call setup, routing, billing and number translation, while the voice network carried only voice. It was this independent control network that later made caller ID, intelligent networks, toll-free services and mobile roaming possible.

Payment networks can adopt the same structure and separate two kinds of networks:

**(1) Clearing control message network (the equivalent of the signaling network)**

- Carries: payment instruction initiation and confirmation, beneficiary account verification, limit and risk checks, compliance screening results, status inquiries, position calculation and netting results;
- Characteristics: high-frequency, real-time, lightweight; scales quickly and supports rich value-added services (payee confirmation, real-time tracking, refunds and inquiries).

**(2) Settlement funds message network (the equivalent of the voice/transport network)**

- Carries: based on clearing results, the final transfer of funds across central bank or settlement institution accounts;
- Characteristics: lower frequency (batched or real-time as needed), high security, strong finality; participants are professional institutions holding settlement accounts.

The benefits are clear: the control network can innovate quickly without touching fund safety; the settlement network can stay minimal and robust, without being modified for every new service. Card networks already partly reflect this idea — authorization messages flow in real time, while clearing and settlement run in batches. But cross-border bank transfers are still stuck in a model where control and fund movement are bundled together and passed hop by hop.

## 3. Make full use of the Internet: direct point-to-point interaction, no unnecessary intermediaries

One of the key design principles behind the Internet's success is "end-to-end": intelligence sits at the edges, and the network in the middle only delivers. Two computers can talk directly, without a "global central server" relaying every message.

Today, technologies for secure point-to-point communication are mature: PKI-based institutional identity certificates, mutual TLS, message-level signing and encryption, and standardized APIs. Licensed payment institutions and banks can **exchange clearing control messages and business content directly over the Internet**.

Blockchain and stablecoin solutions, by contrast, insert a whole set of intermediary systems and players between two parties who could otherwise communicate directly: public or consortium chains, stablecoin issuers, custodians, exchanges, market makers, on-chain swap protocols, on/off-ramps… Every extra link adds another layer of cost, risk and compliance burden. In essence, a stablecoin is a centralized cross-border clearing house dressed in "decentralized" form. If the two parties can already talk directly over the Internet, there is no need for messages to detour through a chain.

Another telecom lesson is also worth borrowing: **an independent addressing layer.** The telephone network has the E.164 numbering plan and number-translation databases; the Internet has DNS. Payments also need an independent, standardized "payee addressing directory" that translates aliases such as phone numbers, emails or business identifiers into "payee institution + account", so the payer can find the payee's institution and communicate with it directly.

## 4. Pre-negotiate through protocol organizations: messages, network architecture and the most efficient intermediate settlement nodes

The global telephone network interconnects not because there is one global operator, but because protocol organizations such as the ITU, 3GPP and IETF defined in advance the signaling protocols, numbering rules and inter-network interfaces, as well as settlement rules between operators (such as the international accounting rate system and clearing arrangements for mobile roaming). Any operator that follows the protocols can interconnect with the world.

Payments need the same kind of "pre-negotiation", covering four areas:

1. **Clearing message standards**: formats and flows for control messages such as instructions, confirmations, verification, inquiries and returns;
2. **Settlement message standards**: formats and flows for fund transfer instructions, finality confirmations and reconciliation messages;
3. **Clearing network architecture**: how participants connect, how identities are authenticated, how control messages are routed, how point-to-point interaction works;
4. **Settlement network architecture**: where settlement happens, who performs it, and how settlement nodes connect to each other.

On the fourth point, the key is **introducing the most efficient intermediate settlement nodes**. In telecom networks, international gateway exchanges and Signal Transfer Points play this role: few in number, critically positioned, single in purpose, they greatly simplify global interconnection.

For payments, the most efficient settlement nodes are central banks. One workable idea: **each central bank builds a global "domestic-currency settlement and exchange house"** —

- Each central bank offers global settlement services for its own currency; licensed foreign institutions can connect under the protocol and complete final settlement in that central bank's money;
- The settlement and exchange house also provides exchange and position management between the domestic currency and other currencies, or connects directly with other central banks' exchange houses;
- The fund path of a cross-border payment then becomes: payer's institution → the central bank settlement and exchange house of the paying currency → (exchange) → the central bank settlement and exchange house of the receiving currency → payee's institution.

Funds no longer need to move hop by hop through multiple correspondent banks, nor take a detour on-chain via stablecoins; control messages travel point-to-point over the clearing network. Few but authoritative settlement nodes, an open and efficient clearing network — this is the payment-world counterpart of telecom's "a few key nodes + interconnection through open protocols".

## Conclusion: Payments don't need a new invention — they need good design

Telecom's evolution offers payments four clear lessons:

1. **Separate business content from underlying operations** — intermediaries don't touch business content and perform only the minimum necessary funds operations;
2. **Separate control from transport** — like SS7, separate the clearing control network from the settlement funds network;
3. **Make full use of the Internet** — institutions interact directly point-to-point, without extra layers of chains, issuers and market makers;
4. **Protocols first** — protocol organizations pre-negotiate clearing and settlement messages and network architectures, and bring in the most efficient intermediate settlement nodes at the central bank level.

The problem with cross-border payments is not the lack of a revolutionary technology, but the lack of a clear layered architecture like that of telecom networks. Telecom has already paved this road; payments only need to learn from it seriously.
