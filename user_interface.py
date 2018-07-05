import datetime
import sys
from bs4 import BeautifulSoup
from get_spread import get_translate_dict
from utils import should_post

status = {'INIT': 0}

class UserInterface(object):
    def __init__(self):
        self.status = status['INIT']

    def first_screen(self):
        print('----*----*----*----*----*----*')
        print('|    SalmonRun Tweet Bot     |')
        print('----*----*----*----*----*----*')

    def schedule(self, crawler):
        (wp_en_jp, wp_en_ko, st_en_jp, st_en_ko) = get_translate_dict()
        (salmon1_times, salmon2_times) = crawler.get_schedule()
        (salmon1_weapons, salmon2_weapons) = crawler.get_weapon()
        (salmon1_stage, salmon2_stage) = crawler.get_stage()
        (start, plan, end) = should_post(salmon1_times)
        print(datetime.datetime.now(), salmon1_times, start, plan, end)

