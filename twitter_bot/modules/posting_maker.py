import os
import sys
import datetime
import copy

from twitter_bot.modules.coordinator import ISO8601
from twitter_bot.modules.file_handler import FileHandler

START = '''[연어런 시작]
시간: {start_time:%m/%d %H:%M} - {end_time:%m/%d %H:%M}
스테이지: {stage}/{stage_jp}
무기: {weapon1}/{weapon1_jp}
{weapon2}/{weapon2_jp}
{weapon3}/{weapon3_jp}
{weapon4}/{weapon4_jp}'''

PLAN = '''[연어런 예정]
시간: {start_time:%m/%d %H:%M} - {end_time:%m/%d %H:%M}
스테이지: {stage}/{stage_jp}
무기: {weapon1}/{weapon1_jp}
{weapon2}/{weapon2_jp}
{weapon3}/{weapon3_jp}
{weapon4}/{weapon4_jp}'''

END = '''[연어런 끝/다음 연어런]
시간: {start_time:%m/%d %H:%M} - {end_time:%m/%d %H:%M}
스테이지: {stage}/{stage_jp}
무기: {weapon1}/{weapon1_jp}
{weapon2}/{weapon2_jp}
{weapon3}/{weapon3_jp}
{weapon4}/{weapon4_jp}'''

BE1H = '''[종료 1시간 전]
{tweet_url}'''


class TweetMaker(object):
    def __init__(self):
        self.file_handler = FileHandler()

    def get_text(self, schedule, types):
        target = copy.deepcopy(schedule)
        if os.path.exists(self.file_handler.file_name):
            url = self.file_handler.read()
            target['tweet_url'] = url
        start_time = ''.join(schedule['start_time'].rsplit(':', 1))
        start_time = datetime.datetime.strptime(start_time, ISO8601)
        target['start_time'] = start_time
        end_time = ''.join(schedule['end_time'].rsplit(':', 1))
        end_time = datetime.datetime.strptime(end_time, ISO8601)
        target['end_time'] = end_time

        text = getattr(sys.modules[__name__], types)
        return text.format_map(target)


tweet_maker = TweetMaker()
