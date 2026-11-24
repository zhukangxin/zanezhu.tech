---
title: "From Paper to Platform (Part 1 of 3): Make Rules Configuration, Not Code"
date: 2026-11-24
description: "Regulatory rules changed faster than we could ship code. Turning compliance rules into low-code configuration cut rule delivery from years to months, turned technical DevOps into product DevOps, and showed why such a change needs senior sponsorship."
tags: ["Product strategy", "Risk & compliance", "Digital transformation", "Bank operations"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_en_paper-to-platform-1.png"
draft: false
---
*From Paper to Platform* series: **Part 1: Rules as configuration** · [Part 2: Fetch the data](/articles/paper-to-platform-2-fetch-the-data/) · [Part 3: Roll out by maturity](/articles/paper-to-platform-3-roll-out-by-maturity/)

For years, every cross-border payment I worked on at a global bank came with a stack of paper: invoices, contracts, customs declarations. People checked each one by hand. When a regulator changed a rule, it took far longer to change our systems than to read the new rule.

We were not unusual. The International Chamber of Commerce estimates that about 4 billion documents move across the trade ecosystem at any given time [[1]](#ref-1). Every one of them is something a bank may be asked to check.

Over several years, my team and I turned that process into a platform. This short series covers three lessons from that work. This first part is about the rules engine at its core.

## Where we started

The business was solid, but the operating model was built for paper. Compliance meant people reading documents. Rules lived in code that only vendors could change. And the data we needed to verify a payment sat in outside systems that didn't talk to each other.

I owned the product and much of the architecture for compliance review, post-payment alerts and external data exchange, and I led vendor selection for the platforms in this series.

## The problem

Regulatory rules changed faster than our delivery cycle. Each change meant a new round of requirements documents and a vendor build, and the gap between "rule announced" and "rule live" was measured in years.

Development capacity was scarce too. Product lines competed for the same limited budget, and winning a development slot meant spending a great deal of time in a complex budget contest before any work could start.

## What we built

A low-code platform where compliance rules are defined as configuration and flowcharts, not as custom code. Operations and compliance defined each rule together. Operations tested it before release. Every change needed sign-off from compliance, product and operations. I designed the data model, field standards and permission rules underneath, so a new rule could reuse what was already there.

[![From code to configuration: before, a rule change went through requirements, a budget contest and a vendor build and took years; after, operations and compliance configure it, operations test it, three functions sign off, and it goes live in months](/images/articles/paper-to-platform-rules-en.svg)](/images/articles/paper-to-platform-rules-en.svg)

The same regulatory change, before and after: the people who understand a rule now change it themselves.

## The trade-offs

We automated only rules that had already been confirmed. Anything ambiguous stayed with a person. That slowed coverage at first, but it meant nobody had to argue about whether the machine was right. We also designed the workflow so that a rule-based step could later be replaced by a model, without rebuilding the process around it.

Building a platform flexible enough for rules we could not yet foresee also cost more up front, in design and development, than hard-coding the next rule would have. We accepted that, because the investment paid back over years of operation: lower development cost, faster response to clients and regulators, and a smoother experience for both.

## The result

New rules went from years to months, and we absorbed a wave of regulatory changes and a new regulatory project with the resources we already had.

Configuration needed very little development budget. After training, operations staff could make most rule changes themselves, so everyday operating cost now covered much of what used to be development cost and time, and we no longer had to win a budget round for every change.

In effect, configuration turned technical DevOps into product DevOps. It removed the slow, expensive hand-off in the middle: the people who understood a rule could now change it themselves. It reminds me of the typing pool. Managers once needed typists to produce their documents. Once every manager had a computer and learned to use it, the typist was no longer needed in between.

## The organizational cost

The typist analogy also shows the cost. Configuration changes who does the work, so it changes the organization: reporting lines, operating procedures, and who owns which decision. The strongest objections were not about technology. They came from incentives: promotion rules tied to headcount, budgets that would shrink, and roles in some teams that would no longer be needed, much like the typist.

Most of the resistance came from the front line. It is a classic principal–agent problem in a large company: what is good for the firm is not always good for each unit inside it. That is why a change like this needs real strategic endorsement and practical support from senior leadership, not just a working platform. I make the same argument about AI in *Why AI Transformations Fail* [[2]](#ref-2).

Even with support, we could not always change the organization as much as the design called for, so we made practical compromises:

- **When we couldn't restructure into a dedicated product DevOps team**, we formed a virtual one, with key people from each department working together across reporting lines.
- **When no department or person was willing to take on the day-to-day rule configuration**, we gave it to the outsourced development team that used to write the code. Their work changed from long coding cycles to short configuration tasks, so most of the speed and cost gains survived.

The goal did not change; the path to it bent around what the organization could absorb at the time.

> Automate only what you already agree on. The ambiguous cases stayed with people, and that is exactly why people trusted the automated ones.

## What's next

In the framework I use for this kind of work, *All Online → Automatic → Autonomous* [[3]](#ref-3), configurable rules are the **Automatic** stage. But automation only works on data that is already online. Part 2 covers how we stopped asking clients for paper and fetched the data ourselves.

If you have tried to move rules out of code in a regulated business, I'd like to hear what got in your way.

## References

1. <span id="ref-1"></span>ICC United Kingdom with ICC France, ICC Germany and the ICC Digital Standards Initiative, *Creating a Modern Digital Trade Ecosystem / Making the Case for Digitalisation: Electronic Transferable Records* (2021), research by Coriolis Technologies, p. 4. [Link](https://www.iccgermany.de/wp-content/uploads/2021/10/Creating-a-Modern-Digital-Trade-Ecosystem-G7.pdf)
2. <span id="ref-2"></span>Kangxin (Zane) Zhu, "Why AI Transformations Fail: When AI Is Just Technology, Not the CEO's Strategy" (21 November 2026). [Link](https://zanezhu.tech/articles/why-ai-transformations-fail/)
3. <span id="ref-3"></span>Kangxin (Zane) Zhu, "From All Online to Autonomous: A Product Strategy for AI-Ready Banking Platforms" (21 November 2026). [Link](https://zanezhu.tech/articles/bank-ai-path-all-online-to-autonomous/)
