import sys
import time
import datetime

from web_crawler import WebCrawler
from get_spread import get_translate_dict
from twitter import execute_retweet, post_tweet
from utils import should_post, should_post2, should_post3
from scheduler import Scheduler
from posting_maker import tweet_maker
from coordinator import Coordinator

def fault_torrent_main():
    for index in range(0, 30):
        try:
            main()
            break
        except Exception as e:
            if index == (30-1):
                return -1
            print('{0} Something is wrong(loop: {1}): {2}'.format(datetime.datetime.now(),
                                                             index+1, e))
            time.sleep(60)
            continue
    return 0


def main(argv = sys.argv):
    # create crawler
    scheduler = Scheduler()
    schedule_list = scheduler.get_schedule_list()
    # create coordinator
    coordinator = Coordinator()
    coordinator.feed_schedule_list(schedule_list)

    # get_variables
    # check_post = should_post3(schedule_list)

    # for debug
    # (start, plan, end) = (True, True, True)
    print(datetime.datetime.now(), schedule_list)

    # switch
    text = None
    start_schedule = coordinator.get_start_schedule()
    if start_schedule is not None:
        schedule = start_schedule
        text = tweet_maker.get_text(schedule, types='START')
        post_tweet(text)
    end_schedule = coordinator.get_end_schedule()
    if end_schedule is not None:
        schedule = end_schedule
        text = tweet_maker.get_text(schedule, types='END')
        post_tweet(text)
    plan_schedule = coordinator.get_plan_schedule()
    if plan_schedule is not None:
        schedule = plan_schedule
        text = tweet_maker.get_text(schedule, types='PLAN')
        post_tweet(text)

    print('Updated {0}'.format(text))

    # always execute
    execute_retweet()


if __name__ == '__main__':
    # sys.exit(main())
    sys.exit(fault_torrent_main())

