---
title: "Why a Decentralized Technology Delivers a Centralization Dividend in Cross-border Payments"
date: 2026-11-15
description: "Blockchain makes cross-border payments faster and cheaper, but almost none of that comes from decentralization. It comes from merging ledgers and merging currencies — and the system it replaces is the one that was truly decentralized."
tags: ["Stablecoins", "Cross-border payments", "Blockchain", "CBDC"]
---

## 1. The core argument

We often hear that blockchain makes cross-border payments "faster, cheaper and available 24/7." But ask where those benefits actually come from, and almost none of them come from decentralization itself. They come from two mergers:

1. **Merging ledgers:** thousands of banks each keeping their own books becomes one ledger for the whole network.
2. **Merging currencies:** exchanging between dozens of fiat currencies becomes everyone using the same token — in practice, mostly dollar stablecoins.

Here is the irony: the system blockchain replaces is the one that was truly decentralized. And it replaces it by building a unified system with a single ledger and a single asset.

## 2. Traditional cross-border payments are a decentralized system

We tend to think of traditional finance as centralized. Cross-border payments are structured the opposite way:

- **No global central ledger:** each bank keeps only its own books; no institution sees the whole picture.
- **Many currencies:** the renminbi, dollar, euro and peso each have their own issuer and settle in their own national clearing systems.
- **A peer-to-peer correspondent network:** Bank A holds an account at Bank B (nostro/vostro), B connects to C, and a single payment can take 3–5 hops.
- **SWIFT is only a messaging network:** it carries instructions; it does not move money or keep accounts.

Topologically, this is a multi-center, multi-ledger, multi-asset mesh. That is exactly why it is slow and expensive:

| Pain point | Root cause |
|---|---|
| Slow (T+1 to T+5) | Multiple hops, each with its own reconciliation and compliance checks, constrained by each country's operating hours |
| Expensive | A fee at every hop, plus FX spreads |
| Trapped capital | Every corridor needs funds pre-positioned at the counterparty bank; trillions of dollars sit idle in correspondent accounts worldwide |
| Opaque | With no shared ledger, the sender can't see where the money is |
| High failure rates | Inconsistent data formats and compliance standards across banks |

These are the costs of fragmentation — in other words, the costs of decentralization.

## 3. What stablecoins get right: merging everything into one

Take a cross-border transfer in USDT or USDC and break down its benefits:

- **Atomic settlement, no reconciliation:** there is one ledger, so the transfer *is* the settlement — "my books don't match yours" cannot happen. This comes from **a unified ledger**.
- **No FX step:** both sides hold "on-chain dollars," so there is no currency conversion in between. This comes from **a unified unit of account** — in essence, dollarization.
- **Pooled liquidity:** no need to pre-fund accounts in N countries; one wallet reaches the world. This comes from **a unified asset**.
- **24/7 availability:** a unified system is not bound by national clearing hours. This comes from **a unified system**.
- **End-to-end transparency:** again, from **a unified ledger**.

Every benefit traces back to unification. None comes from decentralization.

**The counter-test:** any centralized system that achieves the same unification gets the same benefits.

- Cross-border transfers within one bank (for example, inside HSBC) settle instantly.
- Transfers inside Alipay or WeChat Pay take seconds, because each is a single ledger.
- CLS removed settlement risk in FX trading (Herstatt risk) through centralized, simultaneous settlement.
- J.P. Morgan's Kinexys (formerly Onyx), Partior and mBridge are all permissioned ledgers — essentially "a bank consortium sharing one set of books" — and they show the same efficiency gains.

So: **a unified ledger and a unified asset are sufficient for the efficiency gains; decentralization is not necessary.**

## 4. The deeper irony: centralization returns at every layer

1. **Highly centralized issuers:** USDT is issued by one company, Tether; USDC by Circle. They can freeze addresses, hold the reserves, and answer directly to regulators. Users are really trusting the issuer, not the chain.
2. **Centralization of money:** the vast majority of stablecoins are pegged to the dollar. The so-called decentralized currency has, in practice, become an on-chain extension of the dollar's reach, compressing a multi-currency world into a single dollar system.
3. **Concentrated infrastructure:** much of USDT's cross-border volume runs on a handful of public chains, and nodes, on/off-ramps and exchanges are highly concentrated too.
4. **On- and off-ramps lead back to the old system:** last-mile fiat conversion, bank crediting and KYC still go through traditional banks. FX costs haven't disappeared; they've been pushed to the two ends.

## 5. The reverse evidence: add more chains and the problems return

If this argument holds, then as stablecoins and chains multiply, the old problems of cross-border payments should reappear. That is exactly what we see:

- USDT, USDC, PYUSD, EURC and national CBDCs coexisting: the **multi-currency problem** is back.
- Ethereum, Tron, Solana and many layer-2s coexisting: the **multi-ledger problem** is back.
- Cross-chain bridges: **correspondent banks** are back — with more risk, as the large historical losses from bridge hacks show.
- Swaps between chains and between tokens: **FX spreads** are back.

Without unification, blockchain degrades into just another correspondent network. That is the proof in reverse: the value comes from unification, not decentralization.

## 6. Does decentralization contribute nothing? To be fair, two things

**1. Credible neutrality makes unification possible.** In reality, banks and governments don't trust each other, and none wants a rival running the world's only ledger. Decentralized consensus offers a ledger that belongs to no single party, lowering the political barrier to accepting unification.

In other words, **decentralization is the means and unification is the end: a decentralized method to reach a centralized result.** That is the most elegant part of the paradox. (I discuss this in more depth in [When Do You Actually Need a Blockchain? Lessons from mBridge](/articles/blockchain-boundaries-mbridge/).)

**2. Permissionless access.** Anyone with a wallet can send and receive money without a bank account. That has real value for the unbanked and for people in high-inflation countries. But much of this value comes from bypassing controls — capital controls, sanctions, KYC — which is regulatory arbitrage, not technical efficiency.

## 7. In one sentence

> The efficiency blockchain brings to cross-border payments is the efficiency of one ledger plus one currency (the dollar). Decentralization's role is simply to make mutually distrustful parties willing to accept that unification. What it replaces is the genuinely multi-center, multi-currency correspondent network.

**The implication:** if unification is what matters, the endgame for cross-border payments is not "blockchain versus traditional finance." It is **who keeps the single ledger, and which currency becomes the common unit of account.** Candidates include dollar stablecoins, multilateral CBDC platforms such as mBridge, and upgrades to existing networks such as Visa, Mastercard and SWIFT. This is really a question of monetary sovereignty and network effects; the technology is only the surface.
