# sensor_node/ui/components/image_preview.py

from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class ImagePreview(QLabel):

    def __init__(self):
        super().__init__()

        self.setMinimumHeight(350)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setText("No Image Selected")

        self.setStyleSheet("""
            QLabel{
                background:#2B313A;
                color:#9CA3AF;
                border:2px dashed #4B5563;
                border-radius:12px;
                font-size:16px;
            }
        """)

    def load_image(self, image_path):

        pixmap = QPixmap(image_path)

        pixmap = pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.setPixmap(pixmap)

    def resizeEvent(self, event):

        if self.pixmap():

            self.setPixmap(
                self.pixmap().scaled(
                    self.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
            )

        super().resizeEvent(event)