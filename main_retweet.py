import sys
import datetime

import twitter


def main():
    tweet_bot = twitter.TweetAPI()
    cnt = tweet_bot.retweet_by_keyword('#연어런')
    print('{0}: {1} posts are retweeted'.format(datetime.datetime.now(), cnt))


if __name__ == '__main__':
    sys.exit(main())