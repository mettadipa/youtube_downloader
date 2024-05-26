import streamlit as st
from pytube import YouTube
import logging
from moviepy.editor import AudioFileClip
import tempfile
import os
import shutil
from utils import sanitize_filename, download_stream, get_video_info, convert_to_mp3

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
            option = st.radio("Select download option:", ["MP4 Video", "MP3 Audio"])

            # Button to initiate download
            if st.button("Generate Download File"):
                sanitized_title = sanitize_filename(yt.title)
                result = None  # Initialize result variable

                if option == "MP4 Video":
                    stream = yt.streams.get_highest_resolution()
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
                        success, result = download_stream(stream, tmp.name)
                        if success:
                            nice_video_name = sanitized_title + ".mp4"
                            shutil.move(tmp.name, nice_video_name)
                            result = nice_video_name
                        else:
                            os.remove(tmp.name)

                else:  # "MP3 Audio"
                    stream = yt.streams.filter(only_audio=True).first()
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
                        success, temp_video_path = download_stream(stream, tmp.name)

                        if success:
                            output_mp3_path = sanitized_title + ".mp3"
                            success, result = convert_to_mp3(temp_video_path, output_mp3_path)
                            os.remove(temp_video_path)
                        else:
                            os.remove(tmp.name)

                if success:
                    st.success(f"{option} '{yt.title}' downloaded successfully!")
                    with open(result, "rb") as f:
                        data = f.read()
                    st.download_button(
                        label=f"Download {option}",
                        data=data,
                        file_name=os.path.basename(result),
                        mime="video/mp4" if option == "MP4 Video" else "audio/mpeg",
                    )
                    os.remove(result)
                else:
                    st.error(f"Failed to download {option.lower()}. Error: {result}")
                    logger.error(f"Failed to download {option.lower()}. Error: {result}")

        else:
            st.warning(f"Failed to retrieve video information. Error: {error}")

if __name__ == "__main__":
    main()
