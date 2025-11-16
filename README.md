# 🎨 AI Icon Generator

Generate custom icons using AI-powered Stable Diffusion directly in Google Colab with an easy-to-use web interface.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Colab](https://img.shields.io/badge/platform-Google%20Colab-orange.svg)

## ✨ Features

- 🚀 **GPU-Accelerated**: Leverages Google Colab's free GPU for fast generation
- 🎭 **Multiple Styles**: Choose from 6 pre-built icon styles
- 🖼️ **High Quality**: Generates 512x512px icons using Stable Diffusion v1.5
- 🌐 **Web Interface**: User-friendly Gradio interface with shareable public URL
- ⚡ **Optimized**: Memory-efficient with attention slicing and float16 precision

## 🎭 Available Styles

- Flat Minimalist
- Line Art
- Gradient Modern
- 3D Cute
- Neon Glow
- Hand Drawn

## 🚀 Quick Start

### Option 1: Run in Google Colab (Recommended)

1. Open [Google Colab](https://colab.research.google.com/)
2. Create a new notebook
3. Copy and paste the code from `icon_generator.py`
4. Run all cells
5. Click the generated public URL to access the interface

### Option 2: Local Installation

**Requirements:**
- Python 3.8+
- CUDA-compatible GPU (recommended)
- 8GB+ VRAM

**Install dependencies:**
```bash
pip install diffusers transformers torch accelerate gradio
```

**Run the script:**
```bash
python icon_generator.py
```

## 📖 Usage

1. **Enter Description**: Type what icon you want (e.g., "coffee cup", "rocket", "heart")
2. **Select Style**: Choose from dropdown menu
3. **Adjust Quality**: Use slider (20-50 steps) - higher is better but slower
4. **Generate**: Click submit and wait 10-30 seconds
5. **Download**: Right-click on the generated icon to save

### Example Prompts

```
"shopping cart" + flat minimalist → Clean e-commerce icon
"rocket ship" + gradient modern → Futuristic startup logo
"heart" + 3d cute → Adorable love symbol
"lightning bolt" + neon glow → Electric energy icon
```

## 🛠️ Technical Details

- **Model**: Stable Diffusion v1.5 (runwayml/stable-diffusion-v1-5)
- **Framework**: PyTorch with Diffusers library
- **Interface**: Gradio
- **Output**: 512x512px PNG images
- **Optimization**: FP16 precision, attention slicing

## ⚙️ Configuration

Adjust these parameters in the code:

```python
# Image quality vs speed
num_inference_steps=25  # 20-50 recommended

# Prompt adherence
guidance_scale=7.5  # 7-12 recommended

# Image size
width=512, height=512  # Keep square for icons
```

## 📝 Requirements

```
diffusers>=0.21.0
transformers>=4.30.0
torch>=2.0.0
accelerate>=0.20.0
gradio>=3.40.0
```

## 🐛 Troubleshooting

**Out of Memory Error:**
- Reduce `num_inference_steps`
- Ensure GPU runtime is enabled in Colab
- Restart runtime and try again

**Slow Generation:**
- Verify GPU is being used (check Colab runtime type)
- Lower the quality slider

**Model Download Issues:**
- Check internet connection
- Model downloads automatically on first run (~4GB)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Stability AI](https://stability.ai/) for Stable Diffusion
- [Hugging Face](https://huggingface.co/) for the Diffusers library
- [Gradio](https://gradio.app/) for the web interface

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues).

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

⭐ If you find this project useful, please consider giving it a star!
