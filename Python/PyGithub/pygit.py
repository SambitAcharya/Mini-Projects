from github import Github

ACCESS_TOKEN = '5f569116bfbf651b435145d288bc35cb9cdf8b21'

USER = 'ptwobrussell'
REPO = 'Mining-the-Social-Web'

client = Github(ACCESS_TOKEN, per_page=100)
user = client.get_user(USER)
repo = user.get_repo(REPO)

stargazers = [ s for s in repo.get_stargazers() ]
print "Number of stargazers", len(stargazers)
