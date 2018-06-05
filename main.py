import sys
import time
import datetime

from web_crawler import WebCrawler
from get_spread import get_translate_dict
# from get_schedule import get_schedule
from twitter import execute_retweet, post_tweet
from utils import should_post

def main(argv = sys.argv):
    for index in range(0, 30):
        try:
            _main(argv)
            break
        except:
            if index == (30-1):
                return -1
            print('{0} Something is wrong(loop: {1})'.format(datetime.datetime.now(),
                                                             index+1))
            time.sleep(60)
            continue
    return 0


def _main(argv):
    # always execute
    execute_retweet()

    # create crawler
    crawler = WebCrawler()

    # get_variables
    (wp_en_jp, wp_en_ko, st_en_jp, st_en_ko) = get_translate_dict()
    (salmon1_times, salmon2_times) = crawler.get_schedule()
    (salmon1_weapons, salmon2_weapons) = crawler.get_weapon()
    (salmon1_stage, salmon2_stage) = crawler.get_stage()
    (start, plan, end) = should_post(salmon1_times)

    # for debug
    print(datetime.datetime.now(), salmon1_times, start, plan, end)

    # switch
    text = None
    if start == True:
        text = '''[연어런 시작]
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
        post_tweet(text)
    if plan == True:
        text = '''[연어런 예정]
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
        post_tweet(text)
    if end == True:
        text = '''[연어런 끝/다음 연어런]
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
        post_tweet(text)

    print('Updated {0}'.format(text))



if __name__ == '__main__':
    sys.exit(main())
