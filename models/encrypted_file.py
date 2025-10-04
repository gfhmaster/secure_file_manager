from cryptography.fernet import Fernet
from models.file import File


class EncryptedFile(File):
    """
    Класс для работы с зашифрованными файлами.
    Наследуется от File и добавляет функционал шифрования/дешифрования.
    """

    def __init__(self, filename: str, owner: str, content: bytes, key: bytes = None):
        super().__init__(filename, owner, content)
        self.key = key or Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt(self) -> bytes:
        """
        Шифрует содержимое файла.
        """
        if not isinstance(self.content, bytes):
            raise ValueError("Content must be bytes for encryption")
        encrypted = self.fernet.encrypt(self.content)
        self.content = encrypted
        return encrypted

    def decrypt(self) -> bytes:
        """
        Дешифрует содержимое файла.
        """
        try:
            decrypted = self.fernet.decrypt(self.content)
            return decrypted
        except Exception as e:
            raise ValueError(f"Decryption failed: {e}")

    def get_key(self) -> bytes:
        """
        Возвращает ключ для расшифровки.
        """
        return self.key