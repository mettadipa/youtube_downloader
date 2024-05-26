# YouTube Downloader

A simple Streamlit app to download YouTube videos or audio (MP3) using `pytube` and `moviepy`.

## Features
- Download YouTube videos in MP4 format.
- Download YouTube audio in MP3 format.

## Prerequisites
- Python 3.7 or higher

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/mettadipa/youtube_downloader.git
    cd youtube_downloader
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

2. Enter the YouTube video URL in the input box.
3. Select the download option (MP4 Video or MP3 Audio).
4. Click on the "Generate Download File" button.
5. Download the generated file using the provided download button.

## Dependencies

- `streamlit`
- `pytube`
- `moviepy`

These are listed in the `requirements.txt` file.

## Troubleshooting

If you encounter any issues, ensure that:
- You have a stable internet connection.
- The YouTube URL is valid.
- You have the necessary permissions to create and write files in the directory.

If the problem persists, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License.
