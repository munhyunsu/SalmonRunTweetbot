import unittest
import os

from twitter_bot.modules.file_handler import FileHandler

FILENAME = 'test.txt'


class FileHandlerTests(unittest.TestCase):
    def tearDown(self):
        if os.path.exists(self.fhandler.file_name):
            os.remove(self.fhandler.file_name)

    def test___init___default_args(self):
        self.fhandler = FileHandler()
        self.assertEqual('latest_url', self.fhandler.file_name)

    def test___init___pass_args(self):
        test_file_name = 'test.txt'
        self.fhandler = FileHandler(test_file_name)
        self.assertEqual(test_file_name, self.fhandler.file_name)

    def test_write_and_read(self):
        test_file_name = 'test.txt'
        test_text = 'example_text'
        self.fhandler = FileHandler(test_file_name)
        self.fhandler.write(test_text)
        self.assertEqual(test_text, self.fhandler.read())
