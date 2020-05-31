import os
import ssl
import tweepy
from pymongo import MongoClient
import pymongo
# Retriving tokens and keys from environment variables
twitterKey = os.getenv("twitterKey")
twitterSecretKey = os.getenv("twitterSecretKey")
accessToken = os.getenv("twitterAccessToken")
accessTokenSecret = os.getenv("twitterSecretToken")
password = os.getenv("mongoPass")

# Setting MongoDB
client = MongoClient("mongodb+srv://Armaan:" + password + "@cluster-1-dnqxb.mongodb.net/test?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
db = client.Twitter
hashtagCollection = db.Hashtags
# Setting up twitter API
auth = tweepy.OAuthHandler(twitterKey, twitterSecretKey)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
print(api.rate_limit_status())

# Finding tweets
tweetDict = {}
tweetNum = 0
for tweet in tweepy.Cursor(api.search,q="#Twitter",count=100).items():
    print(tweet.place)
    if tweet.coordinates is not None:
        tweetNum += 1
        print(tweet.place)
        tweetDict[str(tweetNum)] = str(tweet.coordinates)
        if tweetNum == 10:
            break

hashtagCollection.insert_one(tweetDict)



