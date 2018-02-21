# Fetch and return api
# NOTE: Still need to request and regester a new bot from twitter

import tweepy, time, sys


def getApi():
	CONSUMER_KEY = 'hgfpOILTmVOceGyzb0paJSAWt'
	CONSUMER_SECRET = '1ukvoVxXyiNQbG7Cd6LTTSueCSZ4ROx3XNyJxaNo3l8JwZCf6J'
	ACCESS_KEY = '266248463-Ug7q5WQh9n3ZrSbtL0L0MQA6AMMN23uJtz5iJ7pV'
	ACCESS_SECRET = 'pjoTMqQ86mCEPBollfSo3OISZaS2S0S3QjvY3smQ2miAd'
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	return api
