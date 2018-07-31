import sys

import twitter


def main():
    retweet = twitter.TweetBot()
    retweet.retweet_by_keyword('#연어런')


if __name__ == '__main__':
    sys.exit(main())