import unittest
import os
import datetime

from bs4 import BeautifulSoup

from modules.inkipedia_parser import InkipediaParser

TEST_HTML = 'inkipedia_parser_tests.html'
SALMONRUN_GT = [{'start_time': datetime.datetime(2018, 8, 20, 3),
                 'end_time': datetime.datetime(2018, 8, 21, 9),
                 'weapon1': 'Squeezer',
                 'weapon2': 'Mini Splatling',
                 'weapon3': 'Undercover Brella',
                 'weapon4': 'Classic Squiffer',
                 'stage': 'Marooner\'s Bay'},
                {'start_time': datetime.datetime(2018, 8, 21, 21),
                 'end_time': datetime.datetime(2018, 8, 23, 3),
                 'weapon1': 'Splattershot',
                 'weapon2': 'Slosher',
                 'weapon3': 'Octobrush',
                 'weapon4': 'E-liter 4K Scope',
                 'stage': 'Salmonid Smokeyard'}]


class InkipediaParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = InkipediaParser(TEST_HTML)

    def tearDown(self):
        del self.parser

    def test___init__(self):
        self.assertIsInstance(self.parser.soup, BeautifulSoup)

    def test_get_salmonrun_schedule(self):
        self.assertEqual(SALMONRUN_GT, self.parser.get_salmonrun_schedule())
