import urllib.request
from bs4 import BeautifulSoup as BS
import datetime
import pickle
from operator import itemgetter

from wiki_parser import SplatoonWikiParser

PICKLENAME = 'salmonrun.pickle'

class Scheduler(object):
    def __init__(self, baseurl = 'https://splatoonwiki.org'):
        super().__init__()
        self.baseurl = baseurl
        self.mainpage = None
        self.data = self.get_update_pickle()

    def get_mainpage(self):
        '''
        :return: HTML of main page
        '''
        url = self.baseurl + '/wiki/Main_Page'
        if self.mainpage == None:
            with urllib.request.urlopen(url) as f:
                self.mainpage = f.read()
        return self.mainpage

    def get_update_pickle(self):
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

        # create parser
        parser = SplatoonWikiParser()
        parser.feed(self.get_mainpage())

        # get current schedule
        # change our algorithm as policy of Splatoon2 WiKi
        schedule = parser.get_schedule()

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

        # archive schedule data
        with open(PICKLENAME, 'wb') as f:
            pickle.dump(schedule_list, f)

        return schedule_list

    def get_schedule_list(self):
        return self.data