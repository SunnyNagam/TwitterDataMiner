import time
import json
import datetime

from twitterApiFetcher import getApi

def getTweets(user, tweets=10):
	api = getApi()
	tweetCollection = []
	tweets = api.user_timeline(screen_name=user, inlcude_retweets=False, count=tweets)

	count = 0
	for tweet in tweets:
		tweetCollection.append({"date":tweet.created_at.strftime("%Y-%m-%d"), "text":tweet.text})

	with open('{}_tweets.json'.format(str(user)), 'w') as f:
		json.dump(tweetCollection, f, indent = 2)

def getUserMeta(user):
	return 0;

