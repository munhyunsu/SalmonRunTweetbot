import unittest
import unittest.mock

from modules.random_selector import RandomSelector


class RandomSelectorTestCase(unittest.TestCase):
    def setUp(self):
        locale1 = {'One': '하나',
                   'Two': '둘',
                   'Three': '셋'}
        locale2 = {'One': 'いち',
                   'Two': 'に',
                   'Three': 'さん'}
        locale = list(locale1.keys())
        self.random_selector = RandomSelector(locale, locale1, locale2)

    def tearDown(self):
        del self.random_selector

    def test_get_meme(self):
        author_mock = unittest.mock.Mock(name='player', mention='@player')
        ctx_mock = unittest.mock.Mock(author=author_mock)
        self.assertRegex(self.random_selector.get_random(ctx_mock),
                         '@player (?:One|Two|Three)/(?:하나|둘|셋)/(?:いち|に|さん)')
