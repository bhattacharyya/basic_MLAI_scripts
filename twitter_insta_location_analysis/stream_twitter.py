#!/usr/bin/python

from twython import TwythonStreamer
import json
import time


class MyStreamer(TwythonStreamer):
	def on_success(self, data):
		#print(data)
		if 'text' in data:
			username = data['user']['screen_name']
			time = data['created_at']
			#tweet_text = data['text']
			tweet_text = "https://t.co/"+data['text'].split("/")[-1].strip() #only for instagram. otherwise choose line above
			source = data['source'].split(">")[1].split("<")[0]
			location = str(data['coordinates'])
			print(username + " | " + time + " | "  + tweet_text + " | " + source + " | " + "loc : " + location)

stream = MyStreamer(
	'urcred', 'urcred','urcred', 'urcred'
)

count_tweets = 0

try:
	stream.statuses.filter(track='instagram')
	count_tweets += 1
	if count_tweets % 1000 == 0:
		time.sleep(60)
except:
	pass

