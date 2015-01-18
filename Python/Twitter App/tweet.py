import twitter
import json
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
IND_WOE_ID = 2295420

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
ind_trends = twitter_api.trends.place(_id=IND_WOE_ID)


# print json.dumps(world_trends, indent=1)
# print "------------------------------------------------------------------------"
# print json.dumps(ind_trends, indent=1)
# print ind_trends[0]['trends']
for trend in ind_trends[0]['trends']:
    print trend['name']
