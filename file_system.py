from datetime import datetime

# -------------------------------
# Класс User
# -------------------------------
class User:
    """
    Представляет пользователя системы.
    Инкапсуляция: пароль и список файлов защищены от прямого доступа.
    """
    def __init__(self, username, password_hash):
        self.name = username
        self._password_hash = password_hash  # защищенный атрибут
        self._files = []  # список файлов пользователя, инкапсулирован

    def upload_file(self, file):
        """Добавляет файл пользователю и возвращает подтверждение."""
        self._files.append(file)
        print(f"{self.username} загрузил файл: {file.filename}")

    def list_files(self):
        """Возвращает список всех файлов пользователя."""
        return [f.filename for f in self._files]

    def share_file(self, file, recipient):
        """Делится файлом с другим пользователем."""
        if file in self._files:
            recipient.upload_file(file)
            print(f"{self.username} поделился файлом {file.filename} с {recipient.username}")

# -------------------------------
# Класс File (базовый) и наследники
# -------------------------------
class File:
    """
    Базовый класс для файлов.
    Полиморфизм: метод info() будет переопределяться в наследниках.
    """
    def __init__(self, filename, owner):
        self.filename = filename
        self.owner = owner
        self.status = "загружен"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def info(self):
        return f"Файл: {self.filename}, Владелец: {self.owner.username}, Статус: {self.status}"

class EncryptedFile(File):
    """Наследник File: добавляет шифрование."""
    def __init__(self, filename, owner):
        super().__init__(filename, owner)
        self.encrypted = False

    def encrypt(self):
        self.encrypted = True
        self.status = "зашифрован"
        self.updated_at = datetime.now()
        print(f"Файл {self.filename} зашифрован.")

    def info(self):
        return f"Зашифрованный файл: {self.filename}, Владелец: {self.owner.username}"

class ArchiveFile(File):
    """Наследник File: архивный файл."""
    def __init__(self, filename, owner):
        super().__init__(filename, owner)
        self.compressed = True
        self.status = "архив"

    def info(self):
        return f"Архивный файл: {self.filename}, Владелец: {self.owner.username}"

# -------------------------------
# Класс FileManager
# -------------------------------
class FileManager:
    """
    Управляет файлами в системе.
    Singleton-подобная логика может быть добавлена для работы с базой данных.
    """
    def __init__(self):
        self._all_files = []

    def add_file(self, file):
        self._all_files.append(file)
        print(f"Файл {file.filename} добавлен в систему.")

    def delete_file(self, file):
        if file in self._all_files:
            self._all_files.remove(file)
            print(f"Файл {file.filename} удалён из системы.")

    def list_all_files(self):
        return [f.filename for f in self._all_files]

