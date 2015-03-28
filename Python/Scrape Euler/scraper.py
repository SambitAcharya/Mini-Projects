from PIL import Image
import argparse
import pytesseract
import re
import urllib
import os

def getEulerScore(username):
    url = 'https://projecteuler.net/profile/'+username+'.png'
    filename = url.split('/')[-1]
    image = urllib.urlretrieve(url, filename)
    img = Image.open(filename)
    c=img.crop((5,40,75,60))
    score = pytesseract.image_to_string(c)
    score = re.sub("[^0-9]", "", score)
    os.remove(filename)
    return score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Username of the Eulerian',type = str)
    args = parser.parse_args()
    username =  args.name
    score = getEulerScore(username)
    print score

if __name__ == '__main__':
    main()
