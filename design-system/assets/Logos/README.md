# Logos

- `hvs-logo.svg` — **The master logo**, full horizontal lockup, vector: "HVS" monogram in graphite (`graphite`, #5A5A5D) with a rearing markhor rising from the V, crimson horn tips (`crimson`, #BD2030), and the wordmark "HUNT VENTURE SAFARIS / (PVT) LIMITED" in black serif capitals. Traced from the original PNG with exact brand colours; scales to any size. Use it on light grounds: `field` in the light theme, the `plate`, white paper.
- `hvs-logo-reversed.svg` — The full lockup for dark grounds: graphite and black become bone (#F4F1EA, the `plate`/`ink` value), crimson horn tips kept. Use it directly on `field`, `field-deep`, `panel` and dark photo scrims in the dark theme.
- `hvs-mark.svg` / `hvs-mark-reversed.svg` — The compact mark: the HVS monogram with the markhor, without the wordmark. Use it for the favicon, social avatars and the mobile navigation bar, and anywhere the full lockup would fall below its minimum size.
- `hvs-logo.png`, `hvs-mark.png` — The original raster versions, kept for reference. Prefer the SVGs.

Rules:
- Positive versions (graphite, black, crimson) on light grounds only; reversed versions on dark grounds only. The bone plate (`hvs-plate`: `plate` fill, `radius-2`, `space-1` vertical and `space-3` horizontal padding) remains an option for the positive logo on dark grounds, as on the brochure covers.
- Never invert, recolour, outline or stretch the logo, and never place it on glass or blur.
- Minimum height of the full lockup: 36px on screen (the wordmark's "(PVT) LIMITED" stops reading below that); below that, use the compact mark (minimum 32px tall; at 16px favicon size check legibility).
- Clear space: at least the height of the "H" on every side.
- Ink notes for `<img>` use: the SVGs carry their own fills (graphite #5A5A5D, black #000000, crimson #BD2030; reversed: bone #F4F1EA and crimson #BD2030) and do not inherit `currentColor`.
