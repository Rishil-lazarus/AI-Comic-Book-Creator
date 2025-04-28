from diffusers import StableDiffusionPipeline
from PIL import Image, ImageDraw, ImageFont
import torch, re, os

pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1")
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image_with_bubble(scene_text, prompt, output_dir, index):
    image = pipe(prompt, num_inference_steps=30, guidance_scale=7.5).images[0]
    img_path = os.path.join(output_dir, f"panel_{index}.jpg")
    image.save(img_path)

    quotes = re.findall(r'"(.*?)"', scene_text)
    if quotes:
        img = Image.open(img_path).convert("RGBA")
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        bubble = quotes[0]
        bbox = draw.textbbox((0, 0), bubble, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        x, y = 20, 20
        draw.rectangle([x-10, y-10, x + w + 20, y + h + 20], fill="white", outline="black")
        draw.text((x, y), bubble, font=font, fill="black")
        img.convert("RGB").save(img_path)

    return img_path
