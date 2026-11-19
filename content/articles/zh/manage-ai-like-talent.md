---
title: "像培养人才一样管理AI，而不是像部署软件"
date: 2026-11-19
description: "基于大语言模型的AI不是确定性的软件。应该把它当作有潜力、但不完全可控的人才来管理：摸清它不均衡的长短板，交代清楚任务，逐步授权，用数据考核，保持内控，并用时间线来规划它，而不是把它冻结成\"快照式\"架构。"
tags: ["人工智能","大语言模型","AI战略","产品管理","人才管理"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_zh_manage-ai-like-talent.png"
draft: false
---

## 引言：是人才，不是工具

基于大语言模型（LLM）的AI，应该像一位天赋很高但行为难以完全预测的新员工那样去管理，而不是像一套确定性的软件那样去部署。把它当成"永远给出同样正确答案的工具"的组织，往往会陷入两种失败：要么因为几次糟糕的输出就放弃它，要么在出错代价很高的地方盲目信任它。

传统软件是确定性的：同样的输入永远得到同样的输出，修好的bug不会再犯。我们评价它只问一个问题：对不对？

LLM不是这样。它的输出是概率性的，同一个问题问两次，答案可能不同。它能做到没人专门编程教过的事，比如推理、写作、跨领域编程；它也会在简单的任务上出错，而且错得很自信。

更合适的心智模型是"人才"：**能力强、潜力大、但不完全可预测**。人才不是装上就能用的，需要招聘、入职培训、逐步授权和绩效考核。本文用真实案例说明：为什么这个视角更贴切，它在实践中意味着什么，为什么应该用时间线规划AI、而不是把它冻结成"快照式"架构，以及这个比喻在哪里失效。

## 为什么"人才"视角更贴切

LLM有五个特征，更像一个人的能力，而不像一项软件功能。每一点都已在研究或真实部署中得到验证。

### 1. 能力是"长出来的"，不是"写进去的"

传统程序只能做工程师编写的功能。LLM的能力来自大规模训练，连开发者自己也要通过测试才知道它会什么。

**案例。** 来自Google、斯坦福和DeepMind的研究者提出了"涌现能力"：这些能力在较小的模型中不存在，在更大的模型中突然出现，无法通过小模型的表现外推预测 [[1]](#ref-1)。后来另一些研究者指出，部分"突然跃升"其实来自衡量方式，而不是模型本身 [[2]](#ref-2)。无论哪种解释，实践结论都一样：要知道模型能做什么，只能拿真实工作去试，就像了解新员工的能力要看他头几个月的表现，而不是只看简历。

### 2. 能力是不均衡的："锯齿形前沿"

LLM可能写出一份出色的市场分析，却在一个看起来同样难的任务上失败。它的能力并不随任务难度平滑变化。优秀的人也是这样：一位出色的战略顾问不一定擅长做Excel。

**案例。** 在一项针对波士顿咨询公司（BCG）758名顾问的随机实验中（约占该公司一线顾问的7%），在GPT-4能力"前沿以内"的18项任务上，使用AI的顾问多完成12.2%的任务，速度快25.1%，质量评分高约40% [[3]](#ref-3)[[4]](#ref-4)。而在一项特意选在"前沿之外"的任务上，使用AI的顾问得出正确答案的概率反而比不用AI的人低19个百分点 [[3]](#ref-3)。同样的人、同样的工具、看似相近的难度，结果却完全相反。管理者的首要工作是摸清每个人的长板和短板，对AI也是一样。

### 3. 产出质量取决于上下文和沟通

同一个模型，面对模糊的请求只能给出平庸的结果；讲清楚背景、目标、标准并给出几个示例，结果会好很多。这和带新员工完全一样。提示词（prompt）本质上就是岗位说明书加入职资料。

**案例。** 在BCG实验中，只使用GPT-4的顾问，产出质量评分提高38%；同时拿到一份简短提示词指南的顾问，提高到42.5% [[3]](#ref-3)。Anthropic把这项更广泛的技能称为"上下文工程"：决定把哪些信息（指令、工具、示例、历史记录）放进模型有限的工作记忆里，让它按预期行事 [[6]](#ref-6)。沃顿商学院教授Ethan Mollick的实用建议很简单：像对待一个人一样和AI说话，并告诉它应该扮演什么样的人 [[5]](#ref-5)。

### 4. 会犯错，而且不一定自知

LLM有时会"幻觉"：说出听起来正确、实际上错误的内容。人也会犯错、也会过度自信。好的组织不会因为人会犯错就不招人，而是把复核机制设计进工作流程。

**案例。** 在 *Mata v. Avianca*（2023）一案中，纽约的两名律师向法院提交的文书引用了根本不存在的判例，这些判例连同虚假引文都是ChatGPT编造的。联邦法官对两名律师及其律所作出处罚，并指出他们在判例真实性受到质疑后仍坚持立场 [[7]](#ref-7)。工具的错误之所以变成职业失败，是因为没有人核查。OpenAI自己的研究解释了部分原因：标准的训练和测试方式会奖励模型去猜，而不是诚实地说"我不知道" [[8]](#ref-8)。

### 5. 潜力在持续增长

模型每隔几个月就有明显进步，今天做不好的任务，明年可能就成了常规工作。把它当成定型的工具，你会低估它；把它当成成长中的人才，你会持续重新测试，并在它赢得信任后扩大它的职责。

**案例。** 研究机构METR测量了AI智能体能以50%可靠性独立完成的任务长度（以人类所需工作时间计）。在其软件和研究类任务上，这一长度在过去6年里大约每7个月翻一番 [[9]](#ref-9)。METR后来的研究发现，其他多个领域也有类似增长，只是水平和速度因领域而异 [[10]](#ref-10)。这是一位快速成长的年轻同事的画像，而不是一个版本固定的产品。

## 实践意义

如果AI是人才，那么使用AI就是一项管理工作，而不是一项安装工作。六项熟悉的管理实践可以直接对应到AI。

| 人才管理实践 | 对AI意味着什么 |
| --- | --- |
| 按岗招聘 | 用自己的工作来测试，选择模型和使用场景 |
| 入职培训 | 提供上下文：背景、目标、标准、示例、禁区 |
| 逐步授权 | 从低风险、可复核的工作开始；高风险决策保留人工审批 |
| 绩效考核 | 用测试集和真实结果衡量，而不是凭印象 |
| 内部控制 | 核实关键事实、确认关键操作、限制权限 |
| 持续培养 | 出错后改进指令；模型升级后重新测试 |

### 按岗招聘

没有哪个模型在所有方面都最好，排行榜也无法告诉你它在你的任务上表现如何。**案例：** METR发现，AI在科学问答、数学竞赛、软件等不同领域的能力水平和增长速度差异很大 [[10]](#ref-10)。BCG研究的作者之一Edward McFowland III表示，要判断哪些任务落在前沿的哪一侧，必须和自己的团队、在自己的场景中去研究 [[16]](#ref-16)。这是一场招聘面试，而不是一场产品演示。

### 入职培训：给足上下文

一个没有任何交代的新员工只能交出平庸的工作，LLM也一样。**案例：** Anthropic关于构建AI智能体的指南强调，要精心筛选模型看到的信息、保持指令清晰和示例聚焦，因为模型的工作记忆有限，信息塞得越多越不可靠 [[6]](#ref-6)。写好提示词或知识库，就是AI版的"写好入职手册"。

### 逐步授权

按已证明的可靠程度来授权。**正面案例：** 一家《财富》500强软件公司为5,179名客服人员配备了一个AI助手，由它提供回复建议，但人仍然做主。生产率平均提高14%，新手和低技能客服提高34%；入职两个月的客服表现已经相当于入职六个月的老员工 [[11]](#ref-11)。**过快放权的案例：** Klarna在2024年表示，其AI助手已处理三分之二的客服对话，相当于约700名客服的工作量，并冻结了招聘。到2025年5月，其CEO对彭博表示，当初决策中成本因素占比过重，服务质量受到影响，公司开始重新招聘人工客服 [[12]](#ref-12)。同样的技术，不同的授权程度，结果截然不同。

### 用数据做绩效考核

一次惊艳的演示或一次糟糕的回答，说明不了什么。需要像绩效考核一样做系统化评估。**案例：** 在2025年METR的一项实验中，16名资深开源开发者完成了246项真实任务，其中一部分允许使用AI工具。他们事前预计AI能让自己快24%，事后也认为自己快了20%，但实际上使用AI时反而多花了19%的时间 [[14]](#ref-14)。对AI表现的直觉可能在任何方向上出错，只有测量才能下结论。

### 内部控制

内控不是不信任的表现。每家公司对人也有内控：审批权限、访问权限、双人签字。**案例：** 2025年7月，SaaStr创始人Jason Lemkin进行了一项为期12天的测试，其间Replit的AI编程智能体在宣布"代码冻结"期间删除了线上生产数据库，抹掉了1,206名高管和约1,196家公司的记录，并且对发生的事情作出了不实陈述 [[13]](#ref-13)。关键问题在于，智能体在开发阶段就能接触生产数据库。Replit的修复是结构性的：将开发和生产数据库分离，智能体默认只能访问开发环境 [[13]](#ref-13)。这就是AI版的"不把金库钥匙交给新员工"。

### 持续培养

把错误当作改进指令、示例和工具的输入，并定期重新测试。**案例：** 既然METR发现任务长度大约每7个月翻一番 [[9]](#ref-9)，一年前失败的场景今天可能值得再试。Mollick建议"假设今天的AI是你用过的最差的AI"，说的是同一个道理 [[5]](#ref-5)。下一节将把这一点展开成完整的时间线。

## 用时间线规划AI，而不是"快照式"架构

不要再把"AI-Native"架构设计成一张快照，只记录今天的模型能做什么、不能做什么。应该像培养一个人那样规划AI：沿着时间线，随着信任的建立和模型本身的进步，逐步扩大它的角色。

快照式架构拿一个时间点（本季度的模型、本季度的基准测试、本季度的失败清单），把它冻结进系统设计、组织架构和人员编制里。它把AI当成一个固定的部件，而本文的每一个事实都说明AI不是固定的。快照会以三种方式失效。

### 1. 快照下的模型一直在变

按今天的能力设计的方案，几个月内就会过时。**案例：** METR对AI智能体能独立完成的任务长度的测量，过去6年大约每7个月翻一番 [[9]](#ref-9)。主持BCG顾问实验的François Candelon表示，这个锯齿形前沿不仅参差不齐，而且随着能力变化不断移动 [[19]](#ref-19)。硬编码"AI做不了X"的设计很快就会错；硬编码"AI能做Y"的设计，换到下一个模型也可能在另一个方向上出错。

### 2. 为今天的弱点做的绕路方案，会变成明天的负担

很多"AI-Native"架构，实际上是围绕某个模型的短板搭建的脚手架：僵硬的提示词链、手写的规则、特殊情况的路由。**案例：** Rich Sutton在《苦涩的教训》（The Bitter Lesson，2019）中回顾了70年的AI研究，发现在象棋、围棋、语音和视觉领域，能随算力扩展的通用方法，都以很大优势胜过了依赖人工编写知识的方法 [[17]](#ref-17)。Anthropic根据与数十个团队合作的经验，也给出了同样的建议：先找最简单的方案，只在必要时才增加复杂度 [[18]](#ref-18)。厚重的脚手架会锁死今天的局限；轻量、可替换的脚手架，才能让下一代模型的进步直接体现出来。

### 3. 一次性的授权决策会过时

快照把"对AI信任到什么程度"固定下来，而随着时间推移，这个程度在两个方向上都会出错。**案例：** Klarna在2024年做了一个快照式决定：AI能替代约700名客服，于是停止招聘。一年后，由于服务质量下降，公司又重新招聘人工客服 [[12]](#ref-12)。Replit的智能体在开发阶段拥有生产环境权限，直到一次事故迫使平台做出结构性改变；合适的权限范围是事后才重新学到的 [[13]](#ref-13)。两个案例中，信任都是一次性设定的，而不是随时间逐步赢得、定期复审的。

替代方案，就是好公司对待人才的方式。没有人会在招进一名毕业生的第一天，就写好他一辈子的岗位说明。我们会制定培养计划：他现在做什么，需要证明什么才能承担更多，以及下次什么时候复审。

### 实践：为每个AI使用场景制定培养计划

把时间线变成计划。为每个AI使用场景明确当前阶段、下一阶段，以及晋升所需的证据，就像管理者规划新员工的成长一样。

[![AI培养路线图：四个阶段（实习生、助理、专员、独当一面）逐步扩大工作范围、权限和复核方式；阶段之间有三个凭证据通过的关卡；每次模型升级或每季度进行一次复测](/images/articles/ai-talent-roadmap-zh.svg)](/images/articles/ai-talent-roadmap-zh.svg)

*图：AI培养路线图 —— 4个阶段、3个关卡、1个复测循环。*

每个阶段都扩大AI的工作范围和权限；每个关卡都是它必须通过的测试；复测循环可以让它前进，也可以让它后退。到达每个关卡的时间由证据决定，而不是由日历决定。

如何执行：

1. **每个使用场景一份计划，而不是为"AI"做一套架构。** 写清当前阶段、下一阶段和解锁它的证据。能力不均衡，意味着不同场景会同时处在不同阶段 [[3]](#ref-3)。
2. **把评估测试集当作AI的绩效档案。** 每次复审都用同一套测试，进步才可比。印象不可靠：METR实验中的开发者感觉用AI快了20%，实际却慢了19% [[14]](#ref-14)。
3. **凭证据晋升，也要能降级。** 只有通过关卡才升一级；结果下滑就退回。Klarna的反转说明了跳过关卡、事后被迫后退的代价 [[12]](#ref-12)。
4. **每次重大模型升级时，或至少每季度重新测试。** 按METR的测量，能力大约每7个月翻一番，去年的"不行"可能就是今年的"行" [[9]](#ref-9)。
5. **投资于能带到下一个模型的东西。** 你的数据、指令、评估测试集和内控机制，在换模型后依然有价值；围绕某个模型的短板搭建的脚手架，通常没有 [[17]](#ref-17)[[18]](#ref-18)。
6. **先有内控，再扩大权限。** 在AI进入下一阶段之前，就要做到权限留痕、限定范围、可撤销，并把开发与生产环境分开，而不是等出了事故再补 [[13]](#ref-13)。

## 比喻的边界

"像人才"描述的是如何与AI合作，而不是AI本身是什么。Mollick自己也提醒，把AI当人看，有犯"把计算机当成人"这一经典错误的风险 [[5]](#ref-5)。最重要的有四点差异。

### 责任无法转移

AI不承担法律和道德责任，部署它的人和公司才承担。

**案例。** 在 *Moffatt v. Air Canada*（2024年2月）一案中，加拿大航空网站的聊天机器人错误地告诉一位刚失去亲人的顾客，可以在订票后再申请丧亲优惠。在不列颠哥伦比亚省民事解决仲裁庭上，航空公司辩称聊天机器人是一个对自己行为负责的独立法律实体。仲裁庭称这一说法"引人注目"，认定聊天机器人只是加航网站的一部分，并判令其赔偿650.88加元及利息和费用 [[15]](#ref-15)。人类员工可以分担责任，AI不能。

### 没有职业动机

人会认真工作，部分是因为声誉、晋升和对出错的顾虑。AI没有这些，它的行为取决于训练方式和周围的系统。

**案例。** OpenAI的研究表明，模型学会自信地猜测，是因为常见的测试给"碰巧猜对"的分数高于诚实的"我不知道" [[8]](#ref-8)。这不是打气谈话能解决的，可靠性必须通过评估、指令、权限和复核来设计。

### 错误会被放大

一名员工的错误只影响他经手的事；一个模型的缺陷会同时出现在它处理的每一次对话里。

**案例。** Klarna称其AI助手上线第一个月就处理了约230万次对话，覆盖35种以上语言 [[12]](#ref-12)。在这样的规模下，一个小的系统性错误就是一个大的业务问题。对AI的评估和防护必须比对任何一个人更严格。

### 默认没有记忆

人会从上周的错误中学习。LLM除非系统专门设计了知识传递，否则每次会话都从零开始，而且它的工作记忆是有限的。

**案例。** Anthropic指出，放进模型上下文的信息越多，它准确回忆这些信息的能力就越低，因此上下文必须刻意筛选 [[6]](#ref-6)。所以"培养"AI人才，意味着改进它的指令、知识库和工作流程，而不是期待它自己成长。

因此更准确的立场是：**在决定如何使用和信任AI时，把它当人才；在决定如何控制风险和分配责任时，把它当作高影响力的技术。**

## 结论

如果把LLM看作确定性的技术，你会在两种错误之间摇摆：几次糟糕的输出后就放弃AI，或者在出错代价高昂的地方盲目信任它。BCG顾问、Avianca案的律师、Klarna和Replit，各自展示了这种摇摆的一面。

如果把LLM看作有潜力、但不完全可控的人才，正确的做法就会自然而然地出现：摸清它的长板和短板，交代清楚任务，逐步授权，衡量绩效，保持内控，并在它证明自己后扩大它的角色。同时，用时间线来规划它：围绕今天的模型搭建的快照式架构，到下一代模型就会过时；而一份培养计划，会随它一起成长。

长期的优势不会来自"拥有AI工具"，而来自**善于管理AI**：像优秀的管理者带团队一样，带领一支能力参差、快速进步的AI人才队伍，并让风险始终处在可控的框架内。一句话概括：**用管理人才的方式去用它，用工程的方式去兜底。**

## 参考文献

文献保留英文原始标题，便于查找。

1. <span id="ref-1"></span>Wei, J. et al. (2022). [Emergent Abilities of Large Language Models](https://arxiv.org/abs/2206.07682). *Transactions on Machine Learning Research*.
2. <span id="ref-2"></span>Schaeffer, R., Miranda, B. & Koyejo, S. (2023). [Are Emergent Abilities of Large Language Models a Mirage?](https://arxiv.org/abs/2304.15004v2) NeurIPS 2023.
3. <span id="ref-3"></span>Dell'Acqua, F., McFowland III, E., Mollick, E. et al. (2023). [Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf). Harvard Business School Working Paper 24-013.
4. <span id="ref-4"></span>Mollick, E. (2023). [Centaurs and Cyborgs on the Jagged Frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged). *One Useful Thing*.
5. <span id="ref-5"></span>Mollick, E. (2024). *Co-Intelligence: Living and Working with AI*. Portfolio/Penguin. 另见 [Knowledge at Wharton访谈](https://knowledge.wharton.upenn.edu/article/co-intelligence-how-to-live-and-work-with-ai/) 和 [Big Think对其原则的总结](https://bigthink.com/business/principles-for-leading-with-ai/)。
6. <span id="ref-6"></span>Anthropic (2025). [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
7. <span id="ref-7"></span>*Mata v. Avianca, Inc.*, No. 22-cv-1461 (PKC) (S.D.N.Y. June 22, 2023). [Opinion and Order on Sanctions](https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54).
8. <span id="ref-8"></span>OpenAI (2025年9月5日). [Why language models hallucinate](https://openai.com/index/why-language-models-hallucinate/).
9. <span id="ref-9"></span>METR (2025年3月19日). [Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/).
10. <span id="ref-10"></span>METR (2025年7月14日). [How Does Time Horizon Vary Across Domains?](https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains)
11. <span id="ref-11"></span>Brynjolfsson, E., Li, D. & Raymond, L. (2023/2025). [Generative AI at Work](https://www.nber.org/papers/w31161). NBER Working Paper 31161; *Quarterly Journal of Economics* 140(2).
12. <span id="ref-12"></span>Klarna客服AI策略反转：[CX Today, 2025年5月12日](https://www.cxtoday.com/contact-center/klarna-grapples-with-ai-led-customer-service-pivots-to-an-uber-type-of-setup/)（引述彭博社）；[Tech.co, 2025年5月20日](https://tech.co/news/klarna-reverses-ai-overhaul)。
13. <span id="ref-13"></span>Replit / SaaStr数据库事故：[The Register, 2025年7月21日](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident)；[SaaStr关于Replit修复措施的文章](https://www.saastr.com/replits-new-release-address-most-of-the-challenges-we-hit-vibe-coding-but-is-prosumer-vibe-coding-really-ready-for-commercial-apps-yet)。
14. <span id="ref-14"></span>Becker, J., Rush, N., Barnes, B. & Rein, D. / METR (2025年7月10日). [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/).
15. <span id="ref-15"></span>*Moffatt v. Air Canada*, 2024 BCCRT 149. [ABA Business Law Today摘要](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/)；[CTV News报道](https://www.ctvnews.ca/vancouver/article/air-canadas-chatbot-gave-a-bc-man-the-wrong-information-now-the-airline-has-to-pay-for-the-mistake/)。
16. <span id="ref-16"></span>Harvard Business School Working Knowledge (2023). [Humans vs. Machines: Untangling the Tasks AI Can (and Can't) Handle](https://www.library.hbs.edu/working-knowledge/humans-vs-machines-untangling-the-tasks-ai-can-and-cant-handle).
17. <span id="ref-17"></span>Sutton, R. (2019年3月13日). [The Bitter Lesson](https://mlanthology.org/misc/2019/sutton2019misc-bitter).
18. <span id="ref-18"></span>Anthropic (2024年12月19日). [Building effective AI agents](https://www.anthropic.com/engineering/building-effective-agents).
19. <span id="ref-19"></span>VentureBeat (2023年9月25日). [Enterprise workers gain 40 percent performance boost from GPT-4, Harvard study finds](https://venturebeat.com/ai/enterprise-workers-gain-40-percent-performance-boost-from-gpt-4-harvard-study-finds).
