from PIL import Image
import argparse
import pytesseract
import re
import urllib
import os

parser = argparse.ArgumentParser()
parser.add_argument('name', help='Username of the user',type = str)
args = parser.parse_args()
username =  args.name
url = 'https://projecteuler.net/profile/'+username+'.png'
filename = url.split('/')[-1]
image = urllib.urlretrieve(url, filename)
# image = requests.get(url)
img = Image.open(filename)
c=img.crop((5,40,75,60))
a = pytesseract.image_to_string(c)
a = re.sub("[^0-9]", "", a)
print a

os.remove(filename)
