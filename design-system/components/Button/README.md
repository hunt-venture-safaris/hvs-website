# Button

One crimson primary per view; everything else is secondary (brass outline) or tertiary (brass text link).

**Provide:** a verb-first label in sentence case ("Enquire about this hunt", "Send enquiry", "View itinerary"); an `href` for navigation (`<a>`) or a `type` for form actions (`<button>`).

**Classes:** `hvs-btn` plus one of `hvs-btn-primary` | `hvs-btn-secondary` | `hvs-btn-tertiary`; size `hvs-btn-lg` (52px, hero and page-end CTAs) or `hvs-btn-sm` (narrower padding, same 44px height); `hvs-btn-block` for full width on mobile.

- Primary: `crimson` fill, `on-crimson` label, `crimson-hover` on hover/press. Use for the enquiry action only. The crimson is the logo's horn-tip colour; keep it as scarce as it is on the mark.
- Secondary: transparent, 1px `brass-rule` border, `ink` label.
- Tertiary: `brass` text, underlined, optional trailing arrow icon.
- Disabled: no fill, `line-strong` border, `ink-muted` label; also set `disabled` or `aria-disabled="true"`.
- Height never below `target-min` (44px). Corners `radius-2` (4px): square-shouldered like the brochure panels, not pills.
- Focus: 2px `brass-bright` outline, 2px offset.

Don't: put two primaries side by side; use crimson for "Read more"; use all caps on buttons (caps belong to eyebrows).
