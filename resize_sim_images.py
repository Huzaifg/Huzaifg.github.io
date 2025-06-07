import os
from PIL import Image

# Set your source and destination directories
src_dir = "assets/img/simulations"
dst_dir = os.path.join(src_dir, "resized")

# Create destination directory if it doesn't exist
os.makedirs(dst_dir, exist_ok=True)

max_width = 600  # pixels

for filename in os.listdir(src_dir):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, filename)
        with Image.open(src_path) as img:
            w, h = img.size
            if w > max_width:
                new_height = int(h * max_width / w)
                img = img.resize((max_width, new_height), Image.LANCZOS)
            img.save(dst_path)
        print(f"Resized {filename} -> {dst_path}") 