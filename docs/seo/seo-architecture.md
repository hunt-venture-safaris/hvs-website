# SEO architecture — huntventuresafaris.com

Owner: SEO workstream · Status: proposal for Phase 1 build · Date: 7 Nov 2026
Source of truth for facts: `hvs-research/BRIEF.md` and the five 2027–28 brochures. Anything not in those is marked **TBC (client to confirm)**. No prices appear anywhere on the site; every price reference is "on request".

Companion files in this folder:

| File | Purpose |
|---|---|
| `robots.txt` | Phase 1 robots file (staged; copy to site root at launch) |
| `sitemap.xml` | Phase 1 sitemap with hreflang pairs (28 indexable URLs) |
| `schema/*.json` | One valid JSON-LD template per type (Organization/TravelAgency, WebSite, 5 × TouristTrip, BreadcrumbList, FAQPage, Article, Spanish WebPage) |

---

## 1. Search landscape

### 1.1 Intent types

| Intent | Typical queries | What the searcher needs | Who serves it today |
|---|---|---|---|
| Commercial (booking) | "markhor hunting Pakistan", "himalayan ibex hunt pakistan", "sindh ibex hunt", "blue sheep hunt shimshal", "pakistan hunting outfitter" | Species, area, dates, duration, what's included, how to enquire, proof the outfitter is legitimate | Marketplaces first: [BookYourHunt](https://www.bookyourhunt.com/hunting-in-pakistan), [Mallard Bay](https://mallardbay.com/markhor-safari), [Hunt Info](https://www.huntinfool.com/adventures/trip-detail/M01KdndOMzJRbDQ90), [Guidefitter](https://www.guidefitter.com/hunt/26452-himalayan-ibex-hunting-in-northern-areas); US agents such as [Outdoors International](https://outdoors-international.com/pakistan); a few Pakistani operators (e.g. [Pakistan Guides](https://pakistanguides.com/hunting), [Jasmine Tours](https://www.jasminetours.com/?p=602)) |
| Informational | permit auction, permit cost, CITES/trophy import, season dates, firearm import, flights to Gilgit, altitude, what to pack | Clear, current explanations | Pakistani news ([Dawn](https://www.dawn.com/news/2028988), [ProPakistani](https://propakistani.pk/2025/09/04/astore-markhor-hunting-permit-sold-for-world-record-fee/), [Arab News](https://www.arabnews.pk/pakistan/trophy-hunting-season-kicks-off-in-pakistans-north-amid-poaching-and-poetry-1784421)), [Conservation Force](https://www.conservationforce.org/markhor), forums ([AccurateReloading](https://forums.accuratereloading.com/eve/forums/a/tpc/f/426108036/m/8541037241)), science papers, the [GB Forest, Wildlife & Environment Dept](https://fwegb.gov.pk/2022/11/15/1st-successful-hunt-of-blue-sheep-in-shimshal-area-of-the-hunting-season-2022-23) |
| Navigational / brand | "hunt venture safaris", "HVS Gilgit", "hunt venture safaris markhor" | Official site, phone, WhatsApp, licence | Today the [BookYourHunt HVS profile](https://www.bookyourhunt.com/en/outfitters/hunt-venture-safaris) competes with the brand's own homepage |
| Spanish commercial | "caza markhor pakistán", "caza íbice pakistán", "cacería en Pakistán" | Same as EN, in Spanish | Weak. A "caza markhor pakistan" search returns mostly English conservation/news pages and a 2019 Spanish magazine piece ([Aire Libre](https://revista-airelibre.com/2019/02/20/otro-ejemplo-de-caza-sustentable)); no Spanish-language outfitter page ranked in my checks |

### 1.2 What competitors publish (and don't)

- **BookYourHunt** Pakistan hub: 22 hunts from 9 outfitters with "price from" figures, species and methods; no permit guide, no firearm guidance, no FAQ on the page ([source](https://www.bookyourhunt.com/hunting-in-pakistan)).
- **Outdoors International**: species and season overview for markhor, Sindh ibex, Himalayan ibex, Blanford urial, blue sheep; no prices, permits, CITES/import or firearms content ([source](https://outdoors-international.com/pakistan)).
- **Per-hunt listings** on marketplaces are thin: price, days, a paragraph, season window.
- **News** covers the annual GB auction in detail (permit numbers and winning bids) — e.g. the 2026–27 auction sold 117 permits (3 Astore markhor + 1 carried over, 14 blue sheep, 100 Himalayan ibex) ([Dawn, Sept 2026](https://www.dawn.com/news/2028988)); the 2025–26 report noted about 80% of revenue goes to local communities ([Dawn, Sept 2025](https://www.dawn.com/news/1939432)).

### 1.3 Gaps HVS can win

1. **Authoritative per-species pages from the outfitter itself** with real legal period, recommended window, altitude, area, day-by-day itinerary, full inclusions/exclusions. Nobody ranking combines all of these on one page.
2. **Permit auction explained from the outfitter's side** (how HVS prices around the auction; minor rises absorbed, substantial rises invoiced) — unique, factual, from the brochure.
3. **Logistics hunters actually worry about**: Islamabad–Gilgit flight with 4x4 fallback, firearm import/export documents (included), trophy export (excluded — say so plainly), altitude.
4. **Community-controlled hunting areas** story — accurate, sourced, not inflated.
5. **Heritage and licence**: "since 1989" and "Govt. licence No. 2087" are rare, verifiable trust signals among Pakistani competitors.
6. **Spanish-language pages** for the Cinegética audience — near-empty SERP.
7. **Brand SERP control**: get the official site above the marketplace profile for "hunt venture safaris".

---

## 2. Keyword map

No search volumes are claimed. "Priority" is relative, reasoned from commercial value, SERP competition observed, and HVS's ability to satisfy the query.

| Page | Primary keyword | Secondary keywords | Intent | Lang | Priority | Reasoning |
|---|---|---|---|---|---|---|
| `/` | pakistan hunting outfitter | trophy hunting pakistan, hunting in gilgit-baltistan, hunt venture safaris | Commercial / brand | EN | High | Brand + head term; homepage carries the most authority |
| `/hunts/` | trophy hunting in pakistan | mountain hunts pakistan, pakistan hunting packages | Commercial | EN | High | Hub; competes with BookYourHunt's Pakistan hub |
| `/hunts/astore-markhor/` | astore markhor hunt | markhor hunting pakistan, markhor hunting gilgit-baltistan, capra falconeri falconeri hunt | Commercial | EN | High | Flagship, highest-value hunt, marketplaces rank with thin pages |
| `/hunts/himalayan-ibex/` | himalayan ibex hunt pakistan | ibex hunting hunza, himalayan ibex hunting | Commercial | EN | High | Largest permit pool (100/season) = most buyers |
| `/hunts/blue-sheep/` | blue sheep hunt pakistan | blue sheep hunting shimshal, bharal hunt pakistan | Commercial | EN | High | Small, specialist SERP; Shimshal is a precise area match |
| `/hunts/blanford-urial-sindh-ibex/` | sindh ibex and blanford urial hunt | sindh ibex hunt, blanford urial hunt, dureji hunting | Commercial | EN | Med | Combo is well served by US agents; HVS can win on detail |
| `/hunts/punjab-urial/` | punjab urial hunt | urial hunting punjab, kala bagh urial | Commercial | EN | Low | Profile-only data; thin until detail sheet exists |
| `/hunting-in-pakistan/` | hunting in pakistan guide | how to hunt in pakistan | Informational | EN | Med | Hub for guides |
| `/hunting-in-pakistan/permits-and-cites/` | pakistan trophy hunting permit | markhor permit auction, cites markhor | Informational | EN | High | High news interest; no outfitter explains it well |
| `/hunting-in-pakistan/trophy-export/` | trophy export pakistan | import markhor trophy, shipping hunting trophies from pakistan | Informational | EN | Med | Excluded from packages, so must be explained |
| `/hunting-in-pakistan/firearms/` | bringing rifle to pakistan for hunting | firearm import pakistan hunting | Informational | EN | Med | Included service; strong reassurance content |
| `/hunting-in-pakistan/travel-and-logistics/` | flights islamabad to gilgit | getting to gilgit, karakoram highway hunting travel | Informational | EN | Med | Real fallback (4x4) is a differentiator |
| `/hunting-in-pakistan/hunting-seasons/` | pakistan hunting season dates | markhor season, ibex season pakistan | Informational | EN | Med | Facts HVS owns; easy featured-snippet target |
| `/plan-your-hunt/` | book a hunt in pakistan | hunting enquiry pakistan | Transactional | EN | High (conversion) | Enquiry endpoint |
| `/about/` | hunt venture safaris | gilgit hunting company since 1989, licence 2087 | Navigational | EN | Med | Brand/E-E-A-T |
| `/conservation/` | trophy hunting conservation pakistan | community trophy hunting gilgit-baltistan | Informational | EN | Med | Trust; links from conservation press |
| `/tours-and-expeditions/` | jeep safari gilgit | trekking gilgit-baltistan, mountaineering expedition pakistan | Commercial | EN | Low | Secondary services |
| `/contact/` | hunt venture safaris contact | hunting outfitter gilgit | Navigational | EN | Med | NAP page for local SEO |
| `/es/` | caza en pakistán | outfitter pakistán, cacería pakistán | Commercial | ES | High (for Cinegética) | Open SERP |
| `/es/cazas/markhor-de-astore/` | caza markhor pakistán | caza markhor de astore, cacería de markhor | Commercial | ES | High | No Spanish outfitter page seen |
| `/es/cazas/ibice-del-himalaya/` | caza íbice del himalaya pakistán | caza íbice pakistán | Commercial | ES | Med | |
| `/es/cazas/carnero-azul/` | caza carnero azul pakistán | caza bharal | Commercial | ES | Med | "Carnero azul" / "bharal" both used in Spanish; test |
| `/es/cazas/urial-de-blanford-e-ibice-de-sind/` | caza íbice de sind | caza urial blanford | Commercial | ES | Med | |
| `/es/cazas/urial-del-punjab/` | caza urial punjab | | Commercial | ES | Low | |

**Note on species names:** use the brochure spellings ("Blanford urial", "Sindh ibex", "Astore markhor") in headings; mention common variants ("Blandford urial", "Sind ibex", "bharal", "flare-horned markhor") once in body copy because marketplaces and forums use them ([BookYourHunt combo listing](https://www.bookyourhunt.com/en/tour/44051), [Outdoors International](https://outdoors-international.com/blandford-urial-hunting/)).

---

## 3. Site architecture

### 3.1 URL rules

- Lowercase, hyphenated, English nouns; Spanish under `/es/` with Spanish slugs.
- No dates, no season years, no `.html` in URLs (season goes in content, not the URL, so URLs survive each season).
- **Trailing slash: always.** Every page is a folder with `index.html` (`/hunts/astore-markhor/index.html` → `/hunts/astore-markhor/`). Canonicals, sitemap, internal links and hreflang all use the slash form.

`vercel.json` (site root):

```json
{
  "cleanUrls": true,
  "trailingSlash": true,
  "redirects": [
    { "source": "/index", "destination": "/", "permanent": true },
    { "source": "/hunts/markhor", "destination": "/hunts/astore-markhor/", "permanent": true },
    { "source": "/hunts/ibex", "destination": "/hunts/himalayan-ibex/", "permanent": true },
    { "source": "/hunts/sindh-ibex", "destination": "/hunts/blanford-urial-sindh-ibex/", "permanent": true },
    { "source": "/hunts/blanford-urial", "destination": "/hunts/blanford-urial-sindh-ibex/", "permanent": true },
    { "source": "/enquiry", "destination": "/plan-your-hunt/", "permanent": true },
    { "source": "/contact-us", "destination": "/contact/", "permanent": true }
  ],
  "headers": [
    { "source": "/assets/(.*)", "headers": [{ "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }] },
    { "source": "/thank-you/", "headers": [{ "key": "X-Robots-Tag", "value": "noindex" }] },
    { "source": "/es/gracias/", "headers": [{ "key": "X-Robots-Tag", "value": "noindex" }] }
  ]
}
```

Behaviour: `cleanUrls` serves `about/index.html` and strips `.html` (redirecting `/x.html` to `/x`); `trailingSlash: true` then 308-redirects slashless paths to the slash form. Test after deploy with `curl -I` on `/about`, `/about.html` and `/about/` (expect 308, 308, 200). (I could not open Vercel's `vercel.json` docs page during research — the fetch was blocked — so confirm against the Vercel docs before merging.) Assets with file extensions (`/sitemap.xml`, `/robots.txt`, images) are not given a slash.

### 3.2 Page tree (P1 = launch, P2 = later)

```
/                                              P1  Home
├── hunts/                                     P1  Hunts hub
│   ├── astore-markhor/                        P1
│   ├── himalayan-ibex/                        P1
│   ├── blue-sheep/                            P1
│   ├── blanford-urial-sindh-ibex/             P1
│   └── punjab-urial/                          P1  (lighter page; profile data only)
├── hunting-in-pakistan/                       P1  Guides hub
│   ├── permits-and-cites/                     P1
│   ├── trophy-export/                         P1
│   ├── firearms/                              P1
│   ├── travel-and-logistics/                  P1
│   ├── hunting-seasons/                       P1
│   ├── altitude-and-fitness/                  P2
│   ├── what-to-pack/                          P2
│   ├── visa-for-hunters/                      P2
│   └── <articles from §8>                     P2
├── regions/                                   P2  Area hub (only when there is enough unique content)
│   ├── gilgit-baltistan/                      P2
│   ├── hunza-and-shimshal/                    P2
│   └── sindh-and-balochistan/                 P2
├── tours-and-expeditions/                     P1  One page: tours & trekking, jeep safaris, mountaineering
│   ├── trekking/                              P2
│   ├── jeep-safaris/                          P2
│   └── mountaineering/                        P2
├── plan-your-hunt/                            P1  Enquiry form
├── thank-you/                                 P1  noindex
├── agents/                                    P1  Booking agents and consultants (B2B)
├── cinegetica/                                P1  noindex; trade-fair QR landing (campaign)
├── about/                                     P1
│   └── references/                            P2  (testimonials, with consent)
├── conservation/                              P1
├── contact/                                   P1
├── privacy/                                   P1
├── 404.html                                   P1  (Vercel serves for unknown paths)
└── es/                                        P1  Spanish
    ├── cazas/                                 P1
    │   ├── markhor-de-astore/                 P1
    │   ├── ibice-del-himalaya/                P1
    │   ├── carnero-azul/                      P1
    │   ├── urial-de-blanford-e-ibice-de-sind/ P1
    │   └── urial-del-punjab/                  P1
    ├── planificar-caceria/                    P1
    ├── gracias/                               P1  noindex
    ├── contacto/                              P1
    ├── cinegetica/                            P1  noindex; Spanish trade-fair landing
    ├── caza-en-pakistan/permisos-y-cites/     P2
    ├── quienes-somos/                         P2
    └── conservacion/                          P2
```

Why no `/regions/` in Phase 1: each region would only repeat hunt-page facts (thin/duplicate). Areas are covered inside hunt pages; regions arrive when there is distinct content (photos, village/community notes, access).

### 3.3 Navigation labels

Primary nav (EN): **Hunts** · **Planning** (links to `/hunting-in-pakistan/`, H1 "Hunting in Pakistan") · **Conservation** · **About** · **Contact** · button **Plan your hunt** · language switch **ES**. Five items keeps the bar within Apple HIG guidance and matches the user-flows IA; **Tours & Expeditions** and **Agents** are linked from the footer and from a home-page section, as secondary services.
Primary nav (ES): **Cazas** · **Contacto** · botón **Planificar cacería** · **EN**. (Spanish nav shows only translated pages; no links to untranslated pages except the EN guides hub, labelled "Guías (en inglés)".)
Footer: legal name, licence No. 2087, address, phones, email, WhatsApp, links to all hunts, guides, privacy.

### 3.4 Hub-and-spoke internal linking

```
            Home
             │
   ┌─────────┼───────────────┐
 Hunts hub   Guides hub     About / Conservation
   │  ▲          │  ▲
   ▼  │          ▼  │
 Hunt pages ◄──► Guides (permits, export, firearms, travel, seasons)
   │
   └──► Plan your hunt (pre-selects species via ?species=astore-markhor)
```

Rules:
- Every hunt page links **up** to `/hunts/`, **across** to 1–2 related hunts (markhor ↔ ibex; ibex ↔ blue sheep; combo ↔ Punjab urial), **out** to each relevant guide (permits, firearms, trophy export, travel, seasons) and **down** to `/plan-your-hunt/?species=…`.
- Every guide links back to every hunt it is relevant to, with species-named anchor text ("Astore markhor hunt"), not "click here".
- `/conservation/` links to permits guide and to each GB hunt; hunt pages link to `/conservation/` from the "community-controlled hunting area" sentence.
- Query parameters on enquiry links are fine; the enquiry page canonical is `/plan-your-hunt/` without parameters.

### 3.5 Breadcrumbs

Visible on every page except Home; marked up with `BreadcrumbList` (template `schema/breadcrumblist-hunt.json`). Breadcrumb rich results remain in Google's [search gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery).

- Home › Hunts › Astore Markhor
- Home › Hunting in Pakistan › Permits & CITES
- Inicio › Cazas › Markhor de Astore

---

## 4. Per-page specs (Phase 1)

Conventions: titles ≤60 characters, descriptions ≤155 (counts checked). Brand suffix "| HVS" or "| Hunt Venture Safaris" only where it fits. One H1 per page. "Rates on request" CTA wording everywhere instead of prices.

Shared hunt-page template (applies to the five hunt pages):

1. Hero: landscape photo (no carcass), H1, one-line summary, primary CTA.
2. **At a glance** table: species (scientific name), area, legal hunting period, recommended period, altitude, duration, start/end city.
3. **Day-by-day itinerary** (from brochure).
4. **Included / Not included** (brochure lists, verbatim facts).
5. **Rates for 2027–28**: "1 hunter · 2 hunters · non-hunting companion · extra hunting day — on request" + permit-auction note (paraphrase of brochure).
6. **Terrain and fitness**: altitude, trek days (blue sheep), terrain (flat for Dureji).
7. **Getting there**: start city; Islamabad–Gilgit flight with 4x4 fallback, or Karachi.
8. **Community-controlled hunting area** paragraph → `/conservation/`.
9. FAQ block (3–5 Qs, visible HTML; FAQPage markup optional, see §5).
10. Related hunts + guides; CTA band.

Schema on every hunt page: `TouristTrip` + `BreadcrumbList` (+ optional `FAQPage`), Organization referenced by `@id`.

### 4.1 English pages

| URL | Title tag | Meta description | H1 |
|---|---|---|---|
| `/` | Trophy Hunting in Pakistan Since 1989 \| Hunt Venture Safaris | Government-licensed (No. 2087) hunting outfitter in Gilgit since 1989. Astore markhor, Himalayan ibex, blue sheep and urial hunts. Rates on request. | Trophy hunting in Pakistan since 1989 |
| `/hunts/` | Hunts in Pakistan: Markhor, Ibex, Blue Sheep, Urial \| HVS | Five guided hunts in Gilgit-Baltistan, Sindh–Balochistan and Punjab: season dates, altitude, duration and itineraries for 2027–28. Rates on request. | Hunts in Pakistan |
| `/hunts/astore-markhor/` | Astore Markhor Hunt, Gilgit-Baltistan \| HVS | 20-day Astore markhor hunt with 15 hunting days at 2,500–4,700 m. Season 15 Oct–30 Apr, best mid Nov–mid Feb. Itinerary, inclusions, rates on request. | Astore markhor hunt |
| `/hunts/himalayan-ibex/` | Himalayan Ibex Hunt in Upper Hunza, Pakistan \| HVS | 10–12 day Himalayan ibex hunt in Upper Hunza at 2,500–4,700 m. Season 1 Nov–26 Apr, best mid Nov–mid Feb. Full itinerary and inclusions. | Himalayan ibex hunt |
| `/hunts/blue-sheep/` | Blue Sheep Hunt in Shimshal Valley, Pakistan \| HVS | 15–16 day blue sheep hunt in Shimshal, Hunza, at 3,200–4,500 m with a two-day trek in. Season 1 Nov–30 Apr, best Nov, Mar and Apr. | Blue sheep hunt in Shimshal Valley |
| `/hunts/blanford-urial-sindh-ibex/` | Blanford Urial & Sindh Ibex Combo Hunt, Dureji \| HVS | 9-day combination hunt in Dureji, Sindh–Balochistan: 3 days for Blanford urial, 2 for Sindh ibex. Karachi to Karachi, best Dec–Jan. | Blanford urial and Sindh ibex combination hunt |
| `/hunts/punjab-urial/` | Punjab Urial Hunt: Kala Bagh, Jhelum, Padri \| HVS | Punjab urial hunt of up to five hunting days in Kala Bagh, Jhelum and Padri. Best December to March. Itinerary and rates on request. | Punjab urial hunt |
| `/hunting-in-pakistan/` | Hunting in Pakistan: A Guide for Visiting Hunters \| HVS | Permits, CITES, firearms, trophy export, seasons and travel to Gilgit: what visiting hunters need to know before a hunt in Pakistan. | Hunting in Pakistan: a guide for visiting hunters |
| `/hunting-in-pakistan/permits-and-cites/` | Trophy Hunting Permits & CITES in Pakistan \| HVS | How Pakistan allocates trophy permits by open government auction, what that means for your rate, and the CITES paperwork for your trophy. | Trophy hunting permits and CITES in Pakistan |
| `/hunting-in-pakistan/trophy-export/` | Exporting Your Hunting Trophy from Pakistan \| HVS | What we include (skinning, salting, packing, permit formalities) and what is arranged separately: trophy export, shipment and customs. | Exporting your trophy from Pakistan |
| `/hunting-in-pakistan/firearms/` | Bringing Your Rifle to Pakistan for a Hunt \| HVS | Firearm import and export documents are included in every HVS hunt. What we need from you, and when, to clear your rifle in Pakistan. | Bringing your rifle to Pakistan |
| `/hunting-in-pakistan/travel-and-logistics/` | Getting to Gilgit and Karachi for Your Hunt \| HVS | Islamabad–Gilgit flights are included, with 4x4 road transport if flights are cancelled. Arrival, transfers, baggage limits and timings. | Travel and logistics for your hunt |
| `/hunting-in-pakistan/hunting-seasons/` | Pakistan Hunting Season Dates 2027–28 \| HVS | Legal and recommended hunting periods for Astore markhor, Himalayan ibex, blue sheep, Blanford urial, Sindh ibex and Punjab urial. | Hunting season dates in Pakistan, 2027–28 |
| `/tours-and-expeditions/` | Tours, Treks, Jeep Safaris & Expeditions, Gilgit \| HVS | Beyond hunting: tours and trekking, jeep safaris and mountaineering expeditions in the Karakoram, Himalaya and Hindu Kush. Ask for details. | Tours, treks and expeditions |
| `/plan-your-hunt/` | Plan Your Hunt in Pakistan: Enquiry \| HVS | Tell us your species, dates and party size. We reply with the 2027–28 rates, availability and a tailored itinerary. | Plan your hunt |
| `/about/` | About Hunt Venture Safaris: Gilgit Since 1989 | Hunt Venture Safaris (Pvt) Limited: government licence No. 2087, Gilgit-based since 1989, guiding hunts across the Karakoram, Himalaya and Hindu Kush. | About Hunt Venture Safaris |
| `/conservation/` | Conservation and Community Hunting Areas \| HVS | How regulated trophy hunting works in community-controlled areas of Gilgit-Baltistan, and how hunts contribute to wildlife and local communities. | Conservation and community hunting areas |
| `/contact/` | Contact Hunt Venture Safaris, Gilgit \| HVS | Call +92 311 166 7829 or +92 300 989 3205, email huntventuresafaris@gmail.com, or visit our office at Hotel Riveria, Chinar Bagh, Gilgit. | Contact us |
| `/privacy/` | Privacy Policy \| Hunt Venture Safaris | How Hunt Venture Safaris collects and uses the details you send through our enquiry form, email and WhatsApp. | Privacy policy |

### 4.2 English page outlines, content blocks, CTAs, links, schema

**`/` Home**
- H2: Our hunts · Why Hunt Venture Safaris · Hunting in Pakistan, explained · Conservation and communities · Beyond hunting · Plan your hunt
- Blocks: trust strip (1989 · Licence No. 2087 · Karakoram, Himalaya, Hindu Kush); five hunt cards (duration, best time, altitude, area); "Why us" paraphrase of brochure; guide teasers; secondary services; contact band.
- CTA: **Plan your hunt** (primary), WhatsApp (secondary).
- Links out: all hunts, guides hub, about, conservation, contact. Links in: every page (logo).
- Schema: `TravelAgency` (full Organization node), `WebSite`.

**`/hunts/` hub**
- H2: Gilgit-Baltistan mountain hunts · Southern Pakistan hunts · Compare hunts at a glance · How rates and permits work
- Blocks: comparison table (hunt, legal period, best time, altitude, duration, start/end); permit-auction note → permits guide.
- CTA: Plan your hunt. Links: all hunt pages, permits guide, seasons guide. Schema: `CollectionPage` (inline, optional), `ItemList` of the five `TouristTrip` `@id`s, `BreadcrumbList`.

**`/hunts/astore-markhor/`**
- H2: At a glance · 20-day itinerary · What's included · What's not included · Rates for 2027–28 · Terrain and altitude · Getting to Gilgit · Community-controlled hunting areas · Questions about the markhor hunt
- Facts: *Capra falconeri falconeri*; Nagar, Skardu, Astore, Gilgit, Bunji, Kargah; 15 Oct–30 Apr; mid Nov–mid Feb; 2,500–4,700 m; 20 days, 15 hunting; Islamabad–Islamabad; permit for one Astore markhor included.
- CTA: **Ask for the 2027–28 markhor rate** → `/plan-your-hunt/?species=astore-markhor`.
- Links out: ibex page, permits, trophy export, firearms, travel, conservation. Links in: home, hunts hub, permits, seasons, conservation, ES twin. Schema: `TouristTrip`, `BreadcrumbList`.

**`/hunts/himalayan-ibex/`**
- H2 as template; "10-day itinerary".
- Facts: *Capra ibex sibirica*; District Hunza (Upper Hunza); 1 Nov–26 Apr; mid Nov–mid Feb; 2,500–4,700 m; 10–12 days, five hunting days in the plan; return to Gilgit evening of day 8.
- CTA: Ask for the 2027–28 ibex rate. Related: markhor, blue sheep. Schema: `TouristTrip`, `BreadcrumbList`.

**`/hunts/blue-sheep/`**
- H2 as template plus "The trek in and out".
- Facts: *Pseudois nayaur*; Shimshal Valley, District Hunza; 1 Nov–30 Apr; Nov, Mar, Apr; 3,200–4,500 m; 15–16 days; trek days 4–5, hunt days 6–12, return trek 13–14.
- CTA: Ask for the 2027–28 blue sheep rate. Related: ibex. Schema: `TouristTrip`, `BreadcrumbList`.

**`/hunts/blanford-urial-sindh-ibex/`**
- H2 as template; "Getting to Karachi" replaces Gilgit.
- Facts: Dureji, Sindh–Balochistan; 1 Nov–30 Apr; Dec–Jan; 500–3,000 ft, flat terrain; 9 days, 5 hunting (3 urial, 2 ibex); Karachi–Karachi; permits for both species; domestic return flight included; accommodation in Karachi and camps.
- CTA: Ask for the 2027–28 combo rate. Related: Punjab urial. Schema: `TouristTrip`, `BreadcrumbList`.

**`/hunts/punjab-urial/`**
- H2: At a glance · What to expect · Rates and itinerary on request · Other southern hunts
- Facts: Kala Bagh, Jhelum, Padri; Dec–Mar; up to 5 hunting days. Legal period, altitude, start city, itinerary: **TBC (client to confirm)** — do not display placeholders; say "itinerary on request".
- Keep indexable but expand when a detail sheet exists; if it stays very thin at launch, add a short note on terrain from the client. Schema: `TouristTrip` (no itinerary), `BreadcrumbList`.

**`/hunting-in-pakistan/` hub**
- H2: Permits and CITES · Firearms · Trophy export · Travel and logistics · Season dates
- Blocks: one-paragraph summary + link per guide. Schema: `CollectionPage`, `BreadcrumbList`.

**`/hunting-in-pakistan/permits-and-cites/`**
- H2: How permits are allocated (open government auction) · What the auction means for your rate · Permits included in your package · Community-controlled hunting areas · CITES and import permits for your home country · What we need from you, and when
- Facts from brochure: permit auction; minor rises absorbed, substantial rises invoiced; included: trophy permit, provincial shooting licence fee, government liaison, trophy permit formalities and fees. External facts may cite official/news sources with dates (e.g. permit counts per season from [Dawn](https://www.dawn.com/news/2028988)). CITES and home-country import requirements (e.g. US, EU) must be **checked by the client or a specialist** before publishing — state "requirements vary by country; we will confirm the documents for yours".
- CTA: Ask about permits for your species. Links: all hunts, trophy export, conservation. Schema: `Article`, `BreadcrumbList`, optional `FAQPage`.

**`/hunting-in-pakistan/trophy-export/`**
- H2: What is included (skinning, salting, packing; trophy permit formalities) · What is not included (trophy export, shipment, customs clearance, excess baggage) · How export is arranged · Timelines · Your home-country import
- Process details beyond the brochure: **TBC (client to confirm)** (shipping agent, typical timeline).
- Schema: `Article`, `BreadcrumbList`.

**`/hunting-in-pakistan/firearms/`**
- H2: Firearm documents are included · What we need from you · Travelling via Islamabad or Karachi · Ammunition (TBC) · Prefer not to travel with a rifle? (TBC whether rifle hire is offered)
- Schema: `Article`, `BreadcrumbList`.

**`/hunting-in-pakistan/travel-and-logistics/`**
- H2: Arriving in Islamabad · Islamabad–Gilgit flights and the 4x4 fallback · Arriving in Karachi (southern hunts) · Baggage (50 kg or two duffle bags) · Accommodation and meals (full board) · Visa assistance · Insurance and rescue (not included — arrange your own)
- Schema: `Article`, `BreadcrumbList`.

**`/hunting-in-pakistan/hunting-seasons/`**
- H2: Season table 2027–28 · Best time for each species · Weather and snow (TBC from client)
- Block: one table, all species — prime featured-snippet target. Season dates are the brochure's; add the note "dates follow the official notification each season and may change". Schema: `Article`, `BreadcrumbList`.

**`/tours-and-expeditions/`**
- H2: Tours and trekking · Jeep safaris · Mountaineering expeditions · Ask for an itinerary
- Facts: only that HVS offers these across the Karakoram, Himalaya and Hindu Kush. Routes/peaks: TBC. CTA: Contact (not the hunt form). Schema: `BreadcrumbList`.

**`/plan-your-hunt/`**
- H2: Your hunt · Your party · Your dates · How we reply · Prefer to talk? (WhatsApp, phone, email)
- Fields: name, email, country, species (pre-filled from `?species=`), season, hunters, non-hunting companions, message, consent checkbox.
- Canonical without parameters. Success → `/thank-you/` (noindex). Schema: `ContactPage`, `BreadcrumbList`.

**`/about/`**
- H2: A legacy since 1989 · Licence No. 2087 · Our team (names/photos TBC with consent) · Where we hunt · How we work (responsible, sustainable hunting) · Visit us in Gilgit
- Schema: `AboutPage` + full `TravelAgency` node can live here or home (one place only, referenced elsewhere by `@id`).

**`/conservation/`**
- H2: Community-controlled hunting areas · How permits are allocated · Where the money goes · Our responsibilities in the field
- Use only the brochure claim ("every hunt contributes to conservation and local community development") plus cited, dated third-party figures. Schema: `Article`, `BreadcrumbList`.

**`/contact/`**
- H2: Call or WhatsApp · Email · Office in Gilgit (map embed, lazy) · Licence and company details
- NAP block exactly as §7.9. Schema: `ContactPage`, `BreadcrumbList`.

### 4.3 Spanish pages (Phase 1)

Same outlines as the EN twins, translated by a human native speaker (not machine-only); species facts identical.

| URL | Title | Meta description | H1 |
|---|---|---|---|
| `/es/` | Caza en Pakistán desde 1989 \| Hunt Venture Safaris | Outfitter con licencia oficial n.º 2087 en Gilgit desde 1989. Caza de markhor de Astore, íbice del Himalaya, carnero azul y urial. Precio a consultar. | Caza en Pakistán desde 1989 |
| `/es/cazas/` | Cazas en Pakistán: markhor, íbice, carnero azul \| HVS | Cinco cacerías guiadas en Gilgit-Baltistán, Sind–Baluchistán y Punjab: temporadas, altitud, duración e itinerarios 2027–28. | Cazas en Pakistán |
| `/es/cazas/markhor-de-astore/` | Caza de markhor de Astore en Pakistán \| HVS | Cacería de 20 días (15 de caza) a 2.500–4.700 m. Temporada 15 oct–30 abr; mejor de mediados de nov. a mediados de feb. Precio a consultar. | Caza de markhor de Astore |
| `/es/cazas/ibice-del-himalaya/` | Caza de íbice del Himalaya en Hunza, Pakistán \| HVS | Cacería de 10–12 días en el Alto Hunza a 2.500–4.700 m. Temporada 1 nov–26 abr; mejor de mediados de nov. a mediados de feb. | Caza de íbice del Himalaya |
| `/es/cazas/carnero-azul/` | Caza de carnero azul (bharal) en Shimshal \| HVS | Cacería de 15–16 días en el valle de Shimshal a 3.200–4.500 m, con dos días de trekking. Mejor en noviembre, marzo y abril. | Caza de carnero azul en el valle de Shimshal |
| `/es/cazas/urial-de-blanford-e-ibice-de-sind/` | Caza de urial de Blanford e íbice de Sind \| HVS | Combinada de 9 días en Dureji, Sind–Baluchistán: 3 días de urial y 2 de íbice. De Karachi a Karachi; mejor en diciembre y enero. | Urial de Blanford e íbice de Sind: cacería combinada |
| `/es/cazas/urial-del-punjab/` | Caza de urial del Punjab en Pakistán \| HVS | Cacería de urial del Punjab, hasta cinco días de caza en Kala Bagh, Jhelum y Padri. Mejor de diciembre a marzo. Itinerario a consultar. | Caza de urial del Punjab |
| `/es/planificar-caceria/` | Planifique su cacería en Pakistán \| HVS | Indíquenos especie, fechas y número de cazadores. Le enviamos precios 2027–28, disponibilidad e itinerario a medida. | Planifique su cacería |
| `/es/contacto/` | Contacto: Hunt Venture Safaris, Gilgit | Llámenos al +92 311 166 7829 o +92 300 989 3205, escriba a huntventuresafaris@gmail.com o visite nuestra oficina en Gilgit. | Contacto |

Spanish register: formal *usted*. Check species names with the client's Cinegética materials (e.g. "carnero azul" vs "bharal"; "íbice de Sind" vs "cabra de Sind"). Schema: `TouristTrip` duplicated with `inLanguage`-bearing `WebPage` (template `schema/webpage-es-hunt.json`) pointing `about` at the EN trip `@id`.

---

## 5. Structured data

### 5.1 What Google actually shows (Nov 2026)

| Type | Rich result? | Use on HVS? |
|---|---|---|
| Organization | Yes — knowledge panel details: logo, legal name, address, contacts, identifiers ([Google docs](https://developers.google.com/search/docs/appearance/structured-data/organization)) | **Yes**, once, on home (or About), as `TravelAgency` |
| LocalBusiness | Yes — local business details ([gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery)); Google says use the most specific subtype | **Yes** — `TravelAgency` is a LocalBusiness subtype, so one node covers both |
| BreadcrumbList | Yes | **Yes**, every page except home |
| FAQPage | **No longer shown.** Google states FAQ rich results stopped appearing on 7 May 2026, with the report and Rich Results Test support dropped in June 2026; the type is still read for understanding ([Google FAQPage doc](https://developers.google.com/search/docs/appearance/structured-data/faqpage), summarised by [TechWyse](https://www.techwyse.com/news/ai-search/google-faq-rich-results-deprecated-2026)) | Optional. Write visible FAQs for users and AI answers; markup is low priority |
| TouristTrip / Trip | Not a Google rich result (absent from the gallery) | **Yes, for semantics** (Bing, AI search, entity understanding). No rich result expected |
| Product + Offer | Product snippets exist, but need price or reviews/ratings; HVS has neither public price nor on-site reviews | **No.** Do not mark hunts up as Product to chase stars |
| Review / AggregateRating | Self-serving reviews of your own business are not eligible for stars | **No** |
| Article | Not a distinct rich result outside news, but supported | Yes on guides (author = organisation) |

### 5.2 Templates (all in `schema/`, all parsed with Python `json.loads`)

| File | Used on |
|---|---|
| `organization-travelagency.json` | Home only (other pages reference `{"@id":"https://huntventuresafaris.com/#organization"}`) |
| `website.json` | Home |
| `touristtrip-astore-markhor.json`, `-himalayan-ibex`, `-blue-sheep`, `-blanford-urial-sindh-ibex`, `-punjab-urial` | Each hunt page |
| `breadcrumblist-hunt.json` | Pattern for all breadcrumbs |
| `faqpage-guide.json` | Guides/hunt FAQ blocks (optional) |
| `article-guide.json` | Guides (dates are placeholders — set real publish/modify dates) |
| `webpage-es-hunt.json` | Spanish hunt pages |

Key decisions in the templates:

- **Licence 2087**: expressed as `identifier` (`PropertyValue`, `propertyID` "Pakistan government outfitter licence") plus `hasCredential`. Google lists its own preferred identifiers (`iso6523Code`, `vatID`, `taxID`, `duns`, `leiCode`); add the company's NTN/registration number as `taxID` only if the client supplies it (**TBC**).
- **foundingDate** "1989"; **address** exactly as the brochure; both phones (one as `reservations` contact point); `areaServed` = GB, Sindh, Balochistan, Punjab.
- **sameAs**: currently only the BookYourHunt profile. Add Facebook/Instagram/YouTube/LinkedIn URLs when the client confirms them (**TBC**). Do not add the Cinegética listing until a public URL exists.
- **Price "on request"**: **omit `offers` entirely.** schema.org `Offer.price` expects a number; `"price": "on request"` or `0` is invalid or misleading, and a `priceSpecification` without a value adds nothing. If the client later publishes a figure, add `offers` with `price`, `priceCurrency` and `validFrom`/`validThrough` for the season.
- **TouristTrip** carries `name`, `description` (incl. season, altitude, duration), `provider`, `tripOrigin`, `touristType`, `itinerary` (`ItemList` of days). Species (`Taxon`), language and location sit on the `subjectOf` `WebPage`, because `about`, `inLanguage` and `contentLocation` are CreativeWork properties, not Trip properties.
- Validate each built page with the [Rich Results Test](https://search.google.com/test/rich-results) (Organization, Breadcrumb) and the [Schema Markup Validator](https://validator.schema.org/) (TouristTrip).

Embed as:

```html
<script type="application/ld+json">{ …contents of the JSON file… }</script>
```

---

## 6. International / multilingual

- **Structure**: `/es/` subfolder on the same domain (inherits authority; one Vercel project; one Search Console property).
- **hreflang**: in `<head>` **and** in the sitemap (already in `sitemap.xml`). Each EN/ES pair lists `en`, `es` and `x-default` (→ EN), self-referencing on both sides. Pages without a twin carry no hreflang.

```html
<link rel="alternate" hreflang="en" href="https://huntventuresafaris.com/hunts/astore-markhor/">
<link rel="alternate" hreflang="es" href="https://huntventuresafaris.com/es/cazas/markhor-de-astore/">
<link rel="alternate" hreflang="x-default" href="https://huntventuresafaris.com/hunts/astore-markhor/">
```

- Use `es` (not `es-ES`) — the audience is Spain plus Latin America.
- `<html lang="es">` on Spanish pages; no automatic IP/Accept-Language redirects (they block Googlebot from seeing ES); a visible language switch that links to the twin page, not to `/es/`.
- **Phase 1 translation**: home, hunts hub, 5 hunt pages, enquiry, contact (+ thank-you). **Phase 2**: permits & CITES, conservation, about, seasons. Other languages (Russian, Arabic, German) are Phase 3 candidates once enquiry data shows demand — BookYourHunt already runs RU and DE versions of Pakistan listings ([RU example](https://www.bookyourhunt.com/ru/tour/44051), [DE example](https://www.bookyourhunt.com/de/tour/43931)), which suggests those audiences exist.

---

## 7. Technical SEO

### 7.1 robots.txt (Phase 1, staged at `docs/seo/robots.txt`)

```
User-agent: *
Allow: /
Disallow: /thank-you/
Disallow: /es/gracias/
Disallow: /drafts/

Sitemap: https://huntventuresafaris.com/sitemap.xml
```

Thank-you pages are also `noindex` by header. Note: a page blocked in robots.txt cannot have its `noindex` read; this is acceptable here because nothing links to the thank-you pages externally. Preview deployments: Vercel already adds `X-Robots-Tag: noindex` on `*.vercel.app` preview URLs by default — check with `curl -I` that the production domain does **not** send it.

### 7.2 sitemap.xml

Staged at `docs/seo/sitemap.xml`: 28 URLs (19 EN + 9 ES) with `xhtml:link` hreflang alternates. Add `<lastmod>` from each file's real git commit date at deploy time; omit `changefreq`/`priority` (Google ignores them). Excluded: thank-you, 404, privacy-ES (not built).

### 7.3 Canonicals and duplicates

- Self-referencing absolute canonical on every page, slash form, `https://huntventuresafaris.com` (no `www`). Redirect `www` → apex as a 308 in Vercel domain settings.
- Query parameters (`?species=`, UTM) never change the canonical.
- EN and ES twins each canonicalise to themselves (never cross-canonical).

### 7.4 Open Graph and Twitter cards

```html
<meta property="og:type" content="website">
<meta property="og:site_name" content="Hunt Venture Safaris">
<meta property="og:title" content="Astore markhor hunt, Gilgit-Baltistan">
<meta property="og:description" content="20 days, 15 hunting days, 2,500–4,700 m. Season 15 Oct–30 Apr.">
<meta property="og:url" content="https://huntventuresafaris.com/hunts/astore-markhor/">
<meta property="og:image" content="https://huntventuresafaris.com/assets/og/astore-markhor.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Snow-covered Karakoram ridges above the Astore valley at dusk">
<meta property="og:locale" content="en_GB">
<meta property="og:locale:alternate" content="es_ES">
<meta name="twitter:card" content="summary_large_image">
```

- 1200 × 630 JPEG, < 300 KB, landscape or live-animal/horn-on-white imagery only. Suggested sources from the inventory: photo-10 (Karakoram peak at dusk) default; photo-05/07/14 for blue sheep; photo-16 (group in snowy valley) for guides; photo-20 (horns on white) for markhor; photo-19 (Sindh ibex on ridge) for the combo — confirm photo-19 shows a live animal. **Never** photo-02 or photo-11.
- Keep the logo off OG images or place it on the cream plate (logo is dark-on-light only).

### 7.5 Performance budget

| Metric | Target (p75, mobile) |
|---|---|
| LCP | ≤ 2.0 s (Google "good" ≤ 2.5 s) |
| INP | ≤ 150 ms (good ≤ 200 ms) |
| CLS | ≤ 0.05 (good ≤ 0.1) |
| Page weight (hunt page, first load) | ≤ 900 KB; hero ≤ 200 KB |
| JS | ≤ 30 KB gzipped, no framework needed |

- Images: AVIF with WebP fallback via `<picture>`, JPEG only as last fallback; `srcset` widths 480/768/1200/1600/2400; explicit `width`/`height` on every `<img>`.
- Hero: `fetchpriority="high"`, no `loading="lazy"`, preload only that one image. Everything below the fold `loading="lazy" decoding="async"`.
- Fonts: self-host WOFF2 (Arimo, and Argent CF only if licensed for web), subset Latin + Latin Extended (Spanish), `font-display: swap`, preload one weight, fallback metrics matched (Arimo is Arial-metric, so CLS from swap is minimal).
- Map on contact page: static image linking to Google Maps; no iframe on first load.
- Long-lived cache headers on `/assets/` (in `vercel.json` above); fingerprint filenames when they change.

### 7.6 Redirects from the current site

The live site is one page with anchors `#species`, `#expedition`, `#conservation`, `#contact`, `#top`. URL fragments are never sent to the server, so they cannot be redirected in `vercel.json`. Plan:

1. Keep `/` as the homepage (no redirect needed for the root).
2. Add a tiny inline script on the new homepage that maps legacy fragments client-side:
   ```html
   <script>
   (function(){var m={"#species":"/hunts/","#expedition":"/hunting-in-pakistan/travel-and-logistics/","#conservation":"/conservation/","#contact":"/contact/"};
   var t=m[location.hash];if(t)location.replace(t);})();
   </script>
   ```
3. `/index.html` → `/` is handled by `cleanUrls`; the `vercel.json` redirects cover likely guessed paths.
4. Remove the old 4-species content entirely (it conflicts with the brochures).

### 7.7 404 page

`/404.html` at the root (Vercel serves it with a 404 status). Content: "This page has moved or doesn't exist", search-free links to the five hunts, guides, Plan your hunt, contact phone/WhatsApp; `noindex` meta; same header/footer. Spanish copy shown when the path starts with `/es/` (small inline script switches the text).

### 7.8 Search Console, Bing and analytics setup

1. Search Console: add a **Domain property** for `huntventuresafaris.com` via DNS TXT record at GoDaddy (covers http/https/www).
2. Submit `https://huntventuresafaris.com/sitemap.xml`; inspect the home and the five hunt URLs and request indexing.
3. Check the International Targeting/hreflang issues and Page indexing reports after two weeks.
4. Bing Webmaster Tools: import from Search Console; submit the sitemap; enable IndexNow (a simple POST on deploy, optional).
5. Analytics: Vercel Web Analytics (cookieless, free tier) for page views plus GA4 for events and country/language, or GA4 only — decide with the privacy policy. If GA4 is used with EU visitors, show a consent banner (Consent Mode v2).
6. Do not track email addresses or form content into analytics.

### 7.9 Google Business Profile (Gilgit office)

- Name: **Hunt Venture Safaris** (no keywords stuffed into the name).
- Category: primary "Hunting and fishing outfitter" if available in GBP's list, else "Tour operator"; secondary "Travel agency". (**Verify the exact category names in GBP at setup.**)
- Address, exactly as the brochure, everywhere (site footer, contact page, schema, GBP, directories):

  > Hotel Riveria, River View Road, Chinar Bagh, Gilgit, Gilgit-Baltistan, Pakistan – 15100

- Phones: +92 311 166 7829 (primary), +92 300 989 3205. Email: huntventuresafaris@gmail.com. Website: https://huntventuresafaris.com/
- On-site, use `tel:+923111667829` and `tel:+923009893205`; display as written above.
- Hours: **TBC (client to confirm)**. Photos: office exterior, team, landscapes; no carcass photos.
- Verification will be by post/video at the Gilgit address; allow time.
- **NAP conflict to fix**: the BookYourHunt profile lists durations and prices that differ from the 2027–28 brochures (e.g. an 8-day ibex hunt and a 10-day combo with dollar prices) ([BookYourHunt HVS profile](https://www.bookyourhunt.com/en/outfitters/hunt-venture-safaris)). Client should decide whether marketplace prices stay public and align durations, since "rates on request" on the site will look inconsistent next to public marketplace prices.

---

## 8. Content plan

### Phase 1 (launch)

The 19 EN and 9 ES pages in §4. The five guides under `/hunting-in-pakistan/` are the informational launch content.

### Next 10 articles (Phase 2, under `/hunting-in-pakistan/`)

| # | Slug | Target keyword | Angle (grounded in HVS facts) |
|---|---|---|---|
| 1 | `/how-the-permit-auction-works/` | markhor permit auction | How the open government auction allocates permits to Pakistani outfitters, and how HVS handles fee changes (minor absorbed, substantial invoiced). Cite dated permit counts per season. |
| 2 | `/best-time-to-hunt-markhor/` | best time to hunt markhor | Legal 15 Oct–30 Apr vs recommended mid Nov–mid Feb; why (TBC: rut/snow reasoning from client's guides). |
| 3 | `/blue-sheep-shimshal-trek/` | shimshal valley blue sheep trek | The two-day trek in, 3,200–4,500 m, seven hunting days; what the walk demands. |
| 4 | `/altitude-and-fitness/` | altitude hunting preparation | Hunts at 2,500–4,700 m; preparation and acclimatisation (medical claims reviewed, general advice only). |
| 5 | `/what-to-pack/` | what to pack for a mountain hunt pakistan | Built around the inclusions: tents, cutlery, camping and safety equipment provided; personal clothing/equipment not; 50 kg/2-duffle limit. |
| 6 | `/islamabad-to-gilgit/` | islamabad to gilgit flight | Included return flights; 4x4 road transport if flights are cancelled; how the itinerary absorbs it. |
| 7 | `/community-controlled-hunting-areas/` | community hunting areas gilgit-baltistan | What a community-controlled area is and how it affects your hunt; cite dated third-party figures on revenue shares. |
| 8 | `/markhor-vs-ibex-hunt/` | markhor or ibex hunt | Side-by-side: 20 vs 10–12 days, same altitude band, same season window; who each suits. |
| 9 | `/sindh-ibex-and-urial-combo/` | sindh ibex hunt pakistan | Why the Dureji combo is a low-altitude (500–3,000 ft) alternative or add-on; Karachi logistics. |
| 10 | `/non-hunting-companions/` | non-hunting companion hunting trip pakistan | Companion rate exists; pair with tours, treks and jeep safaris. |

Also Phase 2: Spanish versions of permits/CITES and conservation; `/about/references/` once consented testimonials exist.

---

## 9. Off-page and E-E-A-T

### Trust signals to publish

| Signal | Where | Status |
|---|---|---|
| Govt. licence No. 2087 | Footer, About, Contact, schema | Confirmed (brochure). Add a scan of the licence certificate if the client agrees (**TBC**) |
| Operating since 1989 | Home trust strip, About | Confirmed |
| Legal entity "(Pvt) Limited" + registration/NTN | Footer, schema `taxID` | Registration number **TBC** |
| Named team: owner/MD, lead guides, years of experience | About | **TBC**. The BookYourHunt profile names a managing director; confirm name and consent before publishing |
| References/testimonials | `/about/references/` | Process: written consent per client (name, country, year, species), quote unedited except trimming, no trophy measurements unless verified by the client's records, offer "contact a past client" by request |
| Cinegética + SCI exhibitor | About, home trust strip | Client has a stand booked for Cinegética (from project notes); next edition 11–14 March 2027, Madrid ([SCI](https://safariclub.org/cinegetica)). State "exhibiting at Cinegética 2027", not "SCI member", unless membership is confirmed |
| Other memberships (SCI, CIC, Pakistan Association of Tour Operators, etc.) | About | **Unverified — TBC** |

### Backlink and citation ideas

| Target | Type | Status |
|---|---|---|
| Cinegética / IFEMA exhibitor directory ([IFEMA Cinegética](https://www.ifema.es/cinegetica)) | Directory link | Check whether the exhibitor profile allows a website URL |
| SCI event / exhibitor pages ([SCI Cinegética](https://safariclub.org/cinegetica)) | Directory | Unverified whether exhibitors are listed |
| BookYourHunt outfitter profile | Existing citation | Live; add website link if allowed; align facts |
| Other marketplaces (Mallard Bay, Guidefitter, Hunt Info) | Listings | Optional; only if facts and pricing policy align |
| GB Forest, Wildlife & Environment Department ([fwegb.gov.pk](https://fwegb.gov.pk/?p=7210)) | Government news/registered outfitter list | Publishes hunt news; whether it lists licensed outfitters is **unverified** |
| Gilgit-Baltistan Tourism Department / Pakistan Tourism Development Corporation directories | Directories | **Unverified** |
| Pakistani press (Dawn, ProPakistani, Pamir Times) | Earned media | They report each season's first hunts with outfitter names; offer factual statements and photos (non-graphic) |
| Hunting forums (AccurateReloading Asian forum, Hunting-Washington) | Community | Participate as the outfitter with disclosure; no link-dropping |
| Hunting writers ([Craig Boddington's Pakistan page](https://www.craigboddington.com/country/pakistan), Sporting Classics) | Editorial | Pitch the 1989 heritage story |
| Booking agents/consultants (HVS's B2B outreach) | Partner links | Ask partners who sell HVS hunts to link to the species page |

---

## 10. Sensitive-topic considerations

- **Conservation claims**: use the brochure's own wording ("contributes to the conservation of these species and the development of local communities") as HVS's claim. Any number (population trends, revenue shares, permit counts) must cite a named, dated source — e.g. the ~80% community share reported for the 2025–26 auction ([Dawn](https://www.dawn.com/news/1939432)) — and be re-checked each season. No "saves the species", no invented success rates, trophy sizes or awards.
- **Balance**: the conservation page can acknowledge that trophy hunting is debated and explain the regulated model (quota, auction, community areas). Calm, factual, no attacks on critics.
- **Images**: heroes and OG images are landscapes, live animals, horns on white, people trekking. Trophy photos, where used, are respectful (no blood, no open wounds, no weapons pointing at camera); photo-02 and photo-11 are excluded.
- **Alt text**: describe neutrally ("Hunter and guide with an Astore markhor, Gilgit-Baltistan, winter"); never "kill", "bagged", gore descriptors.
- **Paid search**: Google Ads prohibits ads for firearms whether for sport or otherwise ([Google Ads dangerous products policy](https://support.google.com/adspolicy/answer/6014299?hl=en); [guns policy](https://support.google.com/adspolicy/answer/16489226)). The policy page I checked does not address guided hunting trips directly, and Google separately prohibits ads for products from endangered species. Treat Google Ads for trophy hunts as **high risk of disapproval**: test only with landing pages that sell the trip (no gun imagery, no "trophy" in ad copy, no animal-part language), expect manual review, and keep SEO as the primary channel. Meta has similar restrictions — check before spending.
- **Firearm content** on the site is limited to documentation logistics; no ammunition sales, no instructions.

---

## 11. Measurement

### KPIs

| KPI | Source | Target direction |
|---|---|---|
| Qualified enquiries per month, by species, country, language | Enquiry form event params + CRM | Primary business metric |
| Enquiry conversion rate per hunt page | GA4 | Rising |
| Organic sessions to `/hunts/*` and `/es/cazas/*` | GA4 / Search Console | Rising season-on-season |
| Impressions, clicks, avg. position for top terms (table below) | Search Console | Top 3 for species + "Pakistan" terms within 12 months |
| Brand SERP: official site ranks #1 for "hunt venture safaris" | Search Console / manual | Within 1 month of launch |
| Core Web Vitals pass rate | Search Console CWV report / Vercel Speed Insights | 100% "good" URLs |
| Spanish share of enquiries around Cinegética (Feb–Apr) | GA4 `language` param | Baseline in 2027 |

Tracked queries: astore markhor hunt · markhor hunting pakistan · himalayan ibex hunt pakistan · blue sheep hunt pakistan · blue sheep hunting shimshal · sindh ibex hunt · blanford urial hunt · pakistan hunting outfitter · trophy hunting pakistan · caza markhor pakistán · caza íbice pakistán.

### Events (GA4 names)

| Event | Trigger | Parameters |
|---|---|---|
| `generate_lead` | Successful enquiry submit (fire on `/thank-you/` load or form success) | `species`, `season`, `hunters`, `companions`, `country`, `page_language` |
| `form_start` | First field interaction on enquiry form | `species`, `page_language` |
| `whatsapp_click` | Click on `wa.me/` link | `link_location` (header/footer/hunt-page), `species` (if on hunt page) |
| `phone_click` | Click on `tel:` link | `link_location`, `number` (last 4 digits only) |
| `email_click` | Click on `mailto:` link | `link_location` |
| `brochure_download` (Phase 2) | PDF download | `species`, `language` |
| `language_switch` | Click EN/ES switch | `from`, `to` |

Mark `generate_lead`, `whatsapp_click`, `phone_click` and `email_click` as key events. Add `?utm_source=cinegetica&utm_medium=print&utm_campaign=2027` to QR codes on stand materials.

---

## Open items for the client (TBC)

1. Punjab urial: legal period, altitude, start city, itinerary.
2. Company registration/NTN; licence certificate scan; office hours.
3. Team names, roles and consent; any association memberships.
4. Social profile URLs for `sameAs`.
5. Trophy export process (agent, timelines) and firearm document checklist.
6. Pricing policy across marketplaces vs "on request" on the site; align BookYourHunt durations with the 2027–28 brochures.
7. Season dates: the GB 2026–27 season was reported as 15 Oct 2026–10 Apr 2027 ([Dawn](https://www.dawn.com/news/2028988)), while the brochure gives later end dates for 2027–28 (e.g. ibex to 26 Apr, blue sheep to 30 Apr). Confirm against the official 2027–28 notification before launch.
8. Spanish species names used in Cinegética materials.
