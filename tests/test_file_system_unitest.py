import unittest
from file_system import User, File, EncryptedFile, FileManager

class TestFileSystem(unittest.TestCase):

    def test_user_creation(self):
        alice = User("Alice", "hash1")
        self.assertEqual(alice.username, "Alice")
        self.assertEqual(alice._password_hash, "hash1")

    def test_file_upload(self):
        alice = User("Alice", "hash1")
        file1 = File("doc.txt", alice)
        alice.upload_file(file1)
        self.assertEqual(len(alice._files), 1)
        self.assertEqual(alice._files[0], file1)

    def test_file_sharing(self):
        alice = User("Alice", "hash1")
        bob = User("Bob", "hash2")
        secret = EncryptedFile("secret.txt", alice)
        alice.upload_file(secret)
        alice.share_file(secret, bob)
        self.assertIn(secret, bob._files)

    def test_file_manager(self):
        manager = FileManager()
        alice = User("Alice", "hash1")
        file1 = File("doc.txt", alice)
        manager.add_file(file1)
        self.assertEqual(len(manager._all_files), 1)

if __name__ == "__main__":
    unittest.main()
