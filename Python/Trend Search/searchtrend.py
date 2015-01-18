'''

Created For Mini Projects Repository

Problem: An application to lookup the top trending topics in Twitter

Implementation: An application to find the top ten trending topics. The list of
places which the code supports is given at the start of the application and then
the top topics are shown according to the input.

@author: Sambit

'''

#Imports
import twitter
import json

#Keys required for authentication.
CONSUMER_KEY = 'Udxy6q9vuMHyESFe5a2Y3tsBv'
CONSUMER_SECRET = 'CDlMreFFIRhjyGRtePZrOPQw3xSOslJPktmDB6P7zHHmnno4Dv'
OAUTH_TOKEN = '2365425174-Cqk55BEV8rSpVDwSgLGIObNow4v3arHJRIkTr1I'
OAUTH_TOKEN_SECRET = 'JwcAgBGZk6yLK5rDRmX662tDngrsp7Z1bbstMRiGv8WJH'

#Authenticating the app
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

#Dictionary containing the WOE ID's of various countries.
country_id = {'World': 1,'UK': 23424975, 'India': 2295420, 'USA': 23424977, 'Japan': 1118129, 'Nigeria': 23424908, 'South Africa': 23424942, 'Canada': 23424775,'Argentina' :23424747}

print "Choose amongst the following. \n"

for country in country_id.keys():
    print country

print

#Getting the user's input.
country = raw_input("Enter the name of the place.\n")

if country_id.has_key(country):

    print 'The top 10 trending topics in ' +country+' are:'
    print '------------------------------\n'

    PLACE_WOE_ID = country_id[country]

    place_trends = twitter_api.trends.place(_id=PLACE_WOE_ID)
    count = 1
    for trend in place_trends[0]['trends']:
        print str(count) + ') ' + trend['name']
        count+=1
    print '\nThank You for using the service.'

else:

    print 'Information for that country is not available.'
