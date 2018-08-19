import unittest
import datetime

import wiki_parser

TEST_HTML = 'sample.html'
GROUND_TRUTH = {'start_time': datetime.datetime(2018, 8, 21, 21),
                'end_time': datetime.datetime(2018, 8, 23, 3),
                'weapon1_en': 'Splattershot',
                'weapon1_jp': 'スプラシューター',
                'weapon2_en': 'Slosher',
                'weapon2_jp': 'バケットスロッシャー',
                'weapon3_en': 'Octobrush',
                'weapon3_jp': 'ホクサイ',
                'weapon4_en': 'E-liter 4K Scope',
                'weapon4_jp': '4Kスコープ',
                'stage_en': 'Salmonid Smokeyard',
                'stage_jp': 'トキシラズいぶし工房'}



class SplatoonWikiParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = wiki_parser.SplatoonWikiParser()
        with open(TEST_HTML, 'rb') as f:
            html = f.read()
        self.parser.feed_html(html)
        wp_en_jp = {GROUND_TRUTH['weapon1_en']: GROUND_TRUTH['weapon1_jp'],
                    GROUND_TRUTH['weapon2_en']: GROUND_TRUTH['weapon2_jp'],
                    GROUND_TRUTH['weapon3_en']: GROUND_TRUTH['weapon3_jp'],
                    GROUND_TRUTH['weapon4_en']: GROUND_TRUTH['weapon4_jp']}
        wp_en_ko = {}
        st_en_jp = {GROUND_TRUTH['stage_en']: GROUND_TRUTH['stage_jp']}
        st_en_ko = {}
        self.parser.feed_translate_dict(wp_en_jp, wp_en_ko, st_en_jp, st_en_ko)

    def tearDown(self):
        del self.parser

    def test_parse_salmon2_times(self):
        times = self.parser.parse_salmon2_times()
        self.assertEqual([GROUND_TRUTH['start_time'],
                          GROUND_TRUTH['end_time']],
                         times)

    def test_parse_salmon2_weapons(self):
        weapons = self.parser.parse_salmon2_weapons()
        self.assertEqual([GROUND_TRUTH['weapon1_en'],
                          GROUND_TRUTH['weapon2_en'],
                          GROUND_TRUTH['weapon3_en'],
                          GROUND_TRUTH['weapon4_en']],
                         weapons)

    def test_parse_salmon2_stage(self):
        stage = self.parser.parse_salmon2_stage()
        self.assertEqual(GROUND_TRUTH['stage_en'], stage)

    def test_get_schedule(self):
        schedule = self.parser.get_schedule()
        self.assertEqual(GROUND_TRUTH, schedule)


if __name__ == '__main__':
    unittest.main(verbosity=2)