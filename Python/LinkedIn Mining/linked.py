from linkedin import linkedin

CONSUMER_KEY = 'YOUR-KEY-HERE'
CONSUMER_SECRET = 'YOUR-SECRET-HERE'
USER_TOKEN = 'YOUR-TOKEN-HERE'
USER_SECRET = 'YOUR-SECRET-HERE'

RETURN_URL = 'http://www.google.com'

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,USER_TOKEN, USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums.values())

app = linkedin.LinkedInApplication(auth)

app.get_profile()
