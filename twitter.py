import tweepy

from tweet_key import consumer_key, consumer_secret, access_token, access_token_secret

def get_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api



def execute_retweet():
    api = get_api()
    # Search tweets contain keywords and retweet them
    try:
        for tweet in tweepy.Cursor(api.search, q='#연어런').items(10):
            tweet.retweet()
    except:
        pass



def post_tweet(text):
    api = get_api()
    api.update_status(text)
