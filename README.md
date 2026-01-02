# AI Video Generator (RunPod / Headless)

This project generates **short cinematic videos** from text prompts using:
- **Stable Diffusion XL (SDXL)**
- **Stable Video Diffusion (SVD)**

Designed for:
- RunPod / GPU servers
- Headless environments (no GUI)
- Instagram / Reels / Shorts content creation

---

## 🚀 Features

- Text → Image → Video pipeline  
- Optimized for low VRAM GPUs (RTX 2000 Ada tested)
- Fully reproducible
- No GUI required
- Instagram-ready output
- Loopable video generation

---

## 📁 Project Structure

ai-video-generator/
├── README.md
├── requirements.txt
├── setup/
│ ├── model_downloads.sh
│ └── models/ # (Downloaded models live here)
├── src/
│ ├── generate_image.py
│ ├── generate_video.py
│ └── pipeline.py
├── outputs/
│ ├── images/
│ └── videos/
└── venv/


---

## 🧠 System Requirements

- GPU: NVIDIA (tested on RTX 2000 Ada)
- CUDA: 12.x
- Python: 3.10
- OS: Ubuntu 20.04+

---

## 🛠️ Setup Instructions

### 1️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate


pip install -r requirements.txt

bash setup/model_downloads.sh

This will populate:
setups/models/sdxl/
setups/models/svd/

### Run the Pipeline

python src/pipeline.py
