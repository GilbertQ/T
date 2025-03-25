from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def download_mp3(url):
    yt = YouTube(url)
    stream = yt.streams.get_audio_only()
    temp_file = stream.download(filename_prefix="temp_")
    
    # Convert to MP3
    audio = AudioFileClip(temp_file)
    audio.write_audiofile(temp_file.replace(".mp4", ".mp3"))
    
    os.remove(temp_file)  # Delete temp file

# Usage
download_mp3("https://www.youtube.com/watch?v=yAdW4sR1rFA")
download_mp3("https://www.youtube.com/watch?v=h790bNliSA0")
download_mp3("https://www.youtube.com/watch?v=knNRV_8gSZk")