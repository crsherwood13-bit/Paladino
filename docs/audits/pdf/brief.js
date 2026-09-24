const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch({proxy:process.env.HTTPS_PROXY?{server:process.env.HTTPS_PROXY}:undefined});const p=await b.newPage({ignoreHTTPSErrors:true});
await p.goto('file://'+__dirname+'/cms-roofing-brief.html',{waitUntil:'networkidle'});
const f=await p.evaluate(async()=>{await document.fonts.ready;return [document.fonts.check('12px "Source Serif 4"'),document.fonts.check('12px "IBM Plex Sans"')]});console.log('fonts',f);
await p.pdf({path:__dirname+'/../CMS-Roofing-Brief.pdf',format:'Letter',printBackground:true,displayHeaderFooter:true,headerTemplate:'<span></span>',
footerTemplate:'<div style="font-size:7.5px;color:#8a8f99;width:100%;padding:0 0.95in;display:flex;justify-content:space-between;font-family:Arial"><span>CMS Roofing · Charles Sherwood</span><span><span class="pageNumber"></span></span></div>',
margin:{top:'0.8in',bottom:'0.85in',left:'0.95in',right:'0.95in'}});
await p.setViewportSize({width:816,height:1056});await p.emulateMedia({media:'print'});await p.screenshot({path:process.env.S+'/brief1.png'});
await p.evaluate(()=>[...document.querySelectorAll('h3')][2].scrollIntoView());await p.screenshot({path:process.env.S+'/brief2.png'});
await b.close();})();
