import os
import numpy as np
import onnxruntime as ort
from PIL import Image, ImageFilter, ImageEnhance

def main():
    input_path = r"C:\Users\trive\.gemini\antigravity-ide\brain\08642518-4109-4e92-bc4f-db6bb45e2f6c\.user_uploaded\media_1787052000924.jpg"
    print(f"Loading user photo: {input_path}")
    img = Image.open(input_path).convert("RGB")
    orig_w, orig_h = img.size
    
    # Load u2net model
    model_path = os.path.join(os.path.expanduser("~"), ".cache_models", "u2net.onnx")
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
    mask_pil = mask_pil.filter(ImageFilter.GaussianBlur(radius=1.0))
    
    cutout = img.convert("RGBA")
    cutout.putalpha(mask_pil)
    
    # Get bounding box of full person
    alpha = np.array(mask_pil)
    ys, xs = np.where(alpha > 30)
    min_x, max_x = int(xs.min()), int(xs.max())
    min_y, max_y = int(ys.min()), int(ys.max())
    
    person_w = max_x - min_x
    person_h = max_y - min_y
    print(f"Full person box: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}], w={person_w}, h={person_h}")
    
    # We want a classic Bust / Upper Torso Crop (from mid-chest/upper arms up to hair)
    # Head top is min_y (~202).
    # Head height is approx ~180px.
    # Shoulders are at ~380px.
    # Mid-chest / upper torso is around y = min_y + int(person_h * 0.58) (~680px).
    bust_top = max(0, min_y - 20)
    bust_bottom = min(orig_h, min_y + int(person_h * 0.65)) # includes chest and shoulders
    bust_left = max(0, min_x - 10)
    bust_right = min(orig_w, max_x + 10)
    
    bust = cutout.crop((bust_left, bust_top, bust_right, bust_bottom))
    bw, bh = bust.size
    print(f"Bust crop size: {bw}x{bh}")
    
    # Apply a soft feather gradient on the bottom 18% of the bust so it fades to transparent
    bust_np = np.array(bust)
    fade_h = int(bh * 0.18)
    for i in range(fade_h):
        row = bh - fade_h + i
        frac = (fade_h - i) / float(fade_h)
        factor = frac * frac
        bust_np[row, :, 3] = (bust_np[row, :, 3] * factor).astype(np.uint8)
        
    faded_bust = Image.fromarray(bust_np, mode="RGBA")
    
    # Place on 800 x 1000 canvas with optimal proportion for Hero
    target_w, target_h = 800, 1000
    canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    
    # Scale to fit nicely with ~90% height
    s = (target_h * 0.92) / bh
    if bw * s > target_w * 0.94:
        s = (target_w * 0.94) / bw
        
    rw = int(bw * s)
    rh = int(bh * s)
    resized_bust = faded_bust.resize((rw, rh), Image.Resampling.LANCZOS)
    
    px = (target_w - rw) // 2
    py = target_h - rh # bottom anchored on canvas
    canvas.paste(resized_bust, (px, py), resized_bust)
    
    # Save to all image destinations
    for fn in ["avatar.png", "aviral-full.png", "profile.png", "hero-portrait.png"]:
        p = os.path.join("public", "images", fn)
        canvas.save(p, "PNG", optimize=True)
        print(f"Saved: {p}")
        
    canvas.save("image.png", "PNG", optimize=True)
    canvas.save(os.path.join("public", "profile.png"), "PNG", optimize=True)
    print("SUCCESS: Perfect template-matched bust portrait generated!")

if __name__ == "__main__":
    main()
