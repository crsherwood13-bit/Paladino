# Paladino

Website build pipeline for Paladino, a boutique investment banking / advisory firm.

## What's in here

- `scripts/ingest_x_skills.py` — pulls web-dev / website-building tips from the X (Twitter) API
  by keyword/hashtag search and converts them into Claude Code skill files under `skills/`.
- `skills/` — generated Claude Code skills (one per web-dev topic) produced by the ingestion script.
- `docs/ib-design-reference.md` — design patterns distilled from boutique/bulge-bracket investment
  banking websites, used as visual reference for the Paladino site.
- `docs/brand/` — Paladino brand assets (logo, palette, type system).
- `site/` — the actual Paladino website (added once brand assets + reference are in place).

## X API ingestion

Requires an X API v2 Bearer Token with read access (Basic tier or above — the Free tier does not
allow search). Set it as an environment variable, never commit it:

```bash
export X_BEARER_TOKEN="..."
python scripts/ingest_x_skills.py --keywords "#webdev,#css,#frontend" --limit 50
```

Run with `--dry-run` to exercise the pipeline against local fixtures instead of calling the live API.
