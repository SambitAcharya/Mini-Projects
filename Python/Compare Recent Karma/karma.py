import json
import urllib2


def obtainKarma(url):

    data = json.load(user_data)
    posts = data["data"]["children"]
    number_of_posts = len(posts)

    scores = []
    comments = []

    for post_id in range(number_of_posts):
        score = posts[post_id]["data"]["score"]
        comment = posts[post_id]["data"]["num_comments"]

        scores.append(score)
        comments.append(comment)

    print scores
    print comments

def getUserInfo():

    while True:

        username = input("Enter the name of the user.\n")
        
        url = "https://www.reddit.com/user/"+ username + ".json"
        print url

        try:
            user_data = urllib2.urlopen(url)
        except urllib2.HTTPError, err:
            if err.code == 404:
                print "This user doesn't exist."
            else:
                raise

obtain_karma("pepsi_next")
