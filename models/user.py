from typing import List

class User:
    """Класс пользователя, хранящий данные о пользователе и его файлах."""

    def __init__(self, username: str, password_hash: str) -> None:
        self.username = username
        self._password_hash = password_hash
        self._files: List["File"] = []

    def upload_file(self, file: "File") -> None:
        """Загрузить файл в личное хранилище пользователя."""
        if file not in self._files:
            self._files.append(file)

    def share_file(self, file: "File", recipient: "User") -> None:
        """Поделиться файлом с другим пользователем."""
        if file in self._files and file not in recipient._files:
            recipient.receive_file(file)

    def receive_file(self, file: "File") -> None:
        """Получить файл от другого пользователя."""
        self._files.append(file)

    def list_files(self) -> List[str]:
        """Получить список файлов пользователя."""
        return [f.name for f in self._files]
