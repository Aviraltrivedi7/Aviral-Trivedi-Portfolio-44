import os
import numpy as np
import onnxruntime as ort
from PIL import Image

def main():
    input_image_path = r"C:\Users\trive\.gemini\antigravity-ide\brain\08642518-4109-4e92-bc4f-db6bb45e2f6c\.user_uploaded\media_1787052000924.jpg"
    print(f"Loading input image: {input_image_path}", flush=True)
    img = Image.open(input_image_path).convert("RGB")
    orig_w, orig_h = img.size
    print(f"Original size: {orig_w}x{orig_h}", flush=True)
    
    cache_dir = os.path.join(os.path.expanduser("~"), ".cache_models")
    model_path = os.path.join(cache_dir, "u2net.onnx")
    if not os.path.exists(model_path):
        model_path = os.path.join(cache_dir, "u2netp.onnx")
    
    print(f"Loading ONNX model from: {model_path}", flush=True)
    session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])
    
    # Preprocess
    img_resized = img.resize((320, 320), Image.Resampling.BILINEAR)
    img_np = np.array(img_resized, dtype=np.float32) / 255.0
    mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
    std = np.array([0.229, 0.224, 0.225], dtype=np.float32)
    img_norm = (img_np - mean) / std
    input_tensor = np.transpose(img_norm, (2, 0, 1))[np.newaxis, ...]
    
    # Run inference
    input_name = session.get_inputs()[0].name
    outputs = session.run(None, {input_name: input_tensor})
    mask = outputs[0][0, 0]
    mask = (mask - mask.min()) / (mask.max() - mask.min() + 1e-8)
    mask = (mask * 255).astype(np.uint8)
    
    # Resize mask
    mask_pil = Image.fromarray(mask, mode="L").resize((orig_w, orig_h), Image.Resampling.LANCZOS)
    
    # Apply alpha mask
    cutout = img.convert("RGBA")
    cutout.putalpha(mask_pil)
    
    # Find bounding box
    alpha = np.array(mask_pil)
    bbox_mask = alpha > 25
    ys, xs = np.where(bbox_mask)
    if len(xs) > 0 and len(ys) > 0:
        # Crop with slight top margin and down to bottom of person
        min_x = max(0, int(xs.min()))
        max_x = min(orig_w, int(xs.max()))
        min_y = max(0, int(ys.min()))
        max_y = min(orig_h, int(ys.max()))
        bbox = (min_x, min_y, max_x, max_y)
    else:
        bbox = (0, 0, orig_w, orig_h)
        
    print(f"Bounding box: {bbox}", flush=True)
    cropped = cutout.crop(bbox)
    cw, ch = cropped.size
    print(f"Cropped person size: {cw}x{ch}", flush=True)
    
    # Full size portrait canvas (900 x 1350)
    target_w, target_h = 900, 1350
    canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    
    # Scale person so that it stands tall taking ~95% of vertical space, anchored at bottom
    scale = (target_h * 0.95) / ch
    if cw * scale > target_w * 0.98:
        scale = (target_w * 0.98) / cw
        
    new_w = int(cw * scale)
    new_h = int(ch * scale)
    resized_person = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Position: center horizontally, anchor to very bottom
    pos_x = (target_w - new_w) // 2
    pos_y = target_h - new_h
    canvas.paste(resized_person, (pos_x, pos_y), resized_person)
    
    # Save to all target paths
    for filename in ["avatar.png", "profile.png", "hero-portrait.png", "aviral-full.png"]:
        p = os.path.join("public", "images", filename)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        canvas.save(p, "PNG", optimize=True)
        print(f"Saved: {p}", flush=True)
        
    prof_path = os.path.join("public", "profile.png")
    canvas.save(prof_path, "PNG", optimize=True)
    print(f"Saved: {prof_path}", flush=True)
    
    canvas.save("image.png", "PNG", optimize=True)
    print("Saved: image.png", flush=True)
    
    # Profile card
    card_w, card_h = 450, 671
    card_bg = Image.new("RGBA", (card_w, card_h), (18, 18, 20, 255))
    card_scale = (card_h * 0.90) / ch
    if cw * card_scale > card_w * 0.95:
        card_scale = (card_w * 0.95) / cw
    card_cw = int(cw * card_scale)
    card_ch = int(ch * card_scale)
    card_sub = cropped.resize((card_cw, card_ch), Image.Resampling.LANCZOS)
    card_bg.paste(card_sub, ((card_w - card_cw) // 2, card_h - card_ch), card_sub)
    card_bg.convert("RGB").save(os.path.join("public", "profile-card.webp"), "WEBP", quality=92)
    print("Saved profile-card.webp", flush=True)
    print("FULL SIZE PORTRAIT COMPLETE!", flush=True)

if __name__ == "__main__":
    main()
