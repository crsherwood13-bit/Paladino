import re, markdown, pathlib
d=pathlib.Path(__file__).resolve().parent.parent
def load(n): return (d/n).read_text()
audit=load('cms-roofing-preliminary-gtm-audit.md')
a=audit.index('## 6. Still to verify'); b=audit.index('*Sources:')
audit=audit[:a]+audit[b:]
audit=audit.replace(' *(Mystery-shop test pending. See Section 6.)*',' *(A mystery-shop test will confirm response times.)*').replace('To check in the Google Ads Transparency Center and the Meta Ad Library.','Next step: review in the Google Ads Transparency Center and the Meta Ad Library.').replace('To run through PageSpeed Insights (mobile). The site is built on Duda.','Next step: PageSpeed Insights (mobile) test. The site is built on Duda.')
audit=audit.replace('**Date:** September 2026 (DRAFT)','**Prepared by:** Charles Sherwood · September 2026')
plan=load('cms-roofing-gtm-operating-plan.md').replace('**Status:** DRAFT. Builds on the Preliminary GTM Audit.','**Builds on:** the Preliminary GTM Audit')
sysd=load('cms-roofing-email-lifecycle-system.md').replace('**Status:** DRAFT v1. All copy is ready to load once the placeholders are filled.','**Note:** All copy is ready to load. Bracketed fields get filled with CMS\'s real data in Week 1.')
def md(t):
    # ensure lists after a paragraph line render
    t=re.sub(r'(?m)^(?!\s*[-*|>#\d])(.+)\n(- |\d+\. )', r'\1\n\n\2', t)
    return markdown.markdown(t, extensions=['tables','fenced_code','sane_lists','nl2br'])
cover='''<section class="cover"><div class="band"><div class="kicker">Prepared for Jaron Jaggers</div>
<h1>CMS Roofing &amp; Restoration</h1><div class="sub">Go-to-Market Audit, Operating Plan &amp; Sequence System</div></div>
<div class="toc"><div><b>Part 1</b> Preliminary GTM Audit</div><div><b>Part 2</b> GTM Operating Plan</div><div><b>Part 3</b> Email, SMS &amp; Sequence System</div></div>
<div class="by">Prepared by Charles Sherwood · September 2026<br>Based on public information. Real figures replace estimates once CMS data is reviewed.</div></section>'''
css='''@page{size:Letter;margin:0.75in 0.75in 0.8in}
body{font-family:Arial,Helvetica,sans-serif;color:#1f2430;font-size:10.5pt;line-height:1.45}
h1{color:#1a2744;font-size:21pt;margin:0 0 6pt;border-bottom:3px solid #c8962e;padding-bottom:6pt}
h2{color:#1a2744;font-size:14pt;margin:18pt 0 6pt;break-after:avoid}
h3{color:#1a2744;font-size:11.5pt;margin:12pt 0 4pt;break-after:avoid}
table{border-collapse:collapse;width:100%;margin:6pt 0 10pt;font-size:9pt;break-inside:auto}
tr{break-inside:avoid}th{background:#1a2744;color:#fff;text-align:left;padding:5pt}
td{border-bottom:1px solid #d9dce3;padding:5pt;vertical-align:top}tr:nth-child(even) td{background:#f5f6f9}
blockquote{margin:6pt 0 8pt;padding:6pt 10pt;border-left:3px solid #c8962e;background:#faf7f0;break-inside:avoid}
blockquote p{margin:3pt 0}
pre{background:#f5f6f9;padding:8pt;font-size:8.5pt;white-space:pre-wrap;border:1px solid #d9dce3}
hr{border:0;border-top:1px solid #d9dce3;margin:12pt 0}
.part{break-before:page}
.cover{height:9.3in;display:flex;flex-direction:column;justify-content:space-between}
.band{background:#1a2744;color:#fff;padding:48pt 36pt;margin-top:60pt}
.band h1{color:#fff;border:0;font-size:30pt}.kicker{color:#c8962e;font-weight:bold;letter-spacing:1px;text-transform:uppercase;font-size:10pt;margin-bottom:10pt}
.sub{font-size:14pt;color:#dfe3ec}.toc div{padding:8pt 0;border-bottom:1px solid #d9dce3;font-size:12pt}.toc b{color:#c8962e;display:inline-block;width:60pt}
.by{color:#5b6272;font-size:10pt}'''
def page(parts,cov,out):
    h=f'<html><head><meta charset="utf-8"><style>{css}</style></head><body>{cov}'
    for t in parts: h+=f'<section class="part">{md(t)}</section>'
    (d/out).write_text(h+'</body></html>')
phase=load('cms-roofing-3-phase-plan.md')
cover2=cover.replace('Go-to-Market Audit, Operating Plan &amp; Sequence System','3-Phase Growth Plan').replace('<div><b>Part 1</b> Preliminary GTM Audit</div><div><b>Part 2</b> GTM Operating Plan</div><div><b>Part 3</b> Email, SMS &amp; Sequence System</div>','<div><b>Phase 1</b> Base: data, KPIs &amp; the revenue story</div><div><b>Phase 2</b> Optimize current systems + AI</div><div><b>Phase 3</b> Outbound &amp; split testing vs. inbound</div>')
page([phase],cover2,'pdf/cms-roofing-3-phase-plan.html')
html=f'<html><head><meta charset="utf-8"><style>{css}</style></head><body>{cover}'
for t in (audit,plan,sysd): html+=f'<section class="part">{md(t)}</section>'
html+='</body></html>'
(d/'pdf/cms-roofing-gtm-packet.html').write_text(html)
