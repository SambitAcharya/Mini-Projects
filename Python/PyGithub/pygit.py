from github import Github

# ACCESS_TOKEN = 'YOUR_TOKEN_HERE'


USER = 'SambitAcharya'
REPO = 'Mini-Projects'
ORG  = 'scipy'

client = Github(ACCESS_TOKEN, per_page=100)

user = client.get_user(USER)
repo = user.get_repo(REPO)
organization = client.get_organization(ORG)

## Code to get repositories of the organization

repos = organization.get_repos()

for repo in repos:
     print repo.name

## End

## Code to get members of organization

# repo_members = organization.get_members()
#
# for member in repo_members:
#     print member.name


## End


# commits = [ s for s in repo.get_commits() ]
# issues =  [ s for s in repo.get_issues() ]

# print "Number of commits:", len(commits)
