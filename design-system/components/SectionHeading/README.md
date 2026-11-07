# SectionHeading

An eyebrow over a serif heading, optionally with a lead paragraph and a short brass rule: the brochures' "HUNT DETAILS / Astore Markhor Hunt" pattern.

**Provide:** eyebrow text (two to four words, written in sentence case in the markup; CSS uppercases it), a heading, an optional lead sentence.

- Wrapper `hvs-heading`; eyebrow `hvs-eyebrow` (`eyebrow` style, `brass`); heading `h1` (`h1` style) for page titles, `h2` (`h2` style) for sections, both in `display` family and `ink`; lead in `lead` style, `ink-muted`.
- `hvs-heading-rule` adds a 64px `brass-rule` hairline under the heading; use it once per section, not under every heading.
- `hvs-heading-center` centres the block (hero and closing CTA only).
- Max width `text-max`.

Don't: skip the eyebrow on a section heading; use the display face below 32px; put two eyebrows in a row.
