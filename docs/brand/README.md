# Paladino Brand System

## Name & positioning

"Paladino" (paladin: a trusted champion/defender) frames the firm as an advocate acting
in a client's interest through a transaction, not just a transaction processor. The mark
and copy lean into that without being literal (no swords/shields-as-clipart) — see
`logo-mark.svg` for how that's expressed as a simple geometric chevron instead.

Positioning line used across brand/site: **"Independent advice. On your side."**

## Palette

Grounded in `docs/ib-design-reference.md`: white/off-white field, near-black text, one
restrained navy accent, a muted secondary accent used only for small highlights — never as
a large color field.

| Token | Hex | Use |
|---|---|---|
| `--color-bg` | `#F7F6F2` | Page background (off-white, not pure white) |
| `--color-surface` | `#FFFFFF` | Cards, nav bar |
| `--color-ink` | `#14181F` | Body text, headlines |
| `--color-ink-muted` | `#4B5563` | Secondary/supporting text |
| `--color-navy` | `#0B1F3A` | Primary brand accent — nav, headlines, primary buttons |
| `--color-navy-dark` | `#081627` | Footer background, hover states |
| `--color-gold` | `#A9812E` | Secondary accent — used only for underlines, small labels, dividers |
| `--color-border` | `#E2E1DB` | Hairlines, card borders |

Rules:
- Gold never fills a background larger than a label chip or a 2px rule.
- Navy is the only color allowed as a large field (hero band, footer, nav).
- No gradients.

## Typography

Sans-serif throughout (matches every firm in the reference set — none run serif body
copy). System: **Inter**, falling back to the OS UI stack.

```css
font-family: "Inter", -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
```

| Role | Size / weight | Notes |
|---|---|---|
| Display (hero headline) | 3.25rem / 700 | Short, declarative lines only |
| H2 (section headline) | 2rem / 700 | |
| H3 (card headline) | 1.25rem / 600 | |
| Body | 1.0625rem / 400, line-height 1.6 | Generous line height per reference notes |
| Small / label | 0.8125rem / 600, letter-spacing 0.04em, uppercase | Section eyebrows, footer labels |

Hierarchy comes from weight and size, never from color — consistent with every firm
surveyed.

## Logo

`logo-mark.svg` — a chevron/shield-adjacent geometric mark built from two overlapping
angular strokes, evoking a paladin's stance without literal iconography. Renders at 1-color
(navy on light backgrounds, white on navy/dark backgrounds). Minimum size: 24px.

Wordmark: "PALADINO" set in Inter 700, small-caps-style tracking (`letter-spacing: 0.06em`),
always navy or white, never gold (gold is reserved for accents, not primary brand marks).
