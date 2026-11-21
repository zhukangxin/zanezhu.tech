---
title: "From Telephone Switches to Stablecoins: What Telecom's Competitive History Predicts for the Stablecoin Market"
date: 2026-11-20
description: "The 2026 stablecoin industry looks like telecom in 1984–1991. This article compares stablecoin competition with the history of digital switching, mobile standards and the AT&T breakup, and makes five predictions, each with its preconditions, evidence and falsification signals."
tags: ["Stablecoins", "Telecom", "Competition", "GENIUS Act", "MiCA", "Payments infrastructure"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_en_telecom-stablecoin-competition.png"
draft: false
---

> Related: [What Payments Can Learn from Telecom](/articles/payments-learn-from-telecom/) · [Cross-Border Payments Don't Need Blockchain](/articles/cross-border-payments-dont-need-blockchain/)
>
> Data as of November 2026. Not investment advice.

## Summary

**Main conclusion**: the stablecoin industry in 2026 resembles telecom in 1984–1991. Regulation has just arrived, competing schemes abound, and the technology has not converged. Telecom took about 20 years to go from China's "seven countries, eight systems" to five equipment vendors and one global standard. Following that path, stablecoins will go through three steps: **issuer shake-out → interoperability that commoditizes the product → profits migrating to distribution and applications**. But the two industries differ in six fundamental ways, so the analogy shows direction, not detail.

**Five predictions at a glance** (see Section 6 for preconditions and falsification signals):

| # | Prediction | Telecom parallel | Window | Confidence |
| --- | --- | --- | --- | --- |
| 1 | Issuance converges to 2–3 global USD issuers plus 1–2 local champions per currency zone | Switch vendors shrank from over ten to five | 2027–2032 | Medium-high |
| 2 | Offshore USDT follows the "PHS" path: it survives, but loses share in regulated channels | China's PHS (Xiaolingtong) faded after 3G licences were issued | 2027–2030 | Medium |
| 3 | The "standards war" among stablecoin chains converges, or is abstracted away by an interoperability ("roaming") layer | GSM vs CDMA → LTE | 2028–2032 | Medium |
| 4 | Once regulated stablecoins become interchangeable at par, issuers become "pipes" and value moves to distribution and applications | Long-distance competition after the AT&T breakup; value moved from vendors to operators to apps | After 2029 | Medium-low (depends on regulation) |
| 5 | Non-USD currency zones foster local champions | China's "market for technology" → Huawei, ZTE and peers | 2026–2030 | Medium-high |

## 1. Framework: mapping the layers

This article splits both industries into five layers and compares them layer by layer: which layer competes first, which converges first, and where profits end up.

| Layer | Telecom (1980–2010) | Stablecoins (2014–today) | Logic |
| --- | --- | --- | --- |
| Core product | Switch vendors: Ericsson, Alcatel, Nortel, NEC, Siemens, AT&T/Lucent | Issuers: Tether, Circle, bank consortia, PayPal, HSBC | Supplies the thing being used |
| Technical standard | Mobile standards: GSM, CDMA, TDMA → 3G → LTE | Chains / settlement layers: Ethereum, Tron, Solana, Tempo, Arc | Sets compatibility and scale |
| Interconnection and clearing | Operator interconnection, GSM roaming settlement | Cross-chain protocols, card-network stablecoin settlement (Visa) | Lets users on different networks reach each other |
| Distribution | Operators (AT&T, Regional Bells, China P&T) | Exchanges, wallets, acquirers (Coinbase, Stripe) | Reaches end users |
| Regulation and sovereignty | AT&T breakup, EU-mandated GSM, Chinese industrial policy | GENIUS Act, MiCA, Hong Kong Stablecoins Ordinance | Reshapes market structure |

The premise of the comparison: both are **infrastructure with network effects**, both are moving from closed and fragmented to standardized, and both are treated by states as strategic. Where the analogy breaks is covered in Section 5.

## 2. Telecom's competitive history (1982–2016)

Telecom competition unfolded in the order "fragmentation → regulatory reshaping → standard convergence → vendor consolidation → value migration", over about 30 years.

### 2.1 Key events

| Year | Event | Significance | Source |
| --- | --- | --- | --- |
| 1982 | China's first 10,000-line digital switch goes live in Fuzhou (Fujitsu F-150) | Start of China's digital switching | [Xinmin Weekly](https://img1.xinmin.cn/xmzk/2020-01-06/830106.pdf) |
| 1980s | Provinces import independently, creating "seven countries, eight systems": NEC, Fujitsu, Lucent, Nortel, Ericsson, Siemens, BTM, Alcatel | Fragmented, but fast to build | [ITHome](https://www.ithome.com/0/533/645.htm) |
| 1984-01-01 | AT&T split into a long-distance company plus seven Regional Bells; long distance opened to MCI and Sprint | Regulation separates monopoly and competitive layers | [Wikipedia](https://en.wikipedia.org/wiki/Breakup_of_the_Bell_System), [EBSCO](https://www.ebsco.com/research-starters/history/att-undergoes-divestiture) |
| 1986–1991 | MPT research institutes build domestic switches (DS-2000, HJD-1024, DS-30) | Import substitution begins | [ITHome](https://www.ithome.com/0/616/767.htm) |
| Late 1980s | China's analog mobile network splits into Network A (Motorola) and Network B (Ericsson), very different from each other | Early "standards war" | [Huxiu](https://www.huxiu.com/article/2794258.html) |
| Early 1990s | Domestic 10,000-line switches appear: Great Dragon HJD04, Huawei C&C08 | Rise of China's domestic vendors | [ITHome](https://www.ithome.com/0/522/054.htm) |
| Mid-1990s | Global switch shake-out ends with Ericsson, Alcatel, Siemens, Northern Telecom and AT&T as winners; China plans to merge eight state makers into Great Dragon | Fixed R&D cost drives concentration | [Tech Monitor](https://www.techmonitor.ai/?p=160397) |
| 1990s | Europe mandates GSM; the US sets no standard, and three technologies coexist | Mandated standard vs market choice | [Curwen 2004](https://emeraldinsight.com/insight/content/doi/10.1108/info.2004.27206aab.001/full/html), [eWeek](https://www.eweek.com/mobile/winner-take-all/) |
| 1996 | AT&T spins off Lucent (equipment) | Operations separated from equipment | [Wikipedia](https://en.wikipedia.org/wiki/Alcatel-Lucent) |
| 2007 | GSM holds about 80–85% of 2G; CDMA (IS-95) about 10–15% | The mandated standard wins on scale | [Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_mobile_phone_standards) |
| 2009 | Nortel files for bankruptcy in Canada and the US; assets auctioned to Ericsson, NSN and others | An old giant exits | [Wikipedia](https://en.wikipedia.org/wiki/Nortel), [telecoms.com](https://www.telecoms.com/digital-ecosystem/end-of-an-era) |
| Around 2010 | CDMA operators move to LTE; 4G largely unifies | Standards converge | General industry history |
| 2016 | Nokia acquires Alcatel-Lucent (formed by merger in 2006) | Consolidation complete | [Wikipedia](https://en.wikipedia.org/wiki/Alcatel-Lucent) |

### 2.2 Three patterns

1. **Fixed cost decides how many vendors survive.** Only vendors with enough global share could fund the next generation of products ([Tech Monitor](https://www.techmonitor.ai/?p=160397)). Ren Zhengfei made the same point at the time: China had too many switch makers, each going its own way, and the industry could not raise its overall level ([ITHome](https://www.ithome.com/0/522/054.htm)).
2. **Standards wars are decided by scale and regulation, not just technical merit.** Without a mandated US standard, vendors had to split R&D budgets across three technologies, which slowed progress ([eWeek](https://www.eweek.com/pt/mobile/winner-take-all/)). Losing the standards war did not mean losing the profits: Qualcomm earned patent revenue from both CDMA and GSM 3G standards ([eWeek](https://www.eweek.com/fr/mobile/winner-take-all/)).
3. **Once regulators force interconnection, value moves toward the user side.** After the AT&T breakup, long-distance competition gave consumers more choice and lower prices, while local service got more expensive as cross-subsidies ended ([EBSCO](https://www.ebsco.com/research-starters/history/att-undergoes-divestiture)). Value later moved from vendors to operators, then to applications (general industry history).

## 3. The stablecoin market today (November 2026)

The stablecoin market is about $287 billion, two issuers hold about 85%, and US, EU and Hong Kong rules have split the market into separate compliance zones.

### 3.1 Market structure

- As of November 12, 2026, total stablecoin market cap was $286.885 billion, including USDT at $175.66 billion, USDC at $69.881 billion and USDS at $5.357 billion ([DefiLlama](https://defillama.com/stablecoins)).
- USDT and USDC together hold about 85% ([Crypto Briefing](https://cryptobriefing.com/tether-circle-stablecoin-dominance/)).
- Growth gap: in 2025, USDC's market cap grew about 73% and USDT's about 36% ([DEXTools](https://www.dextools.io/news/stablecoin-market-tops-320-billion-usdc-usdt-june-2026)). By on-chain transfer volume in 2025, USDC carried about $18.3 trillion versus about $13.3 trillion for USDT ([CoinPaprika](https://coinpaprika.com/cs/education/stablecoin-wars)). USDT wins on supply; USDC wins on flow.

### 3.2 Regulation: three regimes

| Jurisdiction | Framework | Status | Effect on competition | Source |
| --- | --- | --- | --- | --- |
| United States | GENIUS Act (signed July 2025) | Effective January 18, 2027; agencies missed the July 2026 one-year deadline; OCC issued the first final rule in October 2026 | Regulates who may issue, not which technology; bars issuers from paying interest to holders | [The Block](https://www.theblock.co/post/408843/us-regulators-miss-genius-acts-one-year-deadline-for-final-stablecoin-rules), [The Block · OCC](https://theblock.co/news/regulation/2026-10-21-occ-final-rule-implementing-trump-signed-genius-act-421470), [Latham & Watkins](https://www.lw.com/en/insights/2025/07/the-genius-act-of-2025-stablecoin-legislation-adopted-in-the-us) |
| European Union | MiCA | Transition ended July 1, 2026; Tether did not seek authorization and USDT left regulated exchanges | The mandated, "GSM-style" path; USDC and EURC become the default | [The Paypers](https://thepaypers.com/crypto-web3-and-cbdc/news/tether-exits-eu-market-as-mica-rules-block-usdt-from-exchanges), [Cryptopolitan](https://cryptopolitan.com/mica-pushes-usdt-out-leaves-usdc-in) |
| Hong Kong | Stablecoins Ordinance (effective August 2025) | First licences granted April 10, 2026 to HSBC and Anchorpoint (Standard Chartered + HKT + Animoca) | Very few licences, banks first | [HKMA](https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/04/20260410-4/), [Caixin Global](https://www.caixinglobal.com/2026-04-10/hong-kong-grants-first-stablecoin-licenses-to-hsbc-standard-charteredbacked-venture-102432744.html) |

US draft rules already show where the bar will sit: a $5 million capital floor for new federal issuers, same-day liquidity buffers and two-business-day redemption; FinCEN estimates the rules will initially cover about 50 issuers ([Finance Magnates](https://www.financemagnates.com/cryptocurrency/regulation/ten-days-to-the-genius-act-deadline-what-the-draft-rules-already-reveal/)). Hong Kong's first two licences came out of 36 applicants ([Caixin Global](https://www.caixinglobal.com/2026-04-10/hong-kong-grants-first-stablecoin-licenses-to-hsbc-standard-charteredbacked-venture-102432744.html)).

### 3.3 What the main players are doing

| Player | Move | Strategic meaning | Source |
| --- | --- | --- | --- |
| Tether | Launched US-compliant USAT in January 2026, issued by Anchorage Digital; chose to leave the EU | Dual track: offshore plus compliant | [Yahoo Finance](https://finance.yahoo.com/news/tether-launches-us-regulated-usat-161314419.html) |
| Circle | Holds MiCA authorization; building its own Arc chain (testnet October 2025); Coinbase revenue-share renewed to 2029 | Secures the compliant position and extends into settlement | [Everstake](https://everstake.one/resources/blog/tempo-vs-arc-stablechains-the-next-generation-of-finance), [KuCoin](https://www.kucoin.com/blog/in-circle-renews-usdc-revenue-sharing-agreement-with-coinbase-through-2029) |
| 21-bank consortium | BofA, Citi, Goldman Sachs, Deutsche Bank, UBS, MUFG and others plan a USD stablecoin in H1 2027, then euro and other G7 currencies | Incumbents enter as a group | [CoinMarketCap](https://coinmarketcap.com/academy/article/21-banks-stablecoin-venture-usd-token-launch-2027) |
| Qivalis (Europe) | A 37-institution group including BBVA plans a euro stablecoin | Currency-zone champion | [Financial News](https://en.fnnews.com/news/202609020839433776) |
| JPMorgan Chase | Not in the consortium; reportedly evaluating its own | A large player keeps its own "standard" | [Banking Dive](https://www.bankingdive.com/news/bofa-wells-fargo-citi-back-upcoming-stablecoin/829318/) |
| Stripe + Paradigm | Tempo mainnet launched March 18, 2026; fees paid in stablecoins; positioned as "stablecoin-neutral" | A distributor integrating down into settlement | [Everstake](https://everstake.one/resources/blog/tempo-vs-arc-stablechains-the-next-generation-of-finance), [CryptoSlate](https://cryptoslate.com/stripe-and-paradigm-reveal-tempo-layer-1-blockchain-for-stablecoin-payments-infrastructure/) |
| Visa | Annualized stablecoin settlement above $25 billion, about ten times a year earlier; five stablecoins on ten chains | The "roaming clearinghouse" role | [crypto.news](https://crypto.news/visa-stablecoin-settlement-volume-25-billion-2026/) |

## 4. Similarities: five dimensions

Five features of early competition are closely aligned across the two industries. They are the basis for using telecom history to project stablecoins.

| Dimension | Telecom | Stablecoins | Strength of evidence |
| --- | --- | --- | --- |
| 1. Fragmentation, then fast concentration | Eight systems → five global vendors | Hundreds of stablecoins, but the top two already hold about 85% | Strong |
| 2. Two regulatory paths: mandate vs laissez-faire | Europe mandates GSM; the US sets no standard | MiCA mandates authorization and delisting; GENIUS regulates issuers, not technology | Strong |
| 3. Fixed-cost barriers eliminate small players | Switch R&D cost | Compliance cost: capital, liquidity, AML, licences | Medium-strong |
| 4. Incumbents enter as consortia | European vendors and operators jointly back GSM | 21-bank consortium; 37-member Qivalis | Medium (not yet live) |
| 5. A "standards war" underneath | Network A/B; GSM/CDMA/TDMA | Ethereum, Tron, Solana, Tempo, Arc, Plasma | Strong |

**Evidence for dimension 1**: after the global switch shake-out, only five vendors had enough share to fund the next generation ([Tech Monitor](https://www.techmonitor.ai/?p=160397)). Stablecoins are still early, yet already more concentrated than switching was then ([Crypto Briefing](https://cryptobriefing.com/tether-circle-stablecoin-dominance/)).

**Evidence for dimension 2**: the US government did not enforce a national standard, so three mobile technologies coexisted ([Curwen 2004](https://emeraldinsight.com/insight/content/doi/10.1108/info.2004.27206aab.001/full/html)). The EU used MiCA to push USDT off regulated exchanges, and USDC and EURC filled the gap ([The Paypers](https://thepaypers.com/crypto-web3-and-cbdc/news/tether-exits-eu-market-as-mica-rules-block-usdt-from-exchanges)).

**Evidence for dimension 5**: Tempo, Arc, Plasma and Stable belong to the same wave of stablecoin-specific Layer 1 chains ([Fortune](https://fortune.com/crypto/2025/09/04/stripe-paradigm-tempo-blockchain-stablecoins-matt-huang-payments/)). That mirrors the late-1980s coexistence of very different Network A and Network B ([Huxiu](https://www.huxiu.com/article/2794258.html)).

## 5. Key differences: where the analogy breaks

The biggest difference is interconnection: stablecoins are not required to interoperate, and leading issuers have no reason to want it. This decides which predictions in Section 6 hold and which need extra conditions.

| Difference | Telecom | Stablecoins | Effect on the projection |
| --- | --- | --- | --- |
| 1. Interconnection | Regulators required interconnection early; network effects sat at the standard level | No par exchange between issuers; USDT and USDC are liabilities of different firms, so network effects lock into each token's liquidity | Prediction 4 requires an interoperability mechanism to appear |
| 2. Revenue source | Equipment sales | Mainly interest on reserves, highly rate-sensitive | Rate cuts accelerate the shake-out, a macro variable telecom never had |
| 3. Entry barriers | Heavy assets: networks and spectrum, natural-monopoly features | Light assets: runs on public chains; barriers are trust, licences and liquidity | Faster entry, shorter cycles |
| 4. Sovereignty | An industrial-policy issue | A monetary-sovereignty issue: USD stablecoins affect other countries' monetary policy and capital controls | Deeper regulatory fragmentation; currency-zone champions more likely |
| 5. Switching cost | Switches locked in for 10–20 years | Changing chain or token is a software change | The "standards war" may not need a winner; an abstraction layer can dissolve it |
| 6. Incentive to interconnect | Physical coverage and regional competition meant no one could reach every user, so players wanted to cooperate and set common standards | Built on the single global internet; one issuer can reach everyone, so leaders aim for winner-take-all | Interoperability will come only from regulation or from challengers banding together |

**Evidence for difference 1**: research on MiCA found that after USDT was delisted, global USDT and USDC shares barely moved; trading on EU exchanges simply shifted to USDC ([Cryptopolitan, citing Borri & Shakhnov 2026](https://cryptopolitan.com/mica-pushes-usdt-out-leaves-usdc-in)). USDT's liquidity network effect does not depend on any one jurisdiction, a cross-border lock-in no telecom operator ever had.

**Evidence for difference 2**: Section 4 of GENIUS bars issuers from paying holders any form of interest or yield, but does not explicitly bar exchanges from paying rewards ([Congressional Research Service](https://www.everycrsreport.com/reports/IF13174.html)). Circle's reserve return rate reportedly fell to about 3.5% in Q2 2026 ([KuCoin](https://www.kucoin.com/blog/in-circle-renews-usdc-revenue-sharing-agreement-with-coinbase-through-2029), secondary source).

### Difference 6 in detail: the incentive to interconnect

Telecom players were bound by the cost of physical coverage and by regional competition. No one could cover every user alone, so they had a strong tendency to interconnect and to agree common standards, such as GSM international roaming and the joint 3G standards. Stablecoins run on one global internet, so a single issuer can in principle reach the whole world. Leading players aim to be the one dominant winner, and seek interoperability only when they cannot win on their own.

One refinement: telecom's cooperative instinct showed up mainly in cross-border roaming and equipment standards. Inside a single market, the dominant operator refused to interconnect too. After Bell's patents expired, AT&T bought up independent telephone companies while refusing to connect the rest, until antitrust pressure produced the Kingsbury Commitment in 1913 ([Broadband Breakfast](https://broadbandbreakfast.com/the-kingsbury-commitment-promised-competition-at-t-got-98-of-long-distance/)). Even then it opened only long distance, not local interconnection ([Wikipedia](https://en.wikipedia.org/wiki/Kingsbury_Commitment)). In 1980 MCI still had to win in court to compete in long distance ([RCR Wireless](https://www.rcrwireless.com/20010212/carriers/breaking-ma-bell)).

**The combined pattern**: in both industries, the dominant player resists interconnection. Interconnection comes from only three sources:

1. Physical or geographic limits that stop anyone from owning everything, as in international roaming;
2. Regulatory mandate, as with the Kingsbury Commitment and the 1984 AT&T breakup;
3. Weaker challengers joining forces.

Stablecoins lack the first driver, leaving only the second and third. The facts fit: Tether, the market leader, chose to leave the EU's regulated market rather than accept MiCA ([The Paypers](https://thepaypers.com/crypto-web3-and-cbdc/news/tether-exits-eu-market-as-mica-rules-block-usdt-from-exchanges)). The players pushing "neutrality" and multi-token support are Stripe/Tempo and Visa, which do not issue a leading stablecoin themselves.

## 6. Predictions, preconditions and evidence

Of the five predictions, 1 and 5 have the strongest evidence; 4 depends on an interoperability mechanism that does not yet exist and is the least certain. Each is laid out as telecom parallel → preconditions → evidence → falsification signals.

**Timeline**: in telecom, both the path from China's first 10,000-line switch to a settled vendor landscape and the path from GSM's commercial launch in the 1990s to LTE around 2010 took about 20 years. Stablecoins began in 2014, and the 2025–2027 arrival of regulation corresponds to telecom's 1984 (the AT&T breakup). Because software is cheaper to replace, this article assumes stablecoins move at one-half to two-thirds of telecom's pace. That is a judgment, not data.

### Prediction 1: issuance converges to "2–3 global USD issuers plus local champions per currency zone" (2027–2032)

- **Telecom parallel**: switch vendors shrank from over ten to five; Nortel went bankrupt in 2009, and Alcatel-Lucent was absorbed by Nokia in 2016.
- **Preconditions**:
    1. GENIUS implementing rules land roughly as drafted around January 18, 2027 and are enforced, without major loosening of capital and liquidity requirements.
    2. MiCA and Hong Kong keep their strict licensing.
    3. Interest rates hold or fall, squeezing smaller issuers' spread.
    4. No major de-peg or reserve crisis at a leading issuer.
- **Evidence**:
    - Concentration is already high: the top two hold about 85% ([Crypto Briefing](https://cryptobriefing.com/tether-circle-stablecoin-dominance/)).
    - Compliance barriers are rising: US drafts set a $5 million capital floor and two-business-day redemption ([Finance Magnates](https://www.financemagnates.com/cryptocurrency/regulation/ten-days-to-the-genius-act-deadline-what-the-draft-rules-already-reveal/)); Hong Kong licensed 2 of 36 applicants ([Caixin Global](https://www.caixinglobal.com/2026-04-10/hong-kong-grants-first-stablecoin-licenses-to-hsbc-standard-charteredbacked-venture-102432744.html)).
    - Distribution is expensive: in 2024 Circle paid Coinbase about $908 million, roughly 54% of related revenue ([KuCoin](https://www.kucoin.com/blog/in-circle-renews-usdc-revenue-sharing-agreement-with-coinbase-through-2029), secondary source). Subscale issuers cannot afford this kind of channel cost.
    - Incumbents are entering as a group: 21 banks plan a USD stablecoin in H1 2027 ([CoinMarketCap](https://coinmarketcap.com/academy/article/21-banks-stablecoin-venture-usd-token-launch-2027)).
- **Falsification signals**: by 2030, more than ten regulated USD issuers each have over $1 billion in circulation; or the top two's combined share falls below 70%.

### Prediction 2: offshore USDT follows the "PHS" path — it survives, but loses share in regulated channels (2027–2030)

- **Telecom parallel**: China's PHS (Xiaolingtong) served many users through low prices and a policy gap, then faded after 3G licences were issued (general industry history).
- **Preconditions**:
    1. The US enforces GENIUS restrictions on foreign issuers, and USDT does not obtain a "comparable regime" determination.
    2. Tether does not seek MiCA authorization.
    3. Emerging-market dollar demand and offshore derivatives trading persist; this is why USDT will not disappear.
- **Evidence**:
    - GENIUS bars digital asset service providers from offering a foreign issuer's payment stablecoin in the US, with exceptions ([Latham & Watkins](https://www.lw.com/en/insights/genius-act-of-2025-stablecoin-legislation-adopted)).
    - Tether is already running two tracks: offshore USDT and compliant USAT issued by Anchorage Digital ([Yahoo Finance](https://finance.yahoo.com/news/tether-launches-us-regulated-usat-161314419.html)).
    - USDT demand comes mainly from emerging markets and offshore derivatives exchanges ([KuCoin](https://www.kucoin.com/blog/stablecoins-stall-300-billion-tether-usdt-leads)).
    - USDC is growing faster: about 73% vs 36% in 2025 ([DEXTools](https://www.dextools.io/news/stablecoin-market-tops-320-billion-usdc-usdt-june-2026)).
- **Falsification signals**: USDT obtains a US comparable-regime determination or MiCA authorization; or its global share returns above 65%.

### Prediction 3: the chain "standards war" converges, or is abstracted away by an interoperability layer (2028–2032)

- **Telecom parallel**: GSM vs CDMA unified into LTE in the 4G era (general industry history); Qualcomm, which lost the standards war, still profited from patents ([eWeek](https://www.eweek.com/fr/mobile/winner-take-all/)).
- **Preconditions**:
    1. Cross-chain interoperability standards mature and are accepted as secure by regulated institutions.
    2. Regulators do not mandate a specific chain (neither the US nor the EU does today).
    3. Banks and card networks keep bearing multi-chain operating costs, creating pressure to converge.
- **Evidence**:
    - In its expanded multi-chain settlement pilot, Visa hides chain differences behind one interface ([Visa press release](https://investor.visa.com/news/news-details/2026/Visa-Accelerates-Stablecoin-Momentum-Adding-Five-Blockchains-for-Settlement/default.aspx)). That is exactly the role of GSM roaming settlement.
    - Tempo is "stablecoin-neutral" and lets any stablecoin pay fees ([CryptoSlate](https://cryptoslate.com/stripe-and-paradigm-reveal-tempo-layer-1-blockchain-for-stablecoin-payments-infrastructure/)), positioning the chain itself as a pipe.
    - Telecom history shows that coexisting standards split R&D and slow progress ([eWeek](https://www.eweek.com/pt/mobile/winner-take-all/)).
- **Falsification signal**: by 2032, regulated stablecoin settlement is still spread evenly across five or more chains, with no accepted interoperability standard.

### Prediction 4: once interoperability arrives, issuers become "pipes" and value flows to distribution and applications (after 2029)

- **Telecom parallel**: long-distance competition intensified after the AT&T breakup; value then moved from vendors to operators, then to applications.
- **Preconditions** (this prediction is the most conditional):
    1. **Critical**: a par-exchange mechanism appears among regulated stablecoins — via regulation, interbank clearing arrangements or an industry agreement. No such mechanism exists today. It is expected to be driven by regulators or by a coalition of challengers, not by the market leader (see Section 5, difference 6).
    2. The GENIUS ban on issuer interest stays, while distributors remain free to pay rewards.
    3. Rates fall and reserve spreads narrow.
- **Evidence**:
    - Distributors already take most of the profit: Coinbase receives all reserve interest on USDC held on its platform plus 50% of the residual ([KuCoin](https://www.kucoin.com/blog/in-circle-renews-usdc-revenue-sharing-agreement-with-coinbase-through-2029)); the 50% share was first disclosed in Circle's S-1 ([Decrypt](https://decrypt.co/312757/coinbase-circles-residual-usdc-reserve-revenue-sharing-filing)).
    - The law bars issuers from paying yield but does not explicitly bar exchanges from paying it ([CRS](https://www.everycrsreport.com/reports/R49351.html)), which structurally favors whoever owns the customer.
    - Stripe built Tempo so it can collect fees even when neither party is a Stripe customer ([eMarketer](https://www.emarketer.com/content/stripe-makes-payments-infrastructure-stablecoin-blockchain)).
- **Falsification signals**: no par-exchange mechanism by 2030; or issuers' distribution costs fall steadily as a share of revenue.

### Prediction 5: non-USD currency zones foster local champions (2026–2030)

- **Telecom parallel**: China's "market for technology" policy trained engineers while importing the eight systems, and domestic champions eventually emerged ([Huxiu](https://www.huxiu.com/article/2794258.html)).
- **Preconditions**:
    1. The EU, Hong Kong and others keep licensing and protecting local-currency stablecoins.
    2. Local-currency stablecoins find real uses: cross-border trade and settlement of tokenized assets.
    3. CBDCs (such as a digital euro) do not crowd out private issuers entirely.
- **Evidence**:
    - Hong Kong's first licensees plan HKD stablecoins ([FinTech Futures](https://www.fintechfutures.com/blockchain-crypto-digital-assets/hkma-grants-first-hong-kong-stablecoin-licences-to-hsbc-and-standard-chartered)).
    - Under MiCA, euro stablecoins reached a record of about $900 million in mid-2026, with EURC at about half ([Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/euro-stablecoins-hit-record-highs-101822466.html)).
    - The bank consortium plans euro and other G7 tokens after the dollar; Qivalis has its own euro plan ([Financial News](https://en.fnnews.com/news/202609020839433776)).
    - Counter-evidence: euro stablecoins are still under 1% of the global market ([CoinStats, citing Token Terminal](https://coinstats.app/news/3585a5c32c264b62d97d531ee0252738215765c3af60e22608e936331e14f3f6_MiCA-pushes-USDT-out-leaves-USDC-in-the-spotlight)). The prediction is that champions emerge, not that they challenge the dollar.
- **Falsification signals**: by 2030, non-USD stablecoins together remain under 2% of the market, and none exceeds $5 billion in circulation.

## 7. Risks and counterexamples

If any of the following happens, the analogy breaks at the corresponding step.

1. **Regulators never require interoperability.** USDT's liquidity network effect may outlast any telecom operator's, and Prediction 4 fails. Global shares barely moved after MiCA delisted USDT — already a warning sign ([Cryptopolitan](https://cryptopolitan.com/mica-pushes-usdt-out-leaves-usdc-in)).
2. **The CBDC variable.** Telecom had no equivalent of "the government issuing telephones directly". A digital euro or e-CNY could rewrite the non-USD landscape from the top; analysts already see the digital euro as a medium-term regulatory overhang for Visa ([The Block](https://www.theblock.co/amp/post/399405/visa-stablecoin-settlement-hits-7-billion-run-rate-pilot-expands-nine-blockchains)).
3. **Bank consortia may repeat Great Dragon's mistakes.** China planned to merge eight state makers into Great Dragon ([Tech Monitor](https://www.techmonitor.ai/?p=160397)), but with too many shareholders and internal friction it was the first of China's big four to fade ([ITHome](https://www.ithome.com/0/533/645.htm)). The winners were Huawei and ZTE, which built their own technology in the market. A 21-bank joint company may face the same slow decision-making; its launch is still subject to closing conditions, and H1 2027 is only a target ([KuCoin](https://www.kucoin.com/blog/21-financial-institutions-usd-stablecoin-2027)).
4. **Regulatory delay or reversal.** US agencies have already missed the one-year deadline, leaving issuers to prepare against drafts that may change ([The Block](https://www.theblock.co/post/408843/us-regulators-miss-genius-acts-one-year-deadline-for-final-stablecoin-rules)). If the rules loosen substantially, the shake-out in Prediction 1 slows down.

**Methodological limits**: historical analogy points to direction, not probability. The confidence levels and time windows here are the author's judgment and should be reviewed against the falsification signals over time.

## References

**On reliability**: regulator announcements, law-firm analyses, Congressional Research Service reports and company press releases are primary or authoritative sources. Blogs from exchanges and data platforms such as KuCoin and CoinPaprika are secondary; figures from them are flagged in the text. Items marked "general industry history" (the end of PHS, LTE unification, value migrating to applications) are widely accepted history and are not separately cited.

**Telecom history**

1. [ITHome: The rise and fall of Great Dragon Telecom (Chinese)](https://www.ithome.com/0/533/645.htm)
2. [ITHome: The history of Datang Telecom (Chinese)](https://www.ithome.com/0/616/767.htm)
3. [ITHome: The story of Huawei's C&C08 switch (Chinese)](https://www.ithome.com/0/522/054.htm)
4. [Huxiu: "Seven countries, eight systems" and China's mobile choices (Chinese)](https://www.huxiu.com/article/2794258.html)
5. [Xinmin Weekly: History of Shanghai telecommunications (Chinese)](https://img1.xinmin.cn/xmzk/2020-01-06/830106.pdf)
6. [Tech Monitor: Global switch consolidation and China's Great Dragon plan](https://www.techmonitor.ai/?p=160397)
7. [Wikipedia: Breakup of the Bell System](https://en.wikipedia.org/wiki/Breakup_of_the_Bell_System)
8. [EBSCO: AT&T Undergoes Divestiture](https://www.ebsco.com/research-starters/history/att-undergoes-divestiture)
9. [Wikipedia: Kingsbury Commitment](https://en.wikipedia.org/wiki/Kingsbury_Commitment)
10. [Broadband Breakfast: The Kingsbury Commitment Promised Competition](https://broadbandbreakfast.com/the-kingsbury-commitment-promised-competition-at-t-got-98-of-long-distance/)
11. [RCR Wireless: Breaking Ma Bell](https://www.rcrwireless.com/20010212/carriers/breaking-ma-bell)
12. [Curwen (2004), Has GSM won the technology war?, *info* 6(1)](https://emeraldinsight.com/insight/content/doi/10.1108/info.2004.27206aab.001/full/html)
13. [eWeek: Winner Take All](https://www.eweek.com/mobile/winner-take-all/)
14. [Wikipedia: Comparison of mobile phone standards](https://en.wikipedia.org/wiki/Comparison_of_mobile_phone_standards)
15. [Wikipedia: Nortel](https://en.wikipedia.org/wiki/Nortel)
16. [Wikipedia: Alcatel-Lucent](https://en.wikipedia.org/wiki/Alcatel-Lucent)
17. [telecoms.com: End of an era](https://www.telecoms.com/digital-ecosystem/end-of-an-era)

**Stablecoin market**

18. [DefiLlama: Stablecoins](https://defillama.com/stablecoins)
19. [Crypto Briefing: Tether and Circle control 85% of stablecoin supply](https://cryptobriefing.com/tether-circle-stablecoin-dominance/)
20. [DEXTools: Stablecoin Market Tops $320 Billion](https://www.dextools.io/news/stablecoin-market-tops-320-billion-usdc-usdt-june-2026)
21. [CoinPaprika: The Stablecoin Wars](https://coinpaprika.com/cs/education/stablecoin-wars)
22. [KuCoin: Why Stablecoin Growth Stalls at $300 Billion](https://www.kucoin.com/blog/stablecoins-stall-300-billion-tether-usdt-leads)
23. [Yahoo Finance: Euro Stablecoins Hit Record Highs Under MiCA](https://finance.yahoo.com/markets/crypto/articles/euro-stablecoins-hit-record-highs-101822466.html)

**Regulation**

24. [Latham & Watkins: The GENIUS Act of 2025](https://www.lw.com/en/insights/2025/07/the-genius-act-of-2025-stablecoin-legislation-adopted-in-the-us)
25. [CRS: The Stablecoin Yield Debate (IF13174)](https://www.everycrsreport.com/reports/IF13174.html)
26. [CRS: GENIUS Act (P.L. 119-27) (R49351)](https://www.everycrsreport.com/reports/R49351.html)
27. [The Block: US regulators miss GENIUS Act's one-year deadline](https://www.theblock.co/post/408843/us-regulators-miss-genius-acts-one-year-deadline-for-final-stablecoin-rules)
28. [The Block: OCC debuts final rule implementing GENIUS Act](https://theblock.co/news/regulation/2026-10-21-occ-final-rule-implementing-trump-signed-genius-act-421470)
29. [Finance Magnates: What the draft GENIUS rules reveal](https://www.financemagnates.com/cryptocurrency/regulation/ten-days-to-the-genius-act-deadline-what-the-draft-rules-already-reveal/)
30. [HKMA: Granting of stablecoin issuer licences (2026-04-10)](https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/04/20260410-4/)
31. [Caixin Global: Hong Kong grants first stablecoin licenses](https://www.caixinglobal.com/2026-04-10/hong-kong-grants-first-stablecoin-licenses-to-hsbc-standard-charteredbacked-venture-102432744.html)
32. [FinTech Futures: HKMA grants first licences](https://www.fintechfutures.com/blockchain-crypto-digital-assets/hkma-grants-first-hong-kong-stablecoin-licences-to-hsbc-and-standard-chartered)
33. [The Paypers: Tether exits EU market as MiCA rules block USDT](https://thepaypers.com/crypto-web3-and-cbdc/news/tether-exits-eu-market-as-mica-rules-block-usdt-from-exchanges)
34. [Cryptopolitan: MiCA pushes USDT out, leaves USDC in the spotlight](https://cryptopolitan.com/mica-pushes-usdt-out-leaves-usdc-in)

**Main players**

35. [Yahoo Finance: Tether Launches US-Regulated USAT](https://finance.yahoo.com/news/tether-launches-us-regulated-usat-161314419.html)
36. [Decrypt: Coinbase Takes 50% Share of Circle's Residual USDC Reserve Revenue](https://decrypt.co/312757/coinbase-circles-residual-usdc-reserve-revenue-sharing-filing)
37. [KuCoin: Circle Renews USDC Revenue-Sharing Agreement Through 2029](https://www.kucoin.com/blog/in-circle-renews-usdc-revenue-sharing-agreement-with-coinbase-through-2029)
38. [CoinMarketCap: 21 Major Banks Plan Stablecoin Venture](https://coinmarketcap.com/academy/article/21-banks-stablecoin-venture-usd-token-launch-2027)
39. [KuCoin: 21 Global Financial Institutions Back a Joint USD Stablecoin](https://www.kucoin.com/blog/21-financial-institutions-usd-stablecoin-2027)
40. [Banking Dive: BofA, Wells Fargo, Citi back upcoming stablecoin](https://www.bankingdive.com/news/bofa-wells-fargo-citi-back-upcoming-stablecoin/829318/)
41. [Financial News (Korea): 21 institutions to issue a dollar stablecoin](https://en.fnnews.com/news/202609020839433776)
42. [Fortune: Stripe and Paradigm announce Tempo](https://fortune.com/crypto/2025/09/04/stripe-paradigm-tempo-blockchain-stablecoins-matt-huang-payments/)
43. [Everstake: Tempo vs Arc](https://everstake.one/resources/blog/tempo-vs-arc-stablechains-the-next-generation-of-finance)
44. [CryptoSlate: Tempo layer-1 for stablecoin payments](https://cryptoslate.com/stripe-and-paradigm-reveal-tempo-layer-1-blockchain-for-stablecoin-payments-infrastructure/)
45. [eMarketer: Stripe makes payments infrastructure play](https://www.emarketer.com/content/stripe-makes-payments-infrastructure-stablecoin-blockchain)
46. [Visa press release: Adding Five Blockchains for Settlement (2026-04-29)](https://investor.visa.com/news/news-details/2026/Visa-Accelerates-Stablecoin-Momentum-Adding-Five-Blockchains-for-Settlement/default.aspx)
47. [crypto.news: Visa stablecoin settlement surpasses $25B](https://crypto.news/visa-stablecoin-settlement-volume-25-billion-2026/)
48. [The Block: Visa stablecoin settlement hits $7 billion run rate](https://www.theblock.co/amp/post/399405/visa-stablecoin-settlement-hits-7-billion-run-rate-pilot-expands-nine-blockchains)
49. [CoinStats: MiCA pushes USDT out, leaves USDC in the spotlight](https://coinstats.app/news/3585a5c32c264b62d97d531ee0252738215765c3af60e22608e936331e14f3f6_MiCA-pushes-USDT-out-leaves-USDC-in-the-spotlight)
