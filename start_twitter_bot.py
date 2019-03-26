import sys
import datetime
import traceback
import json

from twitter_bot.modules.coordinator import Coordinator
from twitter_bot.modules.twitter_api import TwitterAPI
from twitter_bot.modules.image_handler import ImageHandler
from twitter_bot.modules.file_handler import FileHandler
from twitter_bot.modules.posting_maker import TweetMaker


def fault_torrent_main():
    try:
        main()
    except Exception:
        error_report_main(traceback.format_exc())
        print('{0} Something is wrong: {1}'.format(datetime.datetime.now(),
                                                   traceback.format_exc()))
    return


def main():
    # main sequence
    # 1. read schedule file
    with open('latest_inkipedia_locale.json', 'r') as f:
        inkipedia = json.load(f)
    # 2. create coordinator with schedule_list
    coordinator = Coordinator(inkipedia['Salmon Run'])
    # 3. prepare upload
    tweet = TwitterAPI()
    image_handler = ImageHandler('./images/')
    latest_writer = FileHandler('')
    tweet_maker = TweetMaker()

    print(datetime.datetime.now(), inkipedia['Salmon Run'])

    # switch
    text = None
    end_schedule = coordinator.get_end_schedule()
    if end_schedule is not None:
        schedule = end_schedule
        text = tweet_maker.get_text(schedule, types='END')
        image_name = image_handler.get_merged_image(schedule)
        tweet_url = tweet.post_tweet_with_image(text, image_name)
        if not coordinator.is_open():
            latest_writer.write(tweet_url)
    plan_schedule = coordinator.get_plan_schedule()
    if plan_schedule is not None:
        schedule = plan_schedule
        text = tweet_maker.get_text(schedule, types='PLAN')
        image_name = image_handler.get_merged_image(schedule)
        tweet_url = tweet.post_tweet_with_image(text, image_name)
        if not coordinator.is_open():
            latest_writer.write(tweet_url)
    start_schedule = coordinator.get_start_schedule()
    if start_schedule is not None:
        schedule = start_schedule
        text = tweet_maker.get_text(schedule, types='START')
        image_name = image_handler.get_merged_image(schedule)
        tweet_url = tweet.post_tweet_with_image(text, image_name)
        if not coordinator.is_open():
            latest_writer.write(tweet_url)
    be1h_schedule = coordinator.get_1h_before_end_schedule()
    if be1h_schedule is not None:
        schedule = be1h_schedule
        schedule['tweet_url'] = latest_writer.read()
        text = tweet_maker.get_text(schedule, types='BE1H')
        tweet.post_tweet(text)

    print('Updated {0}'.format(text))


def error_report_main(message):
    # temporary disable
    # tweet = TwitterAPI()
    # tweet.direct_message(message)
    print(message)


if __name__ == '__main__':
    # sys.exit(main())
    sys.exit(fault_torrent_main())
