from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QSizePolicy
)

from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from shared.image_manager import ImageManager

class CameraPage(QWidget):

    def __init__(self):
        super().__init__()

        self.image_path = ""
        self.original_pixmap = None

        self.setup_ui()
        self.connect_signals()

    def setup_ui(self):

        layout = QVBoxLayout()

        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        title = QLabel("Camera")

        title.setStyleSheet("""
            QLabel{
                color:white;
                font-size:30px;
                font-weight:bold;
            }
        """)

        self.capture_btn = QPushButton("Capture Image")

        self.capture_btn.setMinimumHeight(45)

        self.capture_btn.setStyleSheet("""
            QPushButton{
                background:#3B82F6;
                color:white;
                border:none;
                border-radius:10px;
                font-size:15px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#2563EB;
            }
        """)

        self.preview = QLabel("No Image Selected")

        self.preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.preview.setMinimumSize(800, 500)

        self.preview.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        self.preview.setStyleSheet("""
            QLabel{
                background:#2B313A;
                color:#9CA3AF;
                border:2px dashed #4B5563;
                border-radius:12px;
            }
        """)

        self.info = QLabel()

        self.info.setStyleSheet("""
            QLabel{
                color:white;
                font-size:14px;
            }
        """)

        layout.addWidget(title)
        layout.addWidget(self.capture_btn)
        layout.addWidget(self.preview, 1)
        layout.addWidget(self.info)

        self.setLayout(layout)

    def connect_signals(self):

        self.capture_btn.clicked.connect(self.capture_image)

    def capture_image(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if not file_path:
            return

        self.image_path = file_path
        ImageManager.set_image(file_path)

        self.original_pixmap = QPixmap(file_path)

        if self.original_pixmap.isNull():

            self.info.setText("Failed to load image.")

            return

        self.show_image()

        self.info.setText(
            f"Selected Image:\n{file_path}"
        )

    def show_image(self):

        if self.original_pixmap is None:
            return

        scaled_pixmap = self.original_pixmap.scaled(
            self.preview.width() - 20,
            self.preview.height() - 20,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.preview.setPixmap(scaled_pixmap)

        self.preview.setText("")

    def resizeEvent(self, event):

        if self.original_pixmap is not None:

            self.show_image()

        super().resizeEvent(event)