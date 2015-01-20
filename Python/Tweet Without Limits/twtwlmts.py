import textwrap
import sys
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def generateText(text):

    num = 1
    den = len(text)/140 + 1

    add = str(num)+'/'+str(den)+': '
    const = 140 - len(add)
    count = 0

    start = 0
    end = start + const
    tweets = []

    # print '\n----------------------------------           Tweets       -----------------------------------'

    while count < den:

        add = str(num)+'/'+str(den)+': '
        tweet = add + text[start:end]

        tweets.append(tweet)

        start=end+1
        end = start + const

        count+=1
        num+=1

    for tweet in tweets:
        print tweet

def generateImage():
    return 0

def getText():
    print ("Enter Your Tweet.\n")
    return sys.stdin.read()

def main():

    text = getText()
    generateText(text)

main()
