import sys
import time
import datetime

from web_crawler import WebCrawler
from get_spread import get_translate_dict
from twitter import execute_retweet, post_tweet, TweetAPI
from utils import should_post, should_post2, should_post3
from scheduler import Scheduler
from posting_maker import tweet_maker
from coordinator import Coordinator


def fault_torrent_main():
    try:
        main()
    except Exception as e:
        error_report_main('{0}: {1}'.format(type(e).__name__, e))
        print('{0} Something is wrong: {1}'.format(datetime.datetime.now(), e))
    return


def main():
    # create crawler
    scheduler = Scheduler()
    schedule_list = scheduler.get_schedule_list()
    # create coordinator
    coordinator = Coordinator()
    coordinator.feed_schedule_list(schedule_list)
    # create tweet_api
    tweet = TweetAPI()

    print(datetime.datetime.now(), schedule_list)

    # switch
    text = None
    start_schedule = coordinator.get_start_schedule()
    if start_schedule is not None:
        schedule = start_schedule
        text = tweet_maker.get_text(schedule, types='START')
        tweet.post_tweet(text)
    end_schedule = coordinator.get_end_schedule()
    if end_schedule is not None:
        schedule = end_schedule
        text = tweet_maker.get_text(schedule, types='END')
        tweet.post_tweet(text)
    plan_schedule = coordinator.get_plan_schedule()
    if plan_schedule is not None:
        schedule = plan_schedule
        text = tweet_maker.get_text(schedule, types='PLAN')
        tweet.post_tweet(text)

    print('Updated {0}'.format(text))


def error_report_main(message):
    tweet = TweetAPI()
    tweet.direct_message(message)


if __name__ == '__main__':
    # sys.exit(main())
    sys.exit(fault_torrent_main())
