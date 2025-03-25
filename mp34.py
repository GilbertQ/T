import os
from pytube import YouTube
from moviepy import VideoFileClip

def download_mp3(url):
    try:
        # Create a downloads directory if it doesn't exist
        os.makedirs('downloads', exist_ok=True)
        
        # Download YouTube video
        yt = YouTube(url)
        print(f"Downloading: {yt.title}")
        
        # Get audio-only stream
        stream = yt.streams.get_audio_only()
        
        # Download to temp file in downloads directory
        temp_file = stream.download(output_path='downloads', filename_prefix="temp_")
        
        # Convert to MP3
        audio = AudioFileClip(temp_file)
        
        # Create MP3 filename (clean title)
        mp3_filename = os.path.join('downloads', f"{yt.title.replace('/', '_')}.mp3")
        
        # Write audio file
        audio.write_audiofile(mp3_filename)
        
        # Close the audio clip
        audio.close()
        
        # Remove temp file
        os.remove(temp_file)
        
        print(f"Successfully downloaded: {mp3_filename}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
download_mp3("https://www.youtube.com/watch?v=yAdW4sR1rFA")
download_mp3("https://www.youtube.com/watch?v=h790bNliSA0")
download_mp3("https://www.youtube.com/watch?v=knNRV_8gSZk")