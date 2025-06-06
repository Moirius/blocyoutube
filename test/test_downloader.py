import sys
import os

sys.path.append(os.path.abspath("."))  # <- ajoute tiktokbot/ au path

import importlib.util

spec = importlib.util.find_spec("yt_dlp")
if spec is None:
    print("SKIPPED: yt_dlp non installé")
    sys.exit(0)

from generators.youtube import downloader


# Lien test
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
slug = "test_rick"

path = downloader.download(video_url, slug)
print(f"✅ Vidéo téléchargée à : {path}")
