const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for (const [src,out] of [['cms-roofing-gtm-packet.html','CMS-Roofing-GTM-Packet.pdf'],['cms-roofing-3-phase-plan.html','CMS-Roofing-3-Phase-Plan.pdf']]){
await p.goto('file://'+__dirname+'/'+src);
await p.pdf({path:__dirname+'/../'+out,format:'Letter',printBackground:true,displayHeaderFooter:true,
headerTemplate:'<span></span>',footerTemplate:'<div style="font-size:8px;color:#888;width:100%;padding:0 0.75in;display:flex;justify-content:space-between;font-family:Arial"><span>CMS Roofing &amp; Restoration · Charles Sherwood</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
margin:{top:'0.7in',bottom:'0.8in',left:'0.75in',right:'0.75in'}});}await b.close();})();
