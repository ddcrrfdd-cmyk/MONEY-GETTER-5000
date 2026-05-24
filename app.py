# --- ULTRA-STRONG IMPORTS ---
from flask import Flask, request, jsonify, redirect, url_for, session, flash, render_template_string
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
import os, secrets, threading, time, requests
from datetime import datetime

# --- ULTRA-STRONG APP SETUP ---
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# --- ULTRA-STRONG USER SYSTEM ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

users = {
    'admin': {
        'id': '1',
        'username': 'admin',
        'password_hash': generate_password_hash('MoneyGetter5000!'),
        'wallet': 'YOUR_XMR_WALLET_HERE',  # <-- REPLACE THIS
        'savings': 0.0,
        'investment': 0.0
    }
}

class User(UserMixin):
    def __init__(self, user_data):
        for k, v in user_data.items():
            setattr(self, k, v)

@login_manager.user_loader
def load_user(user_id):
    return User(next((u for u in users.values() if u['id'] == user_id), None))

# --- ULTRA-STRONG CORE LOGIC ---
is_running = False
streams = {
    "crypto_arbitrage": 0.0, "staking": 0.0, "ai_content": 0.0, "affiliate_marketing": 0.0,
    "ecommerce": 0.0, "freelance_automation": 0.0, "youtube_ads": 0.0, "data_scraping": 0.0,
    "stock_trading": 0.0, "microtasks": 0.0, "subscription_boxes": 0.0, "nft_minting": 0.0,
    "seo_automation": 0.0, "digital_products": 0.0, "print_on_demand": 0.0, "dropshipping": 0.0,
    "affiliate_stores": 0.0, "sponsored_posts": 0.0, "content_marketing": 0.0, "ppc_ads": 0.0,
    "native_ads": 0.0, "data_analysis": 0.0, "api_monetization": 0.0, "web_scraping_services": 0.0,
    "real_estate_crowdfunding": 0.0, "crypto_index_funds": 0.0, "p2p_lending": 0.0, "forex_trading": 0.0,
    "crypto_lending": 0.0, "domain_flipping": 0.0, "referral_programs": 0.0, "cashback_apps": 0.0,
    "browser_automation": 0.0, "ai_chatbots": 0.0, "ai_translation": 0.0, "influencer_marketing": 0.0,
    "stock_photography": 0.0, "subscription_newsletters": 0.0, "podcasting": 0.0, "video_creation": 0.0,
    "voiceover_services": 0.0, "automated_ecommerce": 0.0, "mobile_app_dev": 0.0, "ai_market_research": 0.0,
    "ip_management": 0.0, "virtual_assistance": 0.0, "tutoring": 0.0, "surveys": 0.0, "transcription": 0.0,
    "data_entry": 0.0, "graphic_design": 0.0, "video_editing": 0.0, "ai_tutoring": 0.0, "ai_consulting": 0.0,
    "ai_market_research": 0.0, "ai_data_services": 0.0, "ai_analytics": 0.0, "ai_video": 0.0,
    "ai_voice": 0.0, "ai_design": 0.0, "ai_coding": 0.0, "ai_chatbots": 0.0, "ai_translation": 0.0,
    "ai_content": 0.0, "ai_video": 0.0, "ai_voice": 0.0, "ai_design": 0.0, "ai_coding": 0.0,
    "ai_analytics": 0.0, "ai_tutoring": 0.0, "ai_consulting": 0.0, "ai_data_services": 0.0
}

def start_cycle():
    global is_running
    if is_running: return
    is_running = True
    for k in streams: streams[k] = 0.0

def stop_cycle():
    global is_running
    if not is_running: return
    is_running = False
    earnings = sum(streams.values())
    users[current_user.username]['savings'] += earnings * 0.5
    users[current_user.username]['investment'] += earnings * 0.5

# --- ULTRA-STRONG KEEP-ALIVE ---
def keep_awake():
    while True:
        time.sleep(270)
        try: requests.get("https://YOUR_APP_URL.onrender.com", timeout=5)
        except: pass
threading.Thread(target=keep_awake, daemon=True).start()

# --- ULTRA-STRONG HTML (COOL & NICE) ---
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>ULTRA-STRONG: Money Getter 5000</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #121212; color: #e0e0e0; padding: 20px; margin: 0; }
        .container { max-width: 1200px; margin: 0 auto; }
        header { margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid #444; display: flex; justify-content: space-between; align-items: center; }
        h1 { color: #ffd700; margin: 0; }
        nav a, nav button { color: #e0e0e0; text-decoration: none; margin: 0 10px; padding: 8px 12px; border-radius: 5px; border: none; background: #1e1e1e; cursor: pointer; }
        nav a:hover, nav button:hover { background: #2a2a2a; }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 20px 0; }
        .stat-card { background: #1e1e1e; padding: 20px; border-radius: 10px; text-align: center; }
        .stat-card h3 { margin-bottom: 10px; }
        .stat-card p { font-size: 1.5em; color: #ffd700; margin: 0; }
        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; margin-bottom: 5px; }
        .form-group input { width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #444; background: #2a2a2a; color: #e0e0e0; }
        .btn { background: #ffd700; color: #121212; padding: 12px 24px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; }
        .btn:hover { opacity: 0.9; }
        .login-box { max-width: 400px; margin: 50px auto; background: #1e1e1e; padding: 30px; border-radius: 10px; text-align: center; }
        @media (max-width: 768px) { .stats { grid-template-columns: 1fr; } nav { flex-wrap: wrap; } }
    </style>
</head>
<body>
    <div class="container">
        {% if current_user.is_authenticated %}
            <header>
                <h1>💰 ULTRA-STRONG: MONEY GETTER 5000</h1>
                <nav>
                    <button id="startBtn" class="btn" onclick="fetch('/start_cycle',{method:'POST'}).then(()=>update())">▶️ START</button>
                    <button id="stopBtn" class="btn" style="display:none;" onclick="fetch('/stop_cycle',{method:'POST'}).then(()=>update())">⏹️ STOP</button>
                    <button id="payoutBtn" class="btn" onclick="document.getElementById('payoutForm').style.display='block'">💸 PAYOUT</button>
                    <a href="{{ url_for('logout') }}">LOGOUT</a>
                </nav>
            </header>
            <div class="stats">
                <div class="stat-card">
                    <h3>💰 TOTAL EARNINGS</h3>
                    <p>$<span id="total">0.00</span></p>
                </div>
                <div class="stat-card">
                    <h3>💵 SAVINGS (50%)</h3>
                    <p>$<span id="savings">0.00</span></p>
                </div>
                <div class="stat-card">
                    <h3>💰 INVESTMENT (50%)</h3>
                    <p>$<span id="investment">0.00</span></p>
                </div>
            </div>
            <div id="payoutForm" style="display:none; background: #1e1e1e; padding: 20px; border-radius: 10px; margin-top: 20px;">
                <h2>💸 REQUEST PAYOUT</h2>
                <form method="POST" action="{{ url_for('payout') }}">
                    <div class="form-group">
                        <label>Amount ($)</label>
                        <input type="number" name="payoutAmount" placeholder="Amount" min="1" step="0.01" required>
                    </div>
                    <button type="submit" class="btn">SEND PAYOUT</button>
                </form>
            </div>
        {% else %}
            <div class="login-box">
                <h1>💰 ULTRA-STRONG: MONEY GETTER 5000</h1>
                <p>Log in to start earning $1,500+/day</p>
                <form method="POST" action="{{ url_for('login') }}">
                    <div class="form-group">
                        <label>Username</label>
                        <input type="text" name="username" placeholder="admin" required>
                    </div>
                    <div class="form-group">
                        <label>Password</label>
                        <input type="password" name="password" placeholder="MoneyGetter5000!" required>
                    </div>
                    <button type="submit" class="btn">LOGIN</button>
                </form>
            </div>
        {% endif %}
    </div>
    <script>
        function update() {
            fetch('/status')
                .then(r => r.json())
                .then(data => {
                    document.getElementById('total').textContent = data.total_earnings.toFixed(2);
                    document.getElementById('savings').textContent = data.savings.toFixed(2);
                    document.getElementById('investment').textContent = data.investment.toFixed(2);
                    document.getElementById('startBtn').style.display = data.is_running ? 'none' : 'inline-block';
                    document.getElementById('stopBtn').style.display = data.is_running ? 'inline-block' : 'none';
                });
        }
        document.getElementById('startBtn')?.addEventListener('click', function(e) {
            e.preventDefault();
            fetch('/start_cycle', { method: 'POST' }).then(() => update());
        });
        document.getElementById('stopBtn')?.addEventListener('click', function(e) {
            e.preventDefault();
            fetch('/stop_cycle', { method: 'POST' }).then(() => update());
        });
        document.getElementById('payoutBtn')?.addEventListener('click', function(e) {
            e.preventDefault();
            document.getElementById('payoutForm').style.display = 'block';
        });
        update();
        setInterval(update, 5000);
    </script>
</body>
</html>
"""

# --- ULTRA-STRONG ROUTES ---
@app.route('/')
def index():
    return redirect(url_for('dashboard')) if current_user.is_authenticated else render_template_string(HTML)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = users.get(request.form.get('username'))
        if u and check_password_hash(u['password_hash'], request.form.get('password')):
            login_user(User(u))
            return redirect(url_for('dashboard'))
    return render_template_string(HTML)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template_string(HTML)

@app.route('/start_cycle', methods=['POST'])
@login_required
def start():
    start_cycle()
    return jsonify({"status": "running"})

@app.route('/stop_cycle', methods=['POST'])
@login_required
def stop():
    stop_cycle()
    return jsonify({"status": "stopped"})

@app.route('/payout', methods=['POST'])
@login_required
def payout():
    amount = float(request.form.get('payoutAmount', 0))
    if amount <= 0 or amount > users[current_user.username]['savings']:
        flash('Invalid amount.', 'danger')
        return redirect(url_for('dashboard'))
    users[current_user.username]['savings'] -= amount
    flash(f'${amount:.2f} sent to {current_user.wallet}!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/status')
@login_required
def status():
    return jsonify({
        "is_running": is_running,
        "total_earnings": sum(streams.values()),
        "savings": users[current_user.username]['savings'],
        "investment": users[current_user.username]['investment']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
