import sys
import datetime

from twitter_bot.modules.twitter_api import TweetAPI


def main():
    tweet_bot = TweetAPI()
    cnt = tweet_bot.retweet_by_keyword('#연어런')
    print('{0}: {1} posts are retweeted'.format(datetime.datetime.now(), cnt))


if __name__ == '__main__':
    sys.exit(main())