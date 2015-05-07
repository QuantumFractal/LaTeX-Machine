
from __future__ import unicode_literals

import twitter

import secrets
import time, string

#Create a Client with the bot's credentials
twitter_access = twitter.Api(secrets.consumer_key, secrets.consumer_secret,
					  secrets.access_token_key, secrets.access_token_secret)




feed = twitter_access.GetUserTimeline()

# Get latest mentions

with open('last_mention.txt', 'r+') as last_mentions:
	last_mention_id = last_mentions.read()
	last_mentions.seek(0)

	mentions = twitter_access.GetMentions(since_id=last_mention_id)

	if len(mentions) != 0:
		for mention in mentions:
			print mention.text
			pass

		last_mentions.write(str(mentions[0].id))

	else:
		print 'Nobody needs me :('


	

#api.PostUpdate(status[:120], None, 37.7833, -122.416)
	
#postStatus(posts[0].title+" "+posts[0].url)
