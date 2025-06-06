# test/test_composer.py

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import importlib.util

for mod in ("moviepy", "PIL"):
    if importlib.util.find_spec(mod) is None:
        print(f"SKIPPED: {mod} non installé")
        sys.exit(0)

from generators.youtube.composer import compose_clip

if __name__ == "__main__":
    slug = "yt_1"
    part_filename = "part_1.mp4"
    part_number = 1

    try:
        output = compose_clip(slug, part_filename, part_number)
        print(f"✅ Clip généré avec succès : {output}")
    except Exception as e:
        print(f"❌ Échec du test : {e}")
