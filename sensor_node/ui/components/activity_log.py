# sensor_node/ui/components/activity_log.py

from PyQt6.QtWidgets import QWidget, QLabel, QTextEdit, QVBoxLayout


class ActivityLog(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        title = QLabel("Activity Log")

        title.setStyleSheet("""
            QLabel{
                color:white;
                font-size:18px;
                font-weight:bold;
            }
        """)

        self.log_box = QTextEdit()

        self.log_box.setReadOnly(True)

        self.log_box.setMinimumHeight(220)

        self.log_box.setStyleSheet("""
            QTextEdit{
                background:#2B313A;
                border:1px solid #3B4252;
                border-radius:12px;
                color:white;
                font-size:13px;
                padding:10px;
            }
        """)

        self.log_box.append("✓ WVSN Simulator Started")
        self.log_box.append("✓ Sensor Node Initialized")
        self.log_box.append("✓ Camera Ready")
        self.log_box.append("✓ Network Connected")

        layout.addWidget(title)
        layout.addWidget(self.log_box)

        self.setLayout(layout)

    def add_log(self, message):

        self.log_box.append(message)