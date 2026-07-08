---
name: web-dev-tip-css
description: Website-building tips on "#css" sourced from real X posts via web search on 2026-07-08.
---

# Web dev tips: #css

Sourced by web-search indexing of public X posts on 2026-07-08 — `x.com` itself returns
HTTP 402 for direct, unauthenticated fetches (search pages, hashtag pages, even individual
status URLs), so this uses a general web search restricted to `site:x.com` rather than the
paid X API v2. Snippets are search-engine excerpts of real posts, sometimes truncated.

- **@Hartdrawss** (Harshil Tomar): "PRO TIP for FRONTEND DEVS: Replicate this Tailwind
  design system setup I use on every client project. Most vibe coded frontends have
  inconsistent spacing, random font sizes, and colors scattered everywhere — because
  [the AI tool] uses Tailwind defaults instead of a defined system." —
  [source](https://x.com/Hartdrawss/status/2042928242865172833)
- **@mizchi**, **@dotHTML5**, **@2020_hira**, **@souporserious**: independent posts
  converging on the same 2026 theme — CSS resets are getting *smaller*, not bigger, because
  modern-baseline browser support has eliminated most of the cross-browser quirks a heavy
  reset used to paper over. Worth revisiting any reset copied from a pre-2023 boilerplate. —
  [example](https://x.com/mizchi/status/2004955823265776101)

## Applied to Paladino

Skip a legacy CSS reset; a minimal modern-baseline reset plus the `:root` custom-property
palette in `docs/brand/README.md` is enough for `site/styles.css`.
