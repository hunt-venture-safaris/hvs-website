# HuntCard

One hunt product in a grid: region eyebrow, species, scientific name, four specs, one link to the hunt page.

**Provide:** region (eyebrow), species common name, scientific name (or "Combination hunt"), area, recommended months, altitude range, duration with hunting days, hunt page href. Optional `hvs-card-media` block above the body with a landscape or animal-in-habitat photo (3:2).

- `hvs-card` on `panel`, `radius-1`, 1px `brass-rule` top edge. Title `h3` in `ink`; scientific name `scientific` (italic, `ink-muted`); spec labels `eyebrow` in `brass`; spec values `data` (tabular figures) in `ink`.
- Use the brochure's exact figures: "2,500–4,700 m", "20 days · 15 hunting". Never invent a figure; write "TBC" if the brochure has none (Punjab Urial altitude).
- The card's single action is the tertiary "View hunt" link. The crimson Enquire button lives on the hunt page, not on every card.
- Grid: 3 across at `container-max`, `space-4` gap, 1 across on phones.

Don't: show prices (they are on request); use trophy photos with blood; add badges like "Popular".
