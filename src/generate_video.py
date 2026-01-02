import torch
from diffusers import StableVideoDiffusionPipeline
from PIL import Image
import imageio


def generate_video(image_path, output_path):
    pipe = StableVideoDiffusionPipeline.from_pretrained(
        "setups/models/svd",
        torch_dtype=torch.float16,
        variant="fp16",
        use_safetensors=True,
    )

    # MEMORY OPTIMIZATION
    pipe.enable_attention_slicing()
    pipe.enable_sequential_cpu_offload()

    # ⚠️ DO NOT CALL pipe.to("cuda") when using offload

    image = Image.open(image_path).convert("RGB")

    frames = pipe(
        image,
        num_frames=14,        # sweet spot
        fps=7,
        motion_bucket_id=90,  # smoother motion
        noise_aug_strength=0.015,
        decode_chunk_size=2
    ).frames[0]
    
    # Loop the video smoothly
    frames = frames + frames[::-1]


    imageio.mimsave(output_path, frames, fps=6)

    print(f"✅ Video saved to {output_path}")

