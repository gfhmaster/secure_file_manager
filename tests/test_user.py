import unittest
from models.user import User
from models.file import File, EncryptedFile


class TestUser(unittest.TestCase):

    def setUp(self):
        self.alice = User("Alice", "hash1")
        self.bob = User("Bob", "hash2")

    def test_user_creation(self):
        self.assertEqual(self.alice.username, "Alice")
        self.assertEqual(self.alice._password_hash, "hash1")

    def test_file_upload(self):
        file1 = File("doc.txt", self.alice)
        self.alice.upload_file(file1)
        self.assertIn("doc.txt", self.alice.list_files())

    def test_file_sharing(self):
        secret = EncryptedFile("secret.txt", self.alice)
        self.alice.upload_file(secret)
        self.alice.share_file(secret, self.bob)

        self.assertIn("secret.txt", self.bob.list_files())
        self.assertIn("secret.txt", self.alice.list_files())


if __name__ == "__main__":
    unittest.main()