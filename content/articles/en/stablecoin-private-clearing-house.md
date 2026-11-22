---
title: "The Economics of Stablecoins: Why an Issuer Works Like a Private Cross-Border Clearing House"
date: 2026-11-20
description: "Economically, a stablecoin issuer works like a privately owned cross-border clearing house: it pools users' fiat, moves value on its own liability ledger and earns the float. This article looks at how issuers operate, how they are licensed, where their users come from and how they make money; how the landscape may shift in a crypto downturn; and where stablecoins genuinely differ from a clearing house. The aim is to understand the business model that payment and bank stablecoins will compete on."
tags: ["Stablecoins", "Clearing houses", "Float", "Payments regulation", "Cross-border payments"]
publication: ""
external_url: ""
cover: "/images/uploads/cover_en_stablecoin-clearing-house.png"
draft: false
---

> Related: [Cross-Border Payments Without a Shared Ledger](/articles/cross-border-payments-dont-need-blockchain/) · [From Telephone Switches to Stablecoins](/articles/telecom-lessons-for-stablecoin-competition/)
>
> Data as of November 2026. Not investment or legal advice.

## 1. The argument

**Economically, a stablecoin issuer works like a privately owned cross-border clearing house.** It does much of what a clearing house does, under issuer and money-transmission licences rather than a clearing-house licence. Its growth has been driven largely by crypto trading and by the reach of public blockchains. It pools users' fiat money, and its main revenue is the interest on that pool. Understanding this model matters for anyone building stablecoin products, because regulation is now pulling it toward the standards of payment infrastructure.

The argument has five parts, plus one consequence:

| Element | Meaning | Section |
| --- | --- | --- |
| Private clearing house | Funds concentrate in one company; transfers happen on its liability ledger | 2, 3 |
| A different licensing regime | Operates under money-transmission, digital-asset or newly created issuer licences, not as regulated market infrastructure | 4 |
| Distribution through blockchain | Wallet access lowers acquisition cost, but users must judge the issuer's credit, not the chain | 5 |
| Growth tied to crypto trading | Many users arrive to trade crypto; the pool has moved with the crypto market | 6 |
| A pool of funds | Takes in fiat without paying interest, invests reserves in Treasuries, keeps the spread | 7, 8 |
| In a crypto downturn | As crypto prices fall, trading-driven demand weakens and the landscape reshuffles | 10 |

## 2. Taking a stablecoin cross-border payment apart

Take a US company paying a Mexican supplier in USDC:

| Step | What it looks like | What actually happens |
| --- | --- | --- |
| ① On-ramp | Buy USDC | The company wires dollars over traditional bank rails (wire, ACH) into the issuer's bank account |
| ② Mint | Tokens created on-chain | The issuer records a liability on its own ledger: it owes the company X dollars |
| ③ On-chain transfer | "Decentralized peer-to-peer payment" | The issuer's liability to the company is re-registered as a liability to the supplier; the money stays in the issuer's bank accounts and Treasuries |
| ④ Off-ramp | Sell USDC for pesos | The supplier goes through an exchange or market maker, then a Mexican bank, to receive pesos |

Three conclusions:

1. **Both ends depend on traditional payment networks.** Fiat moves only at the on-ramp and off-ramp.
2. **The "payment" in the middle is a transfer of a claim.** Holder A's claim on the issuer becomes holder B's claim — economically the same as a transfer between two accounts at one bank.
3. **However fast the chain is, it is only the speed of internal bookkeeping.** The actual cross-border fiat settlement is pushed to the FX and local-bank steps at the off-ramp.

## 3. Why it is a clearing house

The defining features of a clearing house: participants place funds with a central institution, the institution moves value on its internal ledger, and it settles with outside systems only when needed. Stablecoin issuers fit almost exactly:

| Dimension | Traditional clearing house / correspondent bank | Stablecoin issuer |
| --- | --- | --- |
| Where funds sit | Members hold funds at the clearing house or correspondent | Users hand fiat to the issuer |
| Internal transfer | Book entries on the clearing house's ledger | On-chain token transfers, i.e. transfers of the issuer's liability |
| Control | Can suspend or refuse members | Can freeze and blacklist addresses, burn and reissue |
| Final settlement | Central bank or commercial bank accounts | The issuer's bank accounts |
| Main revenue | Transaction fees | Interest on reserves |

International standard setters see it the same way. In 2022 the BIS Committee on Payments and Market Infrastructures (CPMI) and IOSCO issued final guidance confirming that systemically important stablecoin arrangements should observe the *Principles for Financial Market Infrastructures* (PFMI) — the international standards for payment, clearing and settlement systems — on a "same risk, same regulation" basis ([BIS press release](https://www.bis.org/media-releases/20220713-cpmi-and-iosco-publish-final-guidance-stablecoin-arrangements-confirming-application-principles); [IOSCO press release](https://www.iosco.org/news/pdf/IOSCONEWS651.pdf)). The guidance states that the transfer function of a stablecoin arrangement is a financial market infrastructure function ([CPMI-IOSCO report](https://www.bis.org/cpmi/publ/d198.pdf)).

The blockchain here works more like a public display board and messaging layer than an independent monetary system.

## 4. Licensing: clearing-house functions under issuer licences

A regulated clearing institution must meet the full PFMI set of requirements on governance, comprehensive risk management, settlement finality and more ([FSB summary](https://www.fsb.org/2022/07/application-of-the-principles-for-financial-market-infrastructures-to-stablecoin-arrangements/)). Stablecoin issuers have largely been licensed under other frameworks:

- **Tether's choice of domicile.** Tether, originally incorporated in the British Virgin Islands, announced in January 2025 that it would move its headquarters and subsidiaries to El Salvador after obtaining a Digital Asset Service Provider (DASP) and stablecoin-issuer licence there ([Cointelegraph](https://cointelegraph.com/news/tether-el-salvador-securing-license-property)). These are digital-asset licences, not clearing-house or banking licences.
- **New York's finding.** In 2021 Bitfinex and Tether settled with the New York Attorney General for $18.5 million. The settlement alleged that they had misled the market about Tether's reserves while doing business in New York without appropriate licensure ([Hunton summary](https://www.hunton.com/blockchain-legal-resource/2021/03/new-york-attorney-general-announces-settlement-with-bitfinex/)).
- **Circle's federal charter came late.** USDC launched in 2018, but Circle received a national trust bank charter from the US Office of the Comptroller of the Currency (OCC) only in July 2026, starting with digital-asset custody; USDC issuance is set to move to a New York limited-purpose trust company ([The Block](https://www.theblock.co/news/regulation/2026-07-10-stablecoin-firm-circle-wins-final-occ-approval-to-open-national-trust-bank-407876)).
- **The new US law creates an issuer licence, not a clearing-house licence.** The GENIUS Act creates a new category of "permitted payment stablecoin issuer". Under the current drafts, new federal issuers need only a $5 million capital floor ([Finance Magnates](https://www.financemagnates.com/cryptocurrency/regulation/ten-days-to-the-genius-act-deadline-what-the-draft-rules-already-reveal/)), and the regime takes effect only on January 18, 2027 ([The Block](https://www.theblock.co/post/408843/us-regulators-miss-genius-acts-one-year-deadline-for-final-stablecoin-rules)).

The upshot: USDT since 2014 and USDC since 2018 — the two largest stablecoins — have operated for years under licensing regimes other than those for clearing houses. Regulation is catching up through new issuer licences; whether systemically important issuers will also be supervised as financial market infrastructure is still an open question.

## 5. Distribution through blockchain: reach comes with a credit question

Holding a stablecoin means holding a non-interest-bearing claim on a private company. Public blockchains help issuers in four ways:

1. **Trust framing.** Users often see "on-chain dollars" rather than a claim on an issuer, so the issuer's own credit gets less scrutiny than it deserves.
2. **Cheap distribution.** Anyone with a wallet can connect, with no account opening or in-person checks; customer acquisition costs far less than for a bank.
3. **A classification gap.** Early on, issuers operated in the gap over whether a stablecoin is a security, a deposit, e-money or a payment instrument, avoiding the licensing, capital and deposit-insurance requirements of banks and clearing institutions (see Section 4).
4. **Ecosystem lock-in.** Exchanges and DeFi protocols use stablecoins as their base settlement asset, creating network effects.

In other words, **for the issuer, the blockchain works mainly as a distribution channel and a shared display ledger; the core economics sit in the reserves.**

## 6. Growth tied to crypto trading: the pool has moved with the market

Most stablecoin users did not originally come for cross-border payments; they came to trade crypto, and stablecoins became the main instrument for entering and leaving the crypto market. Four pieces of evidence:

1. **The main use is crypto trading.** The BIS noted in 2026 that stablecoin transaction volume is around $35 trillion a year, yet real-economy use is modest; stablecoins have mainly served on-chain trading within the crypto ecosystem ([BIS speech](https://www.bis.org/speeches/20260420-stablecoins-framing-debate)). The BIS 2026 Annual Report likewise found the main uses to be crypto trading and, to a lesser extent, offshore dollar savings in emerging markets ([Bitcoin Foundation report](https://bitcoinfoundation.org/?p=7882)).
2. **Money flows in during bull markets.** JPMorgan estimated that about $165 billion entered the crypto market through stablecoin creation in 2020–2021 ([CoinDesk](https://www.coindesk.com/markets/2022/11/17/jpmorgan-the-shrinking-stablecoin-market-is-another-sign-of-investors-exodus-from-crypto/)).
3. **Money flows out during bear markets.** The same report showed the largest stablecoins' combined market cap peaking at $186 billion in May 2022, then falling by $41 billion, with just under half of that due to Terra's collapse ([CoinDesk](https://www.coindesk.com/markets/2022/11/17/jpmorgan-the-shrinking-stablecoin-market-is-another-sign-of-investors-exodus-from-crypto/)). In November 2026, major stablecoin supply fell $14.2 billion in 30 days, the biggest contraction since the 2022 bear market ([The Block](https://theblock.co/news/ecosystems/2026-11-11-stablecoin-supply-drops-14-2-billion-largest-contraction-since-2022-bear-market-437907)).
4. **The acquisition channel takes a cut.** Exchanges are the main entry point, so issuers share interest with them: Coinbase receives all reserve interest on USDC held on its platform plus 50% of the residual reserve income ([Decrypt, from Circle's IPO filing](https://decrypt.co/312757/coinbase-circles-residual-usdc-reserve-revenue-sharing-filing)).

So the acquisition funnel has run: **crypto trading demand → users join an exchange → they swap fiat for stablecoins as trading chips → the fiat settles into the issuer's pool → the issuer and the exchange share the interest.** So far the pool's size has tracked the crypto market more closely than demand for cross-border payments. Payment use is the part to watch.

## 7. Building the pool: a float business

The issuer's core business model is float:

- Users hand over fiat and receive non-interest-bearing tokens;
- The issuer invests the reserves in short-term US Treasuries, repo and bank deposits, and keeps the interest;
- The GENIUS Act bars issuers from paying holders any interest or yield, but does not explicitly bar exchanges from paying their customers rewards ([Congressional Research Service](https://www.everycrsreport.com/reports/IF13174.html)). In effect, the rules confirm "take deposits without paying interest, and let the issuer and its channels keep the spread".

The business is very profitable. Tether's net profit exceeded $13 billion in 2024 and was about $10.1 billion in 2025, mainly from US Treasury interest ([CoinPaprika](https://coinpaprika.com/news/tether-reports-10b-profit-2025-usdt-supply-hits-186b-record/); [Tether announcement](https://tether.io/news/tether-delivers-10b-profits-in-2025-6-3b-in-excess-reserves-and-record-141-billion-exposure-in-u-s-treasury-holdings/)).

**China has already dealt with the same model.** In the early days, Alipay's and WeChat Pay's customer reserve funds sat in commercial banks, and the interest went to the payment companies. The People's Bank of China took two steps:

1. **It took back clearing.** From June 30, 2018, all online payments by payment institutions involving bank accounts had to go through the NetsUnion clearing platform ([National Business Daily](https://www.nbd.com.cn/articles/2018-06-30/1230579.html)).
2. **It took back the pool.** Starting in 2017, payment institutions had to deposit a rising share of customer reserves centrally; by January 14, 2019, 100% — more than RMB 1.2 trillion — was held centrally ([Jiemian](https://www.jiemian.com/article/2791123.html); [Xinhua via rmzxw.com.cn](https://www.rmzxw.com.cn/c/2019-01-09/2259805.shtml)). Payment institutions lost the income from the float ([Yicai](https://www.yicai.com/news/100094905.html)).

That is precisely how to bring a "private clearing house plus float" model back inside the regulatory system.

**A note on "fund-raising".** In legal terms, especially "illegal fund-raising" in China, fund-raising usually involves a promised return. Stablecoins promise no return, only 1:1 redemption. So the more precise description is "interest-free deposit-taking" or "stored-value pooling", economically closer to e-money and prepaid value. The risk structure is nonetheless similar (see Section 8).

## 8. The old problems of a pooled fund: runs and transparency

- **Run risk.** When Silicon Valley Bank failed in March 2023, Circle had $3.3 billion of reserves (about 8%) there, and USDC fell below 87 cents ([CNBC](https://www.cnbc.com/amp/2023/03/11/stablecoin-usdc-breaks-dollar-peg-after-firm-reveals-it-has-3point3-billion-in-svb-exposure.html); [Federal Reserve FEDS Notes](https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html)). Holders bear the credit risk of the issuer and its banks.
- **Transparency risk.** In October 2021 the US Commodity Futures Trading Commission (CFTC) fined Tether $41 million, finding that from 2016 to 2019 it had misrepresented that USDT was fully backed by US dollars ([CFTC press release](https://www.cftc.gov/PressRoom/pressReleases/8450-21)). According to the CFTC, Tether had enough reserves to back its tokens only 27.6% of the time from 2016 through 2018 ([Advisor.ca](https://www.advisor.ca/industry-news/industry/cftc-sanctions-tether-bitfinex/)). That February, Tether and Bitfinex had also settled with the New York Attorney General for $18.5 million ([CNBC](https://www.cnbc.com/amp/2021/02/23/tether-bitfinex-reach-settlement-with-new-york-attorney-general.html)).

These are the classic risks of a pooled fund — exactly what clearing-house and banking licences exist to guard against.

## 9. To be fair: where stablecoins genuinely differ from a clearing house

1. **Transfers between holders need no issuer approval.** Tokens move on-chain 24/7; the issuer only keeps the power to freeze after the fact.
2. **The ledger is public and verifiable.** The issuer cannot unilaterally rewrite transaction history, and anyone can audit supply on-chain.
3. **Programmable and composable.** Smart contracts can tie payment to delivery, escrow and conditional triggers.
4. **Real value for some people.** For residents of high-inflation countries and people without bank accounts, it is an accessible dollar instrument; the BIS acknowledges this as the second-largest use ([Bitcoin Foundation report](https://bitcoinfoundation.org/?p=7882)).
5. **Regulation is turning it into a bank.** The GENIUS Act and the EU's MiCA require full reserves, regular disclosure and licensed operation. That itself supports this article's argument: regulators in practice treat issuers as a kind of payment institution or quasi-bank, not as "decentralized money".

## 10. In a crypto downturn: trading demand weakens and the landscape reshuffles

Stablecoins grew with crypto's momentum. When that momentum slows, trading-driven balances shrink first, and the competitive landscape reshuffles. This section is a projection from current data, not a price forecast.

### 10.1 The downturn in numbers

- **Bitcoin has roughly halved.** Bitcoin set an all-time high of about $126,000 in October 2025; by mid-November 2026 it had fallen to about $62,000, nearly 47% below the peak. US spot bitcoin ETFs saw about $1.91 billion of net outflows over seven straight trading days from November 5 to 13 ([Crypto Briefing](https://cryptobriefing.com/bitcoin-selloff-tests-committed-investors/)).
- **The stablecoin pool is shrinking with it.** Major stablecoin supply fell $14.2 billion in 30 days, the largest contraction since the 2022 bear market, to just under $280 billion — back to its September 2025 level. USDT fell $6.6 billion in the 60 days to November 7, more than twice its drop over a similar period after FTX collapsed ([The Block](https://theblock.co/news/ecosystems/2026-11-11-stablecoin-supply-drops-14-2-billion-largest-contraction-since-2022-bear-market-437907)).
- **The 2022 precedent.** In June 2022 the 30-day decline in stablecoin supply approached $30 billion, about five months before bitcoin hit its bear-market low of $15,500 (same source).

### 10.2 How the funnel breaks: four links

1. **Acquisition stalls.** When the money-making effect disappears, new users stop arriving and fewer stablecoins are minted.
2. **Existing holders redeem.** Holders cash out stablecoins for dollars and leave, so the pool shrinks. Glassnode reads falling supply as cash leaving the market ([The Block](https://theblock.co/news/ecosystems/2026-11-11-stablecoin-supply-drops-14-2-billion-largest-contraction-since-2022-bear-market-437907)).
3. **A double squeeze on profit.** Issuer revenue is roughly "pool size × interest rate". Lower rates already cut Tether's 2025 net profit by 23% year on year, to about $10.1 billion ([MEXC repost](https://www.mexc.com/news/602839)). If the pool also shrinks with the market, both factors fall together.
4. **Run and fire-sale risk.** The BIS warns that runs on stablecoins would trigger fire sales of reserve assets that could impair market functioning ([BIS speech slides](https://www.bis.org/speeches/sp260420_slides.pdf)). The more a pool depends on crypto trading, the more likely redemptions bunch up in a sharp sell-off.

### 10.3 Effect on the landscape: who is hit hardest, who gains ground

| Type of player | Reliance on the crypto-trading funnel | Effect of the downturn | Assessment |
| --- | --- | --- | --- |
| Yield-bearing and small issuers | Very high | Yield and size shrink together; when yields fell in November 2025, USDe's market cap halved within a month ([ForkLog](https://forklog.com/en/top-ten-dollar-stablecoins-from-would-be-monopolists-to-those-on-the-brink/)) | Most fragile; shake-out accelerates |
| Offshore USDT | High (offshore exchanges, derivatives), cushioned by emerging-market dollar savings | Most directly hit in size; share not necessarily lower, currently about 62.8% ([The Block](https://theblock.co/news/ecosystems/2026-11-11-stablecoin-supply-drops-14-2-billion-largest-contraction-since-2022-bear-market-437907)) | Size under pressure; position stable for now |
| Compliant USDC | Medium (exchanges, institutions, DeFi) | Hurt by lower trading; but compliance can attract share in a flight to safety — in the 2022 bear market USDC's market cap still grew by more than $10 billion ([NewsBTC](https://www.newsbtc.com/news/domino-effect-on-stablecoins-leads-to-reversal-of-growth-trend/)) | Relatively resilient |
| Bank-issued (21-bank consortium, HSBC's HKD stablecoin) | Low; customers come from existing bank relationships | No reliance on the crypto funnel; competition shifts to credit and distribution, banks' home ground | Relative winner |
| Payment chains and card networks (Tempo, Visa stablecoin settlement) | Low; demand comes from B2B and cross-border payouts | The story shifts from "trading chips" to "payment tool" | Relative winner |

**Implication for the landscape:** as the crypto market cools, the growth engine of issuers that rose on the crypto funnel weakens, while banks and payment firms that never relied on that funnel gain ground. The industry's centre of gravity moves from "who has the most trading pairs" to "whose credit is best and whose distribution is deepest".

### 10.4 The value proposition shifts toward payments

In a crypto bull market, much stablecoin demand comes from trading. In a downturn, the lasting value proposition is compliance, credit quality and payment efficiency. In other words, **stablecoins will increasingly be judged as payment infrastructure, and will compete with banks and payment networks on credit and distribution.** That is a healthy shift for the industry, and it supports this article's framing.

Telecom has a precedent: the telecom bubble burst around 2000. At its height Nortel accounted for more than a third of the total valuation of all companies on the Toronto Stock Exchange; it went bankrupt in 2009 ([Wikipedia](https://en.wikipedia.org/wiki/Nortel)). After the bubble, the survivors were the firms with real customers and cash flow.

### 10.5 Counter-evidence and what to watch

**Counter-evidence:**

- The BIS notes that the stablecoin market has remained quite resilient through the recent crypto rout ([BIS speech](https://www.bis.org/speeches/20260420-stablecoins-framing-debate)). So far the $14.2 billion 30-day contraction is only about 5% of the total — far from a collapse. The free fall is in crypto prices, not in stablecoin supply.
- The 2022 contraction was cyclical: supply later recovered and hit new highs in 2025–2026. Emerging-market dollar demand and institutional payments form a base that does not depend on crypto prices.

**What to watch:**

1. Whether 30-day stablecoin supply change stays negative;
2. Shifts in USDT versus USDC share;
3. Whether the share of non-trading use measured by the BIS and others rises;
4. Whether the bank consortium's stablecoin launches on its H1 2027 target.

## 11. Conclusion

Economically, a stablecoin issuer is **a privately owned clearing house, licensed as an issuer, distributed through public blockchains, grown largely on crypto trading, and paid by the spread on its pool of funds.** It gathers fiat through traditional payment networks, issues tokens as non-interest-bearing liabilities, completes "payments" on its own ledger, and pays out again through traditional networks.

Four implications follow:

1. **Competition among stablecoins is a contest of deposit-gathering and distribution, not of technology.**
2. **Their relationship with banks, Visa, Mastercard and SWIFT is not "disruption" but a fight over the float and fees in cross-border clearing.**
3. **A crypto downturn shifts the focus to payments.** Issuers whose pools grew on crypto trading may slow, while issuers built on payment use cases, along with banks and payment firms, gain ground (see Section 10).
4. **The better the regulation, the more a stablecoin looks like a "narrow bank plus clearing house".** The question ultimately comes back to three points: who licenses these institutions, who supervises them, and who owns the interest. China, with NetsUnion and centralized reserve deposits, has given one answer.

## References

**International standards and research**

1. [CPMI-IOSCO: Application of the PFMI to stablecoin arrangements (2022)](https://www.bis.org/cpmi/publ/d198.pdf)
2. [BIS press release: CPMI and IOSCO publish final guidance on stablecoin arrangements (2022-07-13)](https://www.bis.org/media-releases/20220713-cpmi-and-iosco-publish-final-guidance-stablecoin-arrangements-confirming-application-principles)
3. [IOSCO press release (2022-07-13)](https://www.iosco.org/news/pdf/IOSCONEWS651.pdf)
4. [FSB: Application of the PFMI to stablecoin arrangements](https://www.fsb.org/2022/07/application-of-the-principles-for-financial-market-infrastructures-to-stablecoin-arrangements/)
5. [BIS speech: Stablecoins – framing the debate (2026-04-20)](https://www.bis.org/speeches/20260420-stablecoins-framing-debate)
6. [Bitcoin Foundation: BIS annual report says stablecoins mostly serve crypto trading](https://bitcoinfoundation.org/?p=7882)
7. [Federal Reserve FEDS Notes: Lessons from the SVB failure and its impact on stablecoins (2025-12-17)](https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html)
8. [Congressional Research Service: The Stablecoin Yield Debate](https://www.everycrsreport.com/reports/IF13174.html)

**Licensing and enforcement**

9. [Cointelegraph: Tether relocates to El Salvador after securing licence](https://cointelegraph.com/news/tether-el-salvador-securing-license-property)
10. [Hunton: New York Attorney General settlement with Bitfinex/Tether](https://www.hunton.com/blockchain-legal-resource/2021/03/new-york-attorney-general-announces-settlement-with-bitfinex/)
11. [The Block: Circle wins final OCC approval for national trust bank](https://www.theblock.co/news/regulation/2026-07-10-stablecoin-firm-circle-wins-final-occ-approval-to-open-national-trust-bank-407876)
12. [Finance Magnates: What the draft GENIUS rules reveal](https://www.financemagnates.com/cryptocurrency/regulation/ten-days-to-the-genius-act-deadline-what-the-draft-rules-already-reveal/)
13. [The Block: US regulators miss GENIUS Act's one-year deadline](https://www.theblock.co/post/408843/us-regulators-miss-genius-acts-one-year-deadline-for-final-stablecoin-rules)
14. [CFTC press release 8450-21: Tether fined $41 million](https://www.cftc.gov/PressRoom/pressReleases/8450-21)
15. [Advisor.ca: CFTC sanctions Tether, Bitfinex](https://www.advisor.ca/industry-news/industry/cftc-sanctions-tether-bitfinex/)
16. [CNBC: Tether and Bitfinex pay $18.5 million to end New York probe](https://www.cnbc.com/amp/2021/02/23/tether-bitfinex-reach-settlement-with-new-york-attorney-general.html)

**Market and profits**

17. [CoinDesk: JPMorgan says shrinking stablecoin market signals crypto exodus](https://www.coindesk.com/markets/2022/11/17/jpmorgan-the-shrinking-stablecoin-market-is-another-sign-of-investors-exodus-from-crypto/)
18. [The Block: Stablecoin supply drops $14.2 billion in 30 days (2026-11-11)](https://theblock.co/news/ecosystems/2026-11-11-stablecoin-supply-drops-14-2-billion-largest-contraction-since-2022-bear-market-437907)
19. [Decrypt: Coinbase takes 50% of Circle's residual USDC reserve revenue](https://decrypt.co/312757/coinbase-circles-residual-usdc-reserve-revenue-sharing-filing)
20. [Tether: More than $10 billion profit in 2025](https://tether.io/news/tether-delivers-10b-profits-in-2025-6-3b-in-excess-reserves-and-record-141-billion-exposure-in-u-s-treasury-holdings/)
21. [CoinPaprika: Tether's 2025 profit compared with 2024](https://coinpaprika.com/news/tether-reports-10b-profit-2025-usdt-supply-hits-186b-record/)
22. [CNBC: USDC breaks peg over SVB exposure](https://www.cnbc.com/amp/2023/03/11/stablecoin-usdc-breaks-dollar-peg-after-firm-reveals-it-has-3point3-billion-in-svb-exposure.html)

**China's reserve-fund and NetsUnion reforms (Chinese sources)**

23. [National Business Daily: Reserve deposit ratio raised to 100% (2018-06-30)](https://www.nbd.com.cn/articles/2018-06-30/1230579.html)
24. [Jiemian: Over RMB 1.2 trillion of reserves centrally deposited](https://www.jiemian.com/article/2791123.html)
25. [Xinhua (via rmzxw.com.cn): All reserves to be held at the central bank](https://www.rmzxw.com.cn/c/2019-01-09/2259805.shtml)
26. [Yicai: Closing reserve accounts and the loss of float income](https://www.yicai.com/news/100094905.html)

**Crypto market and landscape**

27. [Crypto Briefing: Bitcoin selloff tests resolve of committed investors (Nov 2026)](https://cryptobriefing.com/bitcoin-selloff-tests-committed-investors/)
28. [MEXC repost: Tether's 2025 profit down 23%](https://www.mexc.com/news/602839)
29. [BIS speech slides (2026-04-20)](https://www.bis.org/speeches/sp260420_slides.pdf)
30. [ForkLog: Top ten dollar stablecoins](https://forklog.com/en/top-ten-dollar-stablecoins-from-would-be-monopolists-to-those-on-the-brink/)
31. [NewsBTC: Stablecoins in the 2022 bear market](https://www.newsbtc.com/news/domino-effect-on-stablecoins-leads-to-reversal-of-growth-trend/)
32. [Wikipedia: Nortel](https://en.wikipedia.org/wiki/Nortel)
