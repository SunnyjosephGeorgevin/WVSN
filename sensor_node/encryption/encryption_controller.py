from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os


class EncryptionController:

    def __init__(self):

        self.key = b'1234567890abcdef'

    def encrypt_file(self, file_path):

        with open(file_path, "rb") as file:

            data = file.read()

        cipher = AES.new(
            self.key,
            AES.MODE_ECB
        )

        encrypted = cipher.encrypt(
            pad(data, AES.block_size)
        )

        os.makedirs("temp", exist_ok=True)

        output_file = os.path.join(
            "temp",
            "encrypted.bin"
        )

        with open(output_file, "wb") as file:

            file.write(encrypted)

        return output_file, len(encrypted)