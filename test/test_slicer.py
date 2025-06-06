import sys
import os

sys.path.append(os.path.abspath("."))

import importlib.util

spec = importlib.util.find_spec("moviepy")
if spec is None:
    print("SKIPPED: moviepy non installé")
    sys.exit(0)

from generators.youtube import slicer

slug = "test_rick"
segments = slicer.slice_video(slug)

print(f"✅ {len(segments)} clips créés.")
