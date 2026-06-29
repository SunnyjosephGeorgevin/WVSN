import os
import shutil


class TransmissionController:

    def transmit(self, source_file):

        if not os.path.exists(source_file):
            return None

        os.makedirs("base_station/received", exist_ok=True)

        destination = os.path.join(
            "base_station",
            "received",
            "encrypted.bin"
        )

        shutil.copy(source_file, destination)

        return destination