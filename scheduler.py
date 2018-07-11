import urllib.request
from bs4 import BeautifulSoup as BS
import datetime
import pickle

from web_crawler import WebCrawler

class Scheduler(WebCrawler):
    def __init__(self, baseurl = 'https://splatoonwiki.org'):
        super.__init__(self)
        self.baseurl = baseurl
        # self.mainpage = self._get_mainpage()
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
        (salmon1_times, salmon2_times) = self.get_schedule()
        (salmon1_weapons, salmon2_weapons) = self.get_weapon()
        (salmon1_stage, salmon2_stage) = self.get_stage()
        schedule = {'start_time': salmon1_times[0],
                    'end_time': salmon1_times[1],
                    'weapon1': salmon1_weapons[0],
                    'weapon2': salmon1_weapons[1],
                    'weapon3': salmon1_weapons[2],
                    'weapon4': salmon1_weapons[3],
                    'stage': salmon1_stage}
        schedule_list = list()
        schedule_list.append(schedule)
        # with open('salmon.pickle','rb') as p:

        pass
