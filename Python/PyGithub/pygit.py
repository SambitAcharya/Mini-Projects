from github import Github

ACCESS_TOKEN = 'YOUR_TOKEN_HERE'

USER = 'SambitAcharya'
REPO = 'Mini-Projects'

client = Github(ACCESS_TOKEN, per_page=100)

user = client.get_user(USER)
repo = user.get_repo(REPO)

# print repo
commits = [ s for s in repo.get_commits() ]
# issues =  [ s for s in repo.get_issues() ]

print "Number of commits", len(commits)
