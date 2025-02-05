# YouTube Downloader

This is a simple YouTube downloader application that allows downloading videos and audio files from YouTube. 
The application features a PYGt6-based graphical user interface and utilizes the yt-dlp library to download videos and audio files from YouTube.

## Features

- Download videos from YouTube in mp4 format
- Download audio files from YouTube in mp3 format
- User-friendly graphical user interface using PYGt6
- Automatically creates a download folder in the user's home directory

## Installation

To install the application, you need to have Python 3.6 or higher installed on your system.
If you don't have Python installed, you can download it from the official website: https://www.python.org/downloads/

To install the required dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
```
or
```bash
pip3 install yt-dlp PyQt6
```

## Usage

To run the application, execute the following command in your terminal:

```bash
python main.py
```

This will start the application and open the main window. You can paste the URL of the YouTube video you want to download into the input field and select the desired format (video or audio).
After that, click the "Download" button to start the download process. The application will automatically create a download folder in your home directory and save the downloaded files there.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
