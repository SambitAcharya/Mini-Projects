import twitter
from pprint import pprint

CONSUMER_KEY = 'Udxy6q9vuMHyESFe5a2Y3tsBv'
CONSUMER_SECRET = 'CDlMreFFIRhjyGRtePZrOPQw3xSOslJPktmDB6P7zHHmnno4Dv'
OAUTH_TOKEN = '2365425174-Cqk55BEV8rSpVDwSgLGIObNow4v3arHJRIkTr1I'
OAUTH_TOKEN_SECRET = 'JwcAgBGZk6yLK5rDRmX662tDngrsp7Z1bbstMRiGv8WJH'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# print twitter_api

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

print world_trends

print "------------------------------------------------------------------------"

print us_trends
