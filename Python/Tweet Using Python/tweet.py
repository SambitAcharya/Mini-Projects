from constants import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,\
 ACCESS_TOKEN_SECRET

from twitter import OAuth, Twitter

consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

# Authentication imformation
auth = OAuth(access_token,access_token_secret, consumer_key, consumer_secret)
t = Twitter(auth = auth)

#Tweet which is to be posted
tweet = "Twitter is awesome"

#Posting the tweet
t.statuses.update(status = tweet)
