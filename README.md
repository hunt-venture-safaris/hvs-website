# Hunt Venture Safaris website

Static site for [huntventuresafaris.com](https://huntventuresafaris.com): guided mountain hunts for markhor, ibex and blue sheep in Gilgit-Baltistan, Pakistan.

- `index.html` — homepage (self-contained HTML, CSS and JS; no build step)
- Deployed on Vercel from the `main` branch

## Project files

- `docs/brand/` — brand guidelines, logo master and compact mark
- `docs/seo/` — SEO architecture, staged `robots.txt` and `sitemap.xml`, JSON-LD templates
- `docs/user-flows/` — personas, information architecture, user flows (Mermaid)
- `design-system/` — the HVS design system source (tokens, brand book, component guidelines and previews)
- `assets/css/tokens.css`, `assets/css/components.css` — the design system as website stylesheets

`docs/` and `design-system/` are excluded from deployment by `.vercelignore`.
