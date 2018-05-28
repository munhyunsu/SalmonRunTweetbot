import sys
import datetime

from get_spread import get_translate_dict
from get_schedule import get_schedule
from post_tweet import execute_retweet, post_tweet

def main(argv = sys.argv):
    # always execute
    execute_retweet()

    # get_variables
    (wp_en_jp, wp_en_ko, st_en_jp, st_en_ko) = get_translate_dict()
    (salmon1_start, salmon1_end, weapon1, stage1, salmon2_start, salmon2_end, weapon2, stage2) = get_schedule()
    (start, plan, end) = should_post(salmon1_start, salmon1_end)

    # switch
    text = None
    if start == True:
        text = '''[연어런 시작]
시간: {0} - {1}
스테이지: {2}/{3}
무기: {4}/{5}
{6}/{7}
{8}/{9}
{10}/{11}'''.format(salmon1_start.strftime('%m/%d %H:%M'), salmon1_end.strftime('%m/%d %H:%M'),
                                   stage1, st_en_jp[stage1],
                                   weapon1[0], wp_en_jp[weapon1[0]],
                                   weapon1[1], wp_en_jp[weapon1[1]],
                                   weapon1[2], wp_en_jp[weapon1[2]],
                                   weapon1[3], wp_en_jp[weapon1[3]])
        post_tweet(text)
    if plan == True:
        text = '''[연어런 예정]
시간: {0} - {1}
스테이지: {2}/{3}
무기: {4}/{5}
{6}/{7}
{8}/{9}
{10}/{11}'''.format(salmon1_start.strftime('%m/%d %H:%M'), salmon1_end.strftime('%m/%d %H:%M'),
                                   stage1, st_en_jp[stage1],
                                   weapon1[0], wp_en_jp[weapon1[0]],
                                   weapon1[1], wp_en_jp[weapon1[1]],
                                   weapon1[2], wp_en_jp[weapon1[2]],
                                   weapon1[3], wp_en_jp[weapon1[3]])
        post_tweet(text)
    if end == True:
        text = '''[연어런 끝/다음 연어런]
시간: {0} - {1}
스테이지: {2}/{3}
무기: {4}/{5}
{6}/{7}
{8}/{9}
{10}/{11}'''.format(salmon2_start.strftime('%m/%d %H:%M'), salmon2_end.strftime('%m/%d %H:%M'),
                                   stage2, st_en_jp[stage2],
                                   weapon2[0], wp_en_jp[weapon2[0]],
                                   weapon2[1], wp_en_jp[weapon2[1]],
                                   weapon2[2], wp_en_jp[weapon2[2]],
                                   weapon2[3], wp_en_jp[weapon2[3]])
        post_tweet(text)

    print('Updated {0}'.format(text))



def should_post(salmon1_start, salmon1_end):
    start = False
    plan = False
    end = False
    start_sec = (salmon1_start - datetime.datetime.now()).total_seconds()
    if (start_sec <= 3600) and (start_sec >= 0):
        start = True
    if (start_sec <= 21600) and (start_sec >= 18000):
        plan = True
    end_sec = (salmon1_end - datetime.datetime.now()).total_seconds()
    if (end_sec <= 0) and (end_sec >= -3600):
        end = True

    return (start, plan, end)


if __name__ == '__main__':
    sys.exit(main())
