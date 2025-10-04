from typing import List
from models.file import File


class FileManager:
    """Класс для управления всеми файлами в системе."""

    def __init__(self) -> None:
        self._all_files: List[File] = []

    def add_file(self, file: File) -> None:
        """Добавить файл в систему."""
        if file not in self._all_files:
            self._all_files.append(file)

    def list_files(self) -> List[str]:
        """Вернуть список всех файлов по имени."""
        return [f.name for f in self._all_files]

    def find_file(self, name: str) -> File | None:
        """Найти файл по имени."""
        return next((f for f in self._all_files if f.name == name), None)
