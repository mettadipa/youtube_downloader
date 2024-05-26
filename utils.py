from pytube import YouTube
import re
from moviepy.editor import AudioFileClip
import logging

logger = logging.getLogger(__name__)

def sanitize_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)

def download_stream(stream, output_path):
    try:
        stream.download(filename=output_path)
        return True, output_path
    except Exception as e:
        return False, str(e)

def get_video_info(url):
    try:
        yt = YouTube(url)
        return yt, None
    except Exception as e:
        return None, str(e)

def convert_to_mp3(video_path, output_path):
    try:
        audio_clip = AudioFileClip(video_path)
        audio_clip.write_audiofile(output_path)
        audio_clip.close()
        return True, output_path
    except Exception as e:
        logger.error(f"Error converting video to MP3: {e}")
        return False, str(e)
