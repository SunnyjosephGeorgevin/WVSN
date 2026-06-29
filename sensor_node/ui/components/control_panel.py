# sensor_node/ui/components/control_panel.py

from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout
)

from PyQt6.QtCore import Qt


class ControlPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QHBoxLayout()

        layout.setSpacing(15)

        self.capture_btn = QPushButton("Capture Image")
        self.compress_btn = QPushButton("Compress")
        self.encrypt_btn = QPushButton("Encrypt")
        self.transmit_btn = QPushButton("Transmit")

        buttons = [
            self.capture_btn,
            self.compress_btn,
            self.encrypt_btn,
            self.transmit_btn
        ]

        for button in buttons:

            button.setCursor(Qt.CursorShape.PointingHandCursor)

            button.setMinimumHeight(45)

            button.setStyleSheet("""
                QPushButton{
                    background:#3B82F6;
                    color:white;
                    border:none;
                    border-radius:10px;
                    font-size:14px;
                    font-weight:bold;
                }

                QPushButton:hover{
                    background:#2563EB;
                }

                QPushButton:pressed{
                    background:#1D4ED8;
                }
            """)

            layout.addWidget(button)

        self.setLayout(layout)