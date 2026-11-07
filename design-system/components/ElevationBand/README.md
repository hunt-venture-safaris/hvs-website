# ElevationBand

The system's one signature element: each hunt's real altitude range drawn as a brass band on a vertical metre scale. It turns the brochure's altitude figure into something a hunter can read at a glance and compare across hunts.

**Provide:** the low and high altitude in metres from the brochure (Astore Markhor 2,500–4,700; Himalayan Ibex 2,500–4,700; Blue Sheep 3,200–4,500), the species name for the accessible label, and one sentence about the terrain. Dureji (500–3,000 ft, flat terrain) and Punjab Urial (TBC) do not get a band: show the figure as text in AtAGlance instead.

- An inline SVG (`hvs-elev-svg`, 132×280) with `role="img"` and an `aria-label` that states the range in words ("Astore Markhor hunting altitude: 2,500 to 4,700 metres").
- Scale 0–5,000 m, ticks every 1,000 m: axis `line-strong`, ticks `brass-rule`, labels `caption` in `ink-muted` with tabular figures. Band `brass-rule`, 16px wide, `radius-full`; end caps `brass-bright`.
- Beside it, `hvs-elev-copy`: eyebrow "Altitude", the range in `data-lg`, one line of terrain in `body-small` `ink-muted`.
- Motion: this is the page's one orchestrated moment. Add `hvs-draw` to the band to grow it upward over 900ms when it first scrolls into view; under `prefers-reduced-motion` it appears drawn.
- On the Hunts index, set bands side by side on the same scale (`hvs-elev-compare`, one `hvs-elev-col` per hunt with its name as an eyebrow) so the ranges compare honestly.

Don't: rescale per hunt (always 0–5,000 m); use crimson for the band; animate anything else on the same page.
