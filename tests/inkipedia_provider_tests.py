import unittest
import unittest.mock

from modules.inkipedia_provider import InkipediaProvider

FILENAME = 'tests/latest_inkipedia_locale_tests.json'


class InkipediaProviderTestCase(unittest.TestCase):
    def setUp(self):
        self.reader = InkipediaProvider(FILENAME)

    def tearDown(self):
        del self.reader

    def test_get_regular(self):
        ctx_mock = unittest.mock.MagicMock()
        self.assertEqual(('[Regular Battle]\n'
                          'Now, Turf War\n'
                          'Starfish Mainstage, The Reef\n'
                          'Next, Turf War\n'
                          'Sturgeon Shipyard, Camp Triggerfish\n'),
                         self.reader.get_regular(ctx_mock))

    def test_get_ranked(self):
        ctx_mock = unittest.mock.MagicMock()
        self.assertEqual(('[Ranked Battle]\n'
                          'Now, Clam Blitz\n'
                          'Manta Maria, Moray Towers\n'
                          'Next, Tower Control\n'
                          'Snapper Canal, Port Mackerel\n'),
                         self.reader.get_ranked(ctx_mock))

    def test_get_league(self):
        ctx_mock = unittest.mock.MagicMock()
        self.assertEqual(('[League Battle]\n'
                          'Now, Tower Control\n'
                          'Wahoo World, MakoMart\n'
                          'Next, Rainmaker\n'
                          'Moray Towers, Musselforge Fitness\n'),
                         self.reader.get_league(ctx_mock))
