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
        # restore pickle from file
        with open('salmon.pickle', 'rb') as f:
            schedule_list = pickle.load(f)
        if len(schedule_list) == 0:
            schedule_list = list()

        # get current schedule
        # change our algorithm as policy of Splatoon2 WiKi
        (salmon1_times, salmon2_times) = self.get_schedule()
        (salmon1_weapons, salmon2_weapons) = self.get_weapon()
        (salmon1_stage, salmon2_stage) = self.get_stage()
        schedule = {'start_time': salmon2_times[0],
                    'end_time': salmon2_times[1],
                    'weapon1': salmon2_weapons[0],
                    'weapon2': salmon2_weapons[1],
                    'weapon3': salmon2_weapons[2],
                    'weapon4': salmon2_weapons[3],
                    'stage': salmon2_stage}

        if schedule not in schedule_list:
            schedule_list.append(schedule)

        # remove entry with end time expired over 1H

        # sort by start_time!


        with open('salmon.pickle', 'wb') as f:
            pickle.dump(schedule_list, f)

