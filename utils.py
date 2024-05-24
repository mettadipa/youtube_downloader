import re
import os
from moviepy.editor import AudioFileClip
from pytube import YouTube

def sanitize_filename(filename):
    """Sanitize the filename by replacing illegal characters."""
    return re.sub(r'[\\/:*?"<>|]', '_', filename)

def download_stream(stream, save_path):
    """Download the given stream and return the file path."""
    try:
        file_path = stream.download(output_path=save_path)
        return True, file_path
    except Exception as e:
        return False, str(e)

def convert_to_mp3(video_file_path, save_path):
    """Convert the given video file to MP3."""
    try:
        audio_file_path = os.path.join(save_path, os.path.splitext(os.path.basename(video_file_path))[0] + ".mp3")
        clip = AudioFileClip(video_file_path)
        clip.write_audiofile(audio_file_path)
        return True, audio_file_path
    except Exception as e:
        return False, str(e)

def get_video_info(url):
    """Retrieve video information."""
    try:
        yt = YouTube(url)
        return yt, None
    except Exception as e:
        return None, str(e)
