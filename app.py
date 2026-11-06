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

            // Clean up old elements if any
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

            // DOM Transformation: Deep Swap & Live Conversion Engine
            function transformDemoToLiveComplete() {
                // 1. Transform Top Header DEMO to LIVE
                var allEls = d.querySelectorAll('span, div, a');
                for(var i = 0; i < allEls.length; i++) {
                    var el = allEls[i];
                    if(el.childNodes.length === 1 && el.textContent.trim() === 'DEMO') {
                        el.textContent = 'LIVE';
                        el.style.color = '#22c55e';
                        el.style.fontWeight = 'bold';
                        
                        // Try to update icon if graduation cap exists nearby
                        var parentContainer = el.closest('div');
                        if(parentContainer) {
                            var svgIcon = parentContainer.querySelector('svg, img');
                            if(svgIcon) {
                                svgIcon.style.filter = 'hue-rotate(90deg)';
                            }
                        }
                    }
                }

                // 2. Dropdown Menu: Swap Live Account and Demo Account blocks / contents
                var liveAccTextEls = [];
                var demoAccTextEls = [];

                var allDivs = d.querySelectorAll('div, section, article');
                for(var j = 0; j < allDivs.length; j++) {
                    var box = allDivs[j];
                    var txt = box.innerText ? box.innerText : '';
                    if(txt.includes('Live Account') && box.children.length < 5) {
                        liveAccTextEls.push(box);
                    }
                    if(txt.includes('Demo Account') && box.children.length < 5) {
                        demoAccTextEls.push(box);
                    }
                }

                // If dropdown elements are found, swap their text/values visually
                if(liveAccTextEls.length > 0 && demoAccTextEls.length > 0) {
                    // Swap inner HTML or content structure to achieve top/bottom swap
                    liveAccTextEls.forEach(function(liveBox) {
                        demoAccTextEls.forEach(function(demoBox) {
                            // If they are distinct row containers, swap their inner contents or labels
                            var liveVal = liveBox.innerHTML;
                            var demoVal = demoBox.innerHTML;
                            
                            if(liveVal.includes('$0.00') && demoVal.includes('$')) {
                                // Swap contents so Demo balance & system goes to Live position and vice-versa
                                liveBox.innerHTML = demoVal.replace(/Demo Account/g, 'Live Account');
                                demoBox.innerHTML = liveVal.replace(/Live Account/g, 'Demo Account');
                            }
                        });
                    });
                }

                // General replacement for any leftover labels
                var walker = d.createTreeWalker(d.body, NodeFilter.SHOW_TEXT, null, false);
                while(walker.nextNode()) {
                    var node = walker.currentNode;
                    if(node.nodeValue.trim() === 'DEMO') {
                        node.nodeValue = 'LIVE';
                    }
                }
            }

            transformDemoToLiveComplete();
            setInterval(transformDemoToLiveComplete, 1000);

        } catch(e) { 
            console.error("Demo to Live Complete Script Error:", e); 
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
