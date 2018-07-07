import datetime
import sys
from bs4 import BeautifulSoup
from get_spread import get_translate_dict
from utils import should_post

status = {'INIT': 0}

class UserInterface(object):
    def __init__(self, crawler):
        self.crawler = crawler
        (self.wp_en_jp, self.wp_en_ko, self.st_en_jp, self.st_en_ko) = get_translate_dict()
        (self.salmon1_times, self.salmon2_times) = crawler.get_schedule()
        (self.salmon1_weapons, self.salmon2_weapons) = crawler.get_weapon()
        (self.salmon1_stage, self.salmon2_stage) = crawler.get_stage()
        (self.start, self.plan, self.end) = should_post(salmon1_times)


    def first_screen(self):
        print('----*----*----*----*----*----*')
        print('|    SalmonRun Tweet Bot     |')
        print('----*----*----*----*----*----*')

    def get_start(self):
        start_text = '''[연어런 시작]
        시간: {0} - {1}
        스테이지: {2}/{3}
        무기: {4}/{5}
        {6}/{7}
        {8}/{9}
        {10}/{11}'''.format(salmon1_times[0].strftime('%m/%d %H:%M'), salmon1_times[1].strftime('%m/%d %H:%M'),
                            salmon1_stage, st_en_jp[salmon1_stage],
                            salmon1_weapons[0], wp_en_jp[salmon1_weapons[0]],
                            salmon1_weapons[1], wp_en_jp[salmon1_weapons[1]],
                            salmon1_weapons[2], wp_en_jp[salmon1_weapons[2]],
                            salmon1_weapons[3], wp_en_jp[salmon1_weapons[3]])

    def get_plan(self):
        plan_text = '''[연어런 예정]
        시간: {0} - {1}
        스테이지: {2}/{3}
        무기: {4}/{5}
        {6}/{7}
        {8}/{9}
        {10}/{11}'''.format(salmon1_times[0].strftime('%m/%d %H:%M'), salmon1_times[1].strftime('%m/%d %H:%M'),
                            salmon1_stage, st_en_jp[salmon1_stage],
                            salmon1_weapons[0], wp_en_jp[salmon1_weapons[0]],
                            salmon1_weapons[1], wp_en_jp[salmon1_weapons[1]],
                            salmon1_weapons[2], wp_en_jp[salmon1_weapons[2]],
                            salmon1_weapons[3], wp_en_jp[salmon1_weapons[3]])

    def get_end(self):
        end_text = '''[연어런 끝/다음 연어런]
        시간: {0} - {1}
        스테이지: {2}/{3}
        무기: {4}/{5}
        {6}/{7}
        {8}/{9}
        {10}/{11}'''.format(salmon2_times[0].strftime('%m/%d %H:%M'), salmon2_times[1].strftime('%m/%d %H:%M'),
                            salmon2_stage, st_en_jp[salmon2_stage],
                            salmon2_weapons[0], wp_en_jp[salmon2_weapons[0]],
                            salmon2_weapons[1], wp_en_jp[salmon2_weapons[1]],
                            salmon2_weapons[2], wp_en_jp[salmon2_weapons[2]],
                            salmon2_weapons[3], wp_en_jp[salmon2_weapons[3]])

        (wp_en_jp, wp_en_ko, st_en_jp, st_en_ko) = get_translate_dict()
        (salmon1_times, salmon2_times) = self.crawler.get_schedule()
        (salmon1_weapons, salmon2_weapons) = self.crawler.get_weapon()
        (salmon1_stage, salmon2_stage) = self.crawler.get_stage()
        (start, plan, end) = should_post(salmon1_times)





        #TODO(LuHa): beautify
        print('----*----*----*----*----*----*')
        print('Start {0}'.format(start))
        print(start_text)
        print('----*----*----*')
        print('Plan {0}'.format(plan))
        print(plan_text)
        print('----*----*----*')
        print('End {0}'.format(end))
        print(end_text)
        print('----*----*----*----*----*----*')