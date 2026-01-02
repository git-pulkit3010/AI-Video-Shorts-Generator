#!/bin/bash
set -e

mkdir -p models/sdxl models/svd

# SDXL Turbo
huggingface-cli download \
  stabilityai/sdxl-turbo \
  --local-dir models/sdxl \
  --local-dir-use-symlinks False

# Stable Video Diffusion
huggingface-cli download \
  stabilityai/stable-video-diffusion-img2vid-xt \
  --local-dir models/svd \
  --local-dir-use-symlinks False

