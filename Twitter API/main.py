import pandas as pd
import requests
import json
import mytweepy
from mytweepy import Client

# Consumer Keys
api_key = 'xWV8osh8pqAIJZrrDt9pMnH2x'
api_key_secret = 'OTgPNGRVy76Zpm8jq81Y8E1dprMboZyu9BfNudHSakmhQxdA1Y'

# Access Token Keys
access_token = '750405920442740736-pqwiT4WLy10mIImu7pbTHRwGOQEkBNf'
access_token_secret = 'CjVdnRd762Yo9rdr4ViNqaGFCHEkfwSJ8zUPHefzaXGwT'

bearer_token = r'AAAAAAAAAAAAAAAAAAAAAAOvtwEAAAAA4GlYzbwCrvuWSpHRD2k8ZhEHqss'

auth = mytweepy.OAuth2AppHandler(consumer_key=api_key, consumer_secret=api_key_secret)
api = mytweepy.API(auth)

client = mytweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)

person = Client.get_user(client, username='GokByk')
print(person)

# auth = tweepy.OAuth2AppHandler(
#   api_key, api_key_secret
# )
# api = tweepy.API(auth)

# response = Client.get_user(Client, username='GokByk')
# user = response.data
# print(user)
# search_query = " 'Elon Musk' 'fired' -filter:retweets AND -filter:replies AND -filter:links"
# no_of_tweets = 1

# try:
#   tweets = api.search_tweets(q=search_query, lang="en", count=no_of_tweets, tweet_mode="extended")

#   attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]

#   columns = ['User', 'Date Created', 'Number of Likes', 'Source of Tweet', 'Tweet']

#   tweets_df = pd.DataFrame(attributes_container, columns=columns)
# except BaseException as e:
#   print('Status Failed On,', str(e))

# def fetch_user_account_info(client, username):
#   response = client.get_user(username=username, user_fields=["created_at", "descriptions", "public_metrics"])
#   user = response.data
#   print(user.keys())
#   values = {"user_id": user.id, "username": user.username, "created_at": user.created_at, "description": user.description}
#   values.update(user.public_metrics)
#   ser = pd.Series(values)
  
#   return ser


# with open("twitter_keys.json") as infile:
#   json_obj = json.load(infile)
#   token = json_obj["bearer_token"]

#   client = tweepy.Client(bearer_token=token)

#   username = "GokByk"
#   user_ser = fetch_user_account_info(client, username)
#   print(user_ser)
