import os
import time
from utils.logger import get_logger

try:
    import whisper
except Exception:  # pragma: no cover - optional dependency
    whisper = None

logger = get_logger(__name__)

model_size = os.environ.get("WHISPER_MODEL", "small")
model = None
if whisper is not None:
    try:
        model = whisper.load_model(model_size)
    except Exception:
        logger.warning("Impossible de charger le modèle whisper")
        model = None


def transcribe(video_path: str, slug: str) -> list:
    """
    Transcrit la vidéo et enregistre le transcript dans series/<slug>/transcript.txt
    """
    output_txt = os.path.join("series", slug, "transcript.txt")

    if model is None:
        logger.error("whisper n'est pas disponible")
        raise RuntimeError("whisper non disponible")

    try:
        logger.info(f"📝 Début de transcription : {video_path}")
        start = time.time()

        result = model.transcribe(video_path, verbose=False)

        duration = time.time() - start
        logger.info(
            f"✅ Transcription terminée en {duration:.1f}s, {len(result['segments'])} segments."
        )

        with open(output_txt, "w", encoding="utf-8") as f:
            for segment in result["segments"]:
                f.write(
                    f"[{segment['start']:.2f} --> {segment['end']:.2f}] {segment['text']}\n"
                )

        logger.info(f"💾 Transcription enregistrée dans : {output_txt}")
        return result["segments"]

    except Exception as e:
        logger.exception("❌ Erreur pendant la transcription")
        raise
