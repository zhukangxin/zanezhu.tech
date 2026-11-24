---
title: "From Paper to Platform (Part 2 of 3): Fetch the Data Instead of Asking for the Paper"
date: 2026-11-25
description: "InfoLess: instead of asking clients for customs paperwork, fetch the same facts from the source. How a data-exchange gateway to government single windows made cross-border payments paperless and fed automated compliance checks."
tags: ["Transaction banking", "Product strategy", "Digital transformation", "Risk & compliance"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_en_paper-to-platform-2.png"
draft: false
---
*From Paper to Platform* series: [Part 1: Rules as configuration](/articles/paper-to-platform-1-rules-as-configuration/) · **Part 2: Fetch the data** · [Part 3: Roll out by maturity](/articles/paper-to-platform-3-roll-out-by-maturity/)

In Part 1, I wrote about turning compliance rules into configuration. But rules can only automate what they can read. This part is about the idea that made our data readable in the first place. I call it **InfoLess**: stop asking clients for information we can get from the source.

## Why InfoLess

Every industry is moving its core business online. Orders, contracts, shipping, customs clearance and invoicing increasingly live in digital systems, not on paper.

That matters for cross-border payments, because a payment is rarely the business itself. It is one step in a trade: goods are ordered, shipped, declared and delivered, and then paid for. The business comes first; the payment follows. So proving that a payment is compliant really means proving that the underlying business is real and lawful.

As a trade moves forward, the systems of the buyer and seller, of trusted intermediaries, and of government agencies record it along the way. Those records are, by nature, evidence that the business is real. If a bank can get that evidence directly from the two parties, the intermediaries or the authorities, two things happen at once. The payer no longer spends time and money proving its own case. And the bank gets information that is more authentic and more complete than the copies a client chooses to send.

## The problem

Trade still runs on a lot of paper. The International Chamber of Commerce estimates that about 4 billion documents move across the trade ecosystem at any given time [[1]](#ref-1).

In our case, clients sent us large volumes of customs documents to support their payments, and staff checked them by hand. Yet the same facts already existed in the customs single-window systems run by local governments. We were asking clients to send us copies of information that a government system already held.

Getting it from the source was not simple either. Each regional system used its own message format and charged its own price.

Talking with clients who resisted going digital and paperless taught us something important. They were not against digital tools. What they disliked was the work of copying and uploading documents they already had, or typing the same information again into the bank's system. Asking them to scan instead of mail only moved that burden around. The real fix was to remove it. That is why minimizing the payment information clients have to provide is the key to taking cross-border payments fully online, or **All Online**.

## What we built

A data-exchange gateway that connected our platform directly to the customs single-window systems of local governments. Clients signed up online through an automated agreement process, and from then on data flowed between the systems automatically. It routed each request to the cheapest available source, converted every format into one standard message, and passed the result straight to downstream checks. It adapted outside interfaces on one side and offered interfaces to partners on the other.

The structured data then fed straight into the configurable rules from Part 1. That connection is what turned automated checks from an idea into daily practice.

These single windows follow the model UN/CEFACT has promoted since 2005: traders submit information once, at one entry point, instead of again and again [[2]](#ref-2). We simply connected the bank to that entry point, instead of asking clients for another copy.

[![InfoLess data-exchange gateway: customs single windows in each region connect through adapters, cost-based routing and one standard message to the configurable rules and the payment approval system, with a manual fallback channel built first](/images/articles/paper-to-platform-gateway-en.svg)](/images/articles/paper-to-platform-gateway-en.svg)

The gateway fetches the facts from the source, standardizes them, and feeds the rules from Part 1. A manual fallback was built first.

## The trade-offs

We put cost-based routing and format standardization first. Automatic failover wasn't the priority. We built the manual fallback first. When a data source was unavailable or the automated exchange failed, staff could start a data exchange by hand and feed the result back into the cross-border payment approval system through an internal online channel. This kept the first release lean, gave us a fallback we could verify, and laid the data and interaction groundwork for switching to automated exchange. As I argue in *From All Online to Autonomous*, the goal is to remove unnecessary manual work, not every manual recovery path [[4]](#ref-4).

Team capabilities also shaped the design. Most bank technology teams were used to batch file transfers, so real-time exchange was a new skill for them. We chose between real-time APIs and scheduled batch files interface by interface. The right answer depended on how fresh the data needed to be, not on which technology was newer.

## The result

Most clients no longer had to submit paper documents at all. This gateway design also became one of the main reasons the paperless rollout succeeded: it is easy to ask clients to go paperless when you no longer need their paper.

> The fastest way to remove paper was not a better upload form. It was not needing the document at all, because we could get the same facts, and often more authoritative ones, straight from the source.

## What changed in operation

Once data flowed automatically, we found we were receiving far more information than clients had ever supplied to prove their own case. External systems also kept changing: each evolved its data formats and protocols on its own schedule.

A one-time integration was not enough. Keeping up meant solving three design problems:

1. **How do we keep outside changes from rippling into our internal systems?** Isolate the inside from the outside, with loose coupling. An API gateway or adapter layer translates each external protocol and data format into one internal standard for business logic, rules and data. When a source changes, only its adapter changes.
2. **How do we respond quickly when outside systems change?** Use microservices, or an operating model built on configurable rules, so that most changes need a short development cycle or no development at all. This is where the configurable rules from Part 1 paid off again.
3. **How do we handle more and more incoming information?** Verify it automatically with configurable rules, or have AI verify it with people reviewing the results, so that more data does not mean more manual work.

Looking back, this was more than an integration project. It was an evolution of our operating system: processes and the operating model had to change along with the data. That is the process redesign and operating-model shift I describe in *Why AI Transformations Fail* [[3]](#ref-3).

## Why this worked

This layered, protocol-first thinking comes from my years in telecom. Telephone networks never asked callers to carry routing information by hand. Each layer did its job through agreed protocols. I wrote about applying that idea to payments in *What Payments Can Learn from Telecom* [[5]](#ref-5).

## What's next

In the *All Online → Automatic → Autonomous* framework [[4]](#ref-4), this gateway belongs to **All Online**: it turned documents into structured, online data. But a working gateway does not move clients by itself. Part 3 is about the rollout: how we brought clients and colleagues along, one step at a time.

Where does your organization still ask customers for information it could fetch itself?

## References

1. <span id="ref-1"></span>ICC United Kingdom with ICC France, ICC Germany and the ICC Digital Standards Initiative, *Creating a Modern Digital Trade Ecosystem / Making the Case for Digitalisation: Electronic Transferable Records* (2021), research by Coriolis Technologies, p. 4. [Link](https://www.iccgermany.de/wp-content/uploads/2021/10/Creating-a-Modern-Digital-Trade-Ecosystem-G7.pdf)
2. <span id="ref-2"></span>UNECE / UN/CEFACT, *Recommendation and Guidelines on Establishing a Single Window* (Recommendation No. 33, 2005; updated 2020). [Link](https://www.digitalizetrade.org/legal-instrument/recommendation-and-guidelines-establishing-single-window-recommendation-no-33)
3. <span id="ref-3"></span>Kangxin (Zane) Zhu, "Why AI Transformations Fail: When AI Is Just Technology, Not the CEO's Strategy" (21 November 2026). [Link](https://zanezhu.tech/articles/why-ai-transformations-fail/)
4. <span id="ref-4"></span>Kangxin (Zane) Zhu, "From All Online to Autonomous: A Product Strategy for AI-Ready Banking Platforms" (21 November 2026). [Link](https://zanezhu.tech/articles/bank-ai-path-all-online-to-autonomous/)
5. <span id="ref-5"></span>Kangxin (Zane) Zhu, "What Payments Can Learn from Telecom: Layered Design and the Signaling Idea" (16 November 2026). [Link](https://zanezhu.tech/articles/payments-learn-from-telecom/)
