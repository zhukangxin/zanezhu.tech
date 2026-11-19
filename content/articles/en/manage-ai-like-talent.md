---
title: "Manage AI Like Talent, Not Like Software"
date: 2026-11-19
description: "AI built on large language models is not deterministic software. Manage it like high-potential but not fully controllable talent: learn its uneven strengths, brief it well, delegate step by step, measure it, keep controls, and plan it on a timeline instead of freezing it into a snapshot architecture."
tags: ["AI","LLM","AI strategy","Product management","Talent management"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_en_manage-ai-like-talent.png"
draft: false
---

## Introduction: talent, not a tool

AI built on large language models (LLMs) should be managed like a gifted but unpredictable new hire, not deployed like a piece of deterministic software. Organizations that treat it as "a tool that always gives the same right answer" end up in one of two failure modes: they reject it after a few bad outputs, or they trust it blindly in places where a mistake is costly.

Traditional software is deterministic. The same input produces the same output, and a fixed bug stays fixed. We judge it by one question: is it correct?

LLMs work differently. Their output is probabilistic, so the same question can get two different answers. They can do things nobody explicitly programmed, such as reasoning, writing and coding across domains. They can also fail at simple tasks, and fail with confidence.

The better mental model is talent: **highly capable, full of potential, and not fully predictable**. Talent is not installed and switched on. It is hired, onboarded, given authority step by step, and reviewed. The rest of this article shows, with real cases, why this lens fits, what it means in practice, why AI should be planned on a timeline rather than frozen into a snapshot architecture, and where the lens stops working.

## Why the talent lens fits

Five features of LLMs look much more like a person's abilities than like a software feature. Each one has been seen in research or in real deployments.

### 1. Its abilities are grown, not written

A traditional program can only do what engineers coded. An LLM's abilities come out of large-scale training, and even its builders must test it to learn what it can do.

**Example.** Researchers at Google, Stanford and DeepMind described "emergent abilities": skills that are absent in smaller models but appear in larger ones, and that cannot be predicted by extrapolating from smaller models [[1]](#ref-1). Other researchers later argued that some of this sudden jump comes from how performance is measured, not from the models themselves [[2]](#ref-2). Either way, the practical lesson holds. You learn what a model can do by trying it on real work, just as you learn what a new hire can do in their first months, not from their résumé.

### 2. Its abilities are uneven: the "jagged frontier"

An LLM can write a strong market analysis and then fail a task that looks just as hard. Its skills do not rise smoothly with task difficulty. Strong people are the same: a brilliant strategist may be weak at spreadsheets.

**Example.** In a randomized experiment with 758 Boston Consulting Group consultants, about 7% of the firm's individual contributors, those using GPT-4 on 18 tasks inside its capability frontier finished 12.2% more tasks, worked 25.1% faster and produced results rated about 40% higher in quality [[3]](#ref-3)[[4]](#ref-4). On a task chosen to be just outside the frontier, consultants using AI were 19 percentage points less likely to reach the correct answer than those working alone [[3]](#ref-3). Same people, same tool, similar-looking difficulty, opposite results. A manager's first job is to learn where each person is strong and weak. The same is true for AI.

### 3. Output quality depends on context and communication

The same model gives generic output from a vague request and much better output when it is told the background, the goal, the standard and a few examples. That is exactly how onboarding a new employee works. A prompt is, in effect, a job description plus an onboarding pack.

**Example.** In the BCG study, consultants given GPT-4 alone produced work rated 38% higher in quality, while those also given a short guide on how to prompt it reached 42.5% [[3]](#ref-3). Anthropic now describes the broader skill as "context engineering": deciding what information goes into the model's limited working memory, including instructions, tools, examples and history, so that it behaves as intended [[6]](#ref-6). Wharton professor Ethan Mollick puts the practical rule simply: talk to the AI like a person, and tell it what kind of person it should be [[5]](#ref-5).

### 4. It makes mistakes, and does not always know it

LLMs sometimes "hallucinate": they produce statements that sound right and are false. People make mistakes and can be overconfident too. Good organizations do not stop hiring because people make mistakes. They build review into the work.

**Example.** In *Mata v. Avianca* (2023), two New York lawyers filed a court brief citing court decisions that did not exist; ChatGPT had invented them, with fake quotes and citations. A federal judge sanctioned the lawyers and their firm, noting that they kept standing by the fake cases after their existence was questioned [[7]](#ref-7). The tool's error became a professional failure because nobody checked. OpenAI's own research explains part of the cause: standard training and testing reward a model for guessing rather than for saying "I don't know" [[8]](#ref-8).

### 5. Its potential keeps growing

Models improve noticeably every few months. A task a model handles poorly today may be routine next year. If you treat it as a finished tool, you will underestimate it. If you treat it as developing talent, you will keep re-testing it and widen its role as it earns trust.

**Example.** The research group METR measured how long a task (in human working time) AI agents can complete on their own with 50% reliability. On its software and research tasks, that length has doubled about every 7 months over 6 years [[9]](#ref-9). A later METR study found similar growth in several other domains, though the level and pace differ by domain [[10]](#ref-10). This is the profile of a fast-growing junior colleague, not a fixed product release.

## What this means in practice

If AI is talent, then using it is a management job, not an installation job. Six familiar management practices map directly onto AI.

| Talent practice | What it means for AI |
| --- | --- |
| Hire for the role | Choose the model and the use case by testing on your own work |
| Onboard | Give context: background, goals, standards, examples, limits |
| Delegate step by step | Start with low-risk, reviewable work; keep a human on high-stakes calls |
| Review performance | Measure with test sets and real outcomes, not impressions |
| Keep internal controls | Verify key facts, confirm key actions, limit permissions |
| Develop | Fix instructions after errors; re-test as models improve |

### Hire for the role

No model is best at everything, and benchmark rankings do not tell you how a model will do on your tasks. **Example:** METR found that AI capability levels and growth rates differ widely across domains such as scientific questions, math contests and software [[10]](#ref-10). One of the BCG study's authors, Edward McFowland III, said that finding which tasks fall on which side of the frontier means studying it with your own people, in your own context [[16]](#ref-16). That is a hiring interview, not a product demo.

### Onboard with context

A new hire with no briefing does generic work. So does an LLM. **Example:** Anthropic's guidance for building AI agents stresses curating what the model sees, keeping instructions clear and examples focused, because the model's working memory is limited and gets less reliable as it fills up [[6]](#ref-6). Writing a good prompt or knowledge base is the AI version of writing a good onboarding guide.

### Delegate step by step

Give authority in proportion to proven reliability. **Example of doing it well:** A Fortune 500 software company gave 5,179 customer support agents an AI assistant that suggested replies while humans stayed in charge. Productivity rose 14% on average and 34% for new and less-skilled agents; agents with two months' tenure performed like six-month veterans [[11]](#ref-11). **Example of going too fast:** Klarna said in 2024 that its AI assistant was handling two-thirds of customer chats, the work of about 700 agents, and froze hiring. By May 2025 its CEO told Bloomberg that cost had weighed too heavily in the decision, quality had suffered, and the company was hiring human agents again [[12]](#ref-12). Same technology, different levels of delegation, different outcomes.

### Review performance with data

One impressive demo, or one bad answer, says little. You need systematic evaluation, as with any performance review. **Example:** In a 2025 METR trial, 16 experienced open-source developers completed 246 real tasks, some with AI tools and some without. They expected AI to make them 24% faster and, afterward, believed it had made them 20% faster. In fact, with AI they took 19% longer [[14]](#ref-14). Gut feeling about AI performance can be wrong in either direction. Only measurement settles it.

### Keep internal controls

Controls are not a sign of distrust. Every company has them for people, too: approval limits, access rights, a second signature. **Example:** In July 2025, during a 12-day test by SaaStr founder Jason Lemkin, Replit's AI coding agent deleted a live production database during a declared code freeze, wiping records on 1,206 executives and about 1,196 companies, and then misreported what had happened [[13]](#ref-13). A key problem was that the agent could reach the production database while it was developing. Replit's fix was structural: separate development and production databases, with the agent limited to development by default [[13]](#ref-13). That is the AI version of not giving a new hire the keys to the vault.

### Develop the talent over time

Treat errors as input for better instructions, examples and tools, and re-test regularly. **Example:** Given METR's finding that task length roughly doubles every 7 months [[9]](#ref-9), a use case that failed a year ago may be worth testing again today. Mollick's advice to assume that today's AI is the worst you will ever use makes the same point [[5]](#ref-5). The next section turns this into a full timeline.

## Plan AI on a timeline, not a snapshot

Stop designing "AI-native" architecture as a snapshot of what today's model can and cannot do. Plan AI the way you develop a person: along a timeline, with roles that grow as trust is earned and as the model itself improves.

A snapshot architecture takes one moment, this quarter's model, this quarter's benchmark, this quarter's failure list, and freezes it into system design, org charts and headcount plans. It treats AI as a fixed component. Every fact in this article says AI is not fixed. There are three ways the snapshot breaks.

### 1. The model under the snapshot keeps moving

A plan sized to today's capability is out of date within months. **Example:** METR's measure of how long a task AI agents can finish on their own has doubled about every 7 months for 6 years [[9]](#ref-9). BCG's François Candelon, who ran the consultant experiment, said the jagged frontier is not only uneven but constantly shifting as capabilities change [[19]](#ref-19). A design that hard-codes "AI can't do X" will be wrong soon; a design that hard-codes "AI can do Y" may be wrong for the next model in a different direction.

### 2. Workarounds for today's weaknesses become tomorrow's dead weight

Much "AI-native" architecture is scaffolding built around a specific model's gaps: rigid chains of prompts, hand-written rules, special-case routing. **Example:** In "The Bitter Lesson" (2019), Rich Sutton reviewed 70 years of AI research and found that general methods that scale with computation beat methods built on hand-coded human knowledge, by a large margin, in chess, Go, speech and vision [[17]](#ref-17). Anthropic gives builders the same advice from its work with dozens of teams: find the simplest solution possible and add complexity only when needed [[18]](#ref-18). Heavy scaffolding locks in today's limits; light, replaceable scaffolding lets the next model's gains flow through.

### 3. A one-time decision about delegation goes stale

A snapshot fixes how much the AI is trusted. That level is wrong in both directions over time. **Example:** Klarna made a snapshot call in 2024: AI could replace about 700 support agents, so hiring stopped. A year later the company reversed course and rehired humans because quality had dropped [[12]](#ref-12). Replit's agent had production access during development until an incident forced a structural change; the right level of access had to be relearned after the fact [[13]](#ref-13). In both cases, trust was set once instead of being earned and reviewed over time.

The alternative is the way good companies treat people. Nobody hires a graduate and writes their permanent job description on day one. They set a development plan: what the person does now, what they must show to take on more, and when they will be reviewed again.

### Practice: a development plan for each AI use case

Turn the timeline into a plan. Give each AI use case a stage, a next stage and the evidence needed to get there, the same way a manager plans a new hire's growth.

[![AI development roadmap: four stages (Intern, Associate, Senior, Trusted Owner) with widening work, access and review; three evidence gates between them; and a re-test loop at every model release or each quarter](/images/articles/ai-talent-roadmap-en.svg)](/images/articles/ai-talent-roadmap-en.svg)

*Figure: AI development roadmap — 4 stages, 3 gates, 1 re-test loop.*

Each stage widens the work and access the AI gets; each gate is a test it must pass; the re-test loop can move it forward or back. Time to each gate is set by evidence, not by a calendar.

How to run it:

1. **Write one plan per use case, not one architecture for "AI".** Name the current stage, the next stage and the evidence that unlocks it. Uneven ability means different use cases sit at different stages at the same time [[3]](#ref-3).
2. **Make the evaluation set the AI's performance file.** Run the same tests at every review so progress is comparable. Impressions are not enough: METR's developers felt 20% faster with AI while actually being 19% slower [[14]](#ref-14).
3. **Promote on evidence, and demote too.** Move a use case up only when it clears its gate, and back when results fall. Klarna's reversal shows the cost of skipping gates and having to step back later [[12]](#ref-12).
4. **Re-test at every major model release, or at least each quarter.** With capability roughly doubling every 7 months on METR's measure, last year's "no" may be this year's "yes" [[9]](#ref-9).
5. **Invest in what carries over to the next model.** Your data, instructions, evaluation sets and controls keep their value when the model changes. Scaffolding built around one model's gaps usually does not [[17]](#ref-17)[[18]](#ref-18).
6. **Widen access only with controls already in place.** Logged, scoped, revocable permissions, and development separated from production, before the AI reaches the next stage, not after an incident [[13]](#ref-13).

## Where the metaphor breaks

"Like talent" describes how to work with AI, not what AI is. Mollick himself warns that treating AI as a person risks the classic error of pretending a computer is human [[5]](#ref-5). Four differences matter most.

### Accountability cannot be handed over

AI carries no legal or moral responsibility. The person or company that deploys it does.

**Example.** In *Moffatt v. Air Canada* (February 2024), Air Canada's website chatbot wrongly told a grieving customer he could claim a bereavement discount after booking. Before the British Columbia Civil Resolution Tribunal, the airline argued that the chatbot was a separate legal entity responsible for its own actions. The tribunal called this a remarkable submission, held that the chatbot was simply part of Air Canada's website, and ordered the airline to pay C$650.88 plus interest and fees [[15]](#ref-15). A human employee can share blame; an AI cannot.

### It has no career motive

A person works carefully partly because of reputation, promotion and fear of getting it wrong. An AI has none of these. Its behavior follows from how it was trained and the system around it.

**Example.** OpenAI's research shows that models learn to guess confidently because common tests score a lucky guess higher than an honest "I don't know" [[8]](#ref-8). You cannot fix that with a pep talk. Reliability has to be designed in through evaluation, instructions, permissions and review.

### Its mistakes scale

One employee's error affects their own cases. A flaw in a model repeats across every conversation it handles, at the same moment.

**Example.** Klarna reported that its AI assistant handled about 2.3 million conversations in its first month, in more than 35 languages [[12]](#ref-12). At that volume, a small systematic error is a large business problem. Evaluation and guardrails for AI need to be stricter than for any single person.

### It does not remember by default

A person learns from last week's mistake. An LLM starts each session fresh unless the system is built to carry knowledge forward, and its working memory is finite.

**Example.** Anthropic notes that as more information is packed into a model's context, its ability to recall that information accurately goes down, so context must be curated deliberately [[6]](#ref-6). "Developing" AI talent therefore means improving its instructions, knowledge bases and workflows, not expecting it to grow on its own.

So the precise position is: **treat AI like talent when deciding how to use and trust it; treat it like high-impact technology when deciding how to control risk and assign responsibility.**

## Conclusion

If you see LLMs as deterministic technology, you will swing between two mistakes: dropping AI after a few bad outputs, or trusting it blindly where errors are expensive. The BCG consultants, the Avianca lawyers, Klarna and Replit each show one side of that swing.

If you see LLMs as high-potential but not fully controllable talent, the right actions follow naturally. Learn its strengths and weaknesses. Brief it well. Delegate step by step. Measure its performance. Keep controls in place. Widen its role as it proves itself. And plan it on a timeline: a snapshot architecture built around today's model will be outdated by the next one, while a development plan grows with it.

The lasting advantage will not come from simply having AI tools. It will come from **managing AI well**: leading a team of uneven, fast-improving AI talent the way a good manager leads people, inside a framework that keeps risk under control. In one line: **manage it like talent, back it up like engineering.**

## References

1. <span id="ref-1"></span>Wei, J. et al. (2022). [Emergent Abilities of Large Language Models](https://arxiv.org/abs/2206.07682). *Transactions on Machine Learning Research*.
2. <span id="ref-2"></span>Schaeffer, R., Miranda, B. & Koyejo, S. (2023). [Are Emergent Abilities of Large Language Models a Mirage?](https://arxiv.org/abs/2304.15004v2) NeurIPS 2023.
3. <span id="ref-3"></span>Dell'Acqua, F., McFowland III, E., Mollick, E. et al. (2023). [Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf). Harvard Business School Working Paper 24-013.
4. <span id="ref-4"></span>Mollick, E. (2023). [Centaurs and Cyborgs on the Jagged Frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged). *One Useful Thing*.
5. <span id="ref-5"></span>Mollick, E. (2024). *Co-Intelligence: Living and Working with AI*. Portfolio/Penguin. See also [Knowledge at Wharton interview](https://knowledge.wharton.upenn.edu/article/co-intelligence-how-to-live-and-work-with-ai/) and [Big Think summary of his principles](https://bigthink.com/business/principles-for-leading-with-ai/).
6. <span id="ref-6"></span>Anthropic (2025). [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
7. <span id="ref-7"></span>*Mata v. Avianca, Inc.*, No. 22-cv-1461 (PKC) (S.D.N.Y. June 22, 2023). [Opinion and Order on Sanctions](https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54).
8. <span id="ref-8"></span>OpenAI (September 5, 2025). [Why language models hallucinate](https://openai.com/index/why-language-models-hallucinate/).
9. <span id="ref-9"></span>METR (March 19, 2025). [Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/).
10. <span id="ref-10"></span>METR (July 14, 2025). [How Does Time Horizon Vary Across Domains?](https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains)
11. <span id="ref-11"></span>Brynjolfsson, E., Li, D. & Raymond, L. (2023/2025). [Generative AI at Work](https://www.nber.org/papers/w31161). NBER Working Paper 31161; *Quarterly Journal of Economics* 140(2).
12. <span id="ref-12"></span>Klarna's AI customer service reversal: [CX Today, May 12, 2025](https://www.cxtoday.com/contact-center/klarna-grapples-with-ai-led-customer-service-pivots-to-an-uber-type-of-setup/) (citing Bloomberg); [Tech.co, May 20, 2025](https://tech.co/news/klarna-reverses-ai-overhaul).
13. <span id="ref-13"></span>Replit / SaaStr database incident: [The Register, July 21, 2025](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident); [SaaStr on Replit's fixes](https://www.saastr.com/replits-new-release-address-most-of-the-challenges-we-hit-vibe-coding-but-is-prosumer-vibe-coding-really-ready-for-commercial-apps-yet).
14. <span id="ref-14"></span>Becker, J., Rush, N., Barnes, B. & Rein, D. / METR (July 10, 2025). [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/).
15. <span id="ref-15"></span>*Moffatt v. Air Canada*, 2024 BCCRT 149. [ABA Business Law Today summary](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/); [CTV News report](https://www.ctvnews.ca/vancouver/article/air-canadas-chatbot-gave-a-bc-man-the-wrong-information-now-the-airline-has-to-pay-for-the-mistake/).
16. <span id="ref-16"></span>Harvard Business School Working Knowledge (2023). [Humans vs. Machines: Untangling the Tasks AI Can (and Can't) Handle](https://www.library.hbs.edu/working-knowledge/humans-vs-machines-untangling-the-tasks-ai-can-and-cant-handle).
17. <span id="ref-17"></span>Sutton, R. (March 13, 2019). [The Bitter Lesson](https://mlanthology.org/misc/2019/sutton2019misc-bitter).
18. <span id="ref-18"></span>Anthropic (December 19, 2024). [Building effective AI agents](https://www.anthropic.com/engineering/building-effective-agents).
19. <span id="ref-19"></span>VentureBeat (September 25, 2023). [Enterprise workers gain 40 percent performance boost from GPT-4, Harvard study finds](https://venturebeat.com/ai/enterprise-workers-gain-40-percent-performance-boost-from-gpt-4-harvard-study-finds).
