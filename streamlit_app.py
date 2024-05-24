import streamlit as st
from pytube import YouTube
import os
import logging
from moviepy.editor import AudioFileClip
import tempfile
from utils import sanitize_filename, download_stream, convert_to_mp3, get_video_info

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    st.title("YouTube Downloader")

    # Get YouTube video URL from user input
    url = st.text_input("Enter YouTube Video URL:")

    if url:
        yt, error = get_video_info(url)
        if yt:
            # Display video information
            st.subheader("Video Information:")
            st.write(f"Title: {yt.title}")
            st.write(f"Author: {yt.author}")
            st.write(f"Length: {yt.length} seconds")
            st.image(yt.thumbnail_url)

            # Option to download video or audio
            option = st.radio("Select download option:", ["Download Video", "Download Audio (MP3)"])

            # Button to initiate download
            if st.button("Download"):
                base_save_path = st.text_input("Enter the base directory to save files:", "./downloads")
                
                if not os.path.isdir(base_save_path):
                    st.error("Invalid directory path. Please enter a valid directory.")
                    return
                
                # Define separate paths for video and audio files
                video_save_path = os.path.join(base_save_path, "videos")
                audio_save_path = os.path.join(base_save_path, "audio")

                # Ensure both directories exist
                os.makedirs(video_save_path, exist_ok=True)
                os.makedirs(audio_save_path, exist_ok=True)

                if option == "Download Video":
                    stream = yt.streams.get_highest_resolution()
                    success, result = download_stream(stream, video_save_path)
                else:  # "Download Audio (MP3)"
                    stream = yt.streams.filter(only_audio=True).first()
                    with tempfile.TemporaryDirectory() as temp_dir:
                        success, temp_video_path = download_stream(stream, temp_dir)
                        if success:
                            success, result = convert_to_mp3(temp_video_path, audio_save_path)

                if success:
                    st.success(f"{option} '{yt.title}' downloaded successfully!")
                else:
                    st.error(f"Failed to download {option.lower()}. Error: {result}")
                    logger.error(f"Failed to download {option.lower()}. Error: {result}")
        else:
            st.warning(f"Failed to retrieve video information. Error: {error}")

if __name__ == "__main__":
    main()
