import unittest

from gspread_handler.modules.gspread_handler import GSpreadHandler

CRED_FILE = 'Gspread-39d43309c65c.json'


class MemeLoaderTestCase(unittest.TestCase):
    def setUp(self):
        self.spread = GSpreadHandler(CRED_FILE)

    def tearDown(self):
        del self.spread

    def test_get_traslate_dict(self):
        wp_en_jp, wp_en_ko, st_en_jp, st_en_ko = self.spread.get_translate_dict()
        self.assertEqual(type(wp_en_jp), dict)
        self.assertEqual(type(wp_en_ko), dict)
        self.assertEqual(type(st_en_jp), dict)
        self.assertEqual(type(st_en_ko), dict)

    def test_get_meme_dict(self):
        meme = self.spread.get_meme_dict()
        self.assertEqual(type(meme), dict)

