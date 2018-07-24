import unittest

import wiki_parser


TESTHTML = 'tests/sample180724.html'

class SplatoonWikiParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = wiki_parser.SplatoonWikiParser()
        html = '''
        '''
        self.parser.feed_html(html)

    def test_parse_salmon2_times(self):
        pass

    def test_parse_salmon2_weapons(self):
        pass

    def test_parse_salmon2_stage(self):
        pass

    def test_get_schedule(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)