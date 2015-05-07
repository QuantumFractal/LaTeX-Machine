


import time, string, sys
import requests, Queue, threading
import HTMLParser

import twitter
import secrets

# Clean some warnings up
requests.packages.urllib3.disable_warnings()



def main():

	# Setup Twitter Api
	twitter_access = twitter.Api(secrets.consumer_key, secrets.consumer_secret,
						  secrets.access_token_key, secrets.access_token_secret)
	
	q = Queue.Queue()

	# Open mentions, check for any new mentions
	with open('last_mention.txt', 'r+') as last_mentions:
		# Read our last mention
		last_mention_id = last_mentions.read()
		last_mentions.seek(0)

		# Get mentions using our last as an ID
		mentions = twitter_access.GetMentions(since_id=last_mention_id)

		if len(mentions) != 0:
			# Go through our mentions and parse them
			for mention in mentions:
				t = threading.Thread(target=execute, args=(q, mention))
				t.daemon = True
				t.start()
		

			#print q.get()
			#last_mentions.write(str(mentions[0].id))

		else:
			print 'Nobody needs me :('


def execute(q, mention):
	response = {'user':mention.user,'message':'thomasmoll.co'}

	latex_string = parse(mention.text)
	response['message'] = 'Hi there'



	q.put(response)

def parse(string):
	# Unescape html text
	text = HTMLParser.HTMLParser().unescape(string)

def make_latex(string):
	''' Make the image, return the path for uploading '''
	pass

def upload_image():
	''' Upload image to imgur and return image url '''
	return 'IMAGE URL'



	#api.PostUpdate(status[:120], None, 37.7833, -122.416)
		
	#postStatus(posts[0].title+" "+posts[0].url)

def post_responses(responses):
	# Post that stuff

	pass

if __name__ == '__main__':
	main()