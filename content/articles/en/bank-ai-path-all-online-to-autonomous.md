---
title: "From All Online to Autonomous: A Three-Stage Path for Bank Digitalization and AI"
date: 2026-11-16
description: "When a bank brings in AI, the risk is not the model itself but whether anything can catch it when it fails. This article walks through All Online → Automatic → Autonomous: what each stage solves, how it paves the way for the next, and how the business falls back layer by layer instead of stopping when AI goes wrong."
tags: ["Digital transformation","AI","Bank operations","Transaction banking","Risk & compliance"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_en_bank-ai-path.png"
draft: false
---

## Introduction: the risk of AI is not in the model, but beneath it

When a bank brings in AI, the real risk is not that the model isn't smart enough. It is that nothing underneath can catch it when it gets things wrong. Without structured data, AI has nothing to learn from. Without clear rules, no one can tell whether AI is right. Without preserved human capability, the business stops the moment AI stops.

Over many years in bank transaction services, I led the design and rollout of a “3A” digital strategy: **All Online → Automatic → Autonomous**. The idea behind this path is simple. Each stage must solve the business problems of its day. At the same time, its outputs must become the foundation for the next stage, and the fallback when the next stage fails.

Drawing on several kinds of work I took part in or led — paperless operations, online retrieval and standardization of document data, a low-code rules platform, machine-learning monitoring, automated collections matching, and e-signatures for client onboarding — this article covers what each stage solves, what to consider in its design, how it paves the way for the next, and how the outputs of the first two stages keep the business running when AI fails.

## Stage 1 — All Online: turning business into data

All Online is not just about sparing clients a trip to the branch. More importantly, it turns business that lives on paper, in email and in people's heads into structured, traceable data in the system.

### Main problems it solves

- **Paper documents and manual checks are slow.** In cross-border trade settlement, for example, clients submit large volumes of customs declarations, invoices, bills of lading and other documents, and operations staff check them one by one by hand.
- **Data standards are inconsistent.** Customs, tax, foreign exchange, freight and other authoritative systems — and the same type of system in different regions — each use different message formats and charge different fees for data queries.
- **Signing and approval depend on paper.** To activate new digital features, clients must sign commitment letters, and wet signatures and company chops slow down the whole process.

### Practice and design considerations

I led the entire paperless program. One key practice was to retrieve key documents and data directly from authoritative systems (such as customs, tax, foreign exchange and freight systems) instead of asking clients to submit paper. Each request is automatically routed to the lowest-cost data source, and the various formats are converted into one standard message for automated downstream processing. This significantly increased client adoption of the online channel. Key considerations:

1. **Structure before digitization.** A scanned image is just “digital paper.” Only field-level data in a consistent format can be used by the rules and models that come later. The core value of retrieving key document data online is exactly this: turning messages from different sources and formats into one standard format.
2. **Roll out by client maturity and risk.** I proposed and led a “3L” client go-to-market strategy: Paperless → InfoLess → InfoLeast. Clients that are more digitally mature and lower-risk move first, rather than applying one approach to everyone.
3. **Keep a complete audit trail.** The time, operator and approval record of every step must stay in the system. This was done for compliance and audit at the time; later, it became the most valuable data for rule testing and model evaluation.
4. **Bring legal validity online too.** The client onboarding solution I last designed centered on digital signatures and electronic company seals, so corporate clients could sign commitment letters online and activate new digital features. Without legal validity, an online process eventually falls back to paper.
5. **Don't leave only one road.** One lesson from practice: our document-data channel had no failover at the time. Going online raised efficiency, but it also made the business more dependent on a single channel. Critical processes should keep an alternative channel by design, such as letting clients upload documents themselves.

### Groundwork for the next stage

- **Unified, structured data:** a rules engine can read fields directly and make decisions.
- **Complete process logs:** they show how people actually handle the work — which steps are repetitive and which need judgment.
- **A digitally active client base:** clients already use online channels, so the gains from automation can scale.

## Stage 2 — Automatic: automate only confirmed rules

The Automatic stage hands deterministic decisions to machines and leaves uncertain cases to people. Its core is not “automation” itself, but a clear boundary between human and machine.

### Main problems it solves

- **Once business goes online, volume rises and manual review becomes the bottleneck.**
- **The same rule applied by different people gives different results**, creating compliance risk.
- **Rule changes depend on IT development**: response is slow, and business and compliance staff cannot see what the system actually executes.

### Practice and design considerations

1. **Automate only rules that are already confirmed.** This is my first principle for rule automation. Anything still disputed, or that needs judgment from experience, stays out of scope.
2. **Externalize rules and make them readable by the business.** We used a low-code rules platform to hold the rules. Rules were defined jointly by Operations and Compliance, and Operations took part in rule testing. Rules no longer hid in code; business staff could read and review them.
3. **Control every change.** Every rule change had to be approved jointly by Compliance, Product and Operations. This carried on the practice from my early years in telecom as chair of a change control board (CCB): approve, hold or reject each change based on urgency, importance and whether a quick-win option exists.
4. **Exceptions go back to people, with the reason attached.** In automated collections matching, after funds arrive via SWIFT/CIPS, the system matches on the payer plus each client's own preset conditions. If any condition fails, the receipt goes back to the manual queue with the failure reason. Operations staff don't start from scratch; they go straight to the problem.
5. **Test thoroughly before go-live.** On the machine-learning monitoring platform, I prepared test data and ran rule validation myself. I also routinely used SQLite and Python locally for rule validation and scenario simulation.
6. **Treat organizational change as part of the design.** The 3A rollout changed the work and ways of working of several hundred people across many functions, including Operations, Relationship Managers, Sales, Technology and Compliance. I explained to the Operations team that manual review would still be needed, but their workload would drop significantly. This was true, and it was also a premise of the process design.

### Groundwork for the next stage

- **A rule library:** machine-readable business knowledge and compliance boundaries. In the AI stage, it becomes the guardrail and the evaluation baseline.
- **An exception queue with reasons:** each exception, its reason and how a person finally resolved it is ready-made labeled data for training and evaluation.
- **A three-party change approval process:** it can be extended directly to govern model launches and changes.
- **Manual review capability still in place:** the last line of defense when AI fails.

## Stage 3 — Autonomous: AI judging within guardrails

Autonomous does not mean replacing rules with models. It means letting AI handle what rules cannot cover, while rules still hold the bottom line.

### Main problems it solves

After automation, what remains in the manual queue is usually what “cannot be written as a rule”: fuzzy matching where names don't quite match, unstructured documents and free-text remarks, and exceptions that need historical behavior to judge. This is where AI is useful. Using machine learning for transaction monitoring was our first step toward this stage.

### Design considerations

1. **Rules are the guardrail; AI works inside it.** Hard compliance rules are always enforced by the rules engine, and AI conclusions cannot override them. If a rule says “no,” AI cannot say “yes.”
2. **Run in shadow mode before granting authority.** AI first runs in parallel with existing rules and people, giving conclusions without acting on them. It is tested by replaying historical data and comparing with human results, and only after it meets the bar is authority granted step by step. This extends the rule-testing practice of the Automatic stage.
3. **Tiered authority.** Move from “AI suggests, people decide,” to “AI decides, people confirm,” to “AI executes automatically in low-risk cases.” The scope of authority is tiered by client, amount and risk, in line with the 3L client strategy.
4. **Low confidence goes back to people.** AI gives a confidence score for each decision; below the threshold, the case enters the manual queue — the same queue built in Stage 2.
5. **Explainable, in the same language as exception reasons.** Every AI decision comes with a reason, in the same format as the failure reasons of the Automatic stage. Operations staff don't need to learn a new way of working, and audit and regulators have a clear record.
6. **Models and rules share one governance process.** Model launches, retraining and threshold changes all go through three-party approval by Compliance, Product and Operations, just like rule changes.

## What problems this path avoids

When banks skip the first two stages and go straight to AI, the usual problems are not in the model itself but in what is missing around it. The table shows which stage solves each problem in advance.

| Problem with going straight to AI | Consequence | Where the path solves it |
| --- | --- | --- |
| Unstructured data, inconsistent formats | The model learns nothing, or learns the wrong thing | All Online: standard messages, field-level data |
| No labeled data | Cannot train or evaluate | Automatic: exception queue with reasons and human resolutions |
| No baseline for comparison | Cannot tell if AI is better or worse | Automatic: rules-engine results are the baseline |
| Compliance black box | Regulators and auditors cannot accept it | Rule guardrails + common reason codes + full audit trail |
| Unclear accountability | No one knows who is responsible when things go wrong | Three-party approval by Compliance, Product and Operations |
| Organizational resistance | Staff fear replacement and push back | Phased change: doing the work → handling exceptions → supervising AI |
| No way back | When AI stops, the business stops | Rules engine and manual queue always online (see next section) |

The most underestimated of these is the organizational problem. With a phased approach, people's roles are upgraded step by step: first freed from repetitive work to handle exceptions, then from handling exceptions to supervising and correcting AI. The judgment they build up is exactly what AI needs most.

## When AI fails: catching it with the outputs of earlier stages

When AI fails, the business should not stop. It should fall back layer by layer: AI → rules engine → manual queue → alternative channel. The data and audit trail built in the All Online stage run through every layer and are used for tracing and correction.

[![Fallback path when AI fails: AI → rules engine → manual queue → alternative channel, with All Online data and audit trail spanning every layer](/images/uploads/fig_en_bank-ai-fallback.png)](/images/uploads/fig_en_bank-ai-fallback.png)

*Figure: the fallback path. Each step down the left side means less automation but more certainty; the data and audit trail on the right do not disappear as the business falls back.*

### What triggers a fallback

- **A single case falls below the confidence threshold:** that case goes back to the manual queue.
- **Results keep drifting from the rules baseline or human review (model drift):** AI authority for that scenario is paused.
- **The model service fails, or monitoring detects anomalies:** the whole flow switches back to the rules engine.
- **Regulators or auditors question a type of decision:** that type returns to rules plus human review.

### How each layer catches it

1. **The rules engine takes over.** The rules engine never went offline in the AI stage; it kept running as guardrail and baseline. So switching back needs no new development and no re-approval of rules. Decisions return to “confirmed rules only”: coverage drops, but correctness is assured.
2. **The manual queue absorbs the rest.** Cases the rules cannot cover enter the exception queue built in Stage 2, with reason codes. Because manual review was never removed, the team still has the skills, and no emergency training is needed.
3. **Data and audit trail drive the correction.** Using the complete logs built in the All Online stage, replay every decision AI made during the incident, compare it with the rules baseline, identify affected transactions and clients, correct them proactively, and explain to clients and regulators.
4. **The alternative channel is the last resort.** If the system itself is down, critical processes need a second road. Having run a document-data channel without failover taught me that this must be built in at design time, not patched in after an incident.

### Fallback must be designed, not bolted on afterwards

- **Switch granularity:** AI can be turned off separately by scenario, client tier or amount band, rather than all-on or all-off.
- **Capacity planning:** can the manual team absorb the volume that flows back when AI is withdrawn? This sets the ceiling on how much authority AI can be given.
- **Regular drills:** like disaster-recovery drills, switch AI off regularly to test whether rules and people can step in.
- **Recovery path:** after a fix, do not restore authority directly; go through shadow mode and tiered authority again.

## Conclusion

The race for AI in banking is not about who connects a model to production first. It is about who can keep things safe when the model gets it wrong.

Each step of the 3A path does two things. Looking forward, it builds the data, rules and governance the next stage needs. Looking back, it keeps a way out for the layer above. All Online data makes automation possible; the rules and exception queues of the Automatic stage make AI trainable, measurable and recoverable.

My career began in telecom. Telecom networks are never designed on the assumption that nothing will fail, but on the principle that the call must still go through when something does. Bank AI should work the same way: design how to fall back first, then grant authority with confidence.
