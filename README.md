# Paladino

Website build pipeline for Paladino, a boutique investment banking / advisory firm.

## What's in here

- `scripts/ingest_x_skills.py` — pulls web-dev / website-building tips from the X (Twitter) API
  by keyword/hashtag search and converts them into Claude Code skill files under `skills/`.
  Requires a paid Bearer Token (see below) — this path has not been exercised live yet.
- `skills/` — Claude Code skills (one per web-dev topic), currently hand-curated from real
  `site:x.com` web-search results rather than the script above (see "How `skills/` was
  actually built" below).
- `docs/ib-design-reference.md` — design patterns distilled from boutique/bulge-bracket investment
  banking websites, used as visual reference for the Paladino site.
- `docs/brand/` — Paladino brand assets (logo, palette, type system).
- `site/` — the Paladino website (static HTML/CSS), built from the brand assets and design reference.

## How `skills/` was actually built

`x.com` blocks unauthenticated automated access outright — every direct fetch (search
pages, hashtag pages, even individual status URLs) returns HTTP 402 Payment Required, not
just the official API. What does work without a paid token: general web search restricted
to `site:x.com`, which surfaces real indexed posts (often with the full tip text in the
snippet). The current `skills/*/SKILL.md` files were built that way — each entry links back
to the real post it came from. This is a manual/agent-driven method, not something
`scripts/ingest_x_skills.py` can do on its own (it only knows how to call the official API
or read local fixtures), so it hasn't been automated into the script.

## X API ingestion (official path, untested — needs a paid token)

Requires an X API v2 Bearer Token with read access (Basic tier or above — the Free tier does not
allow search). Set it as an environment variable, never commit it:

```bash
export X_BEARER_TOKEN="..."
python scripts/ingest_x_skills.py --keywords "#webdev,#css,#frontend" --limit 50
```

Run with `--dry-run` to exercise the pipeline against local fixtures instead of calling the live API.
