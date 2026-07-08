# Paladino

Website build pipeline for Paladino, a boutique investment banking / advisory firm.

## What's in here

- `scripts/ingest_x_skills.py` — pulls web-dev / website-building tips from the X (Twitter) API
  by keyword/hashtag search and converts them into Claude Code skill files under `skills/`.
- `skills/` — generated Claude Code skills (one per web-dev topic) produced by the ingestion script.
- `docs/ib-design-reference.md` — design patterns distilled from boutique/bulge-bracket investment
  banking websites, used as visual reference for the Paladino site.
- `docs/brand/` — Paladino brand assets (logo, palette, type system).
- `site/` — the Paladino website (static HTML/CSS), built from the brand assets and design reference.

Note: `skills/` currently reflects a `--dry-run` pull against the fixtures in
`scripts/fixtures/` — no `X_BEARER_TOKEN` has been provided yet, so no live X data has
been ingested. Re-run without `--dry-run` once a real Bearer Token is available to refresh
`skills/` from live search results.

## X API ingestion

Requires an X API v2 Bearer Token with read access (Basic tier or above — the Free tier does not
allow search). Set it as an environment variable, never commit it:

```bash
export X_BEARER_TOKEN="..."
python scripts/ingest_x_skills.py --keywords "#webdev,#css,#frontend" --limit 50
```

Run with `--dry-run` to exercise the pipeline against local fixtures instead of calling the live API.
