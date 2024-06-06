import tweepy

# Consumer Keys
api_key = 'xWV8osh8pqAIJZrrDt9pMnH2x'
api_key_secret = 'OTgPNGRVy76Zpm8jq81Y8E1dprMboZyu9BfNudHSakmhQxdA1Y'

bearer_token = r'AAAAAAAAAAAAAAAAAAAAAAOvtwEAAAAA4GlYzbwCrvuWSpHRD2k8ZhEHqss'


# Access Token Keys
access_token = '750405920442740736-pqwiT4WLy10mIImu7pbTHRwGOQEkBNf'
access_token_secret = 'CjVdnRd762Yo9rdr4ViNqaGFCHEkfwSJ8zUPHefzaXGwT'

auth = tweepy.OAuth2BearerHandler(bearer_token)
api = tweepy.API(auth)

client = tweepy.Client(bearer_token = bearer_token, consumer_key = api_key, consumer_secret = api_key_secret, access_token = access_token, access_token_secret = access_token_secret)
# client = tweepy.Client(bearer_token = bearer_token)

# response = client.create_tweet(text="hello world!")
# response = client.get_followed_lists()
response = client.get_tweets(2)
# print(response)


# user = api.get_user(username="GokByk", user_auth=True)
# print(user)
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)