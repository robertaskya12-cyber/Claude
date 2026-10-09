# Lithuanian high-paying finance employers: salary data, junior pay benchmarks and hiring paths (research as of 9 Oct 2026)

> **Method note (read first).** The sandbox egress proxy refused every direct connection to the primary data hosts (atvira.sodra.lt, data.gov.lt / get.data.gov.lt, rekvizitai.vz.lt, vz.lt, delfi.lt). It answered 403 "connect_rejected" to curl. WebFetch also failed with DNS errors for rekvi.lt, scoris.lt, pinokis.com and tv3.lt. **So the Sodra per-employer dataset could not be downloaded or filtered.** Every entity figure below comes from web search snippets of third-party aggregators that are built on Sodra data (mainly rekvi.lt TOP 100 and scoris.lt). None of it was checked against the raw Sodra file. I wrote a ready-to-run filter script, `raw/sodra_filter_finance.py`, in this folder. Run it on a machine with normal internet access and it will produce the ranked list the brief asked for (EVRK 64/65/66, 70.22, 46.12, 35.14, average wage of EUR 5,000 or more). The script's download URL pattern is unverified.

## 1. Which finance-sector entities have the highest Sodra average wages in 2025-2026, and what are they?

### Takeaway
Two pieces of evidence came through. First, the rekvi.lt Sodra-based TOP 100 (snapshot around Oct 2026) includes at least three finance-coded entities with very high averages but tiny headcounts: GPS Capital Markets Europe UAB at about EUR 55.8k/month (4 staff), AlphaPay UAB at about EUR 15.7k (6 staff) and Kevin EU UAB at about EUR 14.0k. Second, Covalis Capital (a London hedge fund) has a confirmed Vilnius presence with equity analysts on staff. I could not get its Lithuanian legal entity, EVRK code or Sodra wage. A full ranking of the EUR 5,000+ finance tier was **not** achievable from this environment.

### Cited Findings
- rekvi.lt publishes a "TOP 100 companies paying the highest salaries in Lithuania (2026)" based on official SODRA monthly data. It was updated 7 Oct 2026 and gives an overall register average wage of EUR 2,380. The top three are not finance: a VMware International Marketing Ltd Lithuanian branch (Vilnius, about EUR 114,152 average with 5 employees), Talech Lithuania (Kaunas, about EUR 109,870) and Palantir Technologies Lithuania (Vilnius, about EUR 62,868) — [rekvi.lt TOP100](https://rekvi.lt/en/top100?sort=atlyginimai) (search snippet only; the page could not be fetched)
- Finance-coded entities in the same rekvi.lt TOP 100, as shown in search snippets:
  - **GPS Capital Markets Europe, UAB** (Vilnius). Rank about 5, average wage **EUR 55,828**, **4 employees**. Activity: "other auxiliary financial service activities, except insurance and pension funding" (EVRK 66.19).
  - **AlphaPay, UAB** (Vilnius). Rank about 24, average **EUR 15,693**, **6 employees**. Same activity group (66.19).
  - **Kevin EU, UAB**. Rank about 29, average **EUR 13,966**. Activity: "other monetary intermediation" (EVRK 64.19).
  - Source for all three: [rekvi.lt TOP100](https://rekvi.lt/en/top100?sort=atlyginimai)
- TV3 reported on the monthly Sodra leaders. In January 2026, 132 companies paid an average above EUR 10k and the top payer was **Onlychain Fintech Limited** (a crypto/fintech-type name, probably a Lithuanian branch). In March 2026, Talech Lithuania topped the list, with averages reaching about EUR 117k (headline) to 177k (snippet) — [TV3 (Jan 2026)](https://www.tv3.lt/naujiena/verslas/didziausi-atlyginimai-lietuvoje-sausi-kai-kurios-imones-savo-darbuotojams-mokejo-ir-po-79-tukst-euru-n1498035); [TV3 (Mar 2026)](https://www.tv3.lt/naujiena/verslas/didziausi-atlyginimai-lietuvoje-nustebins-kova-sieke-net-117-tukst-euru-n1514886). These are snippets only. The figures in the headline and the snippet are inconsistent.
- Fund-management (66.30) entities on scoris.lt, from search snippets. The period is often unspecified.
  - **Sound asset management, UAB**: average wage about **EUR 6,800**, 5 employees, profit about EUR -10k — [Scoris](https://scoris.lt/en/imone/306274580)
  - **Contrarian Ventures, UAB** (VC, climate-tech): average **EUR 5,380 in 2024**, down 20.1% from 2023 — [Scoris](https://scoris.lt/imone/304584559)
  - **Investicijų valdymas Prosperus, UAB**: about **EUR 3,198 in 2025**, up 39.8% YoY — [Scoris](https://scoris.lt/en/imone/303144788)
  - **SEB investicijų valdymas, UAB**: about **EUR 2,549**, 26 employees (period unstated) — [Scoris](https://scoris.lt/en/imone/125277981)
  - Also surfaced, with no wage figure available: LORDS LB Asset Management ([Scoris](https://scoris.lt/imone/301849625)), Groa Capital ([Scoris](https://scoris.lt/imone/304062479)) and Luminor investicijų valdymas (wage up 8.0% vs 2023) ([Scoris](https://scoris.lt/imone/226299280))
- **Covalis Capital.** Its LinkedIn company page lists a **Vilnius** location. A Lithuanian employee profile shows the title "Equity Analyst – COVALIS CAPITAL", based in Lithuania, from Aug 2022 — [LinkedIn company](https://www.linkedin.com/company/covalis-capital-llp); [LinkedIn profile](https://www.linkedin.com/in/vaidas-ali%C5%A1auskas-b866b9193/). Covalis describes itself as a global asset manager focused on infrastructure, utilities, renewable energy, industrials and materials. It was described as an employee-owned London hedge fund launched in May 2012, with offices in New York and the Cayman Islands — [Insider Monkey](https://www.insidermonkey.com/blog/covalis-capitals-returns-aum-and-holdings-674227/); [Bloomberg profile](https://www.bloomberg.com/profile/company/1100686D:LN)
- Searches for a "Covalis … UAB" in Lithuanian registries returned no match. The only near-hit, "Covalio industry investment, UAB" (Kaunas, code 301870555, 1 employee), is an unrelated name — [Scoris.eu](https://scoris.eu/company/LT/301870555)
- **Sector context.** Sodra's Q4 2025 average was EUR 1,514 net (about EUR 2,480 gross). The 2023 sector average for finance and insurance was about EUR 2,932 gross — [LRT](https://www.lrt.lt/naujienos/verslas/4/2849151/sodra-gyventojai-lietuvoje-vidutiniskai-uzdirba-1-514-euru-i-rankas); [Kauno diena](https://m.kauno.diena.lt/naujienos/verslas/ekonomika/sodra-vidutinis-atlyginimas-metus-augo-12-proc-1163196). The 2026 "average wage" used for social insurance calculations is EUR 2,312.15, and the 2026 minimum monthly wage is EUR 1,153 — [Sodra](https://sodra.lt/sodros-imoku-tarifai-taikomi-nuo-2026-m-sausio-1-d-savarankiskai-dirbantiems-asmenims)
- 15min reported that IT and finance compete for the top average wages by sector, with IT leading and financial services second — [15min](https://www.15min.lt/verslas/naujiena/bendroves/didziausi-atlyginimai-pagal-sektorius-kas-daugiausiai-moka-is-it-imoniu-o-kas-is-prekybininku-ar-viesbuciu-663-2097594)
- There is new finance-operations investment in Vilnius, but in operations roles rather than front-office ones. Alter Domus (alternative-assets administrator) is opening a Vilnius centre of about 300 staff for fund administration, corporate services and payments — [Invest Lithuania](https://investlithuania.com/news/market-leading-alternative-investment-services-provider-expands-operations-to-vilnius/). Nasdaq has a new Vilnius office (Nasdaq Vilnius Services, the exchange and the CSD) — [Invest Lithuania](https://investlithuania.com/news/nasdaq-invites-you-to-take-a-look-at-their-new-office-in-vilnius/)

### Inferences
- The very highest finance averages come from **micro entities of 4 to 13 people**: GPS Capital Markets Europe (probably the EU arm of the US FX/payments firm GPS Capital Markets), AlphaPay and Kevin EU (payments/fintech). For a junior hire these numbers mostly reflect one or two senior executives or bonus months, not typical pay. Sodra averages for headcounts under about 10 are very noisy month to month.
- Covalis's Vilnius team is most likely registered as a branch or service company under a different name, so a name search misses it. It may also sit under EVRK 70.22 or 66.30 rather than a "Covalis" name. Its average wage would only show up by filtering the raw Sodra file by EVRK code, or by searching the Sodra employer search ("Draudėjų paieška") for "Covalis".
- Payment-institution and EMI entities licensed by the Bank of Lithuania (EVRK 64.19 and 66.19) will crowd the top of any "finance" filter. To find investment-research or hedge-fund-type offices, analysts should look at 66.30, 70.22 and 66.12, and screen out payments and crypto names (e.g., Onlychain Fintech).

### Gaps
- **The raw Sodra per-employer dataset could not be downloaded**, so there is no complete ranked list of EUR 5,000+ finance entities with headcounts. This is the central gap. Run `raw/sodra_filter_finance.py` locally to close it.
- Not identified: Covalis's Lithuanian legal entity name, company code, owners and Sodra wage.
- Not found: other hedge-fund or trading research offices, family offices, or energy-trading (35.14 / 46.12) entities with high wages. Searches for a "hedge fund / quant research office in Vilnius" returned nothing relevant.
- Ownership checks (Registrų centras JAR, rekvizitai "dalyviai") were impossible because those hosts were blocked.
- The rekvi.lt and TV3 figures are search-engine snippets, not verified page reads. Data months differ between sources.

## 2. Typical junior salaries by finance segment in Vilnius

### Takeaway
I found no credible, segment-specific junior benchmarks (PE, IB/M&A boutique, hedge fund, trading, asset management, bank CIB, consulting, Big4 deals) for Vilnius from 2025-2026 sources. Public aggregators only give generic "financial analyst" ranges of roughly **EUR 2,000–3,200 gross/month**, and the Glassdoor data for Vilnius is internally inconsistent.

### Cited Findings
- Inedjobs (Dec 2025) gives Financial Analyst pay in Lithuania as **EUR 2,000–3,200 gross/month**, with a Vilnius all-jobs average of about EUR 1,900–2,200 gross — [Inedjobs](https://www.inedjobs.com/2025/12/average-salaries-lithuania-2026.html)
- Glassdoor, Financial Analyst, Vilnius (about 20 submissions): total pay of about **EUR 1k–3k/month, median about EUR 2k/month**. One version of the page says it was last updated Jun 2022, and another labels similar figures as annual. The data is unreliable — [Glassdoor](https://www.glassdoor.com/Salaries/vilnius-financial-analyst-salary-SRCH_IL.0,7_IM1551_KO8,25.htm); [Glassdoor alt](https://www.glassdoor.com/Salaries/vilnius-lithuania-financial-analyst-salary-SRCH_IL.0,17_IM1551_KO18,35.htm)
- Glassdoor, Business Analyst, Vilnius (about 109 submissions, Oct 2026): **EUR 2k–3k/month base** — [Glassdoor](https://www.glassdoor.ca/Salaries/vilnius-business-analyst-salary-SRCH_IL.0,7_IM1551_KO8,24.htm)
- Manoalga.lt, Financial Analyst in Banking: 80% of respondents earn **EUR 1,464–3,403 per month NET** — [Manoalga](https://www.manoalga.lt/en/salaryinfo/banking/financial-analyst)
- TalentUp, Business Analyst, Vilnius: average base **EUR 35,500/year** (30 observations, Mar 2026) — [TalentUp](https://talentup.io/salary/Business%20Analyst/Vilnius)
- Payscale gives an average salary for all occupations in Vilnius of about **EUR 36k/year** (Jul 2026) — [Payscale](https://www.payscale.com/research/LT/Location=Vilnius/Salary)
- Pinigai360 gives "finance and banking" pay of **EUR 3,000–5,000 gross**, without separating seniority — [Pinigai360](https://pinigai360.lt/asmeniniai-finansai/atlyginimu-statistika-lietuvoje-2026/)
- Fund-manager averages (all staff, not juniors) are listed in section 1: SEB IV about EUR 2.5k, Prosperus about EUR 3.2k, Contrarian Ventures about EUR 5.4k (2024), Sound AM about EUR 6.8k.

### Inferences
- A reasonable working range for a fresh analyst in mainstream Vilnius finance (bank, asset manager, Big4) is about EUR 2,000–3,200 gross/month. This comes from the aggregators above.
- Small PE/VC houses and offshore hedge-fund research offices (like Covalis) probably pay well above this. Entity averages of EUR 5k–7k exist even at small 66.30 firms. No junior-specific number could be sourced.
- Lithuanian pay is quoted gross ("neatskaičius mokesčių"), but Manoalga and many news headlines use net ("į rankas"). Gross is roughly 1.6 times net at average wages (EUR 2,480 gross vs EUR 1,514 net in Q4 2025, per LRT above). Always confirm which basis a figure uses.

### Gaps
- Not found: 2025/26 Hays, Michael Page, Alliance for Recruitment or Grafton Lithuania salary guides with finance tables. Searches did not surface these PDFs.
- Not found: segment-specific junior figures for IB/M&A boutiques (e.g., Superia, Avia/Cobalt), PE (INVL, Lords LB, BaltCap, Livonia), bank CIB (SEB, Swedbank, Luminor), MBB or other consulting, and Big4 deals. Searches returned only generic aggregators.
- cvbankas.lt (which legally must post salary ranges in ads) could not be fetched. Scraping posted ranges for "investicijų analitikas", "M&A", "corporate finance" and "deals" there would be the best next step.

## 3. Hiring paths and structured programs for a returning Lithuanian HEC MSc IF graduate

### Takeaway
Three diaspora channels are active in 2026. Global Lithuanian Leaders (GLL) is a 10,000+ member network that runs the LT Big Brother mentoring programme, a summer forum and an awards event. Kurk Lietuvai / Create Lithuania is a government programme that places professionals with foreign experience in public-sector projects for a year. LT Big Brother is GLL's mentoring programme. None of these is a finance-specific recruiting pipeline. Private-sector finance hiring in Vilnius runs mainly through networking, LinkedIn and direct applications.

### Cited Findings
- **GLL** unites 10,000+ global Lithuanian professionals from 60+ countries and 28 clubs. The GLL Forum was held on **30 Jul 2026 in Vilnius** and the **GLL Awards are scheduled for 21 Dec 2026** — [GLL](https://lithuanianleaders.org/); [GLL events](https://lithuanianleaders.org/events/); [GLL Awards](https://gllawards.lt/en/); [Tickets](https://www.tickettailor.com/events/globallithuanianleaders)
- **LT Big Brother** is a volunteer mentoring network pairing established Lithuanian professionals with students and early-career people. It started in London in 2009 and is now run with GLL. Per one mentor's profile it covers six regions: Lithuania, UK, Scandinavia, USA, Benelux and global — LinkedIn mentor profiles via search ([example](https://lt.linkedin.com/in/jonas-kimontas)). This is self-reported, and the official site (ltbigbrother.com) was not fetched.
- **Kurk Lietuvai (Create Lithuania)** is a government initiative placing professionals in public-sector projects. It originally targeted young Lithuanian professionals with considerable foreign experience. Its 2026 cycle had a second project round presenting in March 2026 and results presented on 8 Sep 2026 — [Kurk Lietuvai](https://www.kurklt.lt/en); [About](https://www.kurklt.lt/en/about?lang=en); [Wikipedia](https://en.wikipedia.org/wiki/Kurk_Lietuvai)
- **HEC Paris and Lithuania.** The visible institutional link is the Baltic Management Institute EMBA consortium, which includes HEC Paris and Vytautas Magnus University. This is relevant for the alumni network, not for MSc recruiting — search results via LinkedIn profiles ([example](https://lt.linkedin.com/in/karolinakapustinskaite))

### Inferences
- Kurk Lietuvai pays public-sector-level wages. It is a networking and visibility route, not a high-pay finance entry, though it builds ties with the Ministry of Finance, Invest Lithuania and Bank of Lithuania circles.
- For hedge-fund-type offices like Covalis Vilnius, the practical path is direct outreach to the Lithuanian analysts on LinkedIn and an approach through the London HQ. These roles are rarely advertised locally.

### Gaps
- No sourced information on **HEC Alumni Lithuania** chapter activity, **LiJOT** (Lithuanian Youth Council) career programmes, Create Lithuania's current salary and terms, or any **tax incentive or returning-diaspora relocation programme** for the private sector.
- Not covered by any source: recruiting timing (e.g., Swedbank and SEB graduate programmes typically open in autumn and spring; Big4 hiring follows the academic calendar) and **CFA Society** presence or employer valuation of the CFA in Lithuania.

---
Files in this folder: `raw/sodra_filter_finance.py` (an offline filter for the Sodra monthly per-employer CSV by finance EVRK codes; no raw extracts could be saved because all downloads were blocked).
