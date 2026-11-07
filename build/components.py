"""Layout and components for huntventuresafaris.com, using the HVS design system classes."""
import html, json, datetime
from data import COMPANY, SITE

E = html.escape
YEAR = datetime.date.today().year
IMAGES = json.load(open(__file__.replace("build/components.py", "assets/img/_images.json")))

ICON = {
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "x": '<path d="M6 6l12 12M18 6L6 18"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2"/>',
    "chat": '<path d="M4 20l1.5-4A8 8 0 1112 20a8 8 0 01-4-1.1L4 20z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 7l9 6 9-6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0119 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "copy": '<rect x="9" y="9" width="11" height="11" rx="1"/><path d="M5 15V5a1 1 0 011-1h10"/>',
}


def icon(name, label=None):
    a = f'role="img" aria-label="{E(label)}"' if label else 'aria-hidden="true"'
    return f'<svg class="hvs-icon" viewBox="0 0 24 24" {a}>{ICON[name]}</svg>'


def picture(name, alt, sizes="100vw", eager=False, cls="", fit=None):
    info = IMAGES[name]
    ws = info["sizes"]
    srcset = lambda ext: ", ".join(f"/assets/img/{name}-{w}.{ext} {w}w" for w in ws)
    mid = ws[1] if len(ws) > 1 else ws[0]
    h = round(info["h"] * mid / info["w"])
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    style = f' style="object-position:{fit}"' if fit else ""
    return (f'<picture class="{cls}"><source type="image/webp" srcset="{srcset("webp")}" sizes="{sizes}">'
            f'<img src="/assets/img/{name}-{mid}.jpg" srcset="{srcset("jpg")}" sizes="{sizes}" width="{mid}" height="{h}" alt="{E(alt)}" {load}{style}></picture>')


def logo(L, href):
    return (f'<a class="site-logo hvs-focusable" href="{href}" aria-label="{E(L.UI["home_label"])}">'
            '<picture><source srcset="/assets/brand/hvs-mark.svg" media="(max-width: 860px) and (prefers-color-scheme: light)">'
            '<source srcset="/assets/brand/hvs-mark-reversed.svg" media="(max-width: 860px)">'
            '<source srcset="/assets/brand/hvs-logo.svg" media="(prefers-color-scheme: light)">'
            '<img src="/assets/brand/hvs-logo-reversed.svg" width="985" height="324" alt="Hunt Venture Safaris (Pvt) Limited"></picture></a>')


def wa_link(text=""):
    from urllib.parse import quote
    q = f"?text={quote(text)}" if text else ""
    return f"https://wa.me/{COMPANY['whatsapp_digits']}{q}"


def nav(L, current, alt_href):
    U = L.UI
    es = L.LANG == "es"
    items = ([("hunts", U["nav_hunts"], L.PATHS["hunts"])] +
             ([("planning", U["nav_planning"], "/hunting-in-pakistan/")]) +
             ([] if es else [("conservation", U["nav_conservation"], "/conservation/"), ("about", U["nav_about"], "/about/")]) +
             [("contact", U["nav_contact"], L.PATHS["contact"])])
    lis = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if k == current else ""}>{E(t)}</a></li>' for k, t, h in items)
    lang = (f'<li class="nav-lang"><a href="{alt_href}" hreflang="{"en" if es else "es"}" lang="{"en" if es else "es"}">'
            f'<span aria-hidden="true">{U["lang_switch_short"]}</span><span class="hvs-sr">{E(U["lang_switch_label"])}</span></a></li>')
    return f'''<header class="site-header">
<nav class="hvs-nav" aria-label="Main" id="nav">
  {logo(L, L.PATHS["home"])}
  <ul class="hvs-nav-links" id="nav-links">{lis}{lang}</ul>
  <a class="hvs-btn hvs-btn-primary hvs-nav-cta" href="{L.PATHS["plan"]}">{E(U["nav_cta"])}</a>
  <a class="hvs-btn hvs-btn-primary hvs-btn-sm nav-cta-mobile" href="{L.PATHS["plan"]}">{E(U["nav_cta_short"])}</a>
  <button class="hvs-btn hvs-btn-secondary hvs-btn-sm hvs-nav-toggle" type="button" aria-expanded="false" aria-controls="nav-links">{icon("menu")}<span>{E(U["menu"])}</span></button>
</nav>
</header>'''


def footer(L, hunts):
    U = L.UI
    hp = lambda h: L.PATHS["hunt"].format(slug=h["path_slug"])
    hunt_links = "".join(f'<li><a href="{hp(h)}">{E(h["name"])}</a></li>' for h in hunts)
    company = [(U["footer_about"], "/about/"), (U["footer_conservation"], "/conservation/"),
               (U["footer_planning"], "/hunting-in-pakistan/"), (U["footer_tours"], "/tours-and-expeditions/"),
               (U["footer_agents"], "/agents/"), (U["footer_privacy"], "/privacy/")]
    comp = "".join(f'<li><a href="{h}">{E(t)}</a></li>' for t, h in company)
    return f'''<footer class="hvs-footer">
  <div class="hvs-footer-inner">
    <div class="footer-brand">
      <img class="footer-logo" src="/assets/brand/hvs-logo-reversed.svg" width="985" height="324" alt="Hunt Venture Safaris (Pvt) Limited" loading="lazy">
      <p>{E(U["footer_tagline"])}</p>
      <address>
        <p><a href="tel:+923111667829">+92 311 166 7829</a> <span class="muted">· WhatsApp</span><br><a href="tel:+923009893205">+92 300 989 3205</a><br><a href="mailto:{COMPANY["email"]}">{COMPANY["email"]}</a></p>
        <p>{"<br>".join(E(x) for x in COMPANY["address_lines"])}</p>
      </address>
    </div>
    <div><h2>{E(U["footer_hunts"])}</h2><ul>{hunt_links}</ul></div>
    <div><h2>{E(U["footer_company"])}</h2><ul>{comp}</ul></div>
  </div>
  <div class="hvs-footer-legal"><span>{E(U["rights"].format(year=YEAR))}</span><span>Gilgit · Gilgit-Baltistan · Pakistan</span></div>
</footer>'''


def breadcrumb(L, trail):
    items = "".join(
        (f'<li><a href="{h}">{E(t)}</a></li>' if h else f'<li><span aria-current="page">{E(t)}</span></li>') for t, h in trail)
    return f'<nav class="crumbs" aria-label="{E(L.UI["breadcrumb"])}"><ol>{items}</ol></nav>'


def breadcrumb_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": t, **({"item": SITE + h} if h else {})} for i, (t, h) in enumerate(trail)]}


ORG_ID = SITE + "/#organization"


def org_ld():
    return {
        "@context": "https://schema.org", "@type": "TravelAgency", "@id": ORG_ID,
        "name": COMPANY["name"], "legalName": COMPANY["legal"], "url": SITE + "/",
        "logo": SITE + "/assets/brand/icon-512.png", "image": SITE + "/assets/img/og-default.jpg",
        "foundingDate": COMPANY["founded"], "email": COMPANY["email"], "telephone": COMPANY["phones"][0],
        "identifier": {"@type": "PropertyValue", "name": "Government licence number", "value": COMPANY["licence_no"]},
        "address": {"@type": "PostalAddress", "streetAddress": COMPANY["street"], "addressLocality": COMPANY["locality"],
                    "addressRegion": COMPANY["region"], "postalCode": COMPANY["postcode"], "addressCountry": "PK"},
        "contactPoint": [{"@type": "ContactPoint", "telephone": p, "contactType": "customer service",
                          "availableLanguage": ["English"]} for p in COMPANY["phones"]],
        "areaServed": ["Gilgit-Baltistan", "Sindh", "Balochistan", "Punjab"],
        "knowsAbout": ["Trophy hunting", "Astore markhor", "Himalayan ibex", "Blue sheep", "Blanford urial", "Sindh ibex", "Punjab urial", "Trekking", "Mountaineering"],
    }


def page(L, *, path, title, description, body, current=None, alt_path=None, alternates=None, ld=None,
         noindex=False, og_image="/assets/img/og-default.jpg", sticky=None):
    """alternates: dict lang->path for hreflang (en/es). alt_path: language switch target."""
    alt_href = alt_path or ("/" if L.LANG == "es" else "/es/")
    hreflang = ""
    if alternates:
        hreflang = "".join(f'<link rel="alternate" hreflang="{k}" href="{SITE}{v}">' for k, v in alternates.items())
        if "en" in alternates:
            hreflang += f'<link rel="alternate" hreflang="x-default" href="{SITE}{alternates["en"]}">'
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (ld or []))
    robots = '<meta name="robots" content="noindex, follow">' if noindex else ""
    sticky_html = sticky or ""
    return f'''<!doctype html>
<html lang="{L.HTML_LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(description)}">
{robots}<link rel="canonical" href="{SITE}{path}">
{hreflang}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Hunt Venture Safaris">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:locale" content="{"es_ES" if L.LANG == "es" else "en_GB"}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1B211E">
<link rel="icon" href="/assets/brand/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/brand/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/brand/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Public+Sans:ital,wght@0,400..700;1,400..700&display=swap">
<link rel="stylesheet" href="/assets/css/tokens.css">
<link rel="stylesheet" href="/assets/css/components.css">
<link rel="stylesheet" href="/assets/css/site.css">
{lds}
</head>
<body class="{"has-sticky" if sticky else ""}">
<a class="skip-link" href="#main">{E(L.UI["skip"])}</a>
{nav(L, current, alt_href)}
<main id="main">
{body}
</main>
{footer(L, L.HUNTS)}
{sticky_html}
<script src="/assets/js/site.js" defer></script>
</body>
</html>
'''


# ---------- hunt components

def spec_rows(L, h, with_species=False):
    U = L.UI
    rows = []
    if with_species:
        sci = f' <i>{E(h["sci"])}</i>' if h.get("sci") else ""
        rows.append((U["spec_species"], f'{E(h["name"])}{("<small>" + sci.strip() + "</small>") if sci else ""}'))
    rows.append((U["spec_area"], E(h["area"])))
    rows.append((U["spec_legal"], E(h["legal"]) if h.get("legal") else E(U["on_request"])))
    rows.append((U["spec_best"], E(h["best"])))
    rows.append((U["spec_alt"], E(h["alt_text"]) if h.get("alt_text") else E(U["on_request"])))
    notes = [x for x in (h.get("duration_note"), h.get("route")) if x]
    dur = E(h["duration"]) + "".join(f'<small>{E(n)}</small>' for n in notes)
    rows.append((U["spec_duration"], dur))
    return rows


def glance(L, h):
    cells = "".join(f'<div><dt>{E(k)}</dt><dd>{v}</dd></div>' for k, v in spec_rows(L, h, True))
    return f'<dl class="hvs-glance">{cells}</dl>'


def hunt_card(L, h, heading="h3"):
    U = L.UI
    href = L.PATHS["hunt"].format(slug=h["path_slug"])
    specs = [(U["spec_best_short"], h["best"]), (U["spec_duration"], h["duration"]),
             (U["spec_alt"], h.get("alt_text") or U["on_request"]), (U["spec_area"], h["region"])]
    dl = "".join(f'<div><dt>{E(k)}</dt><dd>{E(v)}</dd></div>' for k, v in specs)
    sci = f'<p class="hvs-sci">{E(h["sci"])}</p>' if h.get("sci") else ""
    months = " ".join(str(m) for m in h["best_months"])
    return f'''<article class="hvs-card hunt-card" data-months="{months}">
  <a class="hvs-card-media" href="{href}" tabindex="-1" aria-hidden="true">{picture(h["img"], h["img_alt"], "(max-width: 760px) 100vw, 400px")}</a>
  <div class="hvs-card-body">
    <div><{heading} class="hvs-card-title"><a class="card-link" href="{href}">{E(h["name"])}</a></{heading}>{sci}</div>
    <p class="card-text">{E(h["card"])}</p>
    <dl class="hvs-specs">{dl}</dl>
    <div class="hvs-card-foot"><a class="hvs-btn hvs-btn-tertiary" href="{href}">{E(U["view_hunt"])} {icon("arrow")}</a></div>
  </div>
</article>'''


def elevation_svg(name, lo, hi, aria, animate=False):
    top = 5000.0
    H = 280.0
    y = lambda m: H - (m / top) * H
    ticks = "".join(
        f'<line class="hvs-elev-tick" x1="68" x2="76" y1="{y(m):.1f}" y2="{y(m):.1f}"/><text class="hvs-elev-label" x="60" y="{y(m) + 4:.1f}" text-anchor="end">{m:,}</text>'
        for m in range(0, 5001, 1000))
    y1, y2 = y(hi), y(lo)
    draw = " hvs-draw" if animate else ""
    return (f'<svg class="hvs-elev-svg" viewBox="0 0 132 280" role="img" aria-label="{E(aria)}">'
            f'<line class="hvs-elev-axis" x1="76" x2="76" y1="0" y2="280"/>{ticks}'
            f'<rect class="hvs-elev-range{draw}" x="84" y="{y1:.1f}" width="16" height="{y2 - y1:.1f}" rx="8"/>'
            f'<rect class="hvs-elev-cap" x="80" y="{y1 - 1:.1f}" width="24" height="2"/><rect class="hvs-elev-cap" x="80" y="{y2 - 1:.1f}" width="24" height="2"/>'
            f'<text class="hvs-elev-label" x="108" y="{y1 + 4:.1f}">{hi:,}</text><text class="hvs-elev-label" x="108" y="{y2 + 4:.1f}">{lo:,}</text></svg>')


def fmt_m(L, n):
    s = f"{n:,}"
    return s.replace(",", ".") if L.LANG == "es" else s


def elevation(L, h):
    lo, hi = h["alt"]
    aria = L.UI["alt_aria"].format(name=h["name"], lo=fmt_m(L, lo), hi=fmt_m(L, hi))
    return f'''<div class="hvs-elev">
  <div class="hvs-elev-scale">{elevation_svg(h["name"], lo, hi, aria, True)}</div>
  <div class="hvs-elev-copy"><span class="hvs-eyebrow">{E(L.UI["alt_label"])}</span><b>{E(h["alt_text"])}</b><p>{E(h["terrain"])}</p></div>
</div>'''


def timeline(L, h):
    items = []
    for day, text, hunting in h["itinerary"]:
        cls = " hvs-tl-hunt" if hunting else ""
        tag = f'<span class="hvs-tl-tag">{E(L.UI["hunting_tag"])}</span>' if hunting else ""
        items.append(f'<li class="hvs-tl-item{cls}"><span class="hvs-tl-dot" aria-hidden="true"></span><span class="hvs-tl-day">{E(day)}</span><span class="hvs-tl-text">{E(text)}{tag}</span></li>')
    return f'<ol class="hvs-timeline">{"".join(items)}</ol>'


def inclusions(L, h, included, not_included, extras):
    U = L.UI
    vals = dict(extras or {})
    vals["permit"] = h["permit"]
    inc = [line.format(**vals) for line in included]
    inc = [t for t in inc if t.strip()]
    if h.get("permit_plural") and L.LANG == "en":
        inc[0] = "Trophy hunting permits for Blanford urial and Sindh ibex"
    yes = "".join(f'<li>{icon("check")}<span>{E(t)}</span></li>' for t in inc)
    no = "".join(f'<li>{icon("x")}<span>{E(t)}</span></li>' for t in not_included)
    return f'''<div class="hvs-incl">
  <section class="hvs-incl-yes" aria-labelledby="incl-yes"><h3 id="incl-yes">{icon("check")}{E(U["h_included_label"])}</h3><ul>{yes}</ul></section>
  <section class="hvs-incl-no" aria-labelledby="incl-no"><h3 id="incl-no">{icon("x")}{E(U["h_not_included_label"])}</h3><ul>{no}</ul></section>
</div>'''


def rates(L, h, permit_note, enquire_href):
    U = L.UI
    cells = "".join(f'<div class="hvs-rate"><h3>{E(k)}</h3><p>{E(U["rates_on_request"])}</p></div>'
                    for k in (U["rate_1"], U["rate_2"], U["rate_comp"], U["rate_extra"]))
    basis = U["rate_basis"].format(route=h["route"]) if h.get("route") else ""
    return f'''<div class="hvs-rates">{cells}</div>
<div class="hvs-rates-meta"><span>{E(basis)}</span><a class="hvs-btn hvs-btn-secondary" href="{enquire_href}">{E(U["rate_cta"])}</a></div>
<div class="hvs-note rate-note">{icon("info")}<div><strong>{E(U["please_note"])}</strong><p>{E(permit_note)}</p></div></div>'''


def faq(items):
    return '<div class="faq">' + "".join(
        f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in items) + "</div>"


def trust(L):
    U = L.UI
    cells = [("1989", U["established"]), ("No. 2087" if L.LANG == "en" else "N.º 2087", U["licence"]), ("3", U["ranges"]), ("5", U["hunts_count"])]
    return '<div class="hvs-trust" role="list">' + "".join(
        f'<div role="listitem"><b>{E(a)}</b><span>{E(b)}</span></div>' for a, b in cells) + "</div>"


def contact_card(L, extra_title=None):
    U = L.UI
    return f'''<div class="hvs-contact">
  {f'<h2 class="card-h">{E(extra_title)}</h2>' if extra_title else ""}
  <dl>
    <div><dt>WhatsApp</dt><dd><a class="hvs-link" href="{wa_link()}" rel="noopener">{icon("chat")}&nbsp;+92 311 166 7829</a></dd></div>
    <div><dt>{E(U["phone"])}</dt><dd><a class="hvs-link" href="tel:+923111667829">+92 311 166 7829</a><br><a class="hvs-link" href="tel:+923009893205">+92 300 989 3205</a></dd></div>
    <div><dt>{E(U["email"])}</dt><dd><a class="hvs-link" href="mailto:{COMPANY["email"]}">{COMPANY["email"]}</a></dd></div>
    <div><dt>{E(U["office"])}</dt><dd><address>{"<br>".join(E(x) for x in COMPANY["address_lines"])}</address></dd></div>
  </dl>
  <p class="reply-note">{E(U["replies"])}</p>
</div>'''


def section(inner, cls="", id=None, label=None):
    i = f' id="{id}"' if id else ""
    lab = f' aria-labelledby="{label}"' if label else ""
    return f'<section class="band {cls}"{i}{lab}><div class="wrap">{inner}</div></section>'


def heading(eyebrow, h, lede=None, level=2, hid=None, center=False):
    idattr = f' id="{hid}"' if hid else ""
    c = " hvs-heading-center" if center else ""
    ey = f'<span class="hvs-eyebrow">{E(eyebrow)}</span>' if eyebrow else ""
    ld = f"<p>{E(lede)}</p>" if lede else ""
    return f'<div class="hvs-heading{c}">{ey}<h{level}{idattr}>{E(h)}</h{level}>{ld}</div>'


def cta_band(L, title, text, href=None, label=None):
    href = href or L.PATHS["plan"]
    label = label or L.UI["nav_cta"]
    return f'''<section class="band cta-band"><div class="wrap cta-inner">
  <div><h2>{E(title)}</h2><p>{E(text)}</p></div>
  <div class="cta-actions"><a class="hvs-btn hvs-btn-primary hvs-btn-lg" href="{href}">{E(label)}</a>
  <a class="hvs-btn hvs-btn-secondary hvs-btn-lg" href="{wa_link()}" rel="noopener">{icon("chat")} {E(L.UI["whatsapp"])}</a></div>
</div></section>'''
