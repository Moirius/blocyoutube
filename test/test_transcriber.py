import sys
import os

sys.path.append(os.path.abspath("."))

import importlib.util

spec = importlib.util.find_spec("whisper")
if spec is None:
    print("SKIPPED: whisper non installé")
    sys.exit(0)

from generators.youtube import transcriber

slug = "test_rick"  # même dossier que tu as utilisé pour download
segments = transcriber.transcribe(slug)

print(f"📄 Transcription obtenue avec {len(segments)} segments.")
