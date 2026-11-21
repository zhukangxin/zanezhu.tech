---
title: "AI转型为何必然失败：当AI只是技术，而不是CEO的战略"
date: 2026-11-21
description: "企业AI的失败，大多不是模型不够好，而是管理方式错了。如果AI不是CEO持续投入的战略，不被当作人才培养，不立足业务流程重构和运营体系变革，只从底层着眼于一次性的部署、应用和架构，失败几乎是必然的。本文用三个失败案例和两个成功对照来说明。"
tags: ["人工智能","AI战略","数字化转型","组织变革","CEO领导力"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_zh_why-ai-transformations-fail.png"
draft: false
---

## 引言：失败的不是模型，是管理方式

企业AI的失败，绝大多数不是因为模型不够好，而是因为管理方式错了。把AI当成一次性采购的IT项目，从底层的架构和部署做起，却不改变战略、人才和运营，结果几乎注定是"试点很热闹，利润表没变化"。

我的判断是：AI要产生企业级的价值，必须同时满足五个条件，缺一个就会失败。

1. **CEO的战略持续投入**：AI是CEO亲自牵头、跨年度持续投入的战略，而不是CIO的一个预算科目。
2. **把AI当作人才对待**：AI像新员工一样，有岗位、有职责、有绩效，也有上岗边界。
3. **持续培养，而非一次交付**：模型、数据、提示和知识库需要持续"带教"，员工也需要持续再培训。
4. **立足业务流程重构**：先问"这项工作应该怎样做"，再问"AI放在哪里"。
5. **改变运营体系**：组织结构、考核、风控、决策权和人机分工都要随之调整。

反面的做法则高度一致：只把AI当技术，只从底层开始，着眼于一次性的部署、应用和架构。

在[上一篇文章](/zh/articles/manage-ai-like-talent/)里，我讨论了为什么应该"像培养人才一样管理AI"。这一篇往上走一层：从CEO和组织的角度，看为什么缺少这五个条件的AI转型会失败。下面先看全局数据，再看三个失败案例和两个成功对照。

## 全局证据：价值的70%在技术之外

三份主流研究指向同一个结论：决定AI成败的，是领导力、人和流程，而不是算法本身。

| 研究 | 关键发现 | 对本文论点的含义 |
| --- | --- | --- |
| MIT NANDA《The GenAI Divide》（2025年7月）[[1]](#ref-1) | 约95%的企业生成式AI试点，对利润表没有可衡量的影响；企业在这一领域的投入约300亿–400亿美元。报告把原因归于脆弱的工作流、缺乏情境学习，以及与日常运营脱节 | 失败不在模型，而在"不改流程、不持续学习" |
| BCG"10-20-70"法则 [[2]](#ref-2) | AI价值约10%来自算法，20%来自技术与数据，70%来自人和流程；领先企业计划对一半以上员工做AI再培训，落后企业约20% | 只管底层架构，等于只做了30%的事 |
| 麦肯锡《State of AI 2025》[[3]](#ref-3) | 只有约6%的企业是AI高绩效者（AI贡献≥5% EBIT）；工作流重构是对业务影响贡献最大的因素之一；高绩效者"强烈认同高层展现了对AI的主导权与承诺"的可能性是同行的3倍 | 流程重构 + 高层亲自牵头 |
| 麦肯锡2025年3月调研 [[4]](#ref-4) | CEO亲自监督AI治理，是与利润影响相关性最高的因素之一，在大公司尤其明显 | CEO是变量，不是旁观者 |

麦肯锡QuantumBlack负责人的一句话概括了这个差别：给员工一个AI工具，只能让旧任务做得更快；围绕AI重新设计工作流，才能改变流程的经济性 [[5]](#ref-5)。

需要说明的是，MIT的95%口径较窄（指"快速带来可衡量的损益影响"），业界对其方法也有争议。但三份独立研究的方向一致，结论是稳健的。

## 案例一：MD Anderson × IBM Watson——缺少战略治理的"技术项目"

**结果。** 美国德州大学MD Anderson癌症中心从2012年6月起与IBM合作，开发"肿瘤专家顾问"（Oncology Expert Advisor，OEA）。四年花费6,210万美元，既没有用于临床，也没有在院外试点，2016年9月终止 [[6]](#ref-6)。

**失败机制。**

- **没有进入机构的战略与治理体系。** 德州大学系统的审计发现，项目绕开了正常的IT采购流程，近4,000万美元付给IBM、2,100多万美元付给普华永道，几乎都未经董事会批准 [[7]](#ref-7)。这是一个部门的"旗舰项目"，而不是机构层面的长期战略。
- **目标反复漂移。** 审计认为项目战略不聚焦，没有达到目标。Engadget的分析指出，项目的重点从白血病转向肺癌，技术也不断切换；而参与的医生其实认可系统的能力 [[8]](#ref-8)。
- **没有嵌入临床流程。** 医院更换了电子病历系统，而OEA始终没有与新系统集成 [[7]](#ref-7)。AI一直是"外挂工具"，没有成为诊疗流程的一部分。

**对应论点。** 技术并不是最大的问题，审计特别声明不评价系统的科学基础。问题在于：缺少最高层的持续战略归属，把AI当成一次性外包构建的技术项目，也没有重构临床流程。

## 案例二：Klarna——把AI当"降本工具"，而不是需要培养的"人才"

**结果。** 瑞典金融科技公司Klarna在2023年12月冻结招聘，宣称AI客服上线第一个月就处理了三分之二的对话，相当于700名客服的工作量 [[9]](#ref-9)。到2025年5月，CEO Sebastian Siemiatkowski在接受彭博社采访时承认服务质量下降，开始重新招聘人工客服。他的反思是：成本在评估中占比过高，结果就是"更低的质量" [[10]](#ref-10)。

**失败机制。**

- **评价体系只看成本。** AI的"绩效"用处理量和省下的人头来衡量，而不是用客户结果来衡量。这是典型的"把AI当技术"，而不是"把AI当岗位上的员工"：我们不会只用工资成本来考核一位新员工。
- **一步到位替代，而不是分级上岗。** 没有先划定AI能独立处理的问题范围、再逐步扩大权限；复杂、带情绪的对话也交给了AI。
- **人机分工是事后补课。** 纠偏后的模式是AI处理常规问题、人工负责高价值对话，这本应在上线前就设计好。

**客观补充。** Klarna并没有放弃AI。CEO表示AI承担的客服工作还在增加，新招的人工主要处理更高阶的对话 [[11]](#ref-11)。这恰好说明：AI本身是可用的，失败的是"成本导向、一次性替代"的管理思路。

**对应论点。** 不把AI当人才对待，不设计培养和分级上岗机制，即使CEO高调推动，也会以客户体验为代价。

## 案例三：Zillow Offers——有CEO战略，却没有配套的运营体系

**结果。** 美国房地产平台Zillow从2018年起，用定价算法收购、翻新、转售房屋。CEO Rich Barton亲自推动，目标是到2024年每月买入5,000套房 [[14]](#ref-14)。2021年11月，这项业务关停，减值最高5.69亿美元，裁员约25% [[12]](#ref-12)。

**失败机制。**

- **把一个预测模型当成了整个业务。** 公司无法准确预测3–6个月后的房价，单位经济的波动超出预期 [[13]](#ref-13)。
- **运营和风控没有跟上算法的扩张速度。** 库存从第二季度的3,142套升到第三季度的9,790套 [[13]](#ref-13)。买入速度远超翻新、转售和风险管理的承载能力。
- **缺少人机制衡和持续纠偏。** Barton事后承认，定价失误的风险超出预期，公司实际上变成了一个高杠杆的房产交易商 [[14]](#ref-14)。

**对应论点。** 这个案例很重要，因为Zillow并不缺CEO投入。它证明了五个条件"缺一不可"：只有战略热情，却把AI当作一次性调好的技术引擎，不同步重构运营和风控体系，仍然会失败，而且规模越大，代价越大。

## 正面对照：做对了会怎样

### 星展银行（DBS）：CEO主导的十年持续投入

星展银行的AI经济价值，从2022年的1.8亿新元 [[15]](#ref-15)，增长到2023年的3.7亿新元、2024年的7.5亿新元，再到2025年的约10亿新元 [[16]](#ref-16)。

- **CEO亲自牵头，跨任期延续。** 高博德（Piyush Gupta）2009年出任CEO，亲自推动星展向数据和AI驱动转型 [[17]](#ref-17)。2025年3月由陈淑珊接任，她此前负责把数字化战略落实到各项业务，上任后继续加速AI转型 [[18]](#ref-18)。
- **用经济价值而不是项目数量考核AI。** 星展用实验组与对照组的方法，只把两者的差值计为AI价值。首席数据与转型官Nimish Panchmatia直言：问题不在技术，而在人、结构和文化 [[19]](#ref-19)。
- **重构运营模式。** 星展拿到约10亿新元的价值，靠的不是在旧流程上叠加AI工具，而是重新设计运营模式 [[20]](#ref-20)。

### Moderna：把AI当"人才"纳入组织设计

- **合并人力资源与IT。** Moderna把人力资源部门和技术部门合并为一个部门，由原首席人力官Tracey Franklin出任"首席人力与数字技术官" [[21]](#ref-21)。
- **从"人力规划"转向"工作规划"。** 她按"哪些工作由人做、哪些由技术做"来重新设计团队，岗位因此被新增、取消或重塑 [[22]](#ref-22)。
- **AI规模化上岗。** Moderna与OpenAI合作，开发了3,000多个定制GPT，嵌入员工的日常工作 [[21]](#ref-21)。

Moderna的做法，是"把AI当人才"最字面的实践：AI和员工在同一个部门、同一套工作设计里被规划、分工和培养。

## 结论：两种思维，两种结局

五个案例说明，AI不是一次买断的系统，而是一种需要战略引领、持续培养、并重塑组织的新型劳动力。

| 维度 | "技术项目"思维（失败路径） | "战略+人才"思维（成功路径） | 案例对照 |
| --- | --- | --- | --- |
| 谁来负责 | CIO或单个部门，绕开治理 | CEO亲自牵头，跨任期延续 | MD Anderson vs 星展 |
| 投入方式 | 一次性预算，交付即结束 | 持续投入，按经济价值滚动追加 | MD Anderson vs 星展 |
| 如何看待AI | 降本工具，替代人头 | 有岗位、有绩效、分级上岗的"人才" | Klarna vs Moderna |
| 从哪里入手 | 底层架构、模型、部署 | 业务流程与工作设计 | Zillow vs 星展 |
| 运营体系 | 不变，AI外挂 | 组织、考核、风控同步重构 | Zillow vs Moderna |

**给CEO的六条行动清单**

1. **亲自挂帅。** CEO本人负责AI战略与治理，并做出3–5年的持续投入承诺。
2. **按"10-20-70"分配精力。** 大部分精力放在人和流程上，而不是算法和平台。
3. **给AI"定岗定编"。** 写清AI的职责、权限边界、人工复核点和KPI；先小范围上岗，达标再扩权。
4. **建立持续培养机制。** 数据、知识库和反馈闭环持续迭代；同时为员工安排AI再培训。
5. **从流程开始，而不是从架构开始。** 选定少数端到端的核心流程，重新设计人机分工。
6. **用经济价值而不是项目数量来评估。** 用对照实验量化AI对收入、成本、风险和客户体验的影响。

最后要说明："必然失败"是概率意义上的判断。个别点状项目即使不改流程，也能提升个人效率，但它们很难进入利润表。从"试点成功"走到"企业级价值"的那一步，没有捷径。

## 相关阅读

- [像培养人才一样管理AI，而不是像部署软件](/zh/articles/manage-ai-like-talent/)
- [从 All Online 到 Autonomous：银行系统数字化与AI化的三阶段路径](/zh/articles/bank-ai-path-all-online-to-autonomous/)

## 参考文献

文献保留英文原始标题，便于查找。

1. <span id="ref-1"></span>MIT Media Lab, Project NANDA (2025年7月). *The GenAI Divide: State of AI in Business 2025*. 报道见 [Campus Technology, 2025年8月26日](https://campustechnology.com/articles/2025/08/26/mit-report-most-organizations-see-no-business-return-on-gen-ai-investments.aspx)；[Fortune, 2025年8月18日](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)。
2. <span id="ref-2"></span>Boston Consulting Group (2026). [AI Transformation Is a Workforce Transformation](https://web-assets.bcg.com/pdf-src/prod-live/ai-transformation-is-a-workforce-transformation.pdf)。
3. <span id="ref-3"></span>McKinsey & Company (2025). [The State of AI in 2025: Agents, Innovation, and Transformation](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025)。
4. <span id="ref-4"></span>McKinsey & Company (2025年3月12日). [The State of AI: How Organizations Are Rewiring to Capture Value](https://mckinsey.com/capabalities/quantumblack/our-insights/the-state-of-ai-how-organizations-are-rewiring-to-capture-value)。
5. <span id="ref-5"></span>McKinsey & Company. [Four Perspectives on What Matters Now in AI](https://www.mckinsey.com/about-us/new-at-mckinsey-blog/four-perspectives-on-what-matters-now-in-ai)。
6. <span id="ref-6"></span>The Register (2017年2月20日). [Watson Can't Cure Cancer … or All the Stuff That Breaks IT Projects](https://www.theregister.com/2017/02/20/watson_cancerbusting_trial_on_hold_after_damning_audit_report/)；另见 [ITPro, 2017年2月24日](https://www.itpro.com/business-intelligence/28193/big-data-news-university-of-texas-pulls-plug-on-ibm-big-data-project)。
7. <span id="ref-7"></span>Network World (2017年3月9日). [Texas Hospital Struggles to Make IBM's Watson Cure Cancer](https://www.networkworld.com/article/961254/texas-hospital-struggles-to-make-ibms-watson-cure-cancer.html)。
8. <span id="ref-8"></span>Engadget (2017年2月20日). [Watson-Based Cancer Project Paused After Running Aground](https://www.engadget.com/2017-02-20-watson-cancer-research-runs-into-trouble.html)。
9. <span id="ref-9"></span>TechSpot. [Klarna Is Hiring Humans Again as AI Replacements Fail to Deliver](https://www.techspot.com/news/107881-klarna-hiring-humans-again-ai-replacements-fail-deliver.html)。
10. <span id="ref-10"></span>eMarketer. [Klarna Backtracks AI Customer Service Plans](https://www.emarketer.com/content/klarna-backtracks-ai-customer-service-plans)。原始采访见彭博社 (2025年5月8日). [Klarna Turns From AI to Real Person Customer Service](https://www.bloomberg.com/news/articles/2025-05-08/klarna-turns-from-ai-to-real-person-customer-service)。
11. <span id="ref-11"></span>CMSWire (2025年5月20日). [Klarna CEO: We're Giving AI More Customer Service Work, Not Less](https://www.cmswire.com/contact-center/klarna-ceo-were-giving-ai-more-customer-service-work-not-less/)。
12. <span id="ref-12"></span>Bloomberg (2021年11月2日). [Zillow Shuts Home-Flipping Business After Racking Up Losses](https://www.bloomberg.com/news/articles/2021-11-02/zillow-shuts-down-home-flipping-business-after-racking-up-losses)。
13. <span id="ref-13"></span>GeekWire (2021年11月2日). [Zillow to Shutter Home-Buying Business, Lay Off 2K Employees](https://www.geekwire.com/2021/zillow-shutter-home-buying-business-lay-off-2k-employees-big-real-estate-bet-falters/)。
14. <span id="ref-14"></span>Boston.com，转载彭博社 (2021年11月4日). [At Risk of Losing Millions, Zillow Ends Its House-Flipping Operation and Cuts Its Workforce](https://www.boston.com/real-estate/untagged/2021/11/04/zillow-ends-house-flipping-operation/)。
15. <span id="ref-15"></span>DBS (2023年8月7日). [DBS' AI-Powered Digital Transformation](https://dbs.com/artificial-intelligence-machine-learning/artificial-intelligence/dbs-ai-powered-digital-transformation.html)。
16. <span id="ref-16"></span>Forrester (2026年1月22日). [DBS Bank's Billion-Dollar AI Dream — Realized](https://www.forrester.com/blogs/dbs-banks-billion-dollar-ai-dream-realized)；另见 [DBS, Singapore FinTech Festival 2025](https://www.dbs.com/artificial-intelligence-machine-learning/artificial-intelligence/singapore-finTech-festival-2025-powering-dbs-next-phase-of-growth-with-ai.html)（2025年11月12日，2024年数据）。
17. <span id="ref-17"></span>McKinsey & Company (2025年2月10日). [An Inside Look at How McKinsey Helped DBS Become an AI-Powered Bank](https://www.mckinsey.com/about-us/new-at-mckinsey-blog/an-inside-look-at-how-mckinsey-helped-dbs-become-an-ai-powered-bank)；Fortune (2024年8月7日). [DBS's Next CEO Will Be Tan Su Shan](https://fortune.com/asia/2024/08/07/dbs-next-ceo-tan-su-shan-first-woman-lead-southeast-asia-largest-bank/)。
18. <span id="ref-18"></span>McKinsey & Company (2025年9月23日). [DBS CEO Tan Su Shan on Building a Gen AI–Enabled Bank with a Heart](https://www.mckinsey.com/sg/our-insights/dbs-ceo-tan-su-shan-on-building-a-gen-ai-enabled-bank-with-a-heart)。
19. <span id="ref-19"></span>Google Cloud Transform (2026年3月11日). [How DBS, Singapore's Largest Bank, Builds AI with Confidence](https://cloud.google.com/transform/how-dbs-singapores-largest-bank-builds-ai-with-confidence)。
20. <span id="ref-20"></span>Computer Weekly (2026年初). [DBS Rewires Operating Models for AI Reasoning Era](https://www.computerweekly.com/news/366639844/DBS-rewires-operating-models-for-AI-reasoning-era)。
21. <span id="ref-21"></span>UNLEASH (2025年6月27日). [Why Moderna Merged HR and IT to Better Architect the Flow of Work](https://www.unleash.ai/artificial-intelligence/why-moderna-merged-hr-and-it-to-better-architect-the-flow-of-work/)。
22. <span id="ref-22"></span>Isabelle Bousquette, The Wall Street Journal (2025年5月12日). Why Moderna Merged Its Tech and HR Departments. [转载](https://www.itiger.com/news/2534822307)。
