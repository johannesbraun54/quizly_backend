import whisper  
from google import genai
import json
import yt_dlp
import os


def get_video_transcript():
    model = whisper.load_model("tiny")
    URL = 'https://www.youtube.com/watch?v=vF03fp_clK4'
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "tmp_filename",
        "quiet": True,
        "noplaylist": True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URL, download=False)
        result = model.transcribe(info['url'])
        transcript = result['text']
        return transcript

def get_prompt(transcript):
    script_dir = os.path.dirname(__file__)
    prompt_template_path = os.path.join(script_dir, 'prompt_template.txt')
    prompt_path = os.path.join(script_dir, 'prompt.txt')
    
    with open(prompt_template_path) as f:
        prompt = f.read()

    with open(prompt_path, 'w') as f:
        f.write(prompt)
    
    with open(prompt_path, 'a') as f:
        f.write(transcript)
        
    with open(prompt_path) as f:
        prompt = f.read()
    return prompt

def generate_quiz_data():
    client = genai.Client()
    transcript = get_video_transcript()
    response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=get_prompt(transcript),
    )
    print(response.text)