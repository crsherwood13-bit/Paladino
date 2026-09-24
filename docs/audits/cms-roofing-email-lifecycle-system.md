# CMS Roofing & Restoration: Email, SMS & Sequence System

**Owner:** Charles Sherwood
**Status:** DRAFT v1. All copy is ready to load once the placeholders are filled.
**Companion docs:** Preliminary GTM Audit · GTM Operating Plan

---

## 0. The system on one page

| # | Sequence | Trigger | Audience | Channels | Length | Goal |
|---|---|---|---|---|---|---|
| 1 | **New inbound lead** | Form, missed call, LSA/Angi lead, chat | Homeowners & businesses who reached out | SMS, call, email | 5 days | Inspection booked in <24h |
| 1B | Booked-inspection confirmations | Appointment set | Same | SMS, email | Until inspection | Show rate 90%+ |
| 2A | **Lead went cold (never reached)** | Seq 1 ends with no contact | Unreached leads | Email, SMS | 30 days → monthly | Re-open the conversation |
| 2B | **Estimate not signed** | Estimate sent, not signed in 24h | Inspected, quoted | Email, SMS, call | 90 days → quarterly | Signed contract |
| 2C | Lost / not now | Marked lost or "not this year" | Quoted, said no | Email | 6 & 12 months | Second chance |
| 3A | **Outbound: commercial** | Added to list | Facility/property owners, low-slope roofs | Email, call, LinkedIn, mail | 21 days | Condition report booked |
| 3B | Outbound: property managers & investors | Added to list | Rental portfolios | Email, call, LinkedIn | 18 days | Portfolio walk / first job |
| 3C | Outbound: HOAs & association managers | Added to list | Boards & managers | Email, call, mail | 21 days | Reserve assessment booked |
| 3D | Outbound: referral partners | Added to list | Realtors, inspectors, insurance agents | Email, call, in person | 14 days | Referral agreement / first referral |
| 3E | Outbound: storm trigger | Hail/wind event in the area | Commercial + PM in affected zips | Email, call, drop-off | 7 days | Post-storm inspection |
| 4A | **Reactivation: past customers** | Scheduled / storm | 10,000+ past roofs | Email, SMS | Ongoing | Check-ups, add-ons, referrals |
| 4B | Reactivation: dead database | One-time blast, then quarterly | Every lead older than 90 days | Email, SMS | 3 touches | Revived conversations |
| 4C | Reactivation: old commercial accounts | One-time, then yearly | Past commercial jobs | Email, call | 14 days | Maintenance agreement |

**Rule for every sequence:** the moment someone replies, books, or signs, they exit the sequence and a human takes over.

---

## 1. Infrastructure (build before sending anything)

### Two sending lanes. Never mix them.

| | **Lane A: Warm** (inbound, customers, estimates, reactivation) | **Lane B: Cold** (outbound) |
|---|---|---|
| Sent from | Main domain `cmsroofing.com` | 2–3 separate look-alike domains, e.g. `cmsroofingky.com`, `trycmsroofing.com` *(check availability)*, each redirecting to cmsroofing.com |
| Tool | The CRM: whatever CMS already uses (JobNimbus, AccuLynx, etc.) if it can do automations; otherwise GoHighLevel | Instantly or Smartlead |
| Why | Protects the main domain's reputation so quotes and invoices land in the inbox | If a cold domain gets burned, the business email is untouched |

### Cold-lane setup checklist
- [ ] Buy 2–3 domains; 2–3 inboxes each (Google Workspace or Microsoft), real names (Jaron, commercial rep)
- [ ] SPF, DKIM, DMARC (`p=none` to start, move to `quarantine` after 30 days) on every domain, including cmsroofing.com
- [ ] Custom tracking domain; **open tracking OFF** for cold (plain text reads more human and delivers better)
- [ ] Warm up every inbox for 14–21 days before the first campaign
- [ ] Cap at **30–40 cold emails per inbox per day** → 6 inboxes ≈ 200/day ≈ 4,000/month
- [ ] Verify every list (MillionVerifier / NeverBounce); drop invalids; send catch-alls in a separate, smaller batch
- [ ] No images, no attachments, max one link (and none in email 1)
- [ ] Physical address + one-line opt-out in every email (CAN-SPAM)

### SMS setup
- [ ] Register A2P 10DLC (carriers block unregistered business texting)
- [ ] Add consent to the website form: *"By submitting, you agree to receive texts from CMS Roofing about your request. Msg & data rates may apply. Reply STOP to opt out."*
- [ ] Text only people who gave consent (inbound leads, customers). **No cold SMS.**
- [ ] Quiet hours: texts only 8am–8pm the recipient's local time *(have counsel confirm KY/TN rules)*

### Data & tracking
- [ ] CRM fields: `lead_source`, `service_type` (repair / replace / storm-insurance / commercial), `property_address`, `segment`, `sequence`, `angle_variant`, `estimate_amount`, `estimate_date`, `lost_reason`
- [ ] Every link has UTM parameters; every outbound campaign logs its angle
- [ ] Reply labels: Interested · Not now · Wrong person (get referral) · Not interested · Unsubscribe
- [ ] One booking calendar for inspections, by territory (Bowling Green / Owensboro)

### List sources
- County property records (PVA: Warren, Daviess, Barren, Simpson, Logan) → owner, property type, year built, square footage
- Apollo / Clay / Sales Navigator → contacts and titles
- Hail maps after every storm → affected zips and buildings
- The CMS database: past customers, old estimates, old leads

---

## 2. Testing framework

### Outbound angles we'll test

| Angle | What it is | Best for | Example first-line hook |
|---|---|---|---|
| **A. Clear offer / pitch** | State the offer and ask directly | Commercial owners who know they have a roof problem | "We'll inspect your roof and give you a written repair-vs-replace budget for next year, at no cost." |
| **B. Lead magnet** | Give something useful first; ask for nothing | Colder, busy decision-makers; HOAs | "Put together a 1-page guide on what flat-roof repairs cost in Kentucky in 2027. Want it?" |
| **C. Loom offer** | A 60–90 sec personalized video of *their* roof from aerial imagery | High-value commercial targets (big buildings, 15+ yr roofs) | "Recorded a quick video looking at the roof on {{property_address}} from the aerial view. Mind if I send it?" |
| **D. Proof / case study** | Lead with a real, similar job | Property managers, commercial owners | "We just finished [REAL JOB] for a [similar business] in {{city}}..." |
| **E. Trigger** | Tie to a real event: storm date, roof age, a sale | Post-storm; buildings 15+ years old | "The {{storm_date}} hail came right through {{zip}}..." |
| **F. Problem question** | One question about their pain; no pitch | Short, curiosity-led follow-ups | "Who handles roof leaks across your properties right now?" |

### Rules
1. **Test one thing at a time.** First the angle, then the subject line, then the CTA.
2. **Minimum sample before calling a winner:** about 250 delivered contacts per variant, per segment.
3. **Primary metric: positive reply rate** (interested replies ÷ delivered). Secondary: meetings booked, inspections done, pipeline $.
4. **Decision rules:**
   - Under 1% positive replies after 250 → kill the variant
   - 1–3% → keep and iterate the copy
   - Over 3% → scale it; becomes the control for the next test
5. **Log everything** in a shared sheet (template below).

### Test calendar (outbound, first 8 weeks of sending)

| Weeks | Test | Segments |
|---|---|---|
| 1–2 | Angle A vs B vs C (email 1 only) | Commercial |
| 1–2 | Angle A vs D | Property managers |
| 3–4 | Winning angle: subject line test (3 variants) | Commercial, PM |
| 3–4 | Angle B vs A | HOAs |
| 5–6 | CTA test: "worth a look?" vs "want me to send it?" vs specific time | All winners |
| 7–8 | Follow-up sequence test: 4 steps vs 6 steps | All winners |

### Inbound & lifecycle tests
| Test | A | B | Metric |
|---|---|---|---|
| First touch | Text first, call at +2 min | Call first, text if no answer | Contact rate within 1 hour |
| Booking | Send booking link | Offer 2 specific times | Inspections booked |
| Estimate follow-up | Financing angle first (Day 3) | Proof/warranty angle first (Day 3) | Estimates signed within 14 days |
| Reactivation subject | "Quick question" | "{{first_name}}, still thinking about the roof?" | Reply rate |

### Test log template
| Date | Segment | Sequence/step | Variable | Variant A | Variant B | Delivered (A/B) | Positive replies (A/B) | Meetings (A/B) | Winner | Next test |
|---|---|---|---|---|---|---|---|---|---|---|

---

## 3. Placeholders used in the copy

`{{first_name}}` · `{{company}}` · `{{property_address}}` · `{{city}}` · `{{zip}}` · `{{rep_name}}` · `{{rep_phone}}` · `{{booking_link}}` · `{{storm_date}}` · `{{estimate_amount}}` · `{{install_year}}`

**[BRACKETS]** = fill with real CMS facts. **Never** fill a proof slot with a job, number, or client that isn't real.

**Copy rules:** short; plain text; no "free!!!", "guarantee", "act now", "limited time", or ALL CAPS in cold email; name the number or date instead. No em dashes in any customer-facing line.

---

## 4. Sequence 1: New inbound lead

**Trigger:** web form, missed call, Google LSA, Angi/HomeAdvisor, chat, Facebook lead.
**Goal:** a human conversation in under 5 minutes; an inspection booked within 24 hours.
**Exit:** booked → Seq 1B. No contact after Day 5 → Seq 2A.

| When | Channel | Action |
|---|---|---|
| Instant | SMS | Text 1 |
| Instant | Email | Email 1 (confirmation) |
| +2 min | Call | Office/ISA calls. Round-robin; if no answer, voicemail script |
| +15 min | SMS | Text 2 (only if call not answered) |
| +2 hrs | Call | Call attempt 2 |
| Next day 8:15am | SMS + call | Text 3 + call attempt 3 |
| Day 2 | Email | Email 2 (what to expect + credentials) |
| Day 3 | Call | Call attempt 4, voicemail |
| Day 5 | SMS | Text 4 (last) |

**Text 1 (instant, business hours)**
> Hi {{first_name}}, this is {{rep_name}} with CMS Roofing. Got your request about {{property_address}}. I'm going to give you a quick call in the next couple minutes. If now's bad, just reply with a better time.

**Text 1 (after hours / weekend variant)**
> Hi {{first_name}}, it's CMS Roofing. Got your request. Our office opens at 8am and you're first on the list. If you have an active leak, reply LEAK and our on-call team will reach out tonight.

**Text 1 (storm variant, used when `service_type` = storm)**
> Hi {{first_name}}, {{rep_name}} with CMS Roofing. Sorry you're dealing with storm damage. We'll get someone out to document everything for your insurance. Calling you in a couple minutes.

**Email 1 (instant)**
Subject: Got your request, {{first_name}}
> Hi {{first_name}},
>
> Thanks for reaching out about {{property_address}}. {{rep_name}} is calling you shortly to set up your inspection.
>
> Want to pick a time yourself? {{booking_link}}
>
> What happens at the inspection: we check the roof, take photos of anything we find, and walk you through it. No pressure, and you'll get a written estimate either way.
>
> {{rep_name}}
> CMS Roofing & Restoration · {{rep_phone}}

**Voicemail script**
> Hi {{first_name}}, it's {{rep_name}} with CMS Roofing returning your request about your roof. I'll send you a text too, so reply there whenever's easy. Or call me back at {{rep_phone}}. Talk soon.

**Text 2 (+15 min, if no answer)**
> Just tried calling. What's a good time today or tomorrow for us to come take a look? Or grab a time here: {{booking_link}}

**Text 3 (next morning)**
> Morning {{first_name}}. Still want us to take a look at the roof? We have openings {{day_1}} and {{day_2}}. Which works?

**Email 2 (Day 2)**
Subject: What to expect from your roof inspection
> Hi {{first_name}},
>
> Quick rundown so you know what you're getting:
>
> 1. We inspect the whole roof and attic where we can, about 30–45 minutes.
> 2. You get photos of everything we find, good and bad.
> 3. You get a written estimate. If it's a storm claim, we help you with the insurance paperwork.
>
> About us: CMS has been roofing South Central Kentucky since 2006. We're GAF Master Elite (GAF's own figure is fewer than 2% of roofers) with a 25-year workmanship warranty.
>
> Pick a time here: {{booking_link}}
>
> {{rep_name}}

**Text 4 (Day 5, last)**
> Hi {{first_name}}, I don't want to keep bugging you. Should I close out your roof request, or do you still want an inspection? Just reply 1 to book or 2 to close it out.

### Sequence 1B: Inspection booked

**Confirmation (instant, SMS + email)**
> You're set, {{first_name}}. {{rep_name}} will be at {{property_address}} on {{date}} at {{time}}. You don't need to be on the roof or in the attic. We just need access to the property. Reply here if anything changes.

**Reminder (24 hours before, SMS)**
> Reminder: your CMS roof inspection is tomorrow at {{time}}. Reply C to confirm or R to reschedule.

**On the way (30–60 min before, SMS)**
> {{rep_name}} from CMS Roofing is on the way, about {{eta}} minutes out. [Photo of rep]

**Estimate delivered (same day as inspection, email)**
Subject: Your roof estimate for {{property_address}}
> Hi {{first_name}},
>
> Thanks for having us out. Your estimate and photos are attached / linked here: {{estimate_link}}
>
> Short version: [ONE-LINE SUMMARY FROM REP]
>
> Monthly payment options are available if that's easier than paying all at once. Just ask.
>
> Any questions, text me here. I'm happy to walk through it again.
>
> {{rep_name}}

---

## 5. Sequence 2: When an inbound lead dies

### 2A: Never reached (after Seq 1 ends)

**Goal:** re-open the conversation without being annoying. Monthly after Day 30.

**Day 7: Email**
Subject: Still need a roofer?
> Hi {{first_name}},
>
> We never connected on your roof request. Is it still something you need looked at?
>
> If so, reply with a good day and we'll make it work. If you already got it handled, no worries at all.
>
> {{rep_name}}, CMS Roofing

**Day 14: SMS**
> Hi {{first_name}}, CMS Roofing here. Still need someone to look at the roof at {{property_address}}? Reply YES and we'll set it up.

**Day 21: Email (helpful, not salesy)**
Subject: 3 signs your roof can wait (and 2 that can't)
> Hi {{first_name}},
>
> Not every roof issue is urgent. Quick guide:
>
> **Can usually wait:** a few granules in the gutters, minor fading, one lifted shingle with no leak.
> **Don't wait:** water stains on ceilings, or missing shingles after a storm. Insurance claims have time limits.
>
> If you're seeing either of the second two, reply and we'll get out there this week.
>
> {{rep_name}}

**Day 30: Email (last in sequence)**
Subject: Closing your file
> Hi {{first_name}},
>
> I'm going to close out your request so we stop reaching out. If the roof comes back up, just reply to this email and it comes straight to me.
>
> {{rep_name}}

**Then:** monthly newsletter list + storm alerts (Seq 4A storm message).

### 2B: Estimate not signed (the biggest money in the system)

**Trigger:** estimate sent, not signed within 24 hours.
**Goal:** signed contract. Rep gets a call task on Days 2, 7, and 14.
**Exit:** signed, lost (→ 2C), or 90 days → quarterly.

**Day 1: SMS (from the rep who inspected)**
> Hi {{first_name}}, it's {{rep_name}}. Wanted to make sure the estimate came through OK and see if any questions came up after you looked it over.

**Day 3: Email (test: financing angle vs. proof angle)**

*Variant A: Financing*
Subject: Your roof, paid monthly
> Hi {{first_name}},
>
> A lot of homeowners don't know this: you don't have to pay for a roof all at once. On your estimate of {{estimate_amount}}, monthly options can start around [$X/MONTH, FROM FINANCING PARTNER].
>
> Want me to send the details? Takes about 5 minutes to see if you qualify, and it won't affect your credit score to check. [CONFIRM WITH FINANCING PARTNER]
>
> {{rep_name}}

*Variant B: Proof*
Subject: What you're getting for {{estimate_amount}}
> Hi {{first_name}},
>
> When you compare quotes, here's what's included in ours that often isn't elsewhere:
>
> - 25-year workmanship warranty, backed by GAF
> - GAF Master Elite installation (fewer than 2% of roofers qualify, per GAF)
> - [REAL DETAIL: e.g. full tear-off, ice & water shield, cleanup/magnet sweep]
> - Local since 2006, so we'll be here if you ever need us
>
> Happy to go line by line against any other quote you have.
>
> {{rep_name}}

**Day 7: Call + SMS if no answer**
> Hi {{first_name}}, tried calling. Is there anything holding you back on the roof? Sometimes it's price, sometimes timing, sometimes you just need to talk to someone at home. Whatever it is, I can probably help.

**Day 14: Email (the "which one" email)**
Subject: Quick question on your roof
> Hi {{first_name}},
>
> Just want to know where you're at so I stop guessing. Which one is closest?
>
> 1. Still deciding, need more time
> 2. Price is the issue
> 3. Went with someone else
> 4. Not doing the roof this year
>
> Just reply with the number. No hard feelings on any of them.
>
> {{rep_name}}

*Routing:* 1 → continue · 2 → rep calls with options (financing, phased repair, material options) · 3 → Seq 2C, ask why · 4 → Seq 2C, 6-month check-in

**Day 30: Email (timing)**
Subject: Before the weather turns
> Hi {{first_name}},
>
> Our schedule for [MONTH/SEASON] is filling up. If you want the roof done before [winter / spring storm season], now's about the time to lock it in.
>
> Your estimate for {{property_address}} is still good through [DATE]. [CONFIRM ESTIMATE VALIDITY POLICY]
>
> {{rep_name}}

**Day 60: SMS**
> Hi {{first_name}}, {{rep_name}} with CMS. Checking in on the roof. Anything change on your end? Happy to update the estimate if needed.

**Day 90: Email (last, then quarterly)**
Subject: Should I keep your estimate on file?
> Hi {{first_name}},
>
> It's been a few months since we looked at your roof. I'll keep your photos and estimate on file. If anything changes, like a leak or a storm, reply here and we'll prioritize you.
>
> {{rep_name}}

### 2C: Lost or "not now"

**Lost to a competitor (immediately): Email**
Subject: Thanks for considering us
> Hi {{first_name}},
>
> Thanks for letting me know. Mind telling me in one line what made the difference? Price, timing, something we did? It genuinely helps us get better.
>
> And if anything ever comes up with the new roof, we're around.
>
> {{rep_name}}

**Not now (6 months): Email**
Subject: Checking back on the roof
> Hi {{first_name}},
>
> Six months ago you mentioned the roof could wait. Just checking in. Want us to come back out and see if anything's changed? Takes 30 minutes, no cost.
>
> {{rep_name}}

**Not now (12 months): Email.** Same as above with "a year ago."

---

## 6. Sequence 3: Outbound

All outbound runs from the cold lane (Section 1). Plain text. Sender: Jaron (commercial and HOA), or the commercial rep once hired.

### 3A: Commercial facility & property owners (low-slope/flat roofs)

**Target:** owners and facility managers of industrial, warehouse, retail, church, school, medical, and dealership buildings, 10,000+ sq ft, roof 12+ years old where known.
**Titles:** Facilities Manager/Director, Plant Manager, Maintenance Manager, Operations Manager, Property Manager, Business Administrator, Owner/President (smaller firms).
**Offer:** free roof condition report: photos, remaining-life estimate, and a written repair-vs-replace budget.
**Goal:** book the condition report.

| Day | Channel | Step |
|---|---|---|
| 1 | Email | Email 1 (angle test A / B / C) |
| 2 | LinkedIn | Connection request (no note or a short note) |
| 3 | Call | Call 1, voicemail |
| 5 | Email | Email 2 (reply in same thread) |
| 8 | Call | Call 2 |
| 10 | Email | Email 3 (proof or question) |
| 14 | Mail/drop | Printed 1-page "roof budget guide" + card, or a drop-off by the rep for local targets |
| 17 | Email | Email 4 (new thread, new angle) |
| 21 | Email | Email 5 (breakup) |

**Email 1, Variant A: Clear offer**
Subject: roof at {{property_address}}
> Hi {{first_name}},
>
> We're a Versico-certified commercial roofer based in Bowling Green. For buildings like {{company}}'s, we do a roof condition report: photos of every problem area, how many years the roof has left, and a written repair-vs-replace budget you can plan next year around.
>
> There's no cost, and we'd work around your schedule.
>
> Worth doing for your building?
>
> Jaron Jaggers
> CMS Roofing & Restoration
> [ADDRESS] · Reply "no thanks" and I won't follow up.

**Email 1, Variant B: Lead magnet**
Subject: flat roof costs in 2027
> Hi {{first_name}},
>
> I put together a 1-page guide on what commercial roof repairs and replacements actually cost in Kentucky right now, and the 4 signs a flat roof has 2–3 years left versus 10.
>
> Useful for budgeting next year. Want me to send it over?
>
> Jaron Jaggers
> CMS Roofing & Restoration

**Email 1, Variant C: Loom offer**
Subject: video of your roof
> Hi {{first_name}},
>
> I pulled up {{company}}'s building on aerial imagery and recorded a quick 90-second video pointing out a couple of things I'd want a closer look at on the roof.
>
> Mind if I send it over?
>
> Jaron Jaggers
> CMS Roofing & Restoration

*(Only send Variant C when the Loom is recorded or can be recorded within 24 hours of a yes. Script in Section 8.)*

**Email 2 (Day 5, same thread)**
> Hi {{first_name}}, following up on this. Is roof maintenance something you handle at {{company}}, or is there someone else I should talk to?

**Email 3 (Day 10, same thread): proof**
> Hi {{first_name}},
>
> For context, we recently [REAL COMMERCIAL JOB: e.g. "replaced a 40,000 sq ft roof for a manufacturer in Warren County with the plant running the whole time"]. The condition report is how that started.
>
> Would a report on your building be useful before next year's budget is set?

*(No real commercial job to cite yet? Use this instead:)*
> Most flat-roof replacements we see could have been pushed out 5+ years with $[X] of repairs done early. The condition report tells you which camp your roof is in. Worth a look?

**Call script (Days 3 and 8)**
> "Hi {{first_name}}, it's Jaron with CMS Roofing in Bowling Green. I sent you a note about a roof condition report for your building. Did I catch you at an OK time for 30 seconds?"
>
> *If yes:* "We do these for commercial buildings around here. Photos, how much life the roof has left, and a written budget. Takes about an hour on-site and there's no cost. Is the roof something that's on your radar, or has it been pretty quiet?"
>
> *If "we have a roofer":* "Makes sense. A lot of the reports we do are a second opinion before a big spend. If you ever want one, I'm easy to find."
>
> *Voicemail:* "Hi {{first_name}}, Jaron with CMS Roofing, 270-843-5405. Sent you a note about a roof condition report for your building. I'll follow up by email."

**LinkedIn note (optional)**
> Hi {{first_name}}, I run commercial roofing at CMS here in Bowling Green. Always good to know the facilities folks in the area.

**Email 4 (Day 17, new thread): trigger or question angle**
Subject: who handles leaks?
> Hi {{first_name}},
>
> When a leak shows up at {{company}}, who gets the call? Is it you, or an outside maintenance company?
>
> Asking because we set up maintenance plans for buildings here so leaks get handled the same week, not whenever a crew frees up.

**Email 5 (Day 21): breakup**
Subject: closing the loop
> Hi {{first_name}},
>
> I'll stop reaching out after this one. If the roof ever becomes a priority, like a leak or a budget question, just reply here and I'll get you a condition report within the week.
>
> Jaron

### 3B: Residential property managers & investors

**Target:** property management companies; investors with 5+ doors (from PVA multi-parcel owners).
**Titles:** Owner/Broker, Property Manager, Maintenance Coordinator, Asset Manager.
**Offer:** priority leak response + a portfolio roof check + volume pricing on replacements.

| Day | Channel | Step |
|---|---|---|
| 1 | Email | Email 1 (A: clear offer vs D: proof) |
| 3 | Call | Call 1 |
| 5 | Email | Email 2 |
| 9 | Email | Email 3 |
| 12 | Call | Call 2 |
| 18 | Email | Email 4 (breakup) |

**Email 1, Variant A: Clear offer**
Subject: roofs across your rentals
> Hi {{first_name}},
>
> For property managers around Bowling Green, we do two things:
>
> 1. When a tenant reports a leak, we're there within [48 HOURS: CONFIRM CMS CAN COMMIT].
> 2. Once a year, we check every roof in your portfolio and give you one list: what's fine, what needs a repair, what needs replacing and when.
>
> Worth a quick call to see if it fits how you run things?
>
> Jaron Jaggers, CMS Roofing & Restoration

**Email 1, Variant D: Proof**
Subject: {{city}} rentals
> Hi {{first_name}},
>
> [REAL EXAMPLE: e.g. "We handle roofs for [X] rental properties for a local owner"]. Most of the work is small repairs caught early, which keeps tenants happy and replacements off the calendar.
>
> Open to doing the same for your properties?
>
> Jaron

**Email 2 (Day 5)**
> Hi {{first_name}}, bumping this up. How are you handling roof leaks across your properties right now? One go-to roofer, or whoever's available?

**Email 3 (Day 9)**
> Hi {{first_name}}, one more idea. If you have a property with a roof you're unsure about, send me the address. We'll look at it this week at no cost, and you'll see how we work before committing to anything.

**Email 4 (Day 18): breakup**
> Hi {{first_name}}, I'll leave it here. If a leak or a roof question comes up on any of your properties, reply and I'll get someone out fast.

### 3C: HOAs & association managers

**Target:** HOA/condo boards with shared roofs; community association management companies.
**Titles:** Board President, Treasurer, Community Association Manager (CAM), Property Manager.
**Offer:** roof reserve assessment: which buildings need what, and when, in dollars, for the reserve budget.

**Email 1, Variant B: Lead magnet (expected winner for boards)**
Subject: roof reserves for {{community_name}}
> Hi {{first_name}},
>
> Most HOA roof surprises come from a reserve budget built on guesses. We put together a simple 1-page checklist boards use to sanity-check their roof reserves.
>
> Want me to send it?
>
> Jaron Jaggers, CMS Roofing & Restoration

**Email 1, Variant A: Clear offer**
Subject: roof reserve assessment
> Hi {{first_name}},
>
> We do roof reserve assessments for associations: every building inspected, photos, and a year-by-year budget for repairs and replacement. Boards use it to set reserves and avoid special assessments.
>
> There's no cost for the assessment. Would that be useful before your next budget meeting?
>
> Jaron

**Email 2 (Day 5)**
> Hi {{first_name}}, following up. When does {{community_name}}'s board usually set next year's budget? The assessment is most useful a month or two before that.

**Email 3 (Day 12)**
> Hi {{first_name}}, if you manage more than one community, happy to start with whichever one has the oldest roofs. You'd see exactly what the report looks like before deciding on the others.

**Mail (Day 14):** printed reserve checklist + cover letter addressed to the board.

**Email 4 (Day 21): breakup**
> Hi {{first_name}}, I'll close this out. If the board ever wants a roof assessment ahead of a budget cycle, just reply here.

### 3D: Referral partners

**Realtors & home inspectors**
**Offer:** fast roof certifications and pre-listing repairs so deals don't stall.

**Email 1**
Subject: roofs holding up closings
> Hi {{first_name}},
>
> When an inspection flags the roof on one of your deals, how long does it usually take to get a roofer out?
>
> We turn around roof inspections and certification letters in [X DAYS: CONFIRM], and repairs before closing when needed. Figured that might save you a delayed closing or two.
>
> Want to be on our quick-response list?
>
> Jaron, CMS Roofing

**Email 2 (Day 4)**
> Hi {{first_name}}, easiest way to try us: next time a roof comes up on an inspection report, send me the address and I'll show you how fast we move.

**Call + drop-in (Day 7):** stop by the brokerage with a one-page "roof issues on inspection reports: what's a deal-breaker and what's not" sheet.

**Email 3 (Day 14): breakup**
> Hi {{first_name}}, I'll leave you my number, 270-843-5405. Anytime a roof holds up a deal, call or text me directly.

**Insurance agents**
**Email 1**
Subject: roof claims for your clients
> Hi {{first_name}},
>
> When a client of yours has storm damage, who do you point them to?
>
> We document damage the way adjusters need it, handle the paperwork with the carrier, and we're GAF Master Elite and a FORTIFIED provider. Some carriers offer better terms on FORTIFIED roofs. [VERIFY WHICH CARRIERS IN KY]
>
> Open to being a name you can hand clients?
>
> Jaron, CMS Roofing

Follow-ups: same pattern as realtors (Day 4 email, Day 7 drop-in, Day 14 breakup).

### 3E: Storm trigger (runs within 72 hours of a hail/wind event)

**Target:** commercial buildings and property managers in affected zips (hail map).

**Email 1 (within 48 hours)**
Subject: {{storm_date}} storm, {{zip}}
> Hi {{first_name}},
>
> The {{storm_date}} storm hit {{zip}} with [HAIL SIZE / WIND SPEED FROM REPORT]. Damage on flat and low-slope roofs often isn't visible from the ground, and most policies have a time limit to file.
>
> We're doing post-storm inspections for buildings in the area this week: photos and a written summary you can hand to your insurance. Want us to add {{company}}?
>
> Jaron, CMS Roofing

**Email 2 (Day 3)**
> Hi {{first_name}}, we still have a few slots this week for {{zip}}. Reply with a good day and we'll document the roof for you.

**Day 4–5:** rep drop-off with a door hanger/card, and a call.

**Email 3 (Day 7): last**
> Hi {{first_name}}, last note on this. If you notice any leaks or damage in the next few weeks, reply here and we'll prioritize you.

*(Only claim storm details that are verifiable from a hail/wind report.)*

---

## 7. Sequence 4: Reactivation

All from the warm lane (cmsroofing.com / CRM). Past customers already know CMS, so this is the cheapest revenue in the system.

### 4A: Past customers

**Annual roof check-up (every spring, SMS + email)**
Subject: Your yearly roof check-up
> Hi {{first_name}},
>
> It's been a while since we put your roof on in {{install_year}}. We're doing spring check-ups for past customers: a quick look for loose flashing, clogged gutters, and storm wear, at no cost.
>
> Want us to add you to the schedule? Reply YES.
>
> CMS Roofing

**Post-storm check (within 48 hours of a storm in their area, SMS)**
> Hi {{first_name}}, CMS Roofing here. That storm on {{storm_date}} came through your area. If you see any damage or leaks, reply and we'll prioritize you as a past customer.

**Referral ask (30 days after install, email)**
Subject: Know anyone who needs a roof?
> Hi {{first_name}},
>
> Hope the new roof is treating you well. If you know a neighbor, friend, or family member who needs roof work, send them our way. As a thank-you, we'll send you [REFERRAL REWARD: e.g. $X gift card] when their job is done.
>
> Just have them mention your name, or reply here with their info.
>
> CMS Roofing

*(Check KY rules on referral rewards; keep it simple and legal.)*

**Cross-sell: gutters & siding (60–90 days after install, and yearly)**
Subject: Gutters that match the new roof
> Hi {{first_name}},
>
> A lot of our roof customers add new seamless gutters or siding once the roof's done so everything matches and drains right. If that's on your list, we can give you a quote at the same visit as your check-up.
>
> Reply GUTTERS or SIDING and we'll set it up.

**Warranty anniversary (at 5 and 10 years)**
Subject: Your roof warranty, 5 years in
> Hi {{first_name}},
>
> Your roof turned 5 this year. Quick reminder that your 25-year workmanship warranty is still active. If anything looks off, reply here and we'll come check it under warranty.

### 4B: Dead database (every lead older than 90 days that never bought)

**Touch 1: the 9-word email** (plain text, from a real person)
Subject: roof
> Hi {{first_name}}, are you still looking to get your roof looked at?
>
> {{rep_name}}

**Touch 2: SMS (Day 3, consented contacts only)**
> Hi {{first_name}}, it's {{rep_name}} at CMS Roofing. A while back you asked about your roof. Still something you need help with?

**Touch 3: Email (Day 10)**
Subject: new options since we last talked
> Hi {{first_name}},
>
> Since you last reached out, we've added [REAL CHANGE: e.g. monthly payment options / FORTIFIED roofs / a new crew for faster scheduling].
>
> If the roof's still on your list, reply and we'll get you on the schedule.

**Then:** quarterly re-run of Touch 1 with a new subject line.

### 4C: Old commercial accounts

**Email 1**
Subject: {{company}} roof, [X] years in
> Hi {{first_name}},
>
> We did the roof at {{property_address}} back in {{install_year}}. Flat roofs last a lot longer with a yearly check and small repairs, so we're offering past commercial customers a maintenance plan: [2 INSPECTIONS/YEAR + PRIORITY LEAK RESPONSE + REPORT FOR YOUR RECORDS: CONFIRM TERMS].
>
> Want me to send the details?
>
> Jaron

**Day 5 call → Day 14 breakup email** (same pattern as 3A).

---

## 8. Supporting assets

### Loom script (60–90 seconds, for outbound Variant C)
1. **(0–10s)** "Hi {{first_name}}, Jaron with CMS Roofing. I pulled up {{company}}'s building to take a quick look."
2. **(10–50s)** Share the aerial view (Google Earth, Nearmap, or EagleView). Point out 2–3 *real, visible* things: ponding areas, patched sections, discoloration, HVAC curbs, drainage. Say "worth a closer look," never "you have damage," since you can't confirm from aerial imagery.
3. **(50–75s)** "The only way to know for sure is to get on it. We do a condition report: photos, how much life it has left, and a written budget. No cost."
4. **(75–90s)** "If that's useful, just reply to the email and we'll find a time. Thanks, {{first_name}}."

### Lead magnets to build (1 page each, PDF, CMS branding)
| Asset | For | Contents |
|---|---|---|
| **Commercial Roof Budget Guide (KY, 2027)** | 3A | Cost ranges for repair / coating / re-roof by type [FROM CMS REAL PRICING]; 4 signs of remaining life; when to repair vs. replace |
| **HOA Roof Reserve Checklist** | 3C | 8 questions to sanity-check reserves; typical lifespans by roof type; a sample 10-year schedule |
| **Roof Issues on Inspection Reports** | 3D realtors | What's a deal-breaker vs. a quick fix; typical turnaround times |
| **Storm Damage Checklist** | Inbound, 3E, 4A | What to photograph; claim deadlines to check with your carrier; what not to sign |

### Condition report template (the actual offer deliverable)
Cover page · building details · roof type/age · photo log with notes · issues ranked (urgent / 1–2 years / monitor) · remaining-life estimate · repair budget vs. replacement budget · recommended next step. Delivered in person when possible.

---

## 9. Rollout

| Week | Build |
|---|---|
| 1 | Access to CRM + phone system; export and clean the database; buy cold domains and start warmup; A2P registration |
| 2 | Load Seq 1 + 1B (inbound) and turn on; form consent + fields; booking calendar |
| 3 | Load Seq 2A + 2B + 2C; launch 4B dead-database blast (warm lane) |
| 4 | Build lead magnets + condition report template; pull first commercial and PM lists; record first Looms |
| 5 | Cold domains warm → launch 3A (angle test A/B/C) and 3B (A/D) |
| 6 | Launch 4A past-customer program (check-ups + referral); 3D referral partners |
| 7 | Launch 3C HOAs; storm playbook (3E) ready to fire |
| 8 | First test readout → pick winners, write next variants; monthly review with Jaron |

### What we track weekly
| Area | Metric | Early target *(set real targets after Day 14 baseline)* |
|---|---|---|
| Inbound | Median speed-to-lead | Under 5 minutes, business hours |
| Inbound | Lead → inspection booked | Baseline, then +[X]% |
| Estimates | Unsold-estimate recovery | Signed jobs and $ from Seq 2B |
| Outbound | Positive reply rate by angle | 2–5% is healthy for cold B2B |
| Outbound | Condition reports / meetings booked | [X] per week |
| Reactivation | Replies, check-ups booked, referrals received | Baseline |
| All | Pipeline $ and signed $ by sequence | The number that matters |

---

## 10. Guardrails

- **No fake proof.** Every bracketed proof slot gets a real job or gets cut. Don't name a client without permission.
- **Aerial ≠ inspection.** Never claim damage from imagery. Say "worth a closer look."
- **Storm claims:** only cite hail sizes and dates from a real weather report. Don't promise insurance outcomes.
- **Consent:** texts only to people who opted in; honor STOP immediately; unsubscribe link or line in every email.
- **One human owner per reply.** Automation starts conversations; people finish them.
