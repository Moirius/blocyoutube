import os
from utils.logger import get_logger

try:
    import yt_dlp
except Exception:  # pragma: no cover - optional dependency
    yt_dlp = None

logger = get_logger(__name__)


def download(youtube_url: str, slug: str) -> str:
    """
    Télécharge une vidéo YouTube et la place dans series/{slug}/original.mp4
    """
    output_dir = os.path.join("series", slug)
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "original.%(ext)s")

    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "outtmpl": output_path,
        "merge_output_format": "mp4",
        "quiet": True,
        "noplaylist": True,
    }

    yt_cookies_path = os.path.abspath(os.path.join("cookies", "cookies_yt.txt"))
    if os.path.exists(yt_cookies_path):
        ydl_opts["cookiefile"] = yt_cookies_path
        logger.info(f"🍪 Utilisation des cookies YouTube : {yt_cookies_path}")

    if yt_dlp is None:
        logger.error("yt_dlp n'est pas installé")
        raise RuntimeError("yt_dlp non disponible")

    try:
        logger.info(f"📥 Téléchargement depuis : {youtube_url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=True)
            filename = ydl.prepare_filename(info)
            final_path = os.path.splitext(filename)[0] + ".mp4"
            logger.info(f"✅ Vidéo téléchargée : {final_path}")
            return final_path
    except Exception:
        logger.exception("❌ Échec du téléchargement")
        raise
