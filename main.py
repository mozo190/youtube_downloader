from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox


class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Downloader")
        self.setGeometry(100, 100, 200, 200)
        self.setStyleSheet("background-color: white;")

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

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
        self.layout.addWidget(self.download_btn)

        self.status_label = QLabel("Status: ")
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    win = YouTubeDownloader()
    win.show()
    app.exec()