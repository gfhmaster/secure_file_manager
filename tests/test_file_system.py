from file_system import User, File, EncryptedFile, ArchiveFile, FileManager

def test_user_creation():
    alice = User("Alice", "hash1")
    assert alice.username == "Alice"
    assert alice._password_hash == "hash1"

def test_file_upload():
    alice = User("Alice", "hash1")
    file1 = File("doc.txt", alice)
    alice.upload_file(file1)
    assert len(alice._files) == 1
    assert alice._files[0] == file1

def test_file_sharing():
    alice = User("Alice", "hash1")
    bob = User("Bob", "hash2")
    secret = EncryptedFile("secret.txt", alice)
    alice.upload_file(secret)
    alice.share_file(secret, bob)
    assert secret in bob._files

def test_file_manager():
    manager = FileManager()
    alice = User("Alice", "hash1")
    file1 = File("doc.txt", alice)
    manager.add_file(file1)
    assert len(manager._all_files) == 1
