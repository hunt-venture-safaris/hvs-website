# AtAGlance

The six-cell spec grid from every hunt brochure: Species, Area, Hunting period, Recommended period, Altitude, Duration, always in that order.

**Provide:** the six values from the hunt's brochure. Species cell carries the scientific name in italic after the common name. Duration cell carries the start and end city as a `<small>` second line.

- A `<dl class="hvs-glance">`; each cell a `<div>` with `<dt>` and `<dd>`. Cells on `panel`, `radius-1`, a 2px `brass-rule` left edge (as in the brochure), `space-4`/`space-5` padding.
- Labels `eyebrow` in `brass`; values `data` in `ink`, tabular figures; secondary lines `body-small` in `ink-muted`.
- 3 columns at desktop, 2 under 760px, 1 under 480px.
- Dates: "15 October – 30 April" (day month, no year, en dash with spaces). Altitude: "2,500 m – 4,700 m" (comma thousands, space before m). Dureji is in feet as the brochure gives it: "500 – 3,000 ft (flat terrain)".

Don't: reorder or rename the six cells; abbreviate months in this component (abbreviations are for HuntCard only).
