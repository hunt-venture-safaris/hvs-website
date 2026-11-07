# NavBar

The floating translucent bar: logo on its bone plate, five links, one Enquire button. It is the only glass surface in the system.

**Provide:** up to five links (Hunts, Season 2027–28, About, Conservation, Contact), `aria-current="page"` on the current one, the logo image, and the enquiry href.

- Fill `glass` with a 20px backdrop blur, 1px `line` border, `radius-2`, `shadow-float`, `z-nav`. Height `nav-height` (64px). Sticky, `space-3` from the top, max width `container-max`.
- Under `prefers-reduced-transparency: reduce` the fill becomes solid `field` and the blur is removed.
- The logo always sits on `hvs-plate` (`plate`, bone) because the master is dark-on-light. Never place the logo directly on `glass` or `field`.
- Links: `label` style in `ink`, 44px tall; hover and current page in `brass`, current page with a 2px `brass-rule` underline.
- Below 860px the links and CTA collapse behind a Menu button (icon and the word "Menu", `aria-expanded`); the open menu stacks links full width under a `line` divider, and the CTA goes full width.

Don't: put photographs or content cards on glass; add a second CTA; hide the Enquire action on mobile (it moves into the menu and also appears at the end of every hunt page).
