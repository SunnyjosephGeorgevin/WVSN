from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

from shared.image_manager import ImageManager

from sensor_node.encryption.encryption_controller import EncryptionController


class EncryptionPage(QWidget):

    def __init__(self):
        super().__init__()

        self.controller = EncryptionController()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        layout.setContentsMargins(30, 30, 30, 30)

        layout.setSpacing(20)

        title = QLabel("AES-128 Encryption")

        title.setStyleSheet("""
            QLabel{
                color:white;
                font-size:30px;
                font-weight:bold;
            }
        """)

        self.button = QPushButton("Encrypt")

        self.button.setMinimumHeight(45)

        self.button.clicked.connect(
            self.encrypt
        )

        self.button.setStyleSheet("""
            QPushButton{
                background:#3B82F6;
                color:white;
                border:none;
                border-radius:10px;
                font-size:15px;
                font-weight:bold;
            }
        """)

        self.status = QLabel("Status : Waiting")

        self.status.setStyleSheet("""
            QLabel{
                color:white;
                font-size:18px;
            }
        """)

        layout.addWidget(title)
        layout.addWidget(self.button)
        layout.addWidget(self.status)
        layout.addStretch()

        self.setLayout(layout)

    def encrypt(self):

        file = ImageManager.get_compressed()

        if file is None:

            self.status.setText(
                "Status : Compress an image first."
            )

            return

        encrypted_file, size = self.controller.encrypt_file(file)

        ImageManager.set_encrypted(
            encrypted_file
        )

        self.status.setText(
            f"Encrypted Successfully\n\nSize : {size} Bytes"
        )