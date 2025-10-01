import whisper  
from google import genai
import json
import yt_dlp

def generate_quiz_data():
    client = genai.Client()
    model = whisper.load_model("tiny")
    URL = 'https://www.youtube.com/watch?v=-D2paaCxb1M'
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "tmp_filename",
        "quiet": True,
        "noplaylist": True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URL, download=False)
        result = model.transcribe(info['url'])
    print(result["text"])