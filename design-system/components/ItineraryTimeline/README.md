# ItineraryTimeline

The day-by-day plan on a vertical brass line, with the hunting block highlighted by the crimson marker, as in the brochures.

**Provide:** an ordered list of steps, each with a day label ("Day 1", "Days 4–18") and one line of text copied from the brochure; mark the hunting block(s) with `hvs-tl-hunt`.

- `<ol class="hvs-timeline">` with an `aria-label` naming the hunt; each `<li class="hvs-tl-item">` holds `hvs-tl-dot`, `hvs-tl-day`, `hvs-tl-text`.
- Line and dots `brass-rule`; day labels `eyebrow` in `brass`; text `body` in `ink`.
- Hunting block: row on `panel-raised`, a 16px `crimson` marker, text weight 600, plus the word "Hunting" (`hvs-tl-tag`, `crimson-on-dark`) so the highlight is not colour alone. This is one of crimson's two permitted non-button uses.
- Blue Sheep has two highlighted kinds of day (trek days 4–5 and hunting days 6–12): highlight only the hunting days; trek days stay plain.

Don't: highlight more than the hunting days; use icons per day; rewrite the brochure's day text.
