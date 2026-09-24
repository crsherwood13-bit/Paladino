import markdown, pathlib, re
d=pathlib.Path(__file__).resolve().parent.parent
t=(d/'cms-roofing-brief.md').read_text()
body=markdown.markdown(t, extensions=['tables','nl2br','sane_lists'])
# wrap header block
body=body.replace('<hr />','<hr>',)
css='''
@page{size:Letter;margin:0.9in 0.95in 0.9in}
:root{--ink:#1d2330;--muted:#5d6574;--rule:#d8d4cc;--accent:#8a2b22;--navy:#1a2744}
body{font-family:"Source Serif 4",Georgia,serif;color:var(--ink);font-size:11pt;line-height:1.55;background:#fff}
h1{font-family:"IBM Plex Sans",Arial,sans-serif;font-weight:600;font-size:22pt;color:var(--navy);margin:0 0 10pt;letter-spacing:-0.2px;text-wrap:balance}
h2{font-family:"IBM Plex Sans",Arial,sans-serif;font-weight:600;font-size:13.5pt;color:var(--navy);margin:20pt 0 6pt;break-after:avoid}
h3{font-family:"IBM Plex Sans",Arial,sans-serif;font-weight:600;font-size:11pt;color:var(--accent);margin:14pt 0 4pt;break-after:avoid}
p{margin:0 0 8pt;orphans:3;widows:3}
strong{font-weight:600}
h1+p{font-family:"IBM Plex Sans",Arial,sans-serif;font-size:9.5pt;color:var(--muted);line-height:1.5;border-bottom:1px solid var(--rule);padding-bottom:10pt;margin-bottom:12pt}
hr{border:0;border-top:1px solid var(--rule);margin:16pt 0}
ul{margin:0 0 8pt;padding-left:16pt}li{margin:0 0 4pt}
table{border-collapse:collapse;width:100%;margin:8pt 0 10pt;font-family:"IBM Plex Sans",Arial,sans-serif;font-size:9pt;break-inside:avoid}
th{text-align:left;font-weight:600;color:var(--muted);border-bottom:1.5px solid var(--navy);padding:5pt 4pt}
th:first-child,td:first-child{text-align:left}
td{text-align:left;padding:6pt 4pt;border-bottom:1px solid var(--rule);font-variant-numeric:tabular-nums}
td:first-child{font-weight:600}
em{font-style:italic}
'''
html=f'''<html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<style>{css}</style></head><body>{body}</body></html>'''
(d/'pdf/cms-roofing-brief.html').write_text(html)
