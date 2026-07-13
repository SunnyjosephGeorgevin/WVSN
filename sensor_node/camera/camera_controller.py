# sensor_node/camera/camera_controller.py

from PyQt6.QtWidgets import QFileDialog


class CameraController:

    def __init__(self):
        self.image_path = None

    def capture_image(self):

        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Select Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if file_path:
            self.image_path = file_path
            return file_path

        return None