from linkedin import linkedin
import json
from prettytable import PrettyTable

CONSUMER_KEY = 'YOUR-KEY-HERE'
CONSUMER_SECRET = 'YOUR-SECRET-HERE'
USER_TOKEN = 'YOUR-TOKEN-HERE'
USER_SECRET = 'YOUR-SECRET-HERE'


RETURN_URL = 'http://www.google.com'

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,USER_TOKEN, USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums.values())

app = linkedin.LinkedInApplication(auth)

app.get_profile()

connections = app.get_connections()
# connections_data = 'linkedin_connections.json'
#
# f = open(connections_data, 'w')
# f.write(json.dumps(connections, indent=1))
# f.close()

# pt = PrettyTable(field_names=['Name', 'Location'])
# pt.align = 'l'
#
# [ pt.add_row((c['firstName'] + ' ' + c['lastName'], c['location']['name'])) for c in connections['values'] if c.has_key('location') ]
#
# print pt


my_positions = app.get_profile(selectors=['positions'])
print json.dumps(my_positions, indent=1)
