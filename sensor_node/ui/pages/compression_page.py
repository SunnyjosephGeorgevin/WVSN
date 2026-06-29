import cv2
import os

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)

from PyQt6.QtGui import QPixmap, QImage

from PyQt6.QtCore import Qt

from shared.image_manager import ImageManager


class CompressionPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        layout.setContentsMargins(30, 30, 30, 30)

        layout.setSpacing(20)

        title = QLabel("Compression")

        title.setStyleSheet("""
            QLabel{
                color:white;
                font-size:30px;
                font-weight:bold;
            }
        """)

        images = QHBoxLayout()

        self.original = QLabel("Original Image")

        self.original.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.original.setMinimumSize(450,350)

        self.original.setStyleSheet("""
            QLabel{
                background:#2B313A;
                color:white;
                border-radius:10px;
            }
        """)

        self.compressed = QLabel("Compressed Image")

        self.compressed.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.compressed.setMinimumSize(450,350)

        self.compressed.setStyleSheet("""
            QLabel{
                background:#2B313A;
                color:white;
                border-radius:10px;
            }
        """)

        images.addWidget(self.original)

        images.addWidget(self.compressed)

        self.compress_btn = QPushButton("Compress")

        self.compress_btn.setMinimumHeight(45)

        self.compress_btn.clicked.connect(
            self.compress_image
        )

        self.compress_btn.setStyleSheet("""
            QPushButton{
                background:#3B82F6;
                color:white;
                border:none;
                border-radius:10px;
                font-size:15px;
                font-weight:bold;
            }
        """)

        self.details = QLabel("Compression Ratio : --")

        self.details.setStyleSheet("""
            QLabel{
                color:white;
                font-size:15px;
            }
        """)

        layout.addWidget(title)

        layout.addLayout(images)

        layout.addWidget(self.compress_btn)

        layout.addWidget(self.details)

        self.setLayout(layout)

    def compress_image(self):

        image_path = ImageManager.get_image()

        if image_path is None:

            self.details.setText(
                "Please capture an image first."
            )

            return

        pix = QPixmap(image_path)

        pix = pix.scaled(
            self.original.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.original.setPixmap(pix)

        image = cv2.imread(image_path)

        compressed = cv2.resize(image,(32,32))
        os.makedirs("temp", exist_ok=True)

        compressed_file = os.path.join(
    "temp",
    "compressed.png"
)

        cv2.imwrite(
        compressed_file,
        compressed
        )

        ImageManager.set_compressed(
        compressed_file
        )

        rgb = cv2.cvtColor(
            compressed,
            cv2.COLOR_BGR2RGB
        )

        h,w,c = rgb.shape

        qimg = QImage(
            rgb.data,
            w,
            h,
            c*w,
            QImage.Format.Format_RGB888
        )

        pix = QPixmap.fromImage(qimg)

        pix = pix.scaled(
            self.compressed.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.FastTransformation
        )

        self.compressed.setPixmap(pix)

        self.details.setText(
            "Compression Ratio : Simulated (256×256 → 32×32)"
        )