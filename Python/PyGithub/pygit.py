from github import Github

ACCESS_TOKEN = 'a8746727dba9944c93842574aa7812a4be791eba'

USER = 'SambitAcharya'
REPO = 'Mini-Projects'

client = Github(ACCESS_TOKEN, per_page=100)

user = client.get_user(USER)
repo = user.get_repo(REPO)

# print repo
commits = [ s for s in repo.get_issues() ]
print "Number of commits", len(commits)
