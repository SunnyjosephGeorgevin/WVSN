from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget
)

from config.settings import (
    APP_NAME,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    MIN_WIDTH,
    MIN_HEIGHT
)

from sensor_node.ui.widgets.sidebar import Sidebar
from sensor_node.ui.widgets.header import Header

from sensor_node.ui.pages.dashboard_page import DashboardPage
from sensor_node.ui.pages.camera_page import CameraPage
from sensor_node.ui.pages.compression_page import CompressionPage
from sensor_node.ui.pages.encryption_page import EncryptionPage
from sensor_node.ui.pages.transmission_page import TransmissionPage
from sensor_node.ui.pages.logs_page import LogsPage
from sensor_node.ui.pages.settings_page import SettingsPage


class DashboardWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(APP_NAME)

        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setMinimumSize(MIN_WIDTH, MIN_HEIGHT)

        self.apply_theme()
        self.setup_ui()
        self.connect_signals()

    def apply_theme(self):

        self.setStyleSheet("""
            QMainWindow{
                background:#1E1E1E;
            }
        """)

    def setup_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()

        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.sidebar = Sidebar()

        self.header = Header()

        self.stack = QStackedWidget()

        self.camera_page = CameraPage()

        self.dashboard_page = DashboardPage(
            self.camera_page
        )

        self.compression_page = CompressionPage()
        self.encryption_page = EncryptionPage()
        self.transmission_page = TransmissionPage()
        self.logs_page = LogsPage()
        self.settings_page = SettingsPage()

        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.camera_page)
        self.stack.addWidget(self.compression_page)
        self.stack.addWidget(self.encryption_page)
        self.stack.addWidget(self.transmission_page)
        self.stack.addWidget(self.logs_page)
        self.stack.addWidget(self.settings_page)

        right_widget = QWidget()

        right_layout = QVBoxLayout()

        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        right_layout.addWidget(self.header)
        right_layout.addWidget(self.stack)

        right_widget.setLayout(right_layout)

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(right_widget)

        central_widget.setLayout(main_layout)

    def connect_signals(self):

        self.sidebar.dashboard_btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(0)
        )

        self.sidebar.camera_btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(1)
        )

        self.sidebar.compression_btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(2)
        )

        self.sidebar.encryption_btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(3)
        )

        self.sidebar.transmission_btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(4)
        )

        self.sidebar.logs_btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(5)
        )

        self.sidebar.settings_btn.clicked.connect(
            lambda: self.stack.setCurrentIndex(6)
        )