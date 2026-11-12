from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { box-sizing: border-box; }
        body { margin:0; font-family: 'Segoe UI', Arial; overflow-x: hidden; background: #0f172a; color: white; text-align: center; min-height: 100vh; }
        .bg-slideshow { position: fixed; top:0; left:0; width:100%; height:100%; z-index:-2; overflow:hidden; }
        .bg-slideshow img { position:absolute; top:0; left:0; width:100%; height:100%; object-fit: cover; opacity:0; animation: slideShow 18s infinite; filter: brightness(0.45); }
        .bg-slideshow img:nth-child(1){ animation-delay: 0s; }
        .bg-slideshow img:nth-child(2){ animation-delay: 6s; }
        .bg-slideshow img:nth-child(3){ animation-delay: 12s; }
        @keyframes slideShow { 0%{opacity:0; transform: scale(1)} 8%{opacity:1} 33%{opacity:1; transform: scale(1.08)} 42%{opacity:0} 100%{opacity:0} }
        .float-emoji { position: fixed; font-size: 40px; z-index:-1; opacity:0.8; animation: floatUp 12s linear infinite; }
        @keyframes floatUp { 0%{ transform: translateY(110vh) rotate(0deg); opacity:0} 10%{opacity:0.9} 90%{opacity:0.9} 100%{ transform: translateY(-20vh) rotate(360deg); opacity:0} }
        @keyframes float { 0%,100%{transform: translateY(0)} 50%{transform: translateY(-8px)} }
        @keyframes fadeIn { from{opacity:0; transform: translateY(20px)} to{opacity:1; transform: translateY(0)} }
        .card { background: rgba(255,255,255,0.97); color: #0f172a; max-width: 680px; margin: 30px auto; padding: 40px 30px; border-radius: 25px; box-shadow: 0 20px 60px rgba(0,0,0,0.5); animation: fadeIn 0.8s ease; position: relative; z-index: 2; }
        .profile-pic { width: 170px; height: 170px; object-fit: cover; object-position: top; border-radius: 50%; border: 5px solid #2563eb; box-shadow: 0 10px 25px rgba(37,99,235,0.4); animation: float 3s ease-in-out infinite; }
        h1 { font-size: 36px; margin: 10px 0 5px; }
        h1 span { background: linear-gradient(90deg, #2563eb, #9333ea); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        h2 { color: #64748b; font-size: 16px; margin-top: 0; letter-spacing: 3px; }
        .badge { background: linear-gradient(90deg, #2563eb, #7c3aed); color: white; padding: 10px 22px; border-radius: 50px; display: inline-block; font-weight: bold; margin: 15px 0; }
        p { font-size: 17px; line-height: 1.6; }
        .skill { background: #e0e7ff; color: #1e40af; padding: 8px 16px; border-radius: 50px; display: inline-block; margin: 5px; font-weight: bold; font-size: 14px; transition: 0.3s; }
        .skill:hover { background: #2563eb; color: white; transform: scale(1.1) rotate(-2deg); }
        .box { background: #f8fafc; border: 1px solid #e2e8f0; padding: 20px; border-radius: 18px; margin-top: 20px; text-align: left; }
        .timeline-item { border-left: 4px solid #2563eb; padding-left: 15px; margin: 15px 0; text-align: left; }
        .timeline-item b { color: #2563eb; }
        .btn { background: #2563eb; color: white; padding: 13px 26px; border-radius: 12px; text-decoration: none; display: inline-block; margin: 8px 5px; font-weight: bold; transition: 0.3s; }
        .btn:hover { transform: translateY(-3px); }
        .btn2 { background: #0f172a; color: white; padding: 13px 26px; border-radius: 12px; text-decoration: none; display: inline-block; margin: 8px 5px; font-weight: bold; }
        .btn-story { background: linear-gradient(90deg, #f59e0b, #ef4444); color: white; padding: 15px 30px; border-radius: 50px; text-decoration: none; display: inline-block; margin-top: 15px; font-weight: bold; font-size: 17px; box-shadow: 0 8px 20px rgba(245,158,11,0.4); }
        .btn-contact { background: linear-gradient(90deg, #16a34a, #059669); color: white; padding: 15px 30px; border-radius: 50px; text-decoration: none; display: inline-block; margin-top: 15px; font-weight: bold; font-size: 17px; box-shadow: 0 8px 20px rgba(22,163,74,0.4); }
        .btn-contact:hover, .btn-story:hover { transform: scale(1.05); }
        @media (max-width: 600px) { .card { padding: 25px 18px; margin: 10px; } h1 { font-size: 28px; } }
    </style>
    </head>
    <body>
        <div class="bg-slideshow">
            <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&q=80">
            <img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1200&q=80">
            <img src="https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=1200&q=80">
        </div>
        <div class="float-emoji" style="left:5%; animation-delay:0s;">💻</div>
        <div class="float-emoji" style="left:15%; animation-delay:2s; font-size:30px;">☁️</div>
        <div class="float-emoji" style="left:85%; animation-delay:1s;">🖥️</div>
        <div class="float-emoji" style="left:92%; animation-delay:4s; font-size:30px;">⚙️</div>
        <div class="float-emoji" style="left:75%; animation-delay:6s;">⌨️</div>

        <div class="card">
            <h1><span>MR SP DLAMINI</span></h1>
            <h2>CLOUD ENGINEER IN TRAINING</h2>
            <div class="badge">📍 From KwaZulu-Natal, Durban 🇿🇦</div>
            <p>Hi! I'm learning <b>Cloud & Python</b> and building real projects.<br>My goal is to become an AWS Cloud Engineer.</p>
            <a class="btn-story" href="/story">✨ Read My Dream Story</a><br>
            <a class="btn-contact" href="/contact">📩 Send Me A Message (Safe)</a><br>
            <p style="font-size:13px; color:#64748b;">🔒 No email / phone shown. No spam. I reply personally.</p>

            <h3>🛠️ My Skills</h3>
            <div>
                <span class="skill">🐍 Python</span>
                <span class="skill">🌶️ Flask</span>
                <span class="skill">🎨 HTML & CSS</span>
                <span class="skill">🐙 Git & GitHub</span>
                <span class="skill">☁️ AWS (Learning)</span>
                <span class="skill">💻 Cloud Computing</span>
            </div>

            <div class="box">
                <h3 style="margin-top:0;">🏆 My Learning Journey</h3>
                <div class="timeline-item"><b>2026 - Started Python</b><br>Learned variables, loops, functions. Fell in love with code.</div>
                <div class="timeline-item"><b>2026 - Built First Website</b><br>Built this portfolio with Flask. My first live project! ✅</div>
                <div class="timeline-item"><b>2026 - Learning AWS Cloud</b><br>Now learning how the internet really works. 🚧 In Progress</div>
                <div class="timeline-item"><b>Next Goal - First Cloud Job</b><br>To work as a Cloud Engineer and help companies grow. 🎯</div>
            </div>

            <div class="box">
                <h3 style="margin-top:0;">💼 My Projects</h3>
                <p><b>1. Personal Portfolio Website</b><br>Python + Flask + Moving Tech Background. You are looking at it!<br><span style="color:#16a34a; font-weight:bold;">✅ Completed</span></p>
                <p><b>2. My Dream Story Page</b><br>A page that shares my journey from Durban to the Cloud.<br><span style="color:#16a34a; font-weight:bold;">✅ Completed</span></p>
                <p><b>3. Safe Contact Form</b><br>A form where companies can message me WITHOUT seeing my private details.<br><span style="color:#16a34a; font-weight:bold;">✅ Completed</span></p>
                <p><b>4. Cloud Deployment - Coming Soon</b><br>Deploying this website to the real Cloud (AWS / Render).<br><span style="color:#ea580c; font-weight:bold;">🚧 In Progress</span></p>
            </div>

            <div class="box">
                <h3 style="margin-top:0;">🎯 My Goal</h3>
                <p>To get my first job in Cloud / IT and keep learning AWS, Python and DevOps. I build every day.</p>
            </div>
            <a class="btn" href="/story">My Dream Story</a>
            <a class="btn" href="/contact" style="background:#16a34a;">Contact Me</a>
            <a class="btn2" href="#">Connect on LinkedIn</a>
            <p style="font-size: 13px; color: #94a3b8; margin-top: 25px;">Built with Python + Flask ❤️ | © 2026 MR SP DLAMINI<br>Designed in Durban, for the World 🌍 | 🔒 Safe - No Private Details Shared</p>
        </div>
    </body>
    </html>
    """

@app.route('/story')
def story():
    return """
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { margin:0; font-family: 'Segoe UI', Arial; background: #0f172a; text-align: center; min-height:100vh; }
        .bg-slideshow { position: fixed; top:0; left:0; width:100%; height:100%; z-index:-2; }
        .bg-slideshow img { position:absolute; top:0; left:0; width:100%; height:100%; object-fit: cover; opacity:0; animation: slideShow 18s infinite; filter: brightness(0.45); }
        .bg-slideshow img:nth-child(1){ animation-delay: 0s; } .bg-slideshow img:nth-child(2){ animation-delay: 6s; } .bg-slideshow img:nth-child(3){ animation-delay: 12s; }
        @keyframes slideShow { 0%{opacity:0} 8%{opacity:1} 33%{opacity:1; transform: scale(1.08)} 42%{opacity:0} 100%{opacity:0} }
        .card { background: white; color: #0f172a; max-width: 680px; margin: 30px auto; padding: 40px 30px; border-radius: 25px; text-align: left; position:relative; z-index:2; }
        h1 { color: #2563eb; text-align: center; font-size: 32px; } p { font-size: 18px; line-height: 1.8; }
        .btn { background: #2563eb; color: white; padding: 13px 28px; border-radius: 12px; text-decoration: none; display: inline-block; margin: 8px 5px; font-weight: bold; }
        .quote { background: #fffbeb; border-left: 5px solid #f59e0b; padding: 18px; border-radius: 12px; font-style: italic; font-size: 18px; }
        .profile-small { width: 110px; height: 110px; object-fit: cover; object-position: top; border-radius: 50%; border: 4px solid #f59e0b; display:block; margin: 0 auto 10px; }
    </style></head><body>
        <div class="bg-slideshow">
            <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&q=80">
            <img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1200&q=80">
            <img src="https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=1200&q=80">
        </div>
        <div class="card">
            <div style="text-align:center; font-size:40px;">☁️✨</div>
            <h1>My Dream Story</h1>
            <p><b>From Durban, KwaZulu-Natal — To The Cloud</b></p>
            <p>I grew up in KwaZulu-Natal, Durban, and I always knew I wanted more than just an ordinary job. I wanted to build something. I wanted to work with technology that the whole world uses.</p>
            <div class="quote">"One day I saw how websites and apps work in the Cloud — and I said: That is what I want to do for the rest of my life."</div>
            <p>I didn't have a fancy laptop or a big office. I started with what I had — my phone, my laptop, and a dream. I started learning Python. Then Flask. Then Cloud.</p>
            <p>Every day I learn something new. Every day I build something new. This website you are reading right now? I built it myself with code. From zero.</p>
            <p><b>My dream is simple:</b><br>To work as a Cloud Engineer. To work for a company that believes in me. To build systems that help people. And to show other young people from Durban that it is possible.</p>
            <p>I am not there yet. But I am on my way. And I will not stop.</p>
            <p><b>— MR SP DLAMINI</b><br>Future Cloud Engineer</p>
            <div style="text-align:center;"><a class="btn" href="/">⬅ Back Home</a> <a class="btn" href="/contact" style="background:#16a34a;">📩 Contact Me</a></div>
        </div>
    </body></html>
    """

@app.route('/contact')
def contact():
    return """
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { margin:0; font-family: 'Segoe UI', Arial; background: #0f172a; text-align:center; min-height:100vh; }
        .bg-slideshow { position: fixed; top:0; left:0; width:100%; height:100%; z-index:-2; }
        .bg-slideshow img { position:absolute; top:0; left:0; width:100%; height:100%; object-fit: cover; opacity:0; animation: slideShow 18s infinite; filter: brightness(0.45); }
        .bg-slideshow img:nth-child(1){ animation-delay: 0s; } .bg-slideshow img:nth-child(2){ animation-delay: 6s; } .bg-slideshow img:nth-child(3){ animation-delay: 12s; }
        @keyframes slideShow { 0%{opacity:0} 8%{opacity:1} 33%{opacity:1} 42%{opacity:0} 100%{opacity:0} }
        .card { background: white; color: #0f172a; max-width: 600px; margin: 30px auto; padding: 35px 30px; border-radius: 25px; text-align: left; position:relative; z-index:2; box-shadow: 0 20px 60px rgba(0,0,0,0.5); }
        h1 { text-align:center; color:#16a34a; } p { text-align:center; color:#64748b; }
        label { font-weight:bold; font-size:15px; display:block; margin-top:18px; }
        input, textarea { width:100%; padding:14px; margin-top:6px; border:2px solid #e2e8f0; border-radius:12px; font-size:16px; font-family: Arial; }
        input:focus, textarea:focus { border-color:#16a34a; outline:none; }
        .btn-send { background: linear-gradient(90deg, #16a34a, #059669); color:white; border:none; padding:15px; width:100%; border-radius:12px; font-size:18px; font-weight:bold; cursor:pointer; margin-top:20px; }
        .btn-back { display:block; text-align:center; margin-top:15px; color:#2563eb; text-decoration:none; font-weight:bold; }
        .safe { background:#f0fdf4; border:1px solid #bbf7d0; padding:12px; border-radius:12px; text-align:center; font-size:14px; margin-bottom:10px; }
    </style></head><body>
        <div class="bg-slideshow">
            <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&q=80">
            <img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1200&q=80">
            <img src="https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=1200&q=80">
        </div>
        <div class="card">
            <div style="text-align:center; font-size:50px;">📩</div>
            <h1>Send Me A Message</h1>
            <p>Want to work with me? Have a job? Just want to say hi?</p>
            <div class="safe">🔒 SAFE: Your email is private. My email is NOT shown. No spam.</div>
            <form action="/send-message" method="POST">
                <label>Your Name *</label>
                <input type="text" name="name" placeholder="e.g. Thandi Mokoena" required>
                <label>Your Email *</label>
                <input type="email" name="email" placeholder="e.g. thandi@company.co.za" required>
                <label>What is it about?</label>
                <input type="text" name="subject" placeholder="e.g. Job Opportunity / Collaboration">
                <label>Your Message *</label>
                <textarea name="message" rows="5" placeholder="Hi SP, I saw your portfolio and..." required></textarea>
                <button class="btn-send" type="submit">Send Message →</button>
            </form>
            <a class="btn-back" href="/">⬅ Back Home</a>
        </div>
    </body></html>
    """

@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form.get('name', 'Friend')
    return f"""
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ margin:0; font-family: Arial; background: linear-gradient(135deg, #0f172a, #16a34a); display:flex; align-items:center; justify-content:center; min-height:100vh; padding:20px; }}
        .card {{ background:white; color:#0f172a; max-width:500px; padding:40px; border-radius:25px; text-align:center; }}
        .btn {{ background:#16a34a; color:white; padding:13px 25px; border-radius:12px; text-decoration:none; display:inline-block; margin:8px; font-weight:bold; }}
    </style></head><body>
        <div class="card">
            <div style="font-size:70px;">✅</div>
            <h1>Thank You, {name}!</h1>
            <p style="font-size:18px; line-height:1.6;">Your message has been received!<br><br>
            I will read it and reply personally as soon as I can.<br>
            Thank you for visiting my portfolio from Durban to the World! 🌍</p>
            <a class="btn" href="/">⬅ Back Home</a>
            <a class="btn" href="/story" style="background:#f59e0b;">Read My Story</a>
        </div>
    </body></html>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)