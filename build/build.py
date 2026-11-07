"""Generate huntventuresafaris.com into ./site. Run: python3 build/build.py"""
import os, re, shutil, json, types, importlib, datetime, glob
import markdown
from data import SITE, COMPANY, HUNTS, INCLUDED, NOT_INCLUDED, PERMIT_NOTE, GUIDES
import components as C
from components import E, icon, picture, page, section, heading, cta_band, breadcrumb, breadcrumb_ld, wa_link

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
TODAY = datetime.date.today().isoformat()
PAGES = []  # (path, lang, alternates, noindex)


def write(path, html_text, lang="en", alternates=None, noindex=False):
    fp = os.path.join(OUT, path.strip("/"), "index.html") if not path.endswith(".html") else os.path.join(OUT, path.strip("/"))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w").write(html_text)
    PAGES.append((path, lang, alternates or {}, noindex))


# ---------------------------------------------------------------- languages

def load_lang(code):
    L = importlib.import_module(f"i18n_{code}")
    L = types.SimpleNamespace(**{k: getattr(L, k) for k in dir(L) if not k.startswith("_")})
    hunts = []
    for h in HUNTS:
        x = dict(h)
        if code == "es":
            tr = L.HUNTS_ES[h["slug"]]
            x.update({k: v for k, v in tr.items() if k not in ("title", "description", "h1")})
            x["seo"] = {k: tr[k] for k in ("title", "description", "h1")}
            x["itinerary"] = [tuple(i) for i in tr["itinerary"]]
            x["faq"] = [tuple(i) for i in tr["faq"]]
            x["gallery"] = [tuple(g) for g in tr["gallery"]]
            x["path_slug"] = h["es_slug"]
            x["extras_l"] = None if h["extras"] is None else L.EXTRAS["south" if h["group"] == "south" else "north"]
        else:
            x["path_slug"] = h["slug"]
            x["extras_l"] = h["extras"]
        hunts.append(x)
    L.HUNTS = hunts
    L.BY = {h["slug"]: h for h in hunts}
    if code == "en":
        L.INCLUDED, L.NOT_INCLUDED, L.PERMIT_NOTE = INCLUDED, NOT_INCLUDED, PERMIT_NOTE
    return L


EN = load_lang("en")
HAS_ES = os.path.exists(os.path.join(ROOT, "build", "i18n_es.py"))
ES = load_lang("es") if HAS_ES else None
LANGS = [EN] + ([ES] if ES else [])


def twin(key, slug=None):
    """hreflang alternates for a page key present in both languages."""
    if not ES:
        return None
    out = {}
    for L in LANGS:
        p = L.PATHS[key]
        if slug:
            p = p.format(slug=L.BY[slug]["path_slug"])
        out[L.LANG] = p
    return out


def alt_of(L, alts):
    other = "es" if L.LANG == "en" else "en"
    return (alts or {}).get(other)


HUNT_SEO_EN = {
    "astore-markhor": ("Astore Markhor Hunt, Gilgit-Baltistan | HVS", "20-day Astore markhor hunt with 15 hunting days at 2,500–4,700 m. Season 15 Oct–30 Apr, best mid Nov–mid Feb. Itinerary, inclusions, rates on request.", "Astore markhor hunt"),
    "himalayan-ibex": ("Himalayan Ibex Hunt in Upper Hunza, Pakistan | HVS", "10–12 day Himalayan ibex hunt in Upper Hunza at 2,500–4,700 m. Season 1 Nov–26 Apr, best mid Nov–mid Feb. Full itinerary and inclusions.", "Himalayan ibex hunt"),
    "blue-sheep": ("Blue Sheep Hunt in Shimshal Valley, Pakistan | HVS", "15–16 day blue sheep hunt in Shimshal, Hunza, at 3,200–4,500 m with a two-day trek in. Season 1 Nov–30 Apr, best Nov, Mar and Apr.", "Blue sheep hunt in Shimshal Valley"),
    "blanford-urial-sindh-ibex": ("Blanford Urial & Sindh Ibex Combo Hunt, Dureji | HVS", "9-day combination hunt in Dureji, Sindh–Balochistan: 3 days for Blanford urial, 2 for Sindh ibex. Karachi to Karachi, best Dec–Jan.", "Blanford urial and Sindh ibex combination hunt"),
    "punjab-urial": ("Punjab Urial Hunt: Kala Bagh, Jhelum, Padri | HVS", "Punjab urial hunt of up to five hunting days in Kala Bagh, Jhelum and Padri. Best December to March. Itinerary and rates on request.", "Punjab urial hunt"),
}
for h in EN.HUNTS:
    t, d, h1 = HUNT_SEO_EN[h["slug"]]
    h["seo"] = {"title": t, "description": d, "h1": h1}


# ---------------------------------------------------------------- pages shared by both languages

def page_home(L):
    P = L.HOME
    hp = lambda h: L.PATHS["hunt"].format(slug=h["path_slug"])
    cards = "".join(C.hunt_card(L, h) for h in L.HUNTS)
    north = [h for h in L.HUNTS if h.get("alt")]
    cols = "".join(
        f'<div class="hvs-elev-col">{C.elevation_svg(h["name"], *h["alt"], L.UI["alt_aria"].format(name=h["name"], lo=C.fmt_m(L, h["alt"][0]), hi=C.fmt_m(L, h["alt"][1])))}<a href="{hp(h)}"><span>{E(h["name"])}</span></a></div>'
        for h in north)
    south = [h for h in L.HUNTS if not h.get("alt")]
    south_txt = " · ".join(f'<a href="{hp(h)}">{E(h["name"])}</a>' + (f' — {E(h["alt_text"])}' if h.get("alt_text") else "") for h in south)
    why = "".join(f'<div class="why-item"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in P["why_points"])
    plan_links = "".join(f'<li><a class="guide-link" href="{u}"><span>{E(t)}</span>{icon("arrow")}</a></li>' for t, u in P["planning_links"])
    body = f'''
<section class="hero" aria-labelledby="hero-h">
  {picture("hero-karakoram", P["hero_alt"], "100vw", eager=True, cls="hero-media")}
  <div class="hero-scrim"></div>
  <div class="wrap hero-inner">
    <span class="hvs-eyebrow">{E(P["eyebrow"])}</span>
    <h1 id="hero-h" class="display">{E(P["h1"])}</h1>
    <p class="lede">{E(P["lede"])}</p>
    <div class="hero-actions"><a class="hvs-btn hvs-btn-primary hvs-btn-lg" href="{L.PATHS["plan"]}">{E(P["cta_primary"])}</a><a class="hvs-btn hvs-btn-secondary hvs-btn-lg on-photo" href="{L.PATHS["hunts"]}">{E(P["cta_secondary"])}</a></div>
  </div>
</section>
{C.trust(L)}
{section(heading(P["hunts_eyebrow"], P["hunts_h2"], P["hunts_lede"], hid="hunts-h") + f'<div class="card-grid card-grid-5">{cards}</div>', label="hunts-h")}
{section(f'<div class="split">{heading(P["alt_eyebrow"], P["alt_h2"], P["alt_lede"], hid="alt-h")}<div><div class="hvs-elev-compare">{cols}</div><p class="south-note">{south_txt}</p></div></div>', cls="band-deep", label="alt-h")}
{section(heading(P["why_eyebrow"], P["why_h2"], hid="why-h") + f'<div class="why-grid">{why}</div>', label="why-h")}
{section(f'<div class="split split-photo"><div>{heading(P["planning_eyebrow"], P["planning_h2"], P["planning_lede"], hid="plan-h")}<ul class="guide-list">{plan_links}</ul></div>{picture("hunters-climbing", "Hunters and a guide climbing a steep rock face", "(max-width: 860px) 100vw, 50vw", cls="split-media")}</div>', cls="band-deep", label="plan-h")}
{section(f'<div class="beyond">{heading(P["beyond_eyebrow"], P["beyond_h2"], P["beyond_text"], hid="beyond-h")}<a class="hvs-btn hvs-btn-secondary" href="/tours-and-expeditions/">{E(P["beyond_cta"])}</a></div>', label="beyond-h")}
{cta_band(L, P["cta_h2"], P["cta_text"])}'''
    alts = twin("home")
    ld = [C.org_ld(), {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Hunt Venture Safaris", "publisher": {"@id": C.ORG_ID}, "inLanguage": [x.HTML_LANG for x in LANGS]}]
    write(L.PATHS["home"], page(L, path=L.PATHS["home"], title=P["title"], description=P["description"], body=body,
                                current="home", alt_path=alt_of(L, alts), alternates=alts, ld=ld), L.LANG, alts)


def page_hunts(L):
    P = L.HUNTS_INDEX
    U = L.UI
    hp = lambda h: L.PATHS["hunt"].format(slug=h["path_slug"])
    north = "".join(C.hunt_card(L, h) for h in L.HUNTS if h["group"] == "north")
    south = "".join(C.hunt_card(L, h) for h in L.HUNTS if h["group"] == "south")
    months = L.PLAN["months"]
    month_nums = [11, 12, 1, 2, 3, 4]
    opts = f'<option value="">{E(P["filter_all"])}</option>' + "".join(f'<option value="{n}">{E(m)}</option>' for n, m in zip(month_nums, months))
    filt = f'<div class="filter"><label class="hvs-label" for="month-filter">{E(P["filter_label"])}</label><select class="hvs-select" id="month-filter">{opts}</select><p class="filter-status hvs-help" aria-live="polite"></p></div>'
    rows = "".join(
        f'<tr><th scope="row"><a href="{hp(h)}">{E(h["name"])}</a></th><td>{E(h.get("legal") or U["on_request"])}</td><td>{E(h["best"])}</td><td>{E(h.get("alt_text") or U["on_request"])}</td><td>{E(h["duration"])}</td><td>{E(h.get("route") or U["on_request"])}</td></tr>'
        for h in L.HUNTS)
    table = f'''<div class="table-wrap"><table class="compare"><caption class="hvs-sr">{E(P["compare_caption"])}</caption>
<thead><tr><th scope="col">{E(P["col_hunt"])}</th><th scope="col">{E(U["spec_legal"])}</th><th scope="col">{E(U["spec_best"])}</th><th scope="col">{E(U["spec_alt"])}</th><th scope="col">{E(U["spec_duration"])}</th><th scope="col">{E(U["spec_route"])}</th></tr></thead><tbody>{rows}</tbody></table></div>'''
    crumbs = [(U["home_crumb"], L.PATHS["home"]), (P["h1"], None)]
    body = f'''
<div class="wrap page-head">{breadcrumb(L, crumbs)}{heading(None, P["h1"], P["lede"], level=1)}{filt}</div>
{section(heading(None, P["north_h2"], P["north_text"], hid="north-h") + f'<div class="card-grid">{north}</div>', label="north-h")}
{section(heading(None, P["south_h2"], P["south_text"], hid="south-h") + f'<div class="card-grid card-grid-2">{south}</div>', label="south-h")}
{section(heading(None, P["compare_h2"], hid="cmp-h") + table, cls="band-deep", label="cmp-h")}
{section(f'<div class="narrow">{heading(None, P["permits_h2"], hid="perm-h")}<p>{E(P["permits_text"])}</p><p><a class="hvs-btn hvs-btn-tertiary" href="/hunting-in-pakistan/permits-and-cites/">{E(P["permits_link"])} {icon("arrow")}</a></p></div>', label="perm-h")}
{cta_band(L, L.HOME["cta_h2"], L.HOME["cta_text"])}'''
    alts = twin("hunts")
    ld = [breadcrumb_ld(crumbs), {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": SITE + hp(h), "name": h["name"]} for i, h in enumerate(L.HUNTS)]}]
    write(L.PATHS["hunts"], page(L, path=L.PATHS["hunts"], title=P["title"], description=P["description"], body=body,
                                 current="hunts", alt_path=alt_of(L, alts), alternates=alts, ld=ld), L.LANG, alts)


def page_hunt(L, h):
    U = L.UI
    path = L.PATHS["hunt"].format(slug=h["path_slug"])
    enquire = f'{L.PATHS["plan"]}?hunt={h["slug"]}'
    crumbs = [(U["home_crumb"], L.PATHS["home"]), (L.HUNTS_INDEX["h1"], L.PATHS["hunts"]), (h["name"], None)]
    sci = f'<p class="hero-sci">{E(h["sci"])}</p>' if h.get("sci") else ""
    secs = []
    secs.append(section(heading(None, U["h_glance"], hid="glance-h") + C.glance(L, h), label="glance-h"))
    if h["itinerary"]:
        it_h = U["h_itinerary"].format(n=h["days"]) if h.get("days") else U["h_itinerary_plain"]
        secs.append(section(f'<div class="split split-top">{heading(None, it_h, hid="itin-h")}{C.timeline(L, h)}</div>', cls="band-deep", label="itin-h"))
    if h.get("alt"):
        secs.append(section(heading(None, U["h_terrain"], hid="terr-h") + C.elevation(L, h), label="terr-h"))
    elif h.get("terrain"):
        secs.append(section(f'<div class="narrow">{heading(None, U["h_terrain"], hid="terr-h")}<p class="big">{E(h["alt_text"])}</p><p>{E(h["terrain"])}</p></div>', label="terr-h"))
    if h.get("extras_l"):
        secs.append(section(heading(None, U["h_included"], hid="inc-h") + C.inclusions(L, h, L.INCLUDED, L.NOT_INCLUDED, h["extras_l"]), cls="band-deep", label="inc-h"))
        secs.append(section(heading(None, U["h_rates"], hid="rate-h") + C.rates(L, h, L.PERMIT_NOTE, enquire), label="rate-h"))
    else:
        secs.append(section(f'<div class="narrow">{heading(None, U["h_rates"], hid="rate-h")}<p>{E(U["punjab_note"])}</p><p><a class="hvs-btn hvs-btn-primary" href="{enquire}">{E(U["enquire_hunt"])}</a></p></div>', cls="band-deep", label="rate-h"))
    getting = U["getting_north"] if h["group"] == "north" else (U["getting_south"] if h.get("route") else U["getting_punjab"])
    gal = ""
    if h["gallery"]:
        figs = "".join(f'<figure>{picture(n, a, "(max-width: 760px) 100vw, 33vw")}<figcaption>{E(a)}</figcaption></figure>' for n, a in h["gallery"])
        gal = f'<div class="gallery">{figs}</div>'
    secs.append(section(f'''<div class="two-col">
  <div>{heading(None, U["h_getting_there"], hid="get-h")}<p>{E(getting)}</p></div>
  <div><h2 class="h2">{E(U["h_community"])}</h2><p>{E(U["community_text"])}</p><p><a class="hvs-btn hvs-btn-tertiary" href="/conservation/">{E(U["community_link"])} {icon("arrow")}</a></p></div>
</div>''' + (f'<h2 class="h2 gallery-h">{E(U["h_gallery"])}</h2>{gal}' if gal else ""), label="get-h"))
    secs.append(section(f'<div class="narrow">{heading(None, U["h_faq"], hid="faq-h")}{C.faq(h["faq"])}</div>', cls="band-deep", label="faq-h"))
    rel = "".join(C.hunt_card(L, L.BY[s]) for s in h["related"])
    secs.append(section(heading(None, U["h_related"], hid="rel-h") + f'<div class="card-grid card-grid-2">{rel}</div>', label="rel-h"))
    hero = f'''<section class="hero hero-hunt" aria-labelledby="hunt-h">
  {picture(h["img"], h["img_alt"], "100vw", eager=True, cls="hero-media")}
  <div class="hero-scrim"></div>
  <div class="wrap hero-inner">
    {breadcrumb(L, crumbs)}
    <span class="hvs-eyebrow">{E(h["region"])} · {E(L.UI["spec_best_short"])}: {E(h["best"])}</span>
    <h1 id="hunt-h" class="display">{E(h["seo"]["h1"])}</h1>{sci}
    <p class="lede">{E(h["summary"])}</p>
    <div class="hero-actions"><a class="hvs-btn hvs-btn-primary hvs-btn-lg" href="{enquire}">{E(U["enquire_hunt"])}</a><a class="hvs-btn hvs-btn-secondary hvs-btn-lg on-photo" href="{wa_link()}" rel="noopener">{icon("chat")} {E(U["whatsapp"])}</a></div>
  </div>
</section>'''
    body = hero + "".join(secs) + cta_band(L, U["hunt_cta_title"].format(name=h["name"]), U["hunt_cta_text"], href=enquire, label=U["enquire_hunt"])
    sticky = f'<div class="sticky-bar"><a class="hvs-btn hvs-btn-primary" href="{enquire}">{E(U["sticky_enquire"])}</a><a class="hvs-btn hvs-btn-secondary" href="{wa_link()}" rel="noopener">{icon("chat")} WhatsApp</a></div>'
    alts = twin("hunt", h["slug"])
    trip = {"@context": "https://schema.org", "@type": "TouristTrip", "@id": SITE + EN.PATHS["hunt"].format(slug=h["slug"]) + "#trip",
            "name": h["name"] if L.LANG == "en" else h["seo"]["h1"], "description": h["summary"], "inLanguage": L.HTML_LANG,
            "touristType": "Trophy hunters", "provider": {"@id": C.ORG_ID},
            "image": f'{SITE}/assets/img/{h["img"]}-{C.IMAGES[h["img"]]["sizes"][-1]}.jpg',
            "contentLocation": {"@type": "Place", "name": h["area"], "address": {"@type": "PostalAddress", "addressRegion": h["region"], "addressCountry": "PK"}}}
    if h["itinerary"]:
        trip["itinerary"] = {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": f"{d}: {t}"} for i, (d, t, _) in enumerate(h["itinerary"])]}
    write(path, page(L, path=path, title=h["seo"]["title"], description=h["seo"]["description"], body=body, current="hunts",
                     alt_path=alt_of(L, alts), alternates=alts, ld=[trip, breadcrumb_ld(crumbs)], sticky=sticky,
                     og_image=f'/assets/img/{h["img"]}-{C.IMAGES[h["img"]]["sizes"][-1]}.jpg'), L.LANG, alts)


def page_plan(L):
    P = L.PLAN
    U = L.UI
    chips = "".join(
        f'<label class="hvs-chip"><input type="checkbox" name="hunt" value="{h["slug"]}" data-label="{E(h["name"])}"><span>{E(h["name"])}</span></label>' for h in L.HUNTS)
    chips += f'<label class="hvs-chip"><input type="checkbox" name="hunt" value="not-sure" data-label="{E(P["f_not_sure"])}"><span>{E(P["f_not_sure"])}</span></label>'
    months = f'<option value="">{E(P["f_month_any"])}</option>' + "".join(f'<option>{E(m)}</option>' for m in P["months"])
    req = f'<span class="hvs-req" aria-hidden="true"> *</span>'
    steps = "".join(f'<li><b>{E(a)}</b><span>{E(b)}</span></li>' for a, b in P["next_steps"])
    labels = {k: P[k] for k in P if k.startswith("msg_") or k in ("send_failed", "sending", "copied", "err_name", "err_contact", "err_email", "err_consent", "err_summary")}
    form = f'''<form class="enquiry" id="enquiry" novalidate data-endpoint="" data-thanks="{L.PATHS["thanks"]}" data-lang="{L.LANG}">
  <div class="form-error hvs-note" id="form-error" hidden tabindex="-1">{icon("info")}<div><strong>{E(P["err_summary"])}</strong></div></div>
  <div class="hvs-form">
    <fieldset class="hvs-field hvs-field-full hvs-chips" id="f-hunt"><legend class="hvs-label">{E(P["f_hunt"])}</legend><span class="hvs-help">{E(P["f_hunt_help"])}</span><div class="chip-row">{chips}</div></fieldset>
    <div class="hvs-field"><label class="hvs-label" for="month">{E(P["f_month"])}</label><select class="hvs-select" id="month" name="month">{months}</select></div>
    <div class="hvs-field two-num">
      <div><label class="hvs-label" for="hunters">{E(P["f_hunters"])}</label><input class="hvs-input" id="hunters" name="hunters" type="number" min="1" max="10" value="1" inputmode="numeric"></div>
      <div><label class="hvs-label" for="companions">{E(P["f_companions"])}</label><input class="hvs-input" id="companions" name="companions" type="number" min="0" max="10" value="0" inputmode="numeric"></div>
    </div>
    <div class="hvs-field" id="fld-name"><label class="hvs-label" for="name">{E(P["f_name"])}{req}</label><input class="hvs-input" id="name" name="name" autocomplete="name" required aria-describedby="err-name"><span class="hvs-error" id="err-name" hidden></span></div>
    <div class="hvs-field"><label class="hvs-label" for="country">{E(P["f_country"])}</label><input class="hvs-input" id="country" name="country" autocomplete="country-name"></div>
    <div class="hvs-field" id="fld-email"><label class="hvs-label" for="email">{E(P["f_email"])}</label><input class="hvs-input" id="email" name="email" type="email" autocomplete="email" aria-describedby="err-email"><span class="hvs-error" id="err-email" hidden></span></div>
    <div class="hvs-field"><label class="hvs-label" for="phone">{E(P["f_phone"])}</label><input class="hvs-input" id="phone" name="phone" type="tel" autocomplete="tel" aria-describedby="phone-help"><span class="hvs-help" id="phone-help">{E(P["f_phone_help"])}</span></div>
    <div class="hvs-field hvs-field-full"><label class="hvs-label" for="message">{E(P["f_message"])}</label><textarea class="hvs-textarea" id="message" name="message" placeholder="{E(P["f_message_ph"])}"></textarea></div>
    <div class="hvs-field hvs-field-full" id="fld-consent"><label class="consent"><input type="checkbox" id="consent" name="consent" required aria-describedby="err-consent"> <span>{E(P["f_consent"])} <a href="/privacy/">{E(P["f_privacy"])}</a></span></label><span class="hvs-error" id="err-consent" hidden></span></div>
    <input type="hidden" name="source" id="source" value="website">
    <div class="hvs-field-full"><button class="hvs-btn hvs-btn-primary hvs-btn-lg" type="submit">{E(P["f_submit"])}</button></div>
  </div>
  <div class="send-panel" id="send-panel" hidden tabindex="-1">
    <div class="hvs-success">{icon("check")}<div><strong>{E(P["send_h"])}</strong><p>{E(P["send_text"])}</p></div></div>
    <pre class="send-preview" id="send-preview"></pre>
    <div class="send-actions"><a class="hvs-btn hvs-btn-primary hvs-btn-lg" id="send-wa" href="#" rel="noopener">{icon("chat")} {E(P["send_whatsapp"])}</a><a class="hvs-btn hvs-btn-secondary hvs-btn-lg" id="send-mail" href="#">{icon("mail")} {E(P["send_email"])}</a><button class="hvs-btn hvs-btn-tertiary" type="button" id="send-copy">{icon("copy")} {E(P["send_copy"])}</button></div>
  </div>
  <script type="application/json" id="form-i18n">{json.dumps(labels, ensure_ascii=False)}</script>
</form>'''
    crumbs = [(U["home_crumb"], L.PATHS["home"]), (P["h1"], None)]
    body = f'''<div class="wrap page-head">{breadcrumb(L, crumbs)}{heading(None, P["h1"], P["lede"], level=1)}<p class="reply-badge">{icon("chat")} {E(P["reply"])}</p></div>
<section class="band band-tight"><div class="wrap plan-grid">
  <div class="plan-form">{form}</div>
  <aside class="plan-aside">
    <div class="next-steps"><h2 class="h3">{E(P["next_h"])}</h2><ol>{steps}</ol></div>
    {C.contact_card(L, P["talk_h"])}
  </aside>
</div></section>'''
    alts = twin("plan")
    write(L.PATHS["plan"], page(L, path=L.PATHS["plan"], title=P["title"], description=P["description"], body=body, current="plan",
                                alt_path=alt_of(L, alts), alternates=alts, ld=[breadcrumb_ld(crumbs)]), L.LANG, alts)


def page_thanks(L):
    P = L.THANKS
    body = f'''<div class="wrap page-head page-head-center">{heading(None, P["h1"], P["lede"], level=1, center=True)}
<p class="center-actions"><a class="hvs-btn hvs-btn-primary hvs-btn-lg" href="{wa_link()}" rel="noopener">{icon("chat")} {E(L.UI["whatsapp"])}</a><a class="hvs-btn hvs-btn-secondary hvs-btn-lg" href="{L.PATHS["hunts"]}">{E(L.HOME["cta_secondary"])}</a></p></div>'''
    alts = twin("thanks")
    write(L.PATHS["thanks"], page(L, path=L.PATHS["thanks"], title=P["title"], description=P["description"], body=body,
                                  alt_path=alt_of(L, alts), noindex=True), L.LANG, None, True)


def page_contact(L):
    P = L.CONTACT
    U = L.UI
    crumbs = [(U["home_crumb"], L.PATHS["home"]), (P["h1"], None)]
    maps = "https://www.google.com/maps/search/?api=1&query=" + "Hotel%20Riveria%20Chinar%20Bagh%20Gilgit"
    body = f'''<div class="wrap page-head">{breadcrumb(L, crumbs)}{heading(None, P["h1"], P["lede"], level=1)}</div>
<section class="band band-tight"><div class="wrap two-col">
  {C.contact_card(L)}
  <div class="stack">
    <div><h2 class="h3">{E(P["office_h"])}</h2><p>{E(P["office_text"])}</p><p><a class="hvs-btn hvs-btn-secondary" href="{maps}" rel="noopener">{icon("pin")} {E(P["map"])}</a></p></div>
    <div><h2 class="h3">{E(P["company_h"])}</h2><p>{"<br>".join(E(x) for x in P["company_lines"])}</p></div>
    <div><h2 class="h3">{E(P["enquire_h"])}</h2><p>{E(P["enquire_text"])}</p><p><a class="hvs-btn hvs-btn-primary" href="{L.PATHS["plan"]}">{E(U["nav_cta"])}</a></p></div>
  </div>
</div></section>'''
    alts = twin("contact")
    ld = [breadcrumb_ld(crumbs), {"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + L.PATHS["contact"], "about": {"@id": C.ORG_ID}}]
    write(L.PATHS["contact"], page(L, path=L.PATHS["contact"], title=P["title"], description=P["description"], body=body,
                                   current="contact", alt_path=alt_of(L, alts), alternates=alts, ld=ld), L.LANG, alts)


def page_cinegetica(L):
    P = L.CINEGETICA
    cards = "".join(C.hunt_card(L, h) for h in L.HUNTS)
    body = f'''<div class="wrap page-head">{heading(P["eyebrow"], P["h1"], P["lede"], level=1)}
<p><a class="hvs-btn hvs-btn-primary hvs-btn-lg" href="{L.PATHS["plan"]}?source=cinegetica">{E(P["cta"])}</a> <a class="hvs-btn hvs-btn-secondary hvs-btn-lg" href="{wa_link()}" rel="noopener">{icon("chat")} WhatsApp</a></p></div>
{section(f'<div class="card-grid card-grid-5">{cards}</div>')}
{C.trust(L)}'''
    alts = twin("cinegetica")
    write(L.PATHS["cinegetica"], page(L, path=L.PATHS["cinegetica"], title=P["title"], description=P["description"], body=body,
                                      alt_path=alt_of(L, alts), alternates=alts, noindex=True), L.LANG, alts, True)


# ---------------------------------------------------------------- English-only pages

def prose_page(path, title, description, h1, lede, html_body, crumbs_label, current=None, eyebrow=None, ld_type=None, image=None):
    U = EN.UI
    crumbs = [(U["home_crumb"], "/"), (crumbs_label, None)]
    media = ""
    if image:
        media = f'<div class="wrap page-media">{picture(image[0], image[1], "(max-width: 1200px) 100vw, 1200px")}</div>'
    body = f'''<div class="wrap page-head">{breadcrumb(EN, crumbs)}{heading(eyebrow, h1, lede, level=1)}</div>{media}
<section class="band band-tight"><div class="wrap"><div class="prose">{html_body}</div></div></section>
{cta_band(EN, EN.HOME["cta_h2"], EN.HOME["cta_text"])}'''
    ld = [breadcrumb_ld(crumbs)]
    if ld_type:
        ld.append({"@context": "https://schema.org", "@type": ld_type, "url": SITE + path, "name": h1, "about": {"@id": C.ORG_ID}})
    write(path, page(EN, path=path, title=title, description=description, body=body, current=current, ld=ld), "en")


def md(text):
    return markdown.markdown(text, extensions=["tables", "sane_lists"])


def pages_en_only():
    prose_page("/about/", "About Hunt Venture Safaris: Gilgit Since 1989",
               "Hunt Venture Safaris (Pvt) Limited: government licence No. 2087, Gilgit-based since 1989, guiding hunts across the Karakoram, Himalaya and Hindu Kush.",
               "About Hunt Venture Safaris", "A Gilgit outfitter, licensed by the government and guiding hunters from around the world since 1989.",
               md(ABOUT_MD), "About", current="about", ld_type="AboutPage", image=("markhor-heritage", "An Astore markhor hunt from the early years of Hunt Venture Safaris"))
    prose_page("/conservation/", "Conservation and Community Hunting Areas | HVS",
               "How regulated trophy hunting works in community-controlled areas of Gilgit-Baltistan, and how hunts contribute to wildlife and local communities.",
               "Conservation and community hunting areas", "Trophy hunting in Gilgit-Baltistan is regulated, limited and run with the communities who live alongside the wildlife.",
               md(CONSERVATION_MD), "Conservation", current="conservation", ld_type="Article", image=("ibex-group", "Hunters and local guides beneath the peaks of Hunza"))
    prose_page("/agents/", "For Booking Agents and Hunting Consultants | HVS",
               "Work with Hunt Venture Safaris, a licensed outfitter in Gilgit since 1989: hunt sheets for 2027–28, quick replies and full in-country logistics.",
               "For booking agents and hunting consultants", "Sell hunts in Pakistan with an outfitter that handles permits, paperwork and the mountain.",
               md(AGENTS_MD), "Booking agents")
    prose_page("/tours-and-expeditions/", "Tours, Treks, Jeep Safaris & Expeditions, Gilgit | HVS",
               "Beyond hunting: tours and trekking, jeep safaris and mountaineering expeditions in the Karakoram, Himalaya and Hindu Kush. Ask for details.",
               "Tours, treks and expeditions", "Outside the hunting season, and for companions who do not hunt, we organise travel across the mountains of northern Pakistan.",
               md(TOURS_MD), "Tours and expeditions", image=("hero-karakoram", "Snow-covered Karakoram peaks at dusk"))
    prose_page("/privacy/", "Privacy Policy | Hunt Venture Safaris",
               "How Hunt Venture Safaris collects and uses the details you send through our enquiry form, email and WhatsApp.",
               "Privacy policy", f"Last updated {datetime.date.today().strftime('%-d %B %Y')}.", md(PRIVACY_MD), "Privacy")


ABOUT_MD = """
## A legacy since 1989

Hunt Venture Safaris (Pvt) Limited was founded in Gilgit in 1989 and is one of the first trophy hunting companies in Gilgit-Baltistan. Since then we have welcomed hunters from around the world to the mountains of northern Pakistan, and to the hills of the south.

Our work is built on respect for the mountains and the animals that live in them, on sustainable hunting, and on a long relationship with the communities who manage the hunting areas.

## Govt. Licence No. 2087

We operate under government licence No. 2087. As a licensed Pakistani outfitter we take part in the government's open auction for trophy permits, and we handle the permit, the provincial shooting licence, the firearm documents and the liaison with the authorities for every hunter we guide.

## Where we hunt

- **Gilgit-Baltistan:** Astore markhor in Nagar, Skardu, Astore, Gilgit, Bunji and Kargah; Himalayan ibex in Upper Hunza; blue sheep in the Shimshal Valley.
- **Sindh–Balochistan:** Blanford urial and Sindh ibex in Dureji.
- **Punjab:** Punjab urial in Kala Bagh, Jhelum and Padri.

See [all hunts for season 2027–28](/hunts/).

## How we work

Every hunt is led by a licensed guide and professional hunter, supported by shikar guides, cooks and staff from the area. We plan conservatively around weather and altitude, we keep our own 4x4 transport in case flights to Gilgit are cancelled, and we look after the trophy from field care to packing.

Beyond hunting, we organise [tours, treks, jeep safaris and mountaineering expeditions](/tours-and-expeditions/) across the Karakoram, Himalaya and Hindu Kush.

## Visit us in Gilgit

Our office is at Hotel Riveria, River View Road, Chinar Bagh, Gilgit, Gilgit-Baltistan, Pakistan – 15100. Call +92 311 166 7829 (also WhatsApp) or +92 300 989 3205, or email huntventuresafaris@gmail.com. [All contact details](/contact/).
"""

CONSERVATION_MD = """
## Community-controlled hunting areas

Our hunts in Gilgit-Baltistan take place in community-controlled hunting areas. The communities who live alongside the markhor, ibex and blue sheep protect them, through village game watchers and limits on grazing and poaching, and they share in the income that regulated hunting brings.

## How permits are allocated

The number of trophy permits is set by the wildlife authorities each season. Permits are then allocated to licensed Pakistani outfitters through an open government auction. Our rates are based on the permit fees for the season; you can read more in our guide to [permits and CITES](/hunting-in-pakistan/permits-and-cites/).

## Where the money goes

Most of the permit fee goes to the communities of the valley where the animal is hunted. Dawn reported that around 80% of trophy hunting revenue in Gilgit-Baltistan went to local communities in the 2025–26 season ([Dawn](https://www.dawn.com/news/1939432)). Communities use this income for conservation and for local needs such as schools and water schemes.

## Our responsibilities in the field

- We hunt only within the permit, the area and the season set by the authorities.
- Our guides work with the community's own game watchers to select a mature animal.
- We respect the animal: field care, skinning, salting and packing are done carefully by our team, and the trophy permit formalities are completed before export.
- We keep camps clean and employ guides, cooks and porters from the area.

Every hunt contributes to the conservation of these species and to the development of the communities who protect them.
"""

AGENTS_MD = """
## Why agents work with us

- **Licensed since 1989:** Hunt Venture Safaris (Pvt) Limited, Govt. Licence No. 2087, based in Gilgit.
- **Everything in-country handled:** trophy permits, provincial licences, firearm import and export documents, visa assistance, transfers, flights to Gilgit, 4x4 transport, camps, guides and trophy preparation.
- **Quick replies:** we usually reply within 10–15 minutes.
- **Clear terms:** a 40% advance confirms a hunt; the balance is due before the hunt starts.

## Hunts for season 2027–28

| Hunt | Area | Recommended period | Duration |
|---|---|---|---|
| [Astore Markhor](/hunts/astore-markhor/) | Nagar, Skardu, Astore, Gilgit, Bunji, Kargah | Mid Nov – mid Feb | 20 days (15 hunting) |
| [Himalayan Ibex](/hunts/himalayan-ibex/) | Upper Hunza | Mid Nov – mid Feb | 10 – 12 days |
| [Blue Sheep](/hunts/blue-sheep/) | Shimshal Valley | Nov, Mar, Apr | 15 – 16 days |
| [Blanford Urial & Sindh Ibex](/hunts/blanford-urial-sindh-ibex/) | Dureji | Dec – Jan | 9 days (5 hunting) |
| [Punjab Urial](/hunts/punjab-urial/) | Kala Bagh, Jhelum, Padri | Dec – Mar | Up to 5 hunting days |

## Ask for the agent pack

Email [huntventuresafaris@gmail.com](mailto:huntventuresafaris@gmail.com) or message us on WhatsApp at +92 311 166 7829 with your agency name and the hunts you sell. We will send the 2027–28 hunt sheets, trade rates and photographs.

We also exhibit at Cinegética in Spain. If we met at the fair, mention it when you write.
"""

TOURS_MD = """
## Tours and trekking

From Gilgit we organise tours and treks through the valleys of the Karakoram, Himalaya and Hindu Kush, with guides, transport and camps arranged by our own team.

## Jeep safaris

Jeep safaris along the Karakoram Highway and into the side valleys, for travellers who want to see the mountains without long days on foot.

## Mountaineering expeditions

Support for mountaineering expeditions in northern Pakistan: permits, liaison, transport, porters and base-camp logistics.

## For companions on a hunt

Non-hunting companions can join a hunt or spend some of the time touring. Tell us who is travelling and we will plan both.

## Ask for an itinerary

Routes and dates depend on the season and your interests. Email [huntventuresafaris@gmail.com](mailto:huntventuresafaris@gmail.com) or message us on WhatsApp at +92 311 166 7829 and we will send an itinerary.
"""

PRIVACY_MD = """
## Who we are

Hunt Venture Safaris (Pvt) Limited, Hotel Riveria, River View Road, Chinar Bagh, Gilgit, Gilgit-Baltistan, Pakistan – 15100. Email: huntventuresafaris@gmail.com.

## What we collect

When you send an enquiry through our website, by email or on WhatsApp, we receive the details you choose to give us: your name, email address, phone or WhatsApp number, country, the hunts and dates you are interested in, the size of your party and any message you write.

The enquiry form on this website does not store your details on our website. It prepares a message that you send to us yourself, by WhatsApp or email.

## How we use it

We use your details only to reply to your enquiry, to plan and book your hunt or trip, and to arrange the permits, documents and travel it needs. To do this we may share the necessary details with Pakistani government authorities (for permits, licences and firearm documents) and with airlines, hotels and transport providers involved in your trip.

We do not sell your details or use them for advertising.

## How long we keep it

We keep enquiry details for as long as we need them to reply and, if you book, for as long as the law requires us to keep booking records.

## Your choices

You can ask us at any time what details we hold about you, ask us to correct them or ask us to delete them. Email huntventuresafaris@gmail.com.

## Third-party services

If you contact us on WhatsApp or by email, those services process your message under their own privacy policies. This website uses fonts from Google Fonts.
"""


# ---------------------------------------------------------------- guides (markdown files)

def parse_front(text):
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    meta, body = {}, text
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
        body = m.group(2)
    return meta, body


def pages_guides():
    gdir = os.path.join(ROOT, "content", "guides")
    files = sorted(glob.glob(os.path.join(gdir, "*.md")))
    if not files:
        return []
    U = EN.UI
    G = EN.GUIDE_UI
    guides = {}
    for f in files:
        meta, body = parse_front(open(f).read())
        guides[meta.get("slug", os.path.basename(f)[:-3])] = (meta, body)
    for slug, (meta, body) in guides.items():
        hub = slug == "hunting-in-pakistan"
        path = "/hunting-in-pakistan/" if hub else f"/hunting-in-pakistan/{slug}/"
        html_body = md(body)
        html_body = re.sub(r'<table>', '<div class="table-wrap"><table>', html_body).replace("</table>", "</table></div>")
        html_body = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" rel="noopener"', html_body)
        hub_title = guides.get("hunting-in-pakistan", ({"h1": "Hunting in Pakistan"}, ""))[0].get("h1", "Hunting in Pakistan")
        crumbs = [(U["home_crumb"], "/"), (meta.get("h1", slug), None)] if hub else [(U["home_crumb"], "/"), ("Hunting in Pakistan", "/hunting-in-pakistan/"), (meta.get("h1", slug), None)]
        related = [s.strip() for s in meta.get("related_hunts", "").split(",") if s.strip() in EN.BY]
        rel = "".join(C.hunt_card(EN, EN.BY[s]) for s in related[:3])
        others = [(s, m.get("h1", s)) for s, (m, _) in guides.items() if s not in (slug, "hunting-in-pakistan")]
        side = "".join(f'<li><a class="guide-link" href="/hunting-in-pakistan/{s}/"><span>{E(t)}</span>{icon("arrow")}</a></li>' for s, t in others)
        upd = meta.get("updated")
        upd_txt = f'<p class="updated">{E(G["updated"])} {datetime.date.fromisoformat(upd).strftime("%-d %B %Y")}</p>' if upd else ""
        body_html = f'''<div class="wrap page-head">{breadcrumb(EN, crumbs)}{heading("Hunting in Pakistan" if not hub else None, meta.get("h1", slug), meta.get("lede"), level=1)}{upd_txt}</div>
<section class="band band-tight"><div class="wrap guide-grid">
  <article class="prose">{html_body}</article>
  <aside class="guide-aside"><h2 class="h3">{E(G["back_hub"] if not hub else "Guides")}</h2><ul class="guide-list">{side}</ul>{'' if hub else f'<p><a class="hvs-btn hvs-btn-tertiary" href="/hunting-in-pakistan/">{E(G["back_hub"])} {icon("arrow")}</a></p>'}</aside>
</div></section>
{section(heading(None, G["related_hunts"], hid="gr-h") + f'<div class="card-grid">{rel}</div>', cls="band-deep", label="gr-h") if rel else ""}
{cta_band(EN, EN.HOME["cta_h2"], EN.HOME["cta_text"])}'''
        ld = [breadcrumb_ld(crumbs), {"@context": "https://schema.org", "@type": "CollectionPage" if hub else "Article",
              "headline": meta.get("h1", slug), "description": meta.get("description", ""), "url": SITE + path,
              "inLanguage": "en-GB", "author": {"@id": C.ORG_ID}, "publisher": {"@id": C.ORG_ID},
              **({"dateModified": upd} if upd else {})}]
        write(path, page(EN, path=path, title=meta.get("title", slug), description=meta.get("description", ""), body=body_html,
                         current="planning", ld=ld), "en")
    return list(guides)


def page_404():
    body = f'''<div class="wrap page-head page-head-center">{heading("404", "We could not find that page", "The page may have moved. These links will get you back on track.", level=1, center=True)}
<p class="center-actions"><a class="hvs-btn hvs-btn-primary hvs-btn-lg" href="/hunts/">See the hunts</a><a class="hvs-btn hvs-btn-secondary hvs-btn-lg" href="/">Home</a><a class="hvs-btn hvs-btn-secondary hvs-btn-lg" href="/contact/">Contact</a></p></div>'''
    fp = os.path.join(OUT, "404.html")
    open(fp, "w").write(page(EN, path="/404", title="Page not found | Hunt Venture Safaris", description="Page not found.", body=body, noindex=True))


# ---------------------------------------------------------------- sitemap, robots, vercel

def write_meta():
    urls = []
    for path, lang, alts, noindex in PAGES:
        if noindex:
            continue
        links = ""
        if alts:
            links = "".join(f'<xhtml:link rel="alternate" hreflang="{k}" href="{SITE}{v}"/>' for k, v in alts.items())
            if "en" in alts:
                links += f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{alts["en"]}"/>'
        urls.append(f"  <url><loc>{SITE}{path}</loc><lastmod>{TODAY}</lastmod>{links}</url>")
    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          + "\n".join(urls) + "\n</urlset>\n")
    open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /thank-you/\nDisallow: /es/gracias/\n\nSitemap: {SITE}/sitemap.xml\n")


def copy_assets():
    dst = os.path.join(OUT, "assets")
    for sub in ("css", "js", "img", "brand"):
        s = os.path.join(ROOT, "assets", sub)
        if os.path.isdir(s):
            shutil.copytree(s, os.path.join(dst, sub), ignore=shutil.ignore_patterns("_*.json"))
    # site.css/js live in build/static
    for f in glob.glob(os.path.join(ROOT, "build", "static", "*")):
        sub = "css" if f.endswith(".css") else "js"
        os.makedirs(os.path.join(dst, sub), exist_ok=True)
        shutil.copy(f, os.path.join(dst, sub, os.path.basename(f)))
    # strip font @import (fonts are linked in <head>)
    for f in ("tokens.css", "components.css"):
        p = os.path.join(dst, "css", f)
        t = open(p).read()
        open(p, "w").write(re.sub(r'@import url\([^)]*\);\s*', '', t))
    shutil.copy(os.path.join(ROOT, "assets", "brand", "favicon-32.png"), os.path.join(OUT, "favicon.ico"))


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    copy_assets()
    for L in LANGS:
        page_home(L); page_hunts(L)
        for h in L.HUNTS:
            page_hunt(L, h)
        page_plan(L); page_thanks(L); page_contact(L); page_cinegetica(L)
    pages_en_only()
    g = pages_guides()
    page_404()
    write_meta()
    print(f"Built {len(PAGES)} pages ({'with' if ES else 'without'} Spanish; {len(g)} guides) into {OUT}")


if __name__ == "__main__":
    main()
