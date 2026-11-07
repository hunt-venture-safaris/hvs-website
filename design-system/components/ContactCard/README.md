# ContactCard

The company's direct contact details as real, selectable text and tappable links.

**Provide:** phone numbers in international format, email, office address. WhatsApp is on +92 311 166 7829 (the first number); link it as `https://wa.me/923111667829`. Show "We usually reply within 10–15 minutes" beside the contact options.

- `hvs-contact` on `panel`, `radius-1`, 1px `brass-rule` top edge, max width 440px.
- Labels `eyebrow` in `brass`; values `body` in `ink`. Phone numbers as `tel:` links, email as `mailto:`, each a `hvs-link` at least 44px tall.
- Address in an `<address>` element, line breaks as on the brochure, never an image.
- One secondary button "Message on WhatsApp" (`wa.me` link). The crimson primary stays with the EnquiryForm.
- Write numbers with spaces in groups as the brochure does: "+92 311 166 7829".

Don't: render contact details as images; add a map embed without a fallback; use crimson here.
