import os
import tweepy
import pymongo
import pygame as pg
# Retriving tokens and keys from environment variables
twitterKey = os.getenv("twitterKey")
twitterSecretKey = os.getenv("twitterSecretKey")
accessToken = os.getenv("twitterAccessToken")
accessTokenSecret = os.getenv("twitterSecretToken")

# Setting up twitter API
auth = tweepy.OAuthHandler(twitterKey, twitterSecretKey)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

