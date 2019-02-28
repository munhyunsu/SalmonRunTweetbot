import unittest
import unittest.mock

from discord_bot.meme_loader import MemeLoader


class MemeLoaderTestCase(unittest.TestCase):
    def setUp(self):
        memes = {'테스트': 'http://test.com/img'}
        self.meme_loader = MemeLoader(memes)

    def tearDown(self):
        del self.meme_loader

    def test_get_meme(self):
        ctx_mock = unittest.mock.MagicMock()
        self.assertEqual('현재 짤이 1개 있습니다.',
                         self.meme_loader.get_meme(ctx_mock))
        args = ('없는테스트',)
        self.assertEqual('검색된 짤이 없습니다.',
                         self.meme_loader.get_meme(ctx_mock, args))
        args = ('테스트',)
        self.assertEqual('http://test.com/img',
                         self.meme_loader.get_meme(ctx_mock, args))
