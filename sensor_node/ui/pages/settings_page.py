from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt


class SettingsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Settings Page")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label.setStyleSheet("""
            QLabel{
                color:white;
                font-size:28px;
                font-weight:bold;
            }
        """)

        layout.addWidget(label)

        self.setLayout(layout)