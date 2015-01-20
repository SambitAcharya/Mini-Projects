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

def generateImage(text, fullpath, color = "#000", bgcolor = "#FFF", fontfullpath = None, fontsize = 52, leftpadding = 3, rightpadding = 3, width = 900):
    REPLACEMENT_CHARACTER = u'\uFFFD'
    NEWLINE_REPLACEMENT_STRING = ' ' + REPLACEMENT_CHARACTER + ' '

    # prepare linkback
    linkback = ""
    fontlinkback = ImageFont.truetype('font.ttf', 8)
    linkbackx = fontlinkback.getsize(linkback)[0]
    linkback_height = fontlinkback.getsize(linkback)[1]
    #end of linkback

    font = ImageFont.load_default() if fontfullpath == None else ImageFont.truetype(fontfullpath, fontsize)
    text = text.replace('\n', NEWLINE_REPLACEMENT_STRING)


def getText():
    print ("Enter Your Tweet.\n")
    return sys.stdin.read()

def main():

    text = getText()
    generateText(text)

main()
