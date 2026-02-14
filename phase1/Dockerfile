# Project SUPRA - Phase 1: SSBM AI Environment
# Base on Ubuntu 22.04 for compatibility with Dolphin dependencies
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies for Dolphin, libmelee, and headless display
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    xvfb \
    libgl1-mesa-dri \
    libgl1-mesa-glx \
    libglu1-mesa \
    libasound2 \
    libusb-1.0-0 \
    libqt5gui5 \
    libqt5widgets5 \
    libqt5core5a \
    libqt5network5 \
    libevdev2 \
    libpugixml1v5 \
    libswscale5 \
    libavformat58 \
    libavcodec58 \
    libavutil56 \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install libmelee and core ML libraries
RUN pip3 install melee torch numpy

# Create workspace
WORKDIR /app

# Note: In a real environment, we would download/copy the Slippi Dolphin AppImage or binary here.
# For this blueprint, we assume the binary 'dolphin-emu' is available or mapped via volume.
# For testing, we'll use a placeholder or install the PPA version if available.
RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository ppa:dolphin-emu/ppa && \
    apt-get update && apt-get install -y dolphin-emu || true

# Copy training scripts
COPY scripts/ /app/scripts/

# Setup entrypoint to handle Xvfb (Virtual Framebuffer) for headless rendering
RUN echo '#!/bin/bash\nXvfb :99 -screen 0 1280x720x24 &\nexport DISPLAY=:99\npython3 /app/scripts/agent.py "$@"' > /app/entrypoint.sh && \
    chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
