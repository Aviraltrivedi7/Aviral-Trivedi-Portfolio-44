import os
import sys
from PIL import Image
from rembg import remove

def process():
    input_path = r"C:\Users\trive\.gemini\antigravity-ide\brain\08642518-4109-4e92-bc4f-db6bb45e2f6c\.user_uploaded\media_1787047088273.jpg"
    print(f"Reading input image from: {input_path}")
    
    img = Image.open(input_path).convert("RGBA")
    print(f"Original image size: {img.size}")
    
    print("Removing background...")
    cutout = remove(img)
    
    # Get bounding box of non-transparent pixels
    bbox = cutout.getbbox()
    print(f"Subject bounding box: {bbox}")
    
    # Crop to subject bounding box
    cropped = cutout.crop(bbox)
    cw, ch = cropped.size
    print(f"Cropped subject size: {cw}x{ch}")
    
    # Target size for hero profile image: 818 x 1220 (crisp 2x retina of 409x610)
    target_w, target_h = 818, 1220
    canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    
    # Scale subject so that it fills nicely from near top to bottom
    # We want subject height to take about 85-90% of canvas height, anchored at bottom
    avail_h = int(target_h * 0.88)
    scale = avail_h / ch
    if cw * scale > target_w * 0.95:
        scale = (target_w * 0.95) / cw
        
    new_w = int(cw * scale)
    new_h = int(ch * scale)
    resized_subject = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Position: horizontally centered, aligned to bottom with small margin
    pos_x = (target_w - new_w) // 2
    pos_y = target_h - new_h
    
    canvas.paste(resized_subject, (pos_x, pos_y), resized_subject)
    
    # Save to public/images/profile.png
    out_hero = os.path.join("public", "images", "profile.png")
    os.makedirs(os.path.dirname(out_hero), exist_ok=True)
    canvas.save(out_hero, "PNG", optimize=True)
    print(f"Saved hero image to: {out_hero}")
    
    # Save high-res to public/profile.png
    out_profile = os.path.join("public", "profile.png")
    canvas.save(out_profile, "PNG", optimize=True)
    print(f"Saved high-res profile to: {out_profile}")
    
    # Also save to root image.png if needed
    canvas.save("image.png", "PNG", optimize=True)
    print("Saved image.png")
    
    # Also create profile-card.webp (450 x 671)
    card_w, card_h = 450, 671
    # Card can have a dark stylish gradient or transparent background with portrait centered
    card_bg = Image.new("RGBA", (card_w, card_h), (18, 18, 20, 255))
    
    # Resize subject for card
    card_scale = (card_h * 0.82) / ch
    if cw * card_scale > card_w * 0.9:
        card_scale = (card_w * 0.9) / cw
    card_sub_w = int(cw * card_scale)
    card_sub_h = int(ch * card_scale)
    card_sub = cropped.resize((card_sub_w, card_sub_h), Image.Resampling.LANCZOS)
    
    card_px = (card_w - card_sub_w) // 2
    card_py = card_h - card_sub_h
    card_bg.paste(card_sub, (card_px, card_py), card_sub)
    
    out_card = os.path.join("public", "profile-card.webp")
    card_bg.convert("RGB").save(out_card, "WEBP", quality=90)
    print(f"Saved profile-card to: {out_card}")

if __name__ == "__main__":
    process()
