import tweepy

from private.tweet_key import account_id, consumer_key, consumer_secret, access_token, access_token_secret
from private.developer_key import developer_id


class TwitterAPI(object):
    def __init__(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def retweet_by_keyword(self, keyword, read_max=10):
        api = self.api
        cnt_retweet = 0
        try:
            for tweet in tweepy.Cursor(api.search, q=keyword).items(read_max):
                tweet.retweet()
                cnt_retweet = cnt_retweet + 1
        except tweepy.error.TweepError:
            pass
        return cnt_retweet

    def post_tweet(self, text):
        api = self.api
        status = api.update_status(text)
        tweet_url = 'https://twitter.com/{0}/status/{1}'
        tweet_url = tweet_url.format(account_id, status.id_str)
        # self.direct_message(tweet_url)
        return tweet_url

    def post_tweet_with_image(self, text, image):
        api = self.api
        status = api.update_with_media(image, text)
        tweet_url = 'https://twitter.com/{0}/status/{1}'
        tweet_url = tweet_url.format(account_id, status.id_str)
        # self.direct_message(tweet_url)
        return tweet_url

    # def direct_message(self, message, receiver=developer_id):
    #     """bugs
    #     """
    #     api = self.api
    #     api.send_direct_message(user=receiver, text=message)


def main():
    tweet = TwitterAPI()
    # tweet.direct_message('here')


if __name__ == '__main__':
    main()
