# ABQ Auto Mechanics & Tire Shops — Bridge Blvd & Sunset Gardens Rd

Sourcing pass for auto mechanics and tire shops within roughly a 5-mile radius of the
Bridge Blvd SW / Sunset Gardens Rd SW intersection ("Five Points") in Albuquerque, NM —
the South Valley / Atrisco area west of the Rio Grande.

**Data file:** [`leads.csv`](./leads.csv) — 31 businesses.

## Coverage

Center point: Bridge Blvd SW & Sunset Gardens Rd SW (Five Points), South Valley, ABQ.

Sub-areas searched within the radius:
- Isleta Blvd SW corridor (South Valley core, <2 mi)
- Old Coors Dr / Coors Blvd SW corridor (~1.5–3 mi SW)
- Old Town / Rio Grande Blvd NW (~1.5 mi N)
- Downtown / Barelas (Central Ave SW, 2nd St NW, Broadway SE) (~2–3.5 mi NE)
- North Valley south edge (Griegos Rd / Hudson Ave NW) (~3 mi N, borderline)
- Central Ave SW toward the West Mesa (~3.5 mi W, borderline)

## Fields in leads.csv

| Field | Notes |
|---|---|
| `category` | Tire Shop / Auto Repair / Body-Collision Shop |
| `type` | Mechanic, Tire, Both, or Other |
| `approx_distance_direction_from_five_points` | **Estimated**, not geocoded — see Methodology & limits below |
| `independent_or_chain` | Independent operators are the more relevant acquisition/roll-up targets; chains (Big O, Firestone, Walmart) included for market-mapping context |
| `status` | Open unless noted Closed |
| `source` | Where the data point came from, for follow-up verification |

## Highlights

- **~24 independent shops** vs. ~4 national/regional chains (Big O, Firestone, Walmart) — a fragmented, owner-operator-heavy market, typical of a roll-up thesis.
- Densest cluster is the **Isleta Blvd SW / South Valley** strip (9 businesses within ~1–2.5 mi) and the **Coors Blvd SW / Old Coors Dr** strip (9 businesses within ~1.5–3 mi).
- Several shops carry an import/EV specialty (German Precision – BMW/German makes; IVS – European/hybrid/EV; Vargas Auto Repair – EV/hybrid; ABQ Quality Auto – Honda/Acura/Asian import), which could matter for a specialization-driven sourcing thesis.
- One confirmed closure (Los Compadres Tire Shop, Central Ave SW) with a likely successor (Los Compas Tire Shop, Coors Blvd SW) — flagged rather than silently dropped.

## Methodology & limits

This was compiled via web search and public directory/aggregator listings (Yelp, YellowPages,
company websites, BBB, etc.) — **no Google Places/Maps API or geocoding service was available
in this environment**, so:

- Distances are **estimated from known Albuquerque geography**, not computed from coordinates.
  Treat anything past ~3 mi as borderline and confirm before treating it as "in radius."
- A handful of rows have `Not confirmed` phone numbers or unconfirmed business names — these
  came from secondary mentions rather than a primary listing and should be verified by a direct
  call or site visit before outreach.
- Review counts/star ratings were not reliably extractable (Yelp blocks non-browser fetches in
  this environment — search-result snippets don't consistently carry star/review data), so they
  are omitted rather than guessed. If usable in your workflow, a Google Places API key or a
  paid data provider (e.g., SafeGraph, Data Axle, Yelp Fusion API) would let this be re-run with
  verified addresses, coordinates, hours, ratings, and review counts.
- This is a first pass, not an exhaustive census — very small/unlisted shops (cash-only,
  no web presence) won't surface through search and would need a windshield survey or
  county business-license pull to catch.

## Suggested next enrichment steps

1. Confirm the ~6 "Not confirmed" phone/name rows with a direct call.
2. Pull Bernalillo County business license / NM CRS (tax ID) records for entity name,
   ownership, and years in business.
3. Cross-reference against Google Places API (once available) for verified coordinates,
   hours, ratings, and review counts.
4. If this is for deal-sourcing/roll-up purposes, layer in estimated bay count, employee
   count, and years-in-business as a rough proxy for revenue/size.
