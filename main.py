# Install
!pip install -q diffusers transformers torch accelerate gradio

# Code
import gradio as gr
import torch
from diffusers import StableDiffusionPipeline

print("🤖 Loading model...")
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",  # No auth needed
    torch_dtype=torch.float16
).to("cuda")

pipe.enable_attention_slicing()

def generate_icon(prompt, style, steps):
    full_prompt = f"{prompt}, {style} icon, simple, clean design, centered, white background"
    
    image = pipe(
        prompt=full_prompt,
        negative_prompt="complex, detailed, realistic, photo, text, watermark",
        num_inference_steps=40,
        guidance_scale=7.5,
        width=512,
        height=512
    ).images[0]
    
    return image

# Create interface
demo = gr.Interface(
    fn=generate_icon,
    inputs=[
        gr.Textbox(
            label="🎨 Icon Description",
            placeholder="coffee cup, rocket, heart, etc.",
            value="coffee cup"
        ),
        gr.Dropdown(
            choices=["flat minimalist", "line art", "gradient modern", "3d cute", "neon glow", "hand drawn"],
            label="🎭 Style",
            value="flat minimalist"
        ),
        gr.Slider(
            minimum=20,
            maximum=50,
            value=25,
            step=5,
            label="⚡ Quality (higher = better but slower)"
        )
    ],
    outputs=gr.Image(label="Generated Icon", type="pil"),
    title="🎨 AI Icon Generator",
    description="Generate custom icons using AI on Google Colab GPU",
    examples=[
        ["shopping cart", "flat minimalist", 25],
        ["rocket ship", "gradient modern", 30],
        ["heart", "3d cute", 25],
        ["lightning bolt", "neon glow", 25],
    ],
    theme=gr.themes.Soft()
)

print("✅ Launching app...")
demo.launch(share=True, debug=False)