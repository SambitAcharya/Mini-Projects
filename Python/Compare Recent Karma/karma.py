import json
import urllib2


def obtainKarma(users_data):

    for user_data in users_data:
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

    users_data = []
    count = 0
    while count<2:

        username = raw_input("Enter the name of the user. \n")
        print username
        count+=1
        url = "https://www.reddit.com/user/"+ username + ".json"
        print url

        try:
            user_data = urllib2.urlopen(url)
        except urllib2.HTTPError, err:
            if err.code == 404:
                print "This user doesn't exist.\nEnter another username."
                count-=1
            else:
                raise


        users_data.append(user_data)

    obtainKarma(users_data)


def main():
    getUserInfo()

main()
