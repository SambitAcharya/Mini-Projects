'''

Created For Mini Projects Repository

Problem: Design a Reddit crawler.

Implementation: The code has been written to crawl Reddit and obtain information
about the user after parsing the json data obtained. The following code obtains
the no of likes and the number of comments on the first 25 posts of two redditors.
The username of the redditors have to be given by the user. The code has been
designed to handle all the invalid username cases.
Comparing the values obtained, we can compare their 'Karmas'

@author: Sambit

'''

#Imports
import json
import urllib2

#Functions

#Function to obtain information from the JSON object.
def obtainKarma(users_data):

    '''

        @param Input: Data of the users returned by @function getUserInfo.
        @print Output: List containing information about the users.

    '''


    users_info = []
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

        users_info.append((scores,comments))

    user_id = 0
    for user_info in users_info:
        user_id+=1
        print "User " + str(user_id)
        for user_attr in user_info:
            #Printing output to the console.
            print user_attr



# Function to obtain reddit user information from the user
def getUserInfo():

    '''

        @param Input: No input parameters
        @print Output: Data of the users

    '''


    users_data = []
    count = 0
    while count<2:

        count+=1

        username = raw_input("Enter the name of the user. \n")
        url = "https://www.reddit.com/user/"+ username + ".json"

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

#Main Function
def main():
    getUserInfo()

main()
