# EnquiryForm

The one conversion form on the site: who you are, how to reach you, what you want to hunt and when. Shown here with a filled field, an error, the species multi-select and the success message together.

**Provide:** an action endpoint, the species list (Astore Markhor, Himalayan Ibex, Blue Sheep, Blanford Urial, Sindh Ibex, Punjab Urial), months October–April plus "No preference". Required fields: full name and email only; everything else optional so agents and first-time hunters are not put off.

- Two-column `hvs-form` grid (one column under 640px). Each field is `hvs-field` with a visible `hvs-label` (`label` style, `ink`) above the control; never placeholder-only labels.
- Controls `hvs-input`, `hvs-select`, `hvs-textarea`: `field-deep` ground, 1px `line-strong` border, `radius-2`, 17px text (stops iOS zoom), min height `target-min`. Set `autocomplete` and `type` (`email`, `tel`, `numeric`).
- Focus: border and 2px outline in `brass-bright`, 2px offset.
- Error: `data-state="error"` on the field, 2px `crimson-on-dark` border, `aria-invalid="true"`, and an `hvs-error` line with an alert icon and the word "Error:" linked by `aria-describedby`. Say what to do, not what went wrong.
- Species: checkbox chips (`hvs-chip`) in a `fieldset` with a `legend`; checked chips get a `brass-bright` border and filled box plus bold text.
- Submit: the page's single crimson primary, "Send enquiry".
- Success: replace the form with `hvs-success` (`role="status"`), a check icon, "Enquiry sent" in `success`, and a sentence that repeats back what they asked for and when we will reply.

Don't: ask for budget or passport details here; use red text on its own for errors; disable the submit button while fields are empty.
