import os
from PIL import Image, ImageDraw, ImageFont

def make_card(title, subtitle, tag, color_accent, output_path):
    w, h = 800, 500
    img = Image.new("RGB", (w, h), (14, 14, 16))
    draw = ImageDraw.Draw(img)
    
    # Draw dark glass card background
    draw.rectangle([0, 0, w, h], fill=(16, 16, 20))
    
    # Draw soft radial accent glow in top right
    for r in range(250, 0, -5):
        alpha = int((250 - r) / 250.0 * 22)
        # Approximate glow with nested ellipses
        bbox = [w - 180 - r, 30 - r, w - 180 + r, 30 + r]
        draw.ellipse(bbox, fill=(color_accent[0]//6, color_accent[1]//6, color_accent[2]//6))
        
    # Draw inner card border
    draw.rectangle([20, 20, w - 20, h - 20], outline=(40, 40, 48), width=2)
    
    # Top status pill
    draw.rounded_rectangle([45, 45, 180, 80], radius=16, fill=(25, 25, 32), outline=color_accent, width=1)
    
    # Mockup browser header bar
    draw.rounded_rectangle([45, 110, w - 45, h - 45], radius=12, fill=(20, 20, 25), outline=(50, 50, 60), width=1)
    # Window dots
    draw.ellipse([65, 128, 77, 140], fill=(239, 68, 68))
    draw.ellipse([85, 128, 97, 140], fill=(234, 179, 8))
    draw.ellipse([105, 128, 117, 140], fill=(34, 197, 94))
    
    # Mock search bar
    draw.rounded_rectangle([140, 124, w - 80, 144], radius=6, fill=(30, 30, 38))
    
    # Content area inside mockup
    draw.rectangle([46, 160, w - 46, h - 46], fill=(12, 12, 15))
    
    # Grid lines / futuristic UI lines
    for y in range(180, h - 60, 40):
        draw.line([(60, y), (w - 60, y)], fill=(22, 22, 28), width=1)
    for x in range(80, w - 60, 80):
        draw.line([(x, 180), (x, h - 60)], fill=(22, 22, 28), width=1)
        
    # Hero highlight bar in center of mockup
    draw.rounded_rectangle([80, 210, w - 80, 360], radius=10, fill=(22, 22, 30), outline=(color_accent[0]//2, color_accent[1]//2, color_accent[2]//2), width=1)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    print(f"Created project card: {output_path}")

def main():
    projects = [
        ("Kanpur Metro Safar Guide", "Metro Navigation PWA", "Live PWA", (6, 182, 212), "public/projects/kanpur-metro.png"),
        ("SmartBudget AI", "AI Personal Finance Assistant", "AI Powered", (16, 185, 129), "public/projects/smartbudget.png"),
        ("CryptoDashboard", "Real-Time Market Analytics", "Web3 Analytics", (245, 158, 11), "public/projects/cryptodashboard.png"),
        ("3D Cyber OS Portfolio", "Interactive Three.js Experience", "Interactive 3D", (168, 85, 247), "public/projects/cyber-os.png"),
        ("BARQ AI Assistant", "Next-Gen AI Workspace", "Featured App", (59, 130, 246), "public/projects/barq-ai-assistant.png"),
    ]
    for title, sub, tag, col, path in projects:
        make_card(title, sub, tag, col, path)

if __name__ == "__main__":
    main()
