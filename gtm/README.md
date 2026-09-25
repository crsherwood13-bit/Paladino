# GTM outreach

`outreach-builder.html` is a single-file tool for "I did Y for you, happy to send it over"
outreach. Open it in a browser (no build step, no server).

1. Enter the prospect (name, company, role, sector, and optionally a "why now" trigger).
2. Pick what you built for them: trading comps, precedent deals, buyer universe, valuation
   range, add-on targets, sector update, refi benchmarks or deal teardown.
3. Write the one finding worth reading. Make it specific and give it a number.
4. Pick a tone (Direct, Warm, Ultra-short) and copy each message, or copy the full sequence.

It generates a six-touch sequence: email (Day 0) with alternate subject lines, a LinkedIn
connection note checked against the 300-character limit, a LinkedIn DM for when they accept,
a text for warm contacts, a Day 3 follow-up and a Day 10 last touch. Any empty field shows up
as a highlighted `[gap]` so a half-filled message is easy to spot before it goes out.

Drafts are saved in the browser's local storage only. Nothing is sent anywhere.

Ground rules: build the file before you send the message, use public information only (no
MNPI), and run anything that quotes numbers past compliance.

## Getting hired for GTM work

- `gtm-teardown.html` builds a one-page GTM teardown of a target company (pick 3 gaps from a
  checklist, write what you actually saw, and it adds the fix, a this-week action and a 30-day
  plan). It also writes the email, LinkedIn note and DM, a 90-second Loom script and a Day 3
  follow-up that offer the teardown. Switch between "A job there" and "Them as a client".
- `portfolio.html` is a one-page GTM portfolio to link from every message. Highlighted fields
  are placeholders for your own results and contact details.
