import sys

import twitter


def main():
    tweet_bot = twitter.TweetBot()
    tweet_bot.retweet_by_keyword('#연어런')


if __name__ == '__main__':
    sys.exit(main())