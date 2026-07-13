from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel
)

from sensor_node.ui.components.info_card import InfoCard


class DashboardPage(QWidget):

    def __init__(self, camera_page):
        super().__init__()

        self.camera_page = camera_page

        self.setup_ui()

    def setup_ui(self):

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)

        row1 = QHBoxLayout()
        row2 = QHBoxLayout()

        row1.setSpacing(20)
        row2.setSpacing(20)

        self.battery = InfoCard("Battery", "100%")
        self.camera = InfoCard("Camera", "Ready")
        self.network = InfoCard("Network", "Connected")
        self.compression = InfoCard("Compression", "Idle")

        row1.addWidget(self.battery)
        row1.addWidget(self.camera)

        row2.addWidget(self.network)
        row2.addWidget(self.compression)

        status = QLabel(
            "Sensor Node Ready\n\nUse the Camera page to capture an image."
        )

        status.setStyleSheet("""
            QLabel{
                color:white;
                font-size:22px;
                font-weight:bold;
            }
        """)

        main_layout.addLayout(row1)
        main_layout.addLayout(row2)
        main_layout.addStretch()
        main_layout.addWidget(status)
        main_layout.addStretch()

        self.setLayout(main_layout)