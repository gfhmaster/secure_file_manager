class File:
    """Базовый класс файла."""

    def __init__(self, name: str, owner: "User") -> None:
        self.name = name
        self.owner = owner

    def __repr__(self) -> str:
        return f"File(name={self.name}, owner={self.owner.username})"


class EncryptedFile(File):
    """Файл с шифрованием."""

    def __init__(self, name: str, owner: "User", encryption: str = "AES256") -> None:
        super().__init__(name, owner)
        self.encryption = encryption

    def __repr__(self) -> str:
        return f"EncryptedFile(name={self.name}, owner={self.owner.username}, enc={self.encryption})"


class ArchiveFile(File):
    """Архивированный файл."""

    def __init__(self, name: str, owner: "User", compression: str = "zip") -> None:
        super().__init__(name, owner)
        self.compression = compression

    def __repr__(self) -> str:
        return f"ArchiveFile(name={self.name}, owner={self.owner.username}, comp={self.compression})"
