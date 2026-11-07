Hunt Venture Safaris (HVS) is a government-licensed trophy hunting outfitter in Gilgit, Pakistan, operating since 1989. The system is built from the HVS logo and the 2027–28 brochures, and follows Apple's Human Interface Guidelines: content first, familiar controls, brand colour kept for the primary action and status, one signature element. It should feel like a serious, established mountain outfitter. Do not use generic travel-template patterns.

## Content fundamentals

- **Voice:** plain, factual, assured. Lead with the fact a hunter needs (species, area, altitude, days, permit) and put adjectives after it, if at all. Quote the brochures; do not paraphrase them into marketing copy. Example: "Fifteen full days for the hunting expedition."
- **Person:** "we" for HVS, "you" for the hunter. Never "I".
- **Spelling:** British: licence (noun), organise, programme, colour, metres.
- **Casing:** sentence case for headings, buttons and labels ("Enquire about this hunt"). Uppercase only through the `eyebrow` style. Write eyebrow text in sentence case in the markup and let CSS uppercase it.
- **Species:** capitalise common names as the brochures do: Astore Markhor, Himalayan Ibex, Blue Sheep, Blanford Urial, Sindh Ibex, Punjab Urial. Scientific names in italic, genus capitalised: *Capra falconeri falconeri*, *Capra ibex sibirica*, *Pseudois nayaur*.
- **Dates:** "15 October – 30 April" (day, full month, spaced en dash). Seasons "2027–28" (closed en dash). Short form for cards only: "Mid Nov – mid Feb".
- **Altitudes:** "2,500 m – 4,700 m" or "2,500–4,700 m" in tight spaces: comma thousands, a space before the unit. Dureji stays in feet as published: "500 – 3,000 ft (flat terrain)".
- **Durations:** "20 days · 15 hunting days"; route "Islamabad to Islamabad". Use the middle dot `·` as the separator in meta lines.
- **Credentials:** "Govt. Licence No. 2087" in compact lines, "Government Licence No. 2087" in running text. "Since 1989". Legal name "Hunt Venture Safaris (Pvt) Limited".
- **Prices:** never shown. Write "On request" and link to the enquiry form.
- **Unknown facts:** write "TBC". Never invent a figure, testimonial or success rate.
- **No emoji, no exclamation marks.**

## Visual foundations

### Colour

- **Dark first.** The brand's own theme is `dark`, the brochures' near-black green. `light` (bone) is the alternative and the logo's native ground. Build every page in `dark` and check it in `light`.
- **Grounds:** `field` for the page; `panel` for cards and spec cells; `panel-raised` for hover and the highlighted itinerary row; `field-deep` for the footer, the trust bar and form inputs. Separate surfaces with these steps and brass hairlines, not shadows.
- **Text:** `ink` for headings and body, `ink-muted` for secondary text and scientific names. Both pass 4.5:1 on all four grounds in both themes.
- **Brass** is the brand's voice in the UI. Use `brass` for eyebrows, labels and spec values; `brass-rule` for 1px hairlines and the top edges of panels; `brass-bright` for the focus ring and selected chips. Brass may appear many times per view.
- **Crimson is rationed**, as on the logo, where it appears only on the horn tips. Use `crimson` (exact logo #BD2030) for (1) the one primary button per view, (2) the hunting-days marker in ItineraryTimeline and (3) the top rule of the "Not included" panel. When crimson is text or a small mark (errors, "Not included", the required asterisk), use `crimson-on-dark`, because #BD2030 is only 2.7:1 on `field`. Label crimson fills with `on-crimson`.
- **Ratio, roughly:** 80% grounds, 15% ink, 4% brass, under 1% crimson.
- **Status:** `success` (blue-teal) for Included and success messages; `warn` (amber) for notes; `danger` (an alias of `crimson-on-dark`) for errors and Not included. Success is deliberately off the red-green axis. Every status always carries an icon and a word ("Included in the package", "Not included", "Please note", "Error:").
- **Photographs:** put text on photos only over a `scrim` band, in `plate`-coloured text. `brand-field` is the fixed dark green for cover slabs and photo scrims.
- `graphite` is a reference value for the logo only. Do not use it in UI.

### Typography

- **Display: Libre Caslon Display** (Google Fonts, `display` family). It is a high-contrast Caslon cut, with heavy stems and hairline serifs like the HVS monogram, and it lacks the fashion-magazine feel of Playfair or Bodoni. It has one weight (400) and is only for sizes 32px and up: `display` (64px hero, 44px mobile), `h1` (48px page title), `h2` (36px section).
- **Text: Public Sans** (`sans` family). It is a neutral grotesque in Arimo's spirit, the face the brochures use, but drawn for screens, with tabular figures and a real italic for scientific names. Use it for `h3`, `lead`, `body`, `body-small`, `label`, `caption`, `eyebrow`, `data`, `data-lg`, `scientific`.
- **System UI** (`ui` family, -apple-system / Segoe UI): use it only for native form controls if Public Sans fails to load. Do not mix it into content.
- Body text is `body` at 17px/28px and never smaller. `body-small` (15px) is for lists, tables and the footer. `caption` (13px) is for captions and legal lines only.
- `eyebrow` is 13px, weight 600, tracked 0.14em, uppercase, in `brass`. Every section heading has one above it ("At a glance", "Proposed hunting plan", "The package").
- Figures (altitudes, days, licence number, years) use `data` / `data-lg` with tabular lining numerals so columns align.
- Keep running text to `text-max` (680px).

### Spacing and layout

- Use the 4px-based `space-1`–`space-10` scale (4, 8, 12, 16, 24, 32, 48, 64, 96, 128). Panels have `space-5` padding. Leave `space-6` between a heading and its content, `space-7` between blocks and `space-9` between sections on desktop (`space-8` on mobile).
- Content max width is `container-max` (1200px) on a 12-column grid. The gutter is `gutter` (24px) at 768px and up and `space-4` (16px) below. Running text max width is `text-max`.
- Breakpoints: 480, 760, 860 (nav collapse) and 1200. Design at 375px first. There must be no horizontal scroll at 320px.
- Hunt pages follow the brochure order: hero → TrustBar → AtAGlance → ElevationBand → ItineraryTimeline → RateTable + InclusionsList → EnquiryForm → Footer.

### Shape, borders, depth

- **Radii are near-square,** like the brochure panels. Use `radius-1` (2px) for panels and cards, `radius-2` (4px) for buttons, inputs and the logo plate, `radius-0` for full-bleed bands and photos, and `radius-full` only for itinerary dots and the elevation band. No pill buttons: pills read as a consumer app, and the brochures are built of rectangles.
- **Borders are brass hairlines:** 1px `brass-rule` on the top edge of cards, under section headings (64px long) and on the TrustBar. Use `line` for quiet row dividers and `line-strong` for control borders (3:1 or better).
- **Shadows:** only `shadow-float`, and only on the floating NavBar and its menu. Nothing else floats.

### Imagery

- Use landscapes at full scale: Karakoram peaks, snow valleys, hunters climbing, animals in their habitat. Mountains carry heroes. Trophy-with-hunter shots belong in galleries, never at hero scale.
- **No blood, ever.** Never use a wounded animal or a gutted carcass. Crop out rifles pointed at camera.
- Vintage 1990s film photographs may appear as "Since 1989" evidence, captioned with year and place if known (TBC).
- Photos are full-bleed or `radius-0`. Do not apply duotones or colour tints. A `scrim` band carries any overlaid text.

### Logo

- The master `assets/Logos/hvs-logo.png` is dark-on-light. On dark grounds it always sits on the bone plate (`hvs-plate`: `plate` fill, `radius-2`). In the light theme it may sit directly on `field`. The minimum height is 36px. Never recolour, invert or put it on glass.

### Motion

- Each page has one orchestrated moment: the ElevationBand grows upward over `duration-reveal` (900ms, ease-out) the first time it scrolls into view. Everything else is a 150ms colour change (`duration-quick`) or a 240ms menu open (`duration-base`).
- Under `prefers-reduced-motion: reduce`, durations are 0 and the band appears drawn. Do not use parallax, auto-playing carousels or count-up numbers.

### Glass

- The floating NavBar is the only translucent surface (`glass` + 20px backdrop blur). Never put glass on content, cards or photos. Under `prefers-reduced-transparency: reduce`, use solid `field`.

## Apple HIG rules

- **Targets:** every interactive element is at least `target-min` (44 × 44px), including inline links in the contact card and footer.
- **Legibility:** body text is 17px or larger. All text meets 4.5:1 on its ground (3:1 for 24px+), in both themes. Respect browser zoom to 200% without loss.
- **Familiar controls:** use native `<a>`, `<button>`, `<select>`, checkboxes and a standard top bar with a Menu button on mobile. Do not build custom scroll-jacking, hover-only menus or gesture-only navigation.
- **Deference:** content (mountains, species, facts) leads. Chrome is quiet. Brand colour goes to the primary action and status only.
- **One signature element: the ElevationBand,** each hunt's real altitude range drawn on a fixed 0–5,000 m scale. It is the one element that is unmistakably HVS. Do not add a second signature (no decorative markhor silhouettes, no topographic background textures).
- **Dark and light:** both themes are first-class. Follow `prefers-color-scheme` unless the visitor has chosen a theme.

## Iconography

- Use **Lucide** (open source, ISC licence) line icons: 24px grid, drawn at 20px, **1.5px stroke**, round caps and joins, `stroke: currentColor` so they take the text colour beside them. Use the `.hvs-icon` class.
- Icons in use: `check`, `x`, `circle-check`, `circle-alert`, `triangle-alert`, `menu`, `arrow-right`, `phone`, `mail`, `map-pin`, `message-circle` (WhatsApp, labelled with the word "WhatsApp"; do not use the WhatsApp brand glyph unless the official asset is used).
- Icons always sit beside a word. An icon alone needs an `aria-label`. Decorative icons get `aria-hidden="true"`.
- No emoji, no filled icon styles, no species pictograms.

## Accessibility

- **Focus ring:** 2px solid `brass-bright` outline with a 2px offset on every focusable element (`shadow-focus` where outline is clipped). It is 5:1 or better on every ground in both themes. Never remove focus styles.
- **Contrast:** every text token's usage note names its grounds, and every named pair is 4.5:1 or better in both themes. Hairlines and control borders are 3:1 or better. The brand crimson as text on dark grounds fails (2.7:1), so use `crimson-on-dark`. Brochure brass on bone fails (2.1:1), so `brass` darkens to #735824 in `light`.
- **Not colour alone:** status always carries an icon and a word. The hunting days in ItineraryTimeline carry the word "Hunting". Errors start with "Error:".
- **Forms:** use visible labels, `autocomplete` attributes, errors linked by `aria-describedby`, and a `role="status"` success message.
- **Structure:** one `h1` per page, landmarks (`nav`, `main`, `footer`), `lang="en-GB"`. Spanish pages (Cinegética audience) use `lang="es"`.
