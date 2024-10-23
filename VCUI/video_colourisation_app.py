import sys
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QFileDialog,
    QLineEdit, QGridLayout, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QSizePolicy
)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt


class VideoColorizationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Colorization")
        self.setFixedSize(1100, 800)
        self.setStyleSheet(self.get_stylesheet())

        grid_layout = QGridLayout()

        grid_layout.setSpacing(0)

        self.caption_input = QLineEdit()
        self.caption_input.setPlaceholderText("Enter Text Caption:")
        self.caption_input.setObjectName("captionInput")

        self.browse_button = QPushButton("  Browse Videos")
        self.browse_button.clicked.connect(self.browse_video)
        self.browse_button.setObjectName("browseButton")
        icon = QIcon("./upload.svg")
        self.browse_button.setIcon(icon)
        self.browse_button.setIconSize(self.browse_button.sizeHint())

        self.colourise_button = QPushButton("Colourise")
        self.colourise_button.clicked.connect(self.colourise_video)
        self.colourise_button.setObjectName("colouriseButton")

        self.grayscale_label = QLabel("Grayscale")
        self.grayscale_label.setAlignment(Qt.AlignCenter)
        self.grayscale_label.setObjectName("videoLabel")

        self.grayscale_view = QGraphicsView()
        self.grayscale_scene = QGraphicsScene()
        self.grayscale_view.setScene(self.grayscale_scene)
        self.grayscale_view.setObjectName("grayscaleView")

        self.colourised_label = QLabel("ControlCol")
        self.colourised_label.setAlignment(Qt.AlignCenter)
        self.colourised_label.setObjectName("videoLabel")

        self.colourised_view = QGraphicsView()
        self.colourised_scene = QGraphicsScene()
        self.colourised_view.setScene(self.colourised_scene)
        self.colourised_view.setObjectName("colourisedView")

        grid_layout.addWidget(self.caption_input, 0, 1, 1, 2)
        grid_layout.addWidget(self.browse_button, 1, 1, 1, 1)
        grid_layout.addWidget(self.colourise_button, 1, 2, 1, 1)

        grid_layout.addWidget(self.grayscale_label, 3, 0, 1, 2, Qt.AlignHCenter)
        grid_layout.addWidget(self.colourised_label, 3, 2, 1, 2, Qt.AlignHCenter)

        grid_layout.addWidget(self.grayscale_view, 4, 0, 1, 2)
        grid_layout.addWidget(self.colourised_view, 4, 2, 1, 2)

        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)
        grid_layout.setColumnStretch(2, 1)
        grid_layout.setColumnStretch(3, 1)

        grid_layout.setRowStretch(0, 0)
        grid_layout.setRowStretch(1, 0)
        grid_layout.setRowStretch(4, 1)

        grid_layout.setRowMinimumHeight(0, 50)
        grid_layout.setRowMinimumHeight(1, 50)
        grid_layout.setRowMinimumHeight(2, 50)
        grid_layout.setRowMinimumHeight(4, 300)

        self.grayscale_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.colourised_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.setLayout(grid_layout)

    def browse_video(self):
        file_dialog = QFileDialog()
        video_file, _ = file_dialog.getOpenFileName(self, "Select Grayscale Video", "", "Video Files (*.mp4 *.avi *.mkv)")
        if video_file:

            pixmap = QPixmap("/path/to/placeholder/grayscale_image.jpg")
            self.grayscale_scene.clear()
            self.grayscale_scene.addItem(QGraphicsPixmapItem(pixmap))

    def colourise_video(self):
        caption = self.caption_input.text()
        if not caption:
            print("Please enter a caption for colorization.")
            return

        pixmap = QPixmap("/path/to/placeholder/colourised_image.jpg")
        self.colourised_scene.clear()
        self.colourised_scene.addItem(QGraphicsPixmapItem(pixmap))

    def get_stylesheet(self):
        """Returns the QSS style for the application."""
        return """
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
            }

            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                font-size: 16px;
                padding: 10px;
                border: none;
                border-radius: 11px;
                width: 200x;
                height: 23px;
            }
            QPushButton:hover {
                background-color: #45a049;

            }

            QPushButton#browseButton {
                background-color: #4CAF50;
                padding-left: 10px;
                padding-right: 10px;
                margin-right: 90px;
            }
            QPushButton#browseButton:hover {
                background-color: #429945;
            }
            QPushButton#browseButton:pressed {
                background-color: #74c377;
            }

            QPushButton#colouriseButton {
                background-color: #2196F3;
                padding-left: 10px;
                padding-right: 10px;
                margin-left: 90px;
            }
            QPushButton#colouriseButton:hover {
                background-color: #0b7dda;
                padding-left: 10px;
                padding-right: 10px;
                margin-left: 90px;
                margin-left: 90px;
            }
            QPushButton#colouriseButton:pressed {
                background-color: #5fb2f6;
                padding-left: 10px;
                padding-right: 10px;
                margin-left: 90px;
                margin-right: 90px;
            }

            QLabel#videoLabel {
                font-size: 24px;
                font-weight: bold;
                margin: 7px;
                padding: 0px;
                alignment: center;
                text-align: center;
            }
            QLineEdit#captionInput {
                padding: 8px;
                font-size: 17px;
                border: 2px solid #bbbbbb;
                border-radius: 8px;
                margin: 8.5px 0;
                height: 23px;
                width: 400;
            }
            QLineEdit#captionInput:hover {
                border: 2.2px solid #a8a8a8;
                background-color: #e5e5e5;
                margin: 8.5px 0;
            }

            QGraphicsView#grayscaleView, QGraphicsView#colourisedView {
                background-color: #dcdcdc;
                border: 2px solid #bbb;
                margin: 12px;
                border-radius: 8px;
                min-height: 400px;
                min-width: 400px;
                max-height: 700px;
                max-width: 700px;
            }
        """
