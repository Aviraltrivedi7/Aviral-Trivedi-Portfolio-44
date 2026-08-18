import os
import numpy as np
import onnxruntime as ort
from PIL import Image, ImageFilter, ImageEnhance

def main():
    input_path = r"C:\Users\trive\.gemini\antigravity-ide\brain\08642518-4109-4e92-bc4f-db6bb45e2f6c\.user_uploaded\media_1787052000924.jpg"
    print(f"Reading user photo from: {input_path}")
    img = Image.open(input_path).convert("RGB")
    orig_w, orig_h = img.size
    
    # Load u2net model
    model_path = os.path.join(os.path.expanduser("~"), ".cache_models", "u2net.onnx")
    if not os.path.exists(model_path):
        model_path = os.path.join(os.path.expanduser("~"), ".cache_models", "u2netp.onnx")
    
    print(f"Using model: {model_path}")
    session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])
    
    # Run segmentation
    img_resized = img.resize((320, 320), Image.Resampling.BILINEAR)
    img_np = np.array(img_resized, dtype=np.float32) / 255.0
    mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
    std = np.array([0.229, 0.224, 0.225], dtype=np.float32)
    img_norm = (img_np - mean) / std
    input_tensor = np.transpose(img_norm, (2, 0, 1))[np.newaxis, ...]
    
    input_name = session.get_inputs()[0].name
    outputs = session.run(None, {input_name: input_tensor})
    mask = outputs[0][0, 0]
    mask = (mask - mask.min()) / (mask.max() - mask.min() + 1e-8)
    mask = (mask * 255).astype(np.uint8)
    
    mask_pil = Image.fromarray(mask, mode="L").resize((orig_w, orig_h), Image.Resampling.LANCZOS)
    
    # Smooth mask edges slightly
    mask_pil = mask_pil.filter(ImageFilter.GaussianBlur(radius=1.0))
    
    cutout = img.convert("RGBA")
    cutout.putalpha(mask_pil)
    
    # Find bounding box
    alpha = np.array(mask_pil)
    bbox_mask = alpha > 30
    ys, xs = np.where(bbox_mask)
    min_x = max(0, int(xs.min()))
    max_x = min(orig_w, int(xs.max()))
    min_y = max(0, int(ys.min()))
    max_y = min(orig_h, int(ys.max()))
    bbox = (min_x, min_y, max_x, max_y)
    
    cropped = cutout.crop(bbox)
    cw, ch = cropped.size
    print(f"Cropped person size: {cw}x{ch}")
    
    # Create smooth bottom gradient fade on the alpha channel (last 15% of height)
    cropped_np = np.array(cropped)
    fade_len = int(ch * 0.16) # fade bottom 16%
    for i in range(fade_len):
        row_idx = ch - fade_len + i
        # Linear/cosine fade factor from 1.0 down to 0.0
        factor = (fade_len - i) / float(fade_len)
        factor = factor * factor # smooth ease-in
        cropped_np[row_idx, :, 3] = (cropped_np[row_idx, :, 3] * factor).astype(np.uint8)
        
    faded_cutout = Image.fromarray(cropped_np, mode="RGBA")
    
    # Canvas for hero: 900 x 1350
    target_w, target_h = 900, 1350
    canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    
    # Scale person so head is nicely positioned near top and body reaches bottom
    scale = (target_h * 0.96) / ch
    if cw * scale > target_w * 0.95:
        scale = (target_w * 0.95) / cw
        
    new_w = int(cw * scale)
    new_h = int(ch * scale)
    resized = faded_cutout.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    pos_x = (target_w - new_w) // 2
    pos_y = target_h - new_h
    canvas.paste(resized, (pos_x, pos_y), resized)
    
    # Save color version
    for fname in ["aviral-full.png", "avatar.png", "profile.png", "hero-portrait.png"]:
        p = os.path.join("public", "images", fname)
        canvas.save(p, "PNG", optimize=True)
        print(f"Saved: {p}")
        
    # Save root image.png and public/profile.png
    canvas.save("image.png", "PNG", optimize=True)
    canvas.save(os.path.join("public", "profile.png"), "PNG", optimize=True)
    
    # Create stylish profile-card.webp
    card_w, card_h = 450, 671
    card_bg = Image.new("RGBA", (card_w, card_h), (18, 18, 20, 255))
    c_scale = (card_h * 0.92) / ch
    if cw * c_scale > card_w * 0.92:
        c_scale = (card_w * 0.92) / cw
    card_pw = int(cw * c_scale)
    card_ph = int(ch * c_scale)
    card_sub = faded_cutout.resize((card_pw, card_ph), Image.Resampling.LANCZOS)
    card_bg.paste(card_sub, ((card_w - card_pw) // 2, card_h - card_ph), card_sub)
    card_bg.convert("RGB").save(os.path.join("public", "profile-card.webp"), "WEBP", quality=92)
    print("Saved public/profile-card.webp")
    print("CINEMATIC PORTRAIT READY!")

if __name__ == "__main__":
    main()
