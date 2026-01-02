from generate_image import generate_image
from generate_video import generate_video

prompt = "Cinematic hoodie floating in neon cyberpunk city"

img_path = "outputs/images/frame.png"
vid_path = "outputs/videos/video.mp4"

generate_image(prompt, img_path)
generate_video(img_path, vid_path)

print("✅ Video generated:", vid_path)

import torch
torch.cuda.empty_cache()

