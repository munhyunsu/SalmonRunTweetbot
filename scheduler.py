import urllib.request
from bs4 import BeautifulSoup as BS
import datetime
import pickle
from operator import itemgetter

from web_crawler import WebCrawler

PICKLENAME = 'salmonrun.pickle'

class Scheduler(WebCrawler):
    def __init__(self, baseurl = 'https://splatoonwiki.org'):
        super().__init__()
        self.baseurl = baseurl
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
        try:
            with open(PICKLENAME, 'rb') as f:
                schedule_list = pickle.load(f)
        except FileNotFoundError:
            schedule_list = list()

        # get current schedule
        # change our algorithm as policy of Splatoon2 WiKi
        salmon_times = self.get_schedule()[1]
        salmon_weapons = self.get_weapon()[1]
        salmon_stage = self.get_stage()[1]
        schedule = {'start_time': salmon_times[0],
                    'end_time': salmon_times[1],
                    'weapon1': salmon_weapons[0],
                    'weapon2': salmon_weapons[1],
                    'weapon3': salmon_weapons[2],
                    'weapon4': salmon_weapons[3],
                    'stage': salmon_stage}

        if schedule not in schedule_list:
            schedule_list.append(schedule)

        # remove entry with end time expired over 1H
        now = datetime.datetime.now()
        for entry in schedule_list:
            time_gap = (entry['end_time'] - now).total_seconds()
            if time_gap <= -3600:
                schedule_list.remove(entry)

        # sort by start_time!
        schedule_list.sort(key = itemgetter('start_time'))

        with open(PICKLENAME, 'wb') as f:
            pickle.dump(schedule_list, f)

        return schedule_list

    def get_schedule_list(self):
        return self.data