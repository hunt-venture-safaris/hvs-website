# RateTable

The four rate cells from the brochure's package page (1 hunter, 2 hunters, non-hunting companion, extra hunting day), with the season line and the permit-fee note.

**Provide:** the hunt's duration and start/end city for the meta line; the price in each cell. Prices are not public: every cell reads "On request" until the client publishes figures. The sub-lines under each price are TBC (client to confirm) and may be removed.

- `hvs-rates` grid of four `hvs-rate` cells on `panel`, 2px `brass-rule` top edge, centred. Headings `eyebrow` in `brass`; value 20px/600 `ink`; sub-line `caption` in `ink-muted`.
- Meta line `body-small` in `ink-muted`, with a tertiary link to the enquiry form.
- Pair with `hvs-note` (Please note): `warn` alert icon and the words "Please note", body in `ink`. Copy the brochure's note verbatim.
- 4 across at desktop, 2 under 760px.

Don't: invent or estimate prices; show currency until the client confirms it; use a crimson button inside the table.
