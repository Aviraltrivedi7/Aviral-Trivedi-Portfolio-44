import os
import urllib.request
import numpy as np
import onnxruntime as ort
from PIL import Image

def download_model(model_name="u2netp.onnx"):
    cache_dir = os.path.join(os.path.expanduser("~"), ".cache_models")
    os.makedirs(cache_dir, exist_ok=True)
    model_path = os.path.join(cache_dir, model_name)
    if not os.path.exists(model_path):
        url = f"https://github.com/danielgatis/rembg/releases/download/v0.0.0/{model_name}"
        print(f"Downloading {model_name} from {url} ...", flush=True)
        urllib.request.urlretrieve(url, model_path)
        print("Download complete!", flush=True)
    else:
        print(f"Using cached model: {model_path}", flush=True)
    return model_path

def remove_background(img_pil, session):
    orig_w, orig_h = img_pil.size
    
    # Preprocess
    img_resized = img_pil.convert("RGB").resize((320, 320), Image.Resampling.BILINEAR)
    img_np = np.array(img_resized, dtype=np.float32) / 255.0
    
    # Normalize: mean = [0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225]
    mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
    std = np.array([0.229, 0.224, 0.225], dtype=np.float32)
    img_norm = (img_np - mean) / std
    
    # Transpose to (1, 3, 320, 320)
    input_tensor = np.transpose(img_norm, (2, 0, 1))[np.newaxis, ...]
    
    # Run inference
    input_name = session.get_inputs()[0].name
    outputs = session.run(None, {input_name: input_tensor})
    
    # Extract mask
    mask = outputs[0][0, 0] # (320, 320)
    # Min-max normalization
    mask_min = mask.min()
    mask_max = mask.max()
    mask = (mask - mask_min) / (mask_max - mask_min + 1e-8)
    mask = (mask * 255).astype(np.uint8)
    
    # Resize mask to original size
    mask_pil = Image.fromarray(mask, mode="L").resize((orig_w, orig_h), Image.Resampling.BILINEAR)
    
    # Apply mask
    result = img_pil.convert("RGBA")
    result.putalpha(mask_pil)
    return result

def main():
    input_image_path = r"C:\Users\trive\.gemini\antigravity-ide\brain\08642518-4109-4e92-bc4f-db6bb45e2f6c\.user_uploaded\media_1787047088273.jpg"
    print(f"Loading input image: {input_image_path}", flush=True)
    img = Image.open(input_image_path)
    
    model_path = download_model("u2netp.onnx")
    print("Creating ONNX Runtime session...", flush=True)
    session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])
    
    print("Segmenting image...", flush=True)
    cutout = remove_background(img, session)
    
    # Get bounding box of alpha > 20
    alpha = np.array(cutout.split()[-1])
    bbox_mask = alpha > 25
    ys, xs = np.where(bbox_mask)
    if len(xs) > 0 and len(ys) > 0:
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max()))
    else:
        bbox = (0, 0, cutout.width, cutout.height)
    print(f"Detected bounding box: {bbox}", flush=True)
    
    cropped = cutout.crop(bbox)
    cw, ch = cropped.size
    print(f"Cropped person size: {cw}x{ch}", flush=True)
    
    # 1. Generate public/images/profile.png (Hero portrait)
    # Dimensions: 818 x 1220 (crisp high-DPI version of 409x610)
    target_w, target_h = 818, 1220
    canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    
    # Fill about 92% of vertical space, aligned to bottom
    avail_h = int(target_h * 0.92)
    scale = avail_h / ch
    if cw * scale > target_w * 0.96:
        scale = (target_w * 0.96) / cw
        
    new_w = int(cw * scale)
    new_h = int(ch * scale)
    resized_subject = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    pos_x = (target_w - new_w) // 2
    pos_y = target_h - new_h
    canvas.paste(resized_subject, (pos_x, pos_y), resized_subject)
    
    hero_path = os.path.join("public", "images", "profile.png")
    os.makedirs(os.path.dirname(hero_path), exist_ok=True)
    canvas.save(hero_path, "PNG", optimize=True)
    print(f"Saved hero image: {hero_path}", flush=True)
    
    # 2. Save public/profile.png
    prof_path = os.path.join("public", "profile.png")
    canvas.save(prof_path, "PNG", optimize=True)
    print(f"Saved public/profile.png: {prof_path}", flush=True)
    
    # 3. Save root image.png
    canvas.save("image.png", "PNG", optimize=True)
    print("Saved root image.png", flush=True)
    
    # 4. Generate public/profile-card.webp (450 x 671)
    card_w, card_h = 450, 671
    card_bg = Image.new("RGBA", (card_w, card_h), (20, 20, 22, 255))
    
    card_scale = (card_h * 0.85) / ch
    if cw * card_scale > card_w * 0.92:
        card_scale = (card_w * 0.92) / cw
    c_w = int(cw * card_scale)
    c_h = int(ch * card_scale)
    card_sub = cropped.resize((c_w, c_h), Image.Resampling.LANCZOS)
    
    c_x = (card_w - c_w) // 2
    c_y = card_h - c_h
    card_bg.paste(card_sub, (c_x, c_y), card_sub)
    
    card_path = os.path.join("public", "profile-card.webp")
    card_bg.convert("RGB").save(card_path, "WEBP", quality=90)
    print(f"Saved card image: {card_path}", flush=True)
    
    print("ALL ASSETS GENERATED SUCCESSFULLY!", flush=True)

if __name__ == "__main__":
    main()
