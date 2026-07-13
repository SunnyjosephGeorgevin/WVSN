from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy
)

from PyQt6.QtCore import Qt

import qtawesome as qta


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(240)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        title = QLabel("WVSN")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setStyleSheet("""
            QLabel{
                color:white;
                font-size:28px;
                font-weight:bold;
            }
        """)

        subtitle = QLabel("Virtual Sensor Node")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle.setStyleSheet("""
            QLabel{
                color:#9ca3af;
                font-size:12px;
            }
        """)

        layout.addWidget(title)
        layout.addWidget(subtitle)

        layout.addSpacing(25)

        self.dashboard_btn = self.create_button(
            "Dashboard",
            qta.icon("fa5s.home")
        )

        self.camera_btn = self.create_button(
            "Camera",
            qta.icon("fa5s.camera")
        )

        self.compression_btn = self.create_button(
            "Compression",
            qta.icon("fa5s.compress")
        )

        self.encryption_btn = self.create_button(
            "Encryption",
            qta.icon("fa5s.lock")
        )

        self.transmission_btn = self.create_button(
            "Transmission",
            qta.icon("fa5s.wifi")
        )

        self.logs_btn = self.create_button(
            "Logs",
            qta.icon("fa5s.file-alt")
        )

        self.settings_btn = self.create_button(
            "Settings",
            qta.icon("fa5s.cog")
        )

        layout.addWidget(self.dashboard_btn)
        layout.addWidget(self.camera_btn)
        layout.addWidget(self.compression_btn)
        layout.addWidget(self.encryption_btn)
        layout.addWidget(self.transmission_btn)
        layout.addWidget(self.logs_btn)

        layout.addStretch()

        layout.addWidget(self.settings_btn)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget{
                background:#23272F;
            }
        """)

    def create_button(self, text, icon):
        button = QPushButton(icon, text)

        button.setCursor(Qt.CursorShape.PointingHandCursor)

        button.setFixedHeight(48)

        button.setIconSize(button.iconSize())

        button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        button.setStyleSheet("""
            QPushButton{

                text-align:left;

                padding-left:18px;

                border:none;

                border-radius:10px;

                color:white;

                font-size:14px;

                background:transparent;
            }

            QPushButton:hover{

                background:#3B82F6;

            }

            QPushButton:pressed{

                background:#2563EB;

            }
        """)

        return button