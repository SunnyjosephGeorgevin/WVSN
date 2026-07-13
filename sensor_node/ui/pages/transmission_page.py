from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QProgressBar
)

from PyQt6.QtCore import QTimer

from shared.image_manager import ImageManager

from sensor_node.transmission.transmission_controller import TransmissionController


class TransmissionPage(QWidget):

    def __init__(self):
        super().__init__()

        self.controller = TransmissionController()

        self.progress_value = 0

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_progress
        )

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        layout.setContentsMargins(30,30,30,30)

        layout.setSpacing(20)

        title = QLabel("Wireless Transmission")

        title.setStyleSheet("""
            QLabel{
                color:white;
                font-size:30px;
                font-weight:bold;
            }
        """)

        self.progress = QProgressBar()

        self.progress.setRange(0,100)

        self.progress.setValue(0)

        self.button = QPushButton("Transmit")

        self.button.setMinimumHeight(45)

        self.button.clicked.connect(
            self.start_transmission
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
        layout.addWidget(self.progress)
        layout.addWidget(self.button)
        layout.addWidget(self.status)
        layout.addStretch()

        self.setLayout(layout)

    def start_transmission(self):

        file = ImageManager.get_encrypted()

        if file is None:

            self.status.setText(
                "Status : Encrypt data first."
            )

            return

        self.source_file = file

        self.progress_value = 0

        self.progress.setValue(0)

        self.timer.start(25)

    def update_progress(self):

        self.progress_value += 2

        self.progress.setValue(
            self.progress_value
        )

        if self.progress_value >= 100:

            self.timer.stop()

            destination = self.controller.transmit(
                self.source_file
            )

            self.status.setText(
                f"Transmission Complete\n\nSaved To:\n{destination}"
            )