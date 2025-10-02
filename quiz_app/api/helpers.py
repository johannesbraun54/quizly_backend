from urllib.parse import urlparse, parse_qs
import yt_dlp

def validate_youtube_url(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc not in ["www.youtube.com", "youtube.com", "youtu.be"]:
        return False

    # Youtube watch links prüfen
    if "youtube.com" in parsed_url.netloc and parsed_url.path == "/watch":
        qs = parse_qs(parsed_url.query)
        if "v" not in qs:
            return False
    
    # youtu.be shortlink prüfen
    if "youtu.be" in parsed_url.netloc and not parsed_url.path.strip("/"):
        return False
    return True


def video_exists(url):
    ydl_opts = {
    'quiet': True,
    'skip_download': True,  # Video nicht herunterladen
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=False)
        return True
    except Exception:
        return False   
