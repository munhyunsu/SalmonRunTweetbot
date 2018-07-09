import urllib
import pickle

class Scheduler(object):
    def __init__(self, baseurl = 'https://splatoonwiki.org'):
        self.baseurl = baseurl
        self.mainpage = self._get_mainpage()
        self.data = self._get_update_pickle()


    def _get_mainpage(self):
        url = self.baseurl + '/wiki/Main_Page'
        with urllib.request.urlopen(url) as f:
            mainpage = f.read()
        return mainpage


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


    def get_schedule(self):
        pass


    def get_weapon(self):
        pass


    def get_stage(self):
        pass