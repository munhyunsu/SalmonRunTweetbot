import sys
import time
import datetime

from web_crawler import WebCrawler
from get_spread import get_translate_dict
from twitter import execute_retweet, post_tweet
from utils import should_post, should_post2
from scheduler import Scheduler
from posting_maker import tweet_maker

def fault_torrent_main():
    for index in range(0, 30):
        try:
            main()
            break
        except:
            if index == (30-1):
                return -1
            print('{0} Something is wrong(loop: {1})'.format(datetime.datetime.now(),
                                                             index+1))
            time.sleep(60)
            continue
    return 0


def main(argv = sys.argv):
    # create crawler
    # crawler = WebCrawler()
    scheduler = Scheduler()

    schedule_list = scheduler.get_schedule_list()
    # print(schedule_list)

    # get_variables
    # (wp_en_jp, wp_en_ko, st_en_jp, st_en_ko) = get_translate_dict()
    (start, plan, end) = should_post2(schedule_list[0])
    # (salmon1_times, salmon2_times) = crawler.get_schedule()
    # (salmon1_weapons, salmon2_weapons) = crawler.get_weapon()
    # (salmon1_stage, salmon2_stage) = crawler.get_stage()
    # (start, plan, end) = should_post(salmon1_times)

    # for debug
    # (start, plan, end) = (False, False, False)
    print(datetime.datetime.now(), schedule_list, start, plan, end)

    # TODO(LuHa): Need to split viewer and controller
    # BUG: end schedule was not posted

    # switch
    text = None
    if start == True:
        schedule = schedule_list[0]
        text = tweet_maker(schedule, types='START')
#         text = '''[연어런 시작]
# 시간: {0} - {1}
# 스테이지: {2}/{3}
# 무기: {4}/{5}
# {6}/{7}
# {8}/{9}
# {10}/{11}'''.format(schedule['start_time'].strftime('%m/%d %H:%M'), schedule['end_time'].strftime('%m/%d %H:%M'),
#                     schedule['stage_en'], schedule['stage_jp'],
#                     schedule['weapon1_en'], schedule['weapon1_jp'],
#                     schedule['weapon2_en'], schedule['weapon2_jp'],
#                     schedule['weapon3_en'], schedule['weapon3_jp'],
#                     schedule['weapon4_en'], schedule['weapon4_jp'])
        post_tweet(text)
    if plan == True:
        schedule = schedule_list[0]
        text = tweet_maker(schedule, types='PLAN')
#         text = '''[연어런 예정]
# 시간: {0} - {1}
# 스테이지: {2}/{3}
# 무기: {4}/{5}
# {6}/{7}
# {8}/{9}
# {10}/{11}'''.format(schedule['start_time'].strftime('%m/%d %H:%M'), schedule['end_time'].strftime('%m/%d %H:%M'),
#                     schedule['stage_en'], schedule['stage_jp'],
#                     schedule['weapon1_en'], schedule['weapon1_jp'],
#                     schedule['weapon2_en'], schedule['weapon2_jp'],
#                     schedule['weapon3_en'], schedule['weapon3_jp'],
#                     schedule['weapon4_en'], schedule['weapon4_jp'])
        post_tweet(text)
    if end == True and len(schedule_list) > 1:
        schedule = schedule_list[1]
        text = tweet_maker(schedule, types='END')
#         text = '''[연어런 끝/다음 연어런]
# 시간: {0} - {1}
# 스테이지: {2}/{3}
# 무기: {4}/{5}
# {6}/{7}
# {8}/{9}
# {10}/{11}'''.format(schedule['start_time'].strftime('%m/%d %H:%M'), schedule['end_time'].strftime('%m/%d %H:%M'),
#                     schedule['stage_en'], schedule['stage_jp'],
#                     schedule['weapon1_en'], schedule['weapon1_jp'],
#                     schedule['weapon2_en'], schedule['weapon2_jp'],
#                     schedule['weapon3_en'], schedule['weapon3_jp'],
#                     schedule['weapon4_en'], schedule['weapon4_jp'])
        post_tweet(text)

    print('Updated {0}'.format(text))

    # always execute
    execute_retweet()


if __name__ == '__main__':
    # sys.exit(main())
    sys.exit(fault_torrent_main())

