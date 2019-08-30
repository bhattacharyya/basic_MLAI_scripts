#!/usr/bin/python

from twython import TwythonStreamer
import json
import time

#twitter = Twython('aGtrJA30BA50LGtZmdAc9zmJ3', 'by2EqbNQji9Xm66fcsVKRVt9B3WU6kAkekV3C4IJJb7ocu6w7q','2586262244-9S520P1X2sZW8ajbNyxUBALo1Ea2z17nVLaJZmt', 'yJVMOueRmiW5rce1tWJK40v6YEUMx5LDvQx9UjaBSf8LM')


'''
x = twitter.get_home_timeline()
for i in x:
	print(i['text']+"\n")

print ("&%^%&**&(&&*()*)(*()&*(^&%^^%^")

y = twitter.search(q='taylor', result_type='popular', count=200)

for n in range(len(y)):
	print(y[n])
'''

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
	'aGtrJA30BA50LGtZmdAc9zmJ3', 'by2EqbNQji9Xm66fcsVKRVt9B3WU6kAkekV3C4IJJb7ocu6w7q','2586262244-9S520P1X2sZW8ajbNyxUBALo1Ea2z17nVLaJZmt', 'yJVMOueRmiW5rce1tWJK40v6YEUMx5LDvQx9UjaBSf8LM'
)

count_tweets = 0

try:
	stream.statuses.filter(track='instagram')
	count_tweets += 1
	if count_tweets % 1000 == 0:
		time.sleep(60)
except:
	pass

