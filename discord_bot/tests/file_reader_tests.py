import unittest
import unittest.mock
import os

from discord_bot.file_reader import FileReader

FILENAME = 'test_file'


class MemeLoaderTestCase(unittest.TestCase):
    def setUp(self):
        with open(FILENAME, 'w') as f:
            f.write('Test String')
        self.file_reader = FileReader(FILENAME)

    def tearDown(self):
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
        del self.file_reader

    def test_get_file_content(self):
        ctx_mock = unittest.mock.MagicMock()
        self.assertEqual('Test String',
                         self.file_reader.get_file_content(ctx_mock))
