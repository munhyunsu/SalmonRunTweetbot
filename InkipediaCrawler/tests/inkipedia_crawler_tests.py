import unittest
import os

from modules.inkipedia_crawler import InkipediaCrawler


class InkipediaCrawlerTestCase(unittest.TestCase):
    def tearDown(self):
        if os.path.exists(self.crawler.file_name):
            os.remove(self.crawler.file_name)

    def test___init___default_args(self):
        self.crawler = InkipediaCrawler()
        self.assertEqual('latest.html', self.crawler.file_name)
        self.assertEqual('https://splatoonwiki.org', self.crawler.base_url)

    def test___init___pass_args(self):
        test_file_name = 'custom.html'
        test_base_url = 'http://test.com'
        self.crawler = InkipediaCrawler(test_base_url, test_file_name)
        self.assertEqual(test_file_name, self.crawler.file_name)
        self.assertEqual(test_base_url, self.crawler.base_url)

    def test_crawl_main_page(self):
        self.crawler = InkipediaCrawler()
        self.crawler.crawl_main_page()
        self.assertTrue(os.path.exists(self.crawler.file_name))
