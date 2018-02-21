import time
import json
import datetime

from twitterApiFetcher import getApi

def getTweets(user, tweetNum=10):
	api = getApi()

	tweetCollection = []

	tweetInd = api.user_timeline(screen_name=user, count=1)[0].id

	for i in range(0, int(tweetNum/20)):
		tweets = api.user_timeline(screen_name=user, inlcude_retweets=False, max_id=tweetInd)
		for tweet in tweets:
			tweetCollection.append({"date":tweet.created_at.strftime("%Y-%m-%d"), "text":tweet.text})
			tweetInd = tweet.id

		time.sleep(0.1)

	tweets = api.user_timeline(screen_name=user, inlcude_retweets=False, count=(tweetNum % 20), max_id=tweetInd)

	for tweet in tweets:
		tweetCollection.append({"date":tweet.created_at.strftime("%Y-%m-%d"), "text":tweet.text})
		print tweet.text + "\n\n"

	with open('{}_tweets.json'.format(str(user)), 'w') as f:
		json.dump(tweetCollection, f, indent = 2)

def getUserMeta(user):
	api = getApi()
	meta = api.get_user(screen_name=user)
	#print meta

	data = {}
	data["name"] = meta.name
	data["tweetNum"] = meta.statuses_count

	with open('{}_meta.json'.format(str(user)), 'w') as f:
		json.dump(data, f, indent = 2)
	
def getData(user):
	getTweets(user)
	getUserMeta(user)


