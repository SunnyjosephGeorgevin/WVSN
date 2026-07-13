class ImageManager:

    image_path = None

    compressed_path = None

    encrypted_path = None

    @classmethod
    def set_image(cls, path):
        cls.image_path = path

    @classmethod
    def get_image(cls):
        return cls.image_path

    @classmethod
    def set_compressed(cls, path):
        cls.compressed_path = path

    @classmethod
    def get_compressed(cls):
        return cls.compressed_path

    @classmethod
    def set_encrypted(cls, path):
        cls.encrypted_path = path

    @classmethod
    def get_encrypted(cls):
        return cls.encrypted_path