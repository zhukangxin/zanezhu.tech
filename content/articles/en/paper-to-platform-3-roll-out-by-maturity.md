---
title: "From Paper to Platform (Part 3 of 3): Roll Out by Client Maturity, Not All at Once"
date: 2026-11-26
description: "A working platform does not mean anyone uses it. A tiered rollout (Paperless, InfoLess, InfoLeast), human-in-the-loop controls and a new operating model moved clients online, and showed why moving from Automatic to Autonomous is the hardest step."
tags: ["Product strategy", "AI", "Bank operations", "Digital transformation"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_en_paper-to-platform-3.png"
draft: false
---
*From Paper to Platform* series: [Part 1: Rules as configuration](/articles/paper-to-platform-1-rules-as-configuration/) · [Part 2: Fetch the data](/articles/paper-to-platform-2-fetch-the-data/) · **Part 3: Roll out by maturity**

Parts 1 and 2 covered what we built: configurable compliance rules, and a gateway that fetched trade data instead of asking clients for paper. This last part is about what made any of it matter: getting clients and colleagues to actually use it.

## The problem

A working platform does not mean anyone uses it. Our clients ranged from highly digital multinationals to firms that still preferred paper, and their risk profiles differed just as widely. One rollout plan could not fit them all.

Inside the bank, the change was just as uneven. The new process changed daily work for operations, sales and relationship teams, and each had its own concerns.

## What we built

A tiered service model, matched to each client's maturity and risk level:

1. **Paperless.** Submit documents electronically instead of on paper.
2. **InfoLess.** Stop asking clients for information we can fetch ourselves (Part 2).
3. **InfoLeast.** For low-risk clients, ask only for the minimum the rules require.

Each client moved one step at a time. I trained sales and relationship managers, and worked with the client service team on regular client training, so everyone understood our digital direction. New features then spread through the everyday contact between clients and their sales or relationship managers, and we drove the change together.

InfoLeast came from a new regulatory opportunity. China's foreign-exchange regulator introduced trade facilitation measures under which qualified banks may simplify the compliance documents that clients meeting low-risk eligibility criteria must submit for cross-border payments [[1]](#ref-1). That created a new need: a way to recognize those clients and give them a lighter process, while the bank still checks that their business is real and compliant.

In practice, InfoLeast worked in three parts:

- **Fast lane before payment.** Configurable rules, or AI, identify low-risk clients in low-risk scenarios and route them first. Those payments skip the slow steps of submitting documents, waiting, and having them checked. Clients no longer prepare paperwork, and their payments go out faster.
- **Stronger checks after payment.** We expanded the post-payment alert system. Configurable alert rules, or AI, flag suspicious transactions for review after the fact. Payments stay fast up front, and mistakes still get caught and corrected.
- **Human in the loop, always.** Only fully approved transaction scenarios are allowed to run automatically. If a problem appears, a rule change switches that scenario back to manual review at any time. And this is not the old manual review: rules or AI show the reviewer the basis for each flag and how likely the issue is, so a person can confirm or clear it quickly.

[![Tiered rollout: Paperless, then InfoLess, then InfoLeast; InfoLeast combines a fast lane before payment, stronger alerts after payment, and human in the loop](/images/articles/paper-to-platform-tiers-en.svg)](/images/articles/paper-to-platform-tiers-en.svg)

Each client moves one step at a time. InfoLeast keeps people in the loop while low-risk cases move faster.

## A new operating model

This design also changed our processes and operating model. Running it well meant answering a new set of questions, again and again:

1. **Alignment.** How do we make sure the rules and AI always stay consistent with the regulations?
2. **Graduation.** How do we tell when a human-in-the-loop scenario is safe and reliable enough to run fully automatically, or even autonomously?
3. **Discovery.** How do we spot new risks, update the configuration, and put the change into operation?
4. **Fallback.** When an alert is confirmed, how do we send that scenario back to manual review as a safety net?
5. **Improvement.** How do we keep refining the rules and AI to make them more accurate and reliable?

None of these are one-time tasks. They became part of daily operations: the kind of process redesign and operating-model change I describe in *Why AI Transformations Fail* [[2]](#ref-2).

One question will never be finished: how to use AI to gradually replace manual judgment in the current process, or rules that have become too rigid. This is the key step from Automatic to Autonomous, and the hardest one. It comes back every time AI improves. And it is not solved by technology alone. It is a real challenge to how a firm allocates resources, runs its management system, and thinks about management. I discuss this in *Why AI Transformations Fail* [[2]](#ref-2) and *Manage AI Like Talent, Not Like Software* [[3]](#ref-3).

## The trade-offs

Inside the bank, we did not promise to "remove manual review." We showed operations colleagues that people would still review payments, but that their workload would drop a lot. That honesty mattered more than any feature.

Outside, we started with low-risk, highly digital clients, and let their experience persuade the rest. It was slower than a big-bang launch, but each step built trust for the next one.

To help clients see the real benefit, and to make their own digital change easier, I designed a carbon emissions calculator. Based on how many documents a client submitted, and whether they came as paper or as data files, it calculated the emissions the client could save. That gave sales a second message beyond less paperwork: a concrete ESG benefit for the client's company. It also gave the client's own team a value case for winning senior support when they changed their back-office routines.

## The result

Most clients moved online. The tiered approach later became part of the bank's broader digital strategy, and changed how several departments worked.

> Adoption is a product feature. We didn't ask every client to jump to the end state. We gave each one the next step it could take.

## The sequence behind the series

The three parts were not separate projects. They followed one path, which I later described as **All Online → Automatic → Autonomous** [[4]](#ref-4):

[![The series on the All Online → Automatic → Autonomous path: Parts 2 and 3 sit in All Online, Part 1 in Automatic; Autonomous begins with human in the loop and the graduation question, and its hardest step is using AI to replace manual judgment and rigid rules](/images/articles/paper-to-platform-3a-en.svg)](/images/articles/paper-to-platform-3a-en.svg)

Each stage pays for itself and remains the fallback for the next.

These steps laid the ground for the last stage, Autonomous, where AI takes on more of the work inside clear guardrails. The human-in-the-loop design and the graduation question in this part are where that stage begins.

Looking back, the technology was rarely the hard part. The hard part was sequencing: getting data online before automating, automating confirmed rules before adding AI, and bringing people along at every step. Each stage paid for itself and became the fallback for the next one. Skipping a stage is, in my experience, one of the most common reasons AI programs stall, a point I make in *Why AI Transformations Fail* [[2]](#ref-2).

If you build compliance or payment platforms, I'd like to hear which of these three lessons you have run into, and what you would add.

## References

1. <span id="ref-1"></span>State Administration of Foreign Exchange (SAFE), Shanghai Branch, *Notice on Further Improving the Effectiveness of the Trade Foreign Exchange Facilitation Pilot for High-Quality Enterprises* (September 2022), with the revised *Guidance on the Trade Foreign Exchange Facilitation Pilot for High-Quality Enterprises*; other SAFE branches issued similar guidance. In Chinese. [Link](https://www.safe.gov.cn/shanghai/2022/0916/1816.html)
2. <span id="ref-2"></span>Kangxin (Zane) Zhu, "Why AI Transformations Fail: When AI Is Just Technology, Not the CEO's Strategy" (21 November 2026). [Link](https://zanezhu.tech/articles/why-ai-transformations-fail/)
3. <span id="ref-3"></span>Kangxin (Zane) Zhu, "Manage AI Like Talent, Not Like Software" (19 November 2026). [Link](https://zanezhu.tech/articles/manage-ai-like-talent/)
4. <span id="ref-4"></span>Kangxin (Zane) Zhu, "From All Online to Autonomous: A Product Strategy for AI-Ready Banking Platforms" (21 November 2026). [Link](https://zanezhu.tech/articles/bank-ai-path-all-online-to-autonomous/)
