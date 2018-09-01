import sys
import time
import datetime
import traceback

from web_crawler import WebCrawler
from get_spread import get_translate_dict
from twitter import execute_retweet, post_tweet, TweetAPI
from utils import should_post, should_post2, should_post3
from scheduler import Scheduler
from posting_maker import tweet_maker
from coordinator import Coordinator
from image_handler import ImageHandler


def fault_torrent_main():
    try:
        main()
    except Exception:
        error_report_main(traceback.format_exc())
        print('{0} Something is wrong: {1}'.format(datetime.datetime.now(),
                                                   traceback.format_exc()))
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
    # create image handler
    image_handler = ImageHandler('./images/')

    print(datetime.datetime.now(), schedule_list)

    # switch
    text = None
    start_schedule = coordinator.get_start_schedule()
    if start_schedule is not None:
        schedule = start_schedule
        text = tweet_maker.get_text(schedule, types='START')
        image_name = image_handler.get_merged_image(schedule)
        tweet_url = tweet.post_tweet_with_image(text, image_name)
        scheduler.update_tweet_url(schedule, tweet_url)
    end_schedule = coordinator.get_end_schedule()
    if end_schedule is not None:
        schedule = end_schedule
        text = tweet_maker.get_text(schedule, types='END')
        image_name = image_handler.get_merged_image(schedule)
        tweet.post_tweet_with_image(text, image_name)
    plan_schedule = coordinator.get_plan_schedule()
    if plan_schedule is not None:
        schedule = plan_schedule
        text = tweet_maker.get_text(schedule, types='PLAN')
        image_name = image_handler.get_merged_image(schedule)
        tweet.post_tweet_with_image(text, image_name)
    be1h_schedule = coordinator.get_1h_before_end_schedule()
    if be1h_schedule is not None:
        schedule = be1h_schedule
        text = tweet_maker.get_text(schedule, types='BE1H')
        tweet.post_tweet(text)

    print('Updated {0}'.format(text))


def error_report_main(message):
    tweet = TweetAPI()
    tweet.direct_message(message)


if __name__ == '__main__':
    # sys.exit(main())
    sys.exit(fault_torrent_main())
