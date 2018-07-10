import urllib.request
from bs4 import BeautifulSoup as BS
import datetime
import pickle

from web_crawler import WebCrawler

class Scheduler(WebCrawler):
    def __init__(self, baseurl = 'https://splatoonwiki.org'):
        self.baseurl = baseurl
        self.mainpage = self._get_mainpage()
        self.data = self._get_update_pickle()

    def _get_update_pickle(self):
        '''
        pickle data form
        [{'start_time': ,
          'end_time': ,
          'weapon1': ,
          'weapon2': ,
          'weapon3': ,
          'weapon4': ,
          'stage': ,},
          {...}, {...}]
        :return:
        '''
        # with open('salmon.pickle','rb') as p:

        pass
