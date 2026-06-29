# sensor_node/ui/components/info_card.py

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt


class InfoCard(QWidget):

    def __init__(self, title: str, value: str):
        super().__init__()

        self.title = title
        self.value = value

        self.setup_ui()

    def setup_ui(self):

        self.setMinimumSize(320, 170)
        self.setMaximumHeight(170)

        layout = QVBoxLayout()

        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(12)

        self.title_label = QLabel(self.title)

        self.title_label.setStyleSheet("""
            QLabel{
                color:#9CA3AF;
                font-size:14px;
                font-weight:600;
                background:transparent;
            }
        """)

        self.value_label = QLabel(self.value)

        self.value_label.setStyleSheet("""
            QLabel{
                color:white;
                font-size:34px;
                font-weight:bold;
                background:transparent;
            }
        """)

        layout.addWidget(self.title_label)

        layout.addStretch()

        layout.addWidget(self.value_label)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget{
                background-color:#2B313A;
                border:1px solid #3B4252;
                border-radius:15px;
            }

            QWidget:hover{
                border:1px solid #3B82F6;
            }
        """)

    def update_value(self, value: str):

        self.value_label.setText(value)