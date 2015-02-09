from github import Github

ACCESS_TOKEN = '03a974af67767d95175c06d728e9904a4d2c4203'

USER = 'SambitAcharya'
REPO = 'Mini-Projects'

client = Github(ACCESS_TOKEN, per_page=100)

user = client.get_user(USER)
repo = user.get_repo(REPO)

# print repo
commits = [ s for s in repo.get_commits() ]
print "Number of commits", len(commits)
