'''

Created For Mini Projects Repository

Problem: An application to stream tweets related to a particular topic

Implementation: Using twitter's API, a script has been made to stream tweets
related to a particular topic. The returned data has been split so as to only
store the tweets in a file along with the UNIX timestamp.

@author: Sambit

'''

#Imports
import tweepy
import time

#Importing functions
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#Tokens provided by the twitter API
ckey = 'FKIofCv16Ct93E3LhQGfRADk9'
csecret = 'eeWQXjuP88ovX2CAzxxZ7SKpsdKqdOFIVRDcpSPUwDrLEKYaec'
atoken = '2365425174-5KtFxyQSCp9NPvJoyXLXXZQyhJg6qWtBMxtypGX'
asecret = 'Q2BCdRYyIRq37xA1llOq9YkvhZajSgvaVFMIjGuj3pciL'

class listener(StreamListener):

	def on_data(self, data):
		try:

			#Splitting data to obtain the tweets only
			tweet = data.split(',"text":"')[1].split('","source')[0]
			print tweet

			#Saving the tweets to a file with a UNIX timestamp
			saveThis = str(time.time()) + '::' + tweet
			saveFile = open('SavedTweets.csv','a')
			saveFile.write(saveThis)
			saveFile.write('\n')
			saveFile.close()
			return True

		except BaseException, e:
			print 'failed ondata,', str(e)
			time.sleep(5)

	def on_error(self,status):
		print status

#Sending twitter authentication information
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["2015"]) # Topic goes here
 
