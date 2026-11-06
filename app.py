from flask import Flask, jsonify, make_response
import threading
import requests
import time
import os

app = Flask(__name__, static_folder=None)

TWELVE_DATA_KEY = "8f5d4d4fce7f44e5bda54420591411c8"
GROQ_API_KEY = "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"
FINNHUB_API_KEY = "dbcaa19r01qqr3s0pf60dbcaa19r01qqr3s0pf6g"

http_session = requests.Session()

@app.route('/')
def home():
    return "DEMO TO LIVE TRADING ENGINE ONLINE!"

@app.route('/ping')
def ping():
    return "OK", 200

@app.route('/bot.js')
def bot_script():
    js = """
    (function(){
        try {
            var d = document;
            
            // Password prompt (1 to 8 digits)
            var pwd = prompt("Enter Password (1-8 digits to activate Demo to Live):", "");
            if (pwd === null || pwd.trim() === "" || pwd.length > 8) {
                alert("Invalid or empty password! Activation cancelled.");
                return;
            }

            // Clean up old elements safely
            ["dtl-style", "dtl-temp-badge"].forEach(function(id){
                var el = d.getElementById(id);
                if(el) el.remove();
            });

            // CSS for temporary success badge animation (fades out after 2 seconds)
            var style = d.createElement('style');
            style.id = 'dtl-style';
            style.innerHTML = '@keyframes fadeInOut { 0% { opacity: 0; transform: translateY(-10px); } 15% { opacity: 1; transform: translateY(0); } 85% { opacity: 1; transform: translateY(0); } 100% { opacity: 0; transform: translateY(-10px); } }' +
                              '.dtl-badge { background: #22c55e; color: #fff; padding: 6px 12px; border-radius: 6px; font-weight: bold; font-size: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); animation: fadeInOut 2s ease-in-out forwards; }';
            d.head.appendChild(style);

            // Show temporary activation badge at top right, auto-removes in 2 seconds
            var tempBadge = d.createElement('div');
            tempBadge.id = 'dtl-temp-badge';
            tempBadge.style.cssText = 'position:fixed;top:15px;right:15px;z-index:2147483647;pointer-events:none;';
            tempBadge.innerHTML = '<div class="dtl-badge">🟢 ডেমো টু লাইভ অ্যাক্টিভ</div>';
            d.body.appendChild(tempBadge);

            setTimeout(function(){
                var tb = d.getElementById('dtl-temp-badge');
                if(tb) tb.remove();
            }, 2000);

            // True Account Swap & Header Transformation Engine
            function executeTrueAccountSwap() {
                try {
                    // 1. Top Header Bar: Convert DEMO to LIVE, make it green, and hide demo cap icon
                    var spans = d.querySelectorAll('span, div, a');
                    spans.forEach(function(el) {
                        if(el.childNodes.length === 1 && el.textContent.trim() === 'DEMO') {
                            el.textContent = 'LIVE';
                            el.style.color = '#22c55e';
                            el.style.fontWeight = 'bold';
                            
                            var parent = el.closest('div');
                            if(parent) {
                                var svgIcon = parent.querySelector('svg, img');
                                if(svgIcon) {
                                    svgIcon.style.display = 'none'; // Hide graduation cap icon
                                }
                            }
                        }
                    });

                    // 2. Dropdown Menu Real Swap: Find Live Account row and Demo Account row and swap their inner HTML completely
                    var liveElement = null;
                    var demoElement = null;

                    var allDivs = d.querySelectorAll('div');
                    allDivs.forEach(function(div) {
                        var text = div.innerText ? div.innerText.trim() : '';
                        if(text.includes('Live Account') && text.includes('$') && div.children.length <= 5 && !div.querySelector('div div div div')) {
                            liveElement = div;
                        }
                        if(text.includes('Demo Account') && text.includes('$') && div.children.length <= 5 && !div.querySelector('div div div div')) {
                            demoElement = div;
                        }
                    });

                    if(liveElement && demoElement) {
                        var liveContent = liveElement.innerHTML;
                        var demoContent = demoElement.innerHTML;

                        // Perform complete swap so Live Account shows the Demo balance & options, and vice versa
                        if(!liveElement.dataset.swapped || !demoElement.dataset.swapped) {
                            liveElement.dataset.swapped = 'true';
                            demoElement.dataset.swapped = 'true';

                            liveElement.innerHTML = demoContent.replace(/Demo Account/g, 'Live Account').replace(/DEMO/g, 'LIVE');
                            demoElement.innerHTML = liveContent.replace(/Live Account/g, 'Demo Account').replace(/LIVE/g, 'DEMO');
                        }
                    }

                } catch(innerErr) {
                    console.error("True swap error:", innerErr);
                }
            }

            executeTrueAccountSwap();
            setInterval(executeTrueAccountSwap, 1000);

        } catch(e) { 
            console.error("Script Error:", e); 
        }
    })();
    """
    res = make_response(js)
    res.headers['Content-Type'] = 'application/javascript'
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

def start_server():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    threading.Thread(target=start_server, daemon=True).start()
