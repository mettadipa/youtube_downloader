# YouTube Downloader

A simple Streamlit app to download YouTube videos and convert them to MP3.

## Features
- Download YouTube videos in the highest resolution
- Convert YouTube videos to MP3

## Requirements
- Python 3.7+
- `pytube`
- `streamlit`
- `moviepy`

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/mettadipa/youtube_downloader.git
    cd youtube_downloader
    ```

2. Create the necessary directories:
    ```sh
    mkdir -p downloads/audio downloads/videos
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```sh
    streamlit run streamlit_app.py
    ```

## Usage
- Enter the YouTube video URL.
- Choose to download the video or extract the audio as MP3.
- The downloaded files will be saved in the `downloads` directory.

## License
This project is licensed under the MIT License.
