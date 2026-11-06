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
            
            // Password prompt (1 to 8 characters/digits)
            var pwd = prompt("Enter Password (1-8 digits to activate Demo to Live):", "");
            if (pwd === null || pwd.trim() === "" || pwd.length > 8) {
                alert("Invalid or empty password! Activation cancelled.");
                return;
            }

            // Clean up old elements if any
            ["demo-to-live-style", "demo-to-live-indicator"].forEach(function(id){
                var el = d.getElementById(id);
                if(el) el.remove();
            });

            // CSS for Live indicator badge
            var style = d.createElement('style');
            style.id = 'demo-to-live-style';
            style.innerHTML = '@keyframes livePulse { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }' +
                              '.demo-to-live-badge { background: #22c55e; color: #fff; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 11px; animation: livePulse 2s infinite; }';
            d.head.appendChild(style);

            // DOM Manipulation: Demo to Live transformation
            function transformDemoToLive() {
                var modified = false;

                // Find account switcher elements or balance containers in Quotex UI
                var selectors = [
                    '.cabinet-user__type', '.account__type', '[class*="account-type"]', 
                    '[class*="cabinet-user"]', '.va-account', '.live-account', '.demo-account',
                    'span', 'div', 'button'
                ];

                for(var i = 0; i < selectors.length; i++) {
                    var elements = d.querySelectorAll(selectors[i]);
                    for(var j = 0; j < elements.length; j++) {
                        var el = elements[j];
                        var txt = el.innerText ? el.innerText.trim().toUpperCase() : '';
                        
                        // If it indicates Demo, swap or morph visual text/class to Live while keeping underlying demo functionality
                        if(txt === 'DEMO' || txt === 'DEMO ACCOUNT' || txt === 'ডেমো') {
                            el.innerText = 'LIVE';
                            el.style.color = '#22c55e';
                            modified = true;
                        }
                    }
                }

                // Add a small status indicator on screen
                if(!d.getElementById('demo-to-live-indicator')) {
                    var indicator = d.div ? d.div : d.createElement('div');
                    // Let's create a subtle fixed badge
                    var badge = d.createElement('div');
                    badge.id = 'demo-to-live-indicator';
                    badge.style.cssText = 'position:fixed;top:10px;right:10px;z-index:2147483647;';
                    badge.innerHTML = '<span class="demo-to-live-badge">🟢 LIVE MODE (DEMO ENGINE)</span>';
                    d.body.appendChild(badge);
                }

                console.log("Demo to Live Transformation Applied Successfully.");
            }

            // Run transformation immediately and periodically to catch dynamic UI re-renders
            transformDemoToLive();
            setInterval(transformDemoToLive, 1500);

            alert("Success! Demo account display successfully converted to Live mode.");

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
