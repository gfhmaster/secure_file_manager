import unittest
from models.user import User
from models.file import File, EncryptedFile, ArchiveFile


class TestFile(unittest.TestCase):

    def setUp(self):
        self.alice = User("Alice", "hash1")

    def test_file_creation(self):
        f = File("doc.txt", self.alice)
        self.assertEqual(f.name, "doc.txt")
        self.assertEqual(f.owner.username, "Alice")

    def test_encrypted_file(self):
        ef = EncryptedFile("secret.txt", self.alice, encryption="RSA")
        self.assertEqual(ef.encryption, "RSA")
        self.assertIn("RSA", repr(ef))

    def test_archive_file(self):
        af = ArchiveFile("backup.zip", self.alice, compression="tar")
        self.assertEqual(af.compression, "tar")
        self.assertIn("tar", repr(af))


if __name__ == "__main__":
    unittest.main()
