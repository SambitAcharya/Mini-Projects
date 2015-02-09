from github import Github

ACCESS_TOKEN = 'YOUR_TOKEN_HERE'


USER = 'SambitAcharya'
REPO = 'Mini-Projects'
ORG  = 'scipy'

client = Github(ACCESS_TOKEN, per_page=100)

user = client.get_user(USER)
repo = user.get_repo(REPO)

organization = client.get_organization(ORG)
repo_org = organization.get_repos()

print repo_org
# commits = [ s for s in repo.get_commits() ]
# issues =  [ s for s in repo.get_issues() ]

# print "Number of commits:", len(commits)
