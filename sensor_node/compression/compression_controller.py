# sensor_node/compression/compression_controller.py

import cv2
import os


class CompressionController:

    def __init__(self):

        self.compressed_path = None

    def compress_image(self, image_path):

        image = cv2.imread(image_path)

        if image is None:
            return None

        compressed = cv2.resize(image, (32, 32))

        os.makedirs("temp", exist_ok=True)

        output_path = os.path.join(
            "temp",
            "compressed_image.png"
        )

        cv2.imwrite(output_path, compressed)

        self.compressed_path = output_path

        return output_path