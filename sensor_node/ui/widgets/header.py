# sensor_node/ui/widgets/header.py

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout
)

from PyQt6.QtCore import Qt


class Header(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(70)

        self.setup_ui()

    def setup_ui(self):

        layout = QHBoxLayout()

        layout.setContentsMargins(25, 10, 25, 10)

        title = QLabel("Virtual Sensor Node")

        title.setStyleSheet("""
            QLabel{
                color:white;
                font-size:22px;
                font-weight:bold;
            }
        """)

        status = QLabel("● Connected")

        status.setStyleSheet("""
            QLabel{
                color:#22C55E;
                font-size:14px;
                font-weight:bold;
            }
        """)

        layout.addWidget(title)

        layout.addStretch()

        layout.addWidget(status)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget{
                background:#2B313A;
                border-bottom:1px solid #3A4049;
            }
        """)