import torch
from diffusers import StableDiffusionXLPipeline

def generate_image(prompt, output_path):
    pipe = StableDiffusionXLPipeline.from_pretrained(
        "setups/models/sdxl",
        torch_dtype=torch.float16,
        variant="fp16",
        use_safetensors=True,
    ).to("cuda")

    image = pipe(
        prompt=prompt,
        num_inference_steps=12,
        guidance_scale=1.8,
        height=768,
        width=432,   # 9:16 ratio
    ).images[0]    
    
    image.save(output_path)


