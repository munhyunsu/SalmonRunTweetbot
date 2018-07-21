import sys

START = '''[연어런 시작]
시간: {start_time:%m/%d %H:%M} - {end_time:%m/%d %H:%M}
스테이지: {stage_en}/{stage_jp}
무기: {weapon1_en}/{weapon1_jp}
{weapon2_en}/{weapon2_jp}
{weapon3_en}/{weapon3_jp}
{weapon4_en}/{weapon4_jp}'''

PLAN = '''[연어런 예정]
시간: {start_time:%m/%d %H:%M} - {end_time:%m/%d %H:%M}
스테이지: {stage_en}/{stage_jp}
무기: {weapon1_en}/{weapon1_jp}
{weapon2_en}/{weapon2_jp}
{weapon3_en}/{weapon3_jp}
{weapon4_en}/{weapon4_jp}'''

END = '''[연어런 끝/다음 연어런]
시간: {start_time:%m/%d %H:%M} - {end_time:%m/%d %H:%M}
스테이지: {stage_en}/{stage_jp}
무기: {weapon1_en}/{weapon1_jp}
{weapon2_en}/{weapon2_jp}
{weapon3_en}/{weapon3_jp}
{weapon4_en}/{weapon4_jp}'''


class TweetMaker(object):
    def get_text(self, schedule, types):
        text = getattr(sys.modules[__name__], types)

        return text.format_map(schedule)


tweet_maker = TweetMaker()