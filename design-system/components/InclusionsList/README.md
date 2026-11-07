# InclusionsList

Two panels side by side: what the package includes and what it does not. Each item carries an icon and the heading carries a word, so the meaning never rests on colour.

**Provide:** the two lists copied from the hunt's brochure (they are identical across hunts except the permit line, which names the species).

- `hvs-incl` grid; `section.hvs-incl-yes` and `section.hvs-incl-no`, each on `panel` with a 2px top edge: `brass-rule` for included, `crimson` for not included (the brochure's red header rule).
- Headings `eyebrow` style: "Included in the package" in `success` with a check-circle icon; "Not included" in `crimson-on-dark` with an alert-circle icon.
- Items `body-small` in `ink`, `line` dividers; a check icon (`success`) or a cross icon (`crimson-on-dark`) before each, plus a visually hidden "Included:" / "Not included:" prefix for screen readers.
- Stacks to one column under 640px, included first.

Don't: shorten items; drop the "Any service not listed as included" line; use green for included (success is blue-teal by design).
