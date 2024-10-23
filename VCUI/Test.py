import sys
from PySide6.QtWidgets import QApplication
from video_colourisation_app import VideoColorizationApp  # Import the class from the new file

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoColorizationApp()
    window.show()
    sys.exit(app.exec())
