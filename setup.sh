#!/bin/bash
set -e

echo "[1/3] Mise à jour des paquets système..."
apt-get update

echo "[2/3] Installation des bibliothèques système nécessaires..."
apt-get install -y \
    build-essential \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1 \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libfreetype6-dev \
    libtiff5-dev \
    libavformat-dev \
    libavcodec-dev \
    libavdevice-dev \
    libavutil-dev \
    libswscale-dev \
    libxrender-dev \
    curl \
    git \
    python3-dev \
    python3-pip

echo "[3/3] Installation des dépendances Python..."
pip install --upgrade pip
pip install --prefer-binary -r requirements.txt
