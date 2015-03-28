# Imports
from PIL import Image
import argparse
import pytesseract
import re
import urllib
import httplib
import os

def getEulerScore(username):

    '''

        Function to get the euler score, accepting the username
        as a parameter.

    '''

    url = 'https://projecteuler.net/profile/'+username+'.png'
    filename = url.split('/')[-1]

    image = urllib.urlretrieve(url, filename) # Downloading the image from projecteuler site.
    img = Image.open(filename)

    cropped_image=img.crop((5,40,75,60)) # Cropping the image for better clarity

    score = pytesseract.image_to_string(cropped_image) # Converting image to text using the library

    score = re.sub("[^0-9]", "", score) # Removing all non digit characters from the extracted text.
    os.remove(filename) # Deleting the downloaded image to save space

    return score


def main():

    '''

        Main Function

    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Username of the Eulerian',type = str)
    args = parser.parse_args()

    username =  args.name
    score = getEulerScore(username)

    print score

if __name__ == '__main__':
    main()
