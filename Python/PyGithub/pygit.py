import requests
from getpass import getpass
import json

username = 'testZaccount'
password = 'mytestaccount1234567890'

url  = 'https://api.github.com/authorizations'
note = 'My note'
post_data = { 'scopes':['repo'],'note': note }

response = requests.post(
    url,
    auth = (username, password),
    data = json.dumps(post_data),
    )

print "API response:", response.text
print
print "Your OAuth token is", response.json()['token']
