import os
import urllib.request
import numpy as np
import onnxruntime as ort
from PIL import Image

def download_model(model_name="u2net.onnx"):
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

def remove_background_u2net(img_pil, session):
    orig_w, orig_h = img_pil.size
    
    # Preprocess (u2net uses 320x320)
    img_resized = img_pil.convert("RGB").resize((320, 320), Image.Resampling.BILINEAR)
    img_np = np.array(img_resized, dtype=np.float32) / 255.0
    
    mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
    std = np.array([0.229, 0.224, 0.225], dtype=np.float32)
    img_norm = (img_np - mean) / std
    
    input_tensor = np.transpose(img_norm, (2, 0, 1))[np.newaxis, ...]
    
    input_name = session.get_inputs()[0].name
    outputs = session.run(None, {input_name: input_tensor})
    
    mask = outputs[0][0, 0]
    mask_min = mask.min()
    mask_max = mask.max()
    mask = (mask - mask_min) / (mask_max - mask_min + 1e-8)
    mask = (mask * 255).astype(np.uint8)
    
    mask_pil = Image.fromarray(mask, mode="L").resize((orig_w, orig_h), Image.Resampling.LANCZOS)
    
    result = img_pil.convert("RGBA")
    result.putalpha(mask_pil)
    return result

def main():
    input_image_path = r"C:\Users\trive\.gemini\antigravity-ide\brain\08642518-4109-4e92-bc4f-db6bb45e2f6c\.user_uploaded\media_1787047088273.jpg"
    print(f"Loading input image: {input_image_path}", flush=True)
    img = Image.open(input_image_path)
    
    # Try u2net first, fallback to u2netp if needed
    try:
        model_path = download_model("u2net.onnx")
        print("Creating ONNX Runtime session with u2net full...", flush=True)
        session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])
    except Exception as e:
        print(f"Full u2net error ({e}), using u2netp...", flush=True)
        model_path = download_model("u2netp.onnx")
        session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])
    
    print("Segmenting image with high precision...", flush=True)
    cutout = remove_background_u2net(img, session)
    
    # Get bounding box of alpha > 25
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
    
    # Generate high quality avatar image
    target_w, target_h = 800, 1200
    canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    
    # Fit nicely vertically and horizontally
    scale = (target_h * 0.90) / ch
    if cw * scale > target_w * 0.95:
        scale = (target_w * 0.95) / cw
        
    new_w = int(cw * scale)
    new_h = int(ch * scale)
    resized_subject = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    pos_x = (target_w - new_w) // 2
    pos_y = target_h - new_h
    canvas.paste(resized_subject, (pos_x, pos_y), resized_subject)
    
    # Save multiple filenames to guarantee busting all Next.js caches
    for filename in ["avatar.png", "profile.png", "hero-portrait.png"]:
        p = os.path.join("public", "images", filename)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        canvas.save(p, "PNG", optimize=True)
        print(f"Saved: {p}", flush=True)
        
    prof_path = os.path.join("public", "profile.png")
    canvas.save(prof_path, "PNG", optimize=True)
    print(f"Saved: {prof_path}", flush=True)
    
    card_path = os.path.join("public", "profile-card.webp")
    # For profile card
    card_w, card_h = 450, 671
    card_bg = Image.new("RGBA", (card_w, card_h), (20, 20, 22, 255))
    card_scale = (card_h * 0.85) / ch
    if cw * card_scale > card_w * 0.92:
        card_scale = (card_w * 0.92) / cw
    c_w = int(cw * card_scale)
    c_h = int(ch * card_scale)
    card_sub = cropped.resize((c_w, c_h), Image.Resampling.LANCZOS)
    card_bg.paste(card_sub, ((card_w - c_w) // 2, card_h - c_h), card_sub)
    card_bg.convert("RGB").save(card_path, "WEBP", quality=92)
    print(f"Saved: {card_path}", flush=True)
    
    print("DONE_ALL", flush=True)

if __name__ == "__main__":
    main()
