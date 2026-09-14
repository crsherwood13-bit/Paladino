#!/usr/bin/env python3
"""Pull web-dev / website-building tips from X (Twitter) and emit Claude Code skills.

Requires an X API v2 Bearer Token (Basic tier or above -- the Free tier has no
search access) in the X_BEARER_TOKEN environment variable. Use --dry-run to
exercise the pipeline against local fixtures with no network calls.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SEARCH_URL = "https://api.twitter.com/2/tweets/search/recent"
REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def slugify(text: str) -> str:
    text = text.strip().lstrip("#").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "topic"


def fetch_live(keyword: str, bearer_token: str, limit: int) -> list[dict]:
    query = f"({keyword}) -is:retweet lang:en"
    tweets: list[dict] = []
    next_token = None
    headers = {"Authorization": f"Bearer {bearer_token}"}

    while len(tweets) < limit:
        params = {
            "query": query,
            "max_results": str(min(100, max(10, limit - len(tweets)))),
            "tweet.fields": "author_id,created_at,public_metrics,entities",
            "expansions": "author_id",
            "user.fields": "username,name",
        }
        if next_token:
            params["next_token"] = next_token

        url = f"{SEARCH_URL}?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                payload = json.loads(resp.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"X API error {e.code} for query {query!r}: {body}") from e

        users_by_id = {u["id"]: u for u in payload.get("includes", {}).get("users", [])}
        for tweet in payload.get("data", []):
            author = users_by_id.get(tweet.get("author_id"), {})
            tweets.append(
                {
                    "id": tweet["id"],
                    "text": tweet["text"],
                    "created_at": tweet.get("created_at"),
                    "metrics": tweet.get("public_metrics", {}),
                    "author_username": author.get("username"),
                    "author_name": author.get("name"),
                }
            )
            if len(tweets) >= limit:
                break

        next_token = payload.get("meta", {}).get("next_token")
        if not next_token or len(tweets) >= limit:
            break
        time.sleep(1)  # stay well under rate limits between pages

    return tweets


def fetch_dry_run(keyword: str, limit: int) -> list[dict]:
    fixture_file = FIXTURES_DIR / "sample_tweets.json"
    if not fixture_file.exists():
        return []
    all_tweets = json.loads(fixture_file.read_text())
    matched = [t for t in all_tweets if keyword.lstrip("#").lower() in t["text"].lower()]
    return matched[:limit]


def write_skill(keyword: str, tweets: list[dict], output_dir: Path) -> Path:
    slug = slugify(keyword)
    skill_dir = output_dir / slug
    skill_dir.mkdir(parents=True, exist_ok=True)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    skill_md = skill_dir / "SKILL.md"

    lines = [
        "---",
        f"name: web-dev-tip-{slug}",
        f"description: Website-building tips on \"{keyword}\" sourced from X on {today}.",
        "---",
        "",
        f"# Web dev tips: {keyword}",
        "",
        f"Sourced from X (Twitter) search on {today}. Raw source data in `source.json`.",
        "",
    ]

    sorted_tweets = sorted(
        tweets, key=lambda t: t.get("metrics", {}).get("like_count", 0), reverse=True
    )
    for t in sorted_tweets:
        handle = f"@{t['author_username']}" if t.get("author_username") else "unknown"
        likes = t.get("metrics", {}).get("like_count", 0)
        text = " ".join(t["text"].split())
        lines.append(f"- **{handle}** ({likes} likes): {text}")

    skill_md.write_text("\n".join(lines) + "\n")
    (skill_dir / "source.json").write_text(json.dumps(tweets, indent=2))
    return skill_md


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--keywords",
        required=True,
        help="Comma-separated list of keywords/hashtags, e.g. '#webdev,#css,#frontend'",
    )
    parser.add_argument("--limit", type=int, default=50, help="Max tweets per keyword")
    parser.add_argument(
        "--output-dir", default=str(REPO_ROOT / "skills"), help="Where to write skill folders"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Use local fixtures instead of calling the X API"
    )
    args = parser.parse_args()

    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    if not keywords:
        parser.error("--keywords must include at least one term")

    bearer_token = os.environ.get("X_BEARER_TOKEN")
    if not args.dry_run and not bearer_token:
        print(
            "error: X_BEARER_TOKEN is not set. Export it or pass --dry-run to use fixtures.",
            file=sys.stderr,
        )
        return 1

    output_dir = Path(args.output_dir)
    seen_ids: set[str] = set()

    for keyword in keywords:
        print(f"Fetching tweets for {keyword!r}...")
        if args.dry_run:
            tweets = fetch_dry_run(keyword, args.limit)
        else:
            tweets = fetch_live(keyword, bearer_token, args.limit)

        deduped = [t for t in tweets if t["id"] not in seen_ids]
        seen_ids.update(t["id"] for t in deduped)

        if not deduped:
            print(f"  no results for {keyword!r}, skipping")
            continue

        skill_path = write_skill(keyword, deduped, output_dir)
        print(f"  wrote {len(deduped)} tweets -> {skill_path.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
