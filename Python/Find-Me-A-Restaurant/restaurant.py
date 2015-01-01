'''

Created For Mini Projects Repository

Problem: Obtain the name and phone nuumbers of restaurants in a given locality.

Implementation: All of the above information is obtained by using the locu api.

@author: Sambit

'''

#Imports
import urllib2
import json

# Function to print the name and the phone numbers of restaurants in a locality.
def locu_search(query,key):

    """

        @param Input:  Locality of the restaurant
        @print Output: Name and phone number of the restaurant

    """

    api_key = key
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    locality = query.replace(' ','%20')
    final_url = url + "&locality=" + locality + "&category=restaurant"
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)

    for item in data['objects']:
       print item['name'], item['phone']

#Main Function
def main():

    #API key obtained after registering as a locu developer.
    key = 'd2e36f1a04204eee891140a7e61387133cd51b1d'
    locu_search('Hyderabad',key)

main()
