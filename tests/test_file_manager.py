import unittest
from managers.file_manager import FileManager
from models.user import User
from models.file import File


class TestFileManager(unittest.TestCase):

    def setUp(self)
        self.manager = FileManager()
        self.alice = User(Alice, hash1)
        self.file1 = File(doc.txt, self.alice)

    def test_add_file(self)
        self.manager.add_file(self.file1)
        self.assertIn(doc.txt, self.manager.list_files())

    def test_find_file(self)
        self.manager.add_file(self.file1)
        found = self.manager.find_file(doc.txt)
        self.assertEqual(found, self.file1)

    def test_find_nonexistent_file(self)
        found = self.manager.find_file(nofile.txt)
        self.assertIsNone(found)


if __name__ == __main__
    unittest.main()
