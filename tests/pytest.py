# -------------------------------
# Пример использования
# -------------------------------
# Создание пользователей
alice = User("Alice", "hash1")
bob = User("Bob", "hash2")

# Создание файлов
file1 = File("document.txt", alice)
file2 = EncryptedFile("secret.txt", alice)
file3 = ArchiveFile("backup.zip", bob)

# Работа с файлами
alice.upload_file(file1)
alice.upload_file(file2)
file2.encrypt()
bob.upload_file(file3)

# FileManager управляет всеми файлами
manager = FileManager()
manager.add_file(file1)
manager.add_file(file2)
manager.add_file(file3)

# Просмотр информации
for f in manager._all_files:
    print(f.info())

# Совместный доступ
alice.share_file(file2, bob)
print("Файлы Bob:", bob.list_files())