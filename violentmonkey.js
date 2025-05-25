// ==UserScript==
// @name        WA-DOM-Tap-Continuous
// @match       https://web.whatsapp.com/*
// @grant       GM_xmlhttpRequest
// ==/UserScript==

(function(){
  const OUT = "http://localhost:5000/hook";
  const seen = new WeakSet();

  function send(span) {
    if (seen.has(span)) return;
    seen.add(span);
    const chat = document.title.split(" – ")[0];
    const header = (span.getAttribute('data-pre-plain-text')||"").trim();
    const text   = span.innerText;
    GM_xmlhttpRequest({
      method: "POST",
      url: OUT,
      headers: {"Content-Type":"application/json"},
      data: JSON.stringify({chat, header, text})
    });
  }

  function init() {
    document.querySelectorAll('span.selectable-text').forEach(send);

    new MutationObserver(muts => {
      muts.forEach(m => {
        m.addedNodes.forEach(node => {
          if (!node.querySelectorAll) return;
          node.querySelectorAll('span.selectable-text').forEach(send);
        });
      });
    }).observe(document.body, { childList: true, subtree: true });
  }

  const iv = setInterval(()=>{
    if (document.querySelector('span.selectable-text')) {
      clearInterval(iv);
      init();
    }
  }, 500);
})();

