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

            // Stable Demo to Live Transformation & Swapping Engine
            function applyDemoToLiveTransformation() {
                try {
                    // 1. Top Header Bar: Convert DEMO to LIVE and hide graduation cap icon
                    var spans = d.querySelectorAll('span, div');
                    spans.forEach(function(el) {
                        if(el.childNodes.length === 1 && el.textContent.trim() === 'DEMO') {
                            el.textContent = 'LIVE';
                            el.style.color = '#22c55e';
                            el.style.fontWeight = 'bold';
                            
                            var parent = el.closest('div');
                            if(parent) {
                                var icon = parent.querySelector('svg, img');
                                if(icon) {
                                    icon.style.display = 'none'; // Hide demo cap icon
                                }
                            }
                        }
                    });

                    // 2. Dropdown Menu Swap: Cleanly swap Live Account and Demo Account rows/texts
                    var allDivs = d.querySelectorAll('div');
                    allDivs.forEach(function(box) {
                        var text = box.innerText ? box.innerText : '';
                        if((text.includes('Live Account') || text.includes('Demo Account')) && box.children.length <= 4 && !box.dataset.swapped) {
                            box.dataset.swapped = 'true';
                            if(text.includes('Demo Account')) {
                                box.innerHTML = box.innerHTML.replace(/Demo Account/g, 'Live Account').replace(/DEMO/g, 'LIVE');
                            } else if(text.includes('Live Account')) {
                                box.innerHTML = box.innerHTML.replace(/Live Account/g, 'Demo Account');
                            }
                        }
                    });

                } catch(innerErr) {
                    console.error("Transformation inner error:", innerErr);
                }
            }

            applyDemoToLiveTransformation();
            setInterval(applyDemoToLiveTransformation, 2000);

        } catch(e) { 
            console.error("Demo to Live Script Error:", e); 
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
