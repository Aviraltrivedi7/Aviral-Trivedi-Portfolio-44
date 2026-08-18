import os
from PIL import Image, ImageDraw, ImageFont

def get_font(size):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except:
        return ImageFont.load_default()

def create_metro_mockup(path):
    w, h = 1600, 900
    img = Image.new("RGB", (w, h), (13, 15, 20))
    d = ImageDraw.Draw(img)
    
    f_lg = get_font(28)
    f_md = get_font(20)
    f_sm = get_font(16)
    f_title = get_font(34)
    
    d.rectangle([0, 0, w, h], fill=(12, 14, 18))
    
    # Subtle ambient gradient
    for r in range(400, 0, -8):
        d.ellipse([w-250-r, 100-r, w-250+r, 100+r], fill=(int(6*r/400), int(182*r/400*0.25), int(212*r/400*0.3)))
        
    # Browser window container
    d.rounded_rectangle([40, 40, w-40, h-40], radius=16, fill=(18, 20, 26), outline=(40, 45, 58), width=2)
    
    # Top navbar inside browser
    d.rounded_rectangle([40, 40, w-40, 110], radius=16, fill=(24, 27, 36))
    d.rectangle([40, 90, w-40, 110], fill=(24, 27, 36))
    d.line([(40, 110), (w-40, 110)], fill=(45, 50, 65), width=1)
    
    # Traffic lights
    d.ellipse([70, 70, 84, 84], fill=(239, 68, 68))
    d.ellipse([94, 70, 108, 84], fill=(234, 179, 8))
    d.ellipse([118, 70, 132, 84], fill=(34, 197, 94))
    
    # App title & URL in address bar
    d.rounded_rectangle([200, 60, w-200, 92], radius=8, fill=(14, 16, 22), outline=(50, 55, 70), width=1)
    d.text((220, 66), "https://kanpur-metro-safar-guide.vercel.app - Kanpur Metro Route & Fare Guide", font=f_sm, fill=(160, 170, 190))
    
    # App Header inside
    d.rectangle([42, 111, w-42, 185], fill=(20, 24, 32))
    d.text((80, 132), "KANPUR METRO SAFAR GUIDE (Kanpur Metro Guide)", font=f_title, fill=(255, 255, 255))
    d.rounded_rectangle([w-260, 130, w-80, 170], radius=18, fill=(6, 182, 212), outline=(6, 182, 212))
    d.text((w-235, 140), "PWA Live Ready", font=f_sm, fill=(10, 20, 30))
    
    # Left Card: Route Selector & Fare
    d.rounded_rectangle([80, 210, 600, h-80], radius=16, fill=(24, 28, 38), outline=(50, 56, 75), width=1)
    d.text((110, 235), "ROUTE PLANNER & FARE CALCULATOR", font=f_md, fill=(6, 182, 212))
    
    # From Box
    d.rounded_rectangle([110, 280, 570, 350], radius=10, fill=(16, 18, 26), outline=(45, 50, 65))
    d.text((130, 290), "FROM:", font=f_sm, fill=(120, 130, 150))
    d.text((130, 315), "IIT Kanpur Metro Station", font=f_md, fill=(255, 255, 255))
    
    # Arrow
    d.text((310, 360), "| 9 Stations (Orange Line) |", font=f_sm, fill=(6, 182, 212))
    
    # To Box
    d.rounded_rectangle([110, 395, 570, 465], radius=10, fill=(16, 18, 26), outline=(45, 50, 65))
    d.text((130, 405), "TO:", font=f_sm, fill=(120, 130, 150))
    d.text((130, 430), "Kanpur Central Railway Station", font=f_md, fill=(255, 255, 255))
    
    # Route Stats Box
    d.rounded_rectangle([110, 490, 570, 620], radius=12, fill=(14, 28, 38), outline=(6, 182, 212), width=1)
    d.text((130, 505), "ESTIMATED FARE & DURATION", font=f_sm, fill=(140, 190, 210))
    d.text((130, 535), "Rs 30  |  32 Mins Duration", font=f_lg, fill=(6, 220, 245))
    d.text((130, 580), "Next Train: in 4 mins (Platform 1)", font=f_sm, fill=(34, 197, 94))
    
    # Offline PWA Badge
    d.rounded_rectangle([110, 645, 570, 720], radius=10, fill=(20, 24, 34), outline=(40, 45, 60))
    d.text((130, 660), "Works 100% Offline in Underground Stations", font=f_md, fill=(200, 210, 225))
    d.text((130, 690), "Service Worker Caching & Instant Route Computation", font=f_sm, fill=(120, 130, 150))

    # Right Card: Interactive Map & Station Line
    d.rounded_rectangle([630, 210, w-80, h-80], radius=16, fill=(22, 26, 36), outline=(50, 56, 75), width=1)
    d.text((660, 235), "ORANGE LINE INTERACTIVE STATIONS", font=f_md, fill=(255, 255, 255))
    
    stations = [
        "1. IIT Kanpur (IIT Kanpur)",
        "2. Kalyanpur (Kalyanpur)",
        "3. SPM Hospital (SPM Hospital)",
        "4. CSJMU University (CSJMU Univ)",
        "5. Gurudev Chauraha (Gurudev)",
        "6. Geeta Nagar (Geeta Nagar)",
        "7. Rawatpur (Rawatpur)",
        "8. Moti Jheel (Moti Jheel)",
        "9. Kanpur Central (Kanpur Central)"
    ]
    
    d.line([(690, 305), (690, 305 + len(stations)*42)], fill=(6, 182, 212), width=4)
    for idx, st_name in enumerate(stations):
        sy = 305 + idx * 42
        d.ellipse([682, sy-8, 698, sy+8], fill=(6, 182, 212), outline=(255, 255, 255), width=2)
        d.text((720, sy-9), st_name, font=f_md, fill=(230, 235, 245))
        d.rounded_rectangle([w-240, sy-10, w-110, sy+14], radius=6, fill=(30, 36, 48))
        d.text((w-225, sy-7), "5:30 AM - 10 PM", font=f_sm, fill=(140, 150, 170))
        
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "PNG", optimize=True)
    print(f"Saved: {path}")

def create_budget_mockup(path):
    w, h = 1600, 900
    img = Image.new("RGB", (w, h), (12, 18, 16))
    d = ImageDraw.Draw(img)
    
    f_lg = get_font(28)
    f_md = get_font(20)
    f_sm = get_font(16)
    f_title = get_font(34)
    
    d.rectangle([0, 0, w, h], fill=(10, 16, 14))
    d.rounded_rectangle([40, 40, w-40, h-40], radius=16, fill=(16, 24, 20), outline=(30, 55, 45), width=2)
    d.rounded_rectangle([40, 40, w-40, 110], radius=16, fill=(22, 34, 28))
    d.rectangle([40, 90, w-40, 110], fill=(22, 34, 28))
    d.ellipse([70, 70, 84, 84], fill=(239, 68, 68))
    d.ellipse([94, 70, 108, 84], fill=(234, 179, 8))
    d.ellipse([118, 70, 132, 84], fill=(34, 197, 94))
    d.rounded_rectangle([200, 60, w-200, 92], radius=8, fill=(12, 20, 16), outline=(35, 60, 48))
    d.text((220, 66), "https://smartbudget-ai-enhanced7.vercel.app - SmartBudget AI Financial Assistant", font=f_sm, fill=(140, 180, 160))
    
    d.text((80, 132), "SMARTBUDGET AI - Intelligent Wealth & Expense Tracker", font=f_title, fill=(255, 255, 255))
    d.rounded_rectangle([w-280, 130, w-80, 170], radius=18, fill=(16, 185, 129))
    d.text((w-260, 140), "AI Assistant Active", font=f_sm, fill=(10, 30, 20))
    
    # Top 3 Stat Cards
    d.rounded_rectangle([80, 200, 520, 320], radius=14, fill=(22, 34, 28), outline=(35, 65, 50))
    d.text((110, 220), "TOTAL BALANCE", font=f_sm, fill=(140, 180, 160))
    d.text((110, 245), "Rs 1,42,850.00", font=f_title, fill=(255, 255, 255))
    d.text((110, 290), "+ 14.8% vs last month", font=f_sm, fill=(34, 197, 94))
    
    d.rounded_rectangle([550, 200, 990, 320], radius=14, fill=(22, 34, 28), outline=(35, 65, 50))
    d.text((580, 220), "MONTHLY EXPENSES", font=f_sm, fill=(140, 180, 160))
    d.text((580, 245), "Rs 38,420.00", font=f_title, fill=(248, 113, 113))
    d.text((580, 290), "Budget limit: Rs 50,000", font=f_sm, fill=(140, 180, 160))

    d.rounded_rectangle([1020, 200, w-80, 320], radius=14, fill=(22, 34, 28), outline=(35, 65, 50))
    d.text((1050, 220), "AI SAVINGS ESTIMATOR", font=f_sm, fill=(140, 180, 160))
    d.text((1050, 245), "Rs 18,500.00", font=f_title, fill=(52, 211, 153))
    d.text((1050, 290), "Auto-investing Rs 8,000 in SIP", font=f_sm, fill=(140, 180, 160))
    
    # Charts & AI Suggestions Area
    d.rounded_rectangle([80, 350, 920, h-80], radius=14, fill=(20, 30, 26), outline=(35, 60, 48))
    d.text((110, 375), "SPENDING BY CATEGORY (CHART.JS VISUALIZATION)", font=f_md, fill=(255, 255, 255))
    
    # Mock Bar chart
    bars = [("Housing", 45), ("Food & Dining", 65), ("Transport", 30), ("Shopping", 50), ("Utilities", 25), ("Tech/Cloud", 40)]
    for i, (cat, val) in enumerate(bars):
        bx = 120 + i * 130
        by = 680 - val * 3.5
        d.rectangle([bx, by, bx + 70, 680], fill=(16, 185, 129))
        d.text((bx, 700), cat, font=f_sm, fill=(160, 190, 175))
        d.text((bx + 10, by - 22), f"Rs {val*200}", font=f_sm, fill=(200, 230, 215))

    # Right: AI Insights Card
    d.rounded_rectangle([950, 350, w-80, h-80], radius=14, fill=(18, 32, 26), outline=(16, 185, 129), width=1)
    d.text((980, 375), "AI FINANCIAL INSIGHTS & RECOMMENDATIONS", font=f_md, fill=(52, 211, 153))
    
    insights = [
        "1. Dining spend exceeded typical average by 18% this weekend.",
        "2. Recurring subscriptions detected: 4 active ($42/mo).",
        "3. You can save Rs 4,200 by switching utility payment modes.",
        "4. Emergency fund is now at 4.2 months of fixed expenses."
    ]
    for idx, ins in enumerate(insights):
        iy = 430 + idx * 78
        d.rounded_rectangle([980, iy, w-110, iy+62], radius=8, fill=(14, 24, 20))
        d.text((1000, iy+20), ins, font=f_sm, fill=(220, 240, 230))
        
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "PNG", optimize=True)
    print(f"Saved: {path}")

def create_crypto_mockup(path):
    w, h = 1600, 900
    img = Image.new("RGB", (w, h), (18, 14, 10))
    d = ImageDraw.Draw(img)
    
    f_lg = get_font(28)
    f_md = get_font(20)
    f_sm = get_font(16)
    f_title = get_font(34)
    
    d.rectangle([0, 0, w, h], fill=(16, 12, 8))
    d.rounded_rectangle([40, 40, w-40, h-40], radius=16, fill=(24, 18, 12), outline=(60, 45, 30), width=2)
    d.rounded_rectangle([40, 40, w-40, 110], radius=16, fill=(34, 24, 16))
    d.rectangle([40, 90, w-40, 110], fill=(34, 24, 16))
    d.ellipse([70, 70, 84, 84], fill=(239, 68, 68))
    d.ellipse([94, 70, 108, 84], fill=(234, 179, 8))
    d.ellipse([118, 70, 132, 84], fill=(34, 197, 94))
    d.rounded_rectangle([200, 60, w-200, 92], radius=8, fill=(18, 12, 8), outline=(60, 45, 30))
    d.text((220, 66), "https://cryptodashboard11425.vercel.app - Real-Time Cryptocurrency Market Analytics", font=f_sm, fill=(190, 160, 130))
    
    d.text((80, 132), "CRYPTODASHBOARD - Live Multi-Currency Trading Console", font=f_title, fill=(255, 255, 255))
    d.rounded_rectangle([w-260, 130, w-80, 170], radius=18, fill=(245, 158, 11))
    d.text((w-240, 140), "Live Feeds Active", font=f_sm, fill=(20, 15, 5))
    
    # Bitcoin highlight
    d.rounded_rectangle([80, 200, 520, 320], radius=14, fill=(30, 22, 14), outline=(80, 55, 25))
    d.text((110, 220), "BITCOIN (BTC / USDT)", font=f_sm, fill=(245, 158, 11))
    d.text((110, 245), "$ 94,820.50", font=f_title, fill=(255, 255, 255))
    d.text((110, 290), "+ 5.42%  |  24h High: $96,100", font=f_sm, fill=(34, 197, 94))
    
    # Ethereum highlight
    d.rounded_rectangle([550, 200, 990, 320], radius=14, fill=(30, 22, 14), outline=(80, 55, 25))
    d.text((580, 220), "ETHEREUM (ETH / USDT)", font=f_sm, fill=(147, 197, 253))
    d.text((580, 245), "$ 3,460.20", font=f_title, fill=(255, 255, 255))
    d.text((580, 290), "+ 3.80%  |  24h High: $3,520", font=f_sm, fill=(34, 197, 94))

    # Solana highlight
    d.rounded_rectangle([1020, 200, w-80, 320], radius=14, fill=(30, 22, 14), outline=(80, 55, 25))
    d.text((1050, 220), "SOLANA (SOL / USDT)", font=f_sm, fill=(192, 132, 252))
    d.text((1050, 245), "$ 196.40", font=f_title, fill=(255, 255, 255))
    d.text((1050, 290), "+ 8.12%  |  24h Vol: $4.2B", font=f_sm, fill=(34, 197, 94))
    
    # Candlestick chart simulation
    d.rounded_rectangle([80, 350, w-80, h-80], radius=14, fill=(22, 16, 10), outline=(60, 45, 25))
    d.text((110, 375), "LIVE CANDLESTICK CHART & ORDER DEPTH", font=f_md, fill=(255, 255, 255))
    
    for i in range(24):
        cx = 120 + i * 55
        is_green = (i % 3 != 0)
        col = (34, 197, 94) if is_green else (239, 68, 68)
        top_wick = 450 + (i * 7) % 80
        bot_wick = top_wick + 160 + (i * 5) % 90
        d.line([(cx + 15, top_wick), (cx + 15, bot_wick)], fill=col, width=2)
        body_top = top_wick + 30
        body_bot = bot_wick - 40
        d.rectangle([cx, body_top, cx + 30, body_bot], fill=col)
        
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "PNG", optimize=True)
    print(f"Saved: {path}")

def create_cyber_os_mockup(path):
    w, h = 1600, 900
    img = Image.new("RGB", (w, h), (10, 8, 18))
    d = ImageDraw.Draw(img)
    
    f_lg = get_font(28)
    f_md = get_font(20)
    f_sm = get_font(16)
    f_title = get_font(34)
    
    d.rectangle([0, 0, w, h], fill=(8, 6, 14))
    d.rounded_rectangle([40, 40, w-40, h-40], radius=16, fill=(16, 12, 28), outline=(80, 40, 110), width=2)
    d.rounded_rectangle([40, 40, w-40, 110], radius=16, fill=(24, 18, 42))
    d.rectangle([40, 90, w-40, 110], fill=(24, 18, 42))
    d.ellipse([70, 70, 84, 84], fill=(239, 68, 68))
    d.ellipse([94, 70, 108, 84], fill=(234, 179, 8))
    d.ellipse([118, 70, 132, 84], fill=(34, 197, 94))
    d.rounded_rectangle([200, 60, w-200, 92], radius=8, fill=(12, 8, 20), outline=(70, 35, 95))
    d.text((220, 66), "https://aviraltrivedi.in - 3D Cyber OS Terminal Portfolio", font=f_sm, fill=(210, 160, 240))
    
    d.text((80, 132), "AVIRAL CYBER OS v3.0 - Interactive 3D Web Environment", font=f_title, fill=(255, 255, 255))
    d.rounded_rectangle([w-260, 130, w-80, 170], radius=18, fill=(236, 72, 153))
    d.text((w-240, 140), "Three.js Engine", font=f_sm, fill=(255, 255, 255))
    
    # Left CLI Terminal Box
    d.rounded_rectangle([80, 200, 700, h-80], radius=14, fill=(12, 9, 22), outline=(147, 51, 234), width=1)
    d.text((110, 230), "CYBER_TERMINAL [BASH]", font=f_md, fill=(236, 72, 153))
    
    lines = [
        "aviral@cyber-os:~$ whoami",
        "-> Aviral Trivedi (Full Stack Developer)",
        "aviral@cyber-os:~$ cat skills.json",
        "-> [React, Next.js, Three.js, Node.js, Tailwind, GSAP]",
        "aviral@cyber-os:~$ fetch --projects",
        "-> 1. Kanpur Metro Safar Guide (PWA)",
        "-> 2. SmartBudget AI (Finance Assistant)",
        "-> 3. CryptoDashboard (Live Trading)",
        "aviral@cyber-os:~$ launch --mode 3d",
        "-> Initializing WebGL Renderer... OK [60 FPS]"
    ]
    for idx, l in enumerate(lines):
        d.text((110, 275 + idx * 42), l, font=f_md, fill=(6, 182, 212) if "aviral@" in l else (220, 220, 240))

    # Right: 3D Wireframe Grid Simulation
    d.rounded_rectangle([730, 200, w-80, h-80], radius=14, fill=(14, 10, 25), outline=(236, 72, 153), width=1)
    d.text((760, 230), "3D CANVAS SCENE (THREE.JS / WEBGL)", font=f_md, fill=(255, 255, 255))
    
    vanish_x, vanish_y = 1150, 420
    for gx in range(750, w-80, 45):
        d.line([(gx, h-100), (vanish_x, vanish_y)], fill=(120, 30, 150), width=1)
    for gy in range(450, h-100, 30):
        d.line([(750, gy), (w-100, gy)], fill=(80, 20, 110), width=1)
        
    d.polygon([(1050, 340), (1250, 340), (1300, 450), (1100, 450)], outline=(6, 182, 212), fill=(10, 30, 50))
    d.polygon([(1050, 340), (1100, 450), (1100, 570), (1050, 460)], outline=(236, 72, 153), fill=(40, 10, 35))
    d.polygon([(1100, 450), (1300, 450), (1300, 570), (1100, 570)], outline=(6, 182, 212), fill=(15, 25, 45))
    d.text((1130, 490), "3D MESH", font=f_md, fill=(255, 255, 255))
    
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "PNG", optimize=True)
    print(f"Saved: {path}")

def main():
    create_metro_mockup("public/projects/kanpur-metro.png")
    create_budget_mockup("public/projects/smartbudget.png")
    create_crypto_mockup("public/projects/cryptodashboard.png")
    create_cyber_os_mockup("public/projects/cyber-os.png")

if __name__ == "__main__":
    main()
