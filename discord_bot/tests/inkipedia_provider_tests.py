import unittest
import unittest.mock

from discord_bot.modules.inkipedia_provider import InkipediaProvider

FILENAME = 'tests/latest_inkipedia_locale_tests.json'


class InkipediaProviderTestCase(unittest.TestCase):
    def setUp(self):
        self.reader = InkipediaProvider(FILENAME)

    def tearDown(self):
        del self.reader

    def test_get_regular(self):
        ctx_mock = unittest.mock.MagicMock()
        self.assertEqual(('**[Regular Battle]**\n'
                          'Now, __Turf War__\n'
                          'Starfish Mainstage, The Reef\n'
                          'Next, __Turf War__\n'
                          'Sturgeon Shipyard, Camp Triggerfish\n'),
                         self.reader.get_regular(ctx_mock))

    def test_get_ranked(self):
        ctx_mock = unittest.mock.MagicMock()
        self.assertEqual(('**[Ranked Battle]**\n'
                          'Now, __Clam Blitz__\n'
                          'Manta Maria, Moray Towers\n'
                          'Next, __Tower Control__\n'
                          'Snapper Canal, Port Mackerel\n'),
                         self.reader.get_ranked(ctx_mock))

    def test_get_league(self):
        ctx_mock = unittest.mock.MagicMock()
        self.assertEqual(('**[League Battle]**\n'
                          'Now, __Tower Control__\n'
                          'Wahoo World, MakoMart\n'
                          'Next, __Rainmaker__\n'
                          'Moray Towers, Musselforge Fitness\n'),
                         self.reader.get_league(ctx_mock))
