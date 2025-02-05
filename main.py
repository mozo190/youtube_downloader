import os

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox
from youtube3 import youtube

class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Downloader")
        self.setGeometry(100, 100, 200, 200)
        self.setStyleSheet("background-color: white;")

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(20, 0, 20, 0)

        self.url_input = QLineEdit()
        self.url_input.setStyleSheet("background-color: white;")
        self.url_input.setPlaceholderText("Enter URL")
        self.layout.addWidget(self.url_input)

        self.format_label = QLabel("Select format:")
        self.layout.addWidget(self.format_label)

        self.format_combo = QComboBox()
        self.format_combo.setStyleSheet("background-color: lightgray;")
        self.format_combo.addItems(["audio", "video"])
        self.layout.addWidget(self.format_combo)

        self.download_btn = QPushButton("Download")
        self.download_btn.setStyleSheet("background-color: #4CAF50; color: orange; ")
        self.download_btn.clicked.connect(self.start_download)
        self.layout.addWidget(self.download_btn)

        self.status_label = QLabel("Status: ")
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)

    def start_download(self):
        self.status_label.setText("Status: Downloading...")
        url = self.url_input.text()
        format_choice = self.format_combo.currentText()

        if format_choice == "audio":
            self.download_audio(url)
        else:
            self.download_video(url)
        self.status_label.setText("Status: Download completed!")

    def download_audio(self, url, path="downloads"):
        print(f"Download audio from {url}")
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            if not os.path.exists(path):
                os.makedirs(path)
            out_file = stream.download(output_path=path)
            base, ext = os.path.splitext(out_file)
            new_file = base + ".mp3"
            os.rename(out_file, new_file)
        except Exception as e:
            print(e)
            self.status_label.setText("Status: Download failed!", e)


if __name__ == "__main__":
    app = QApplication([])
    win = YouTubeDownloader()
    win.show()
    app.exec()