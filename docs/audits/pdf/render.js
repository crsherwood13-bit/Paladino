const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+__dirname+'/cms-roofing-gtm-packet.html');
await p.pdf({path:__dirname+'/../CMS-Roofing-GTM-Packet.pdf',format:'Letter',printBackground:true,displayHeaderFooter:true,
headerTemplate:'<span></span>',footerTemplate:'<div style="font-size:8px;color:#888;width:100%;padding:0 0.75in;display:flex;justify-content:space-between;font-family:Arial"><span>CMS Roofing &amp; Restoration · GTM Packet · Charles Sherwood</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
margin:{top:'0.7in',bottom:'0.8in',left:'0.75in',right:'0.75in'}});await b.close();})();
