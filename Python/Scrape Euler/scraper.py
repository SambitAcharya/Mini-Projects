from PIL import Image
import pytesseract
import re
import urllib


# url = 'http://code.org/images/code-logo-640x640.png'
url = 'https://projecteuler.net/profile/SambitAcharya.png'
filename = url.split('/')[-1]
image = urllib.urlretrieve(url, filename)
# image = requests.get(url)
img = Image.open(filename)
img.show()
c=img.crop((5,40,75,60))
a = pytesseract.image_to_string(c)
a = re.sub("[^0-9]", "", a)
#
print a

# with open('img.png', 'wb') as out_file:
#     shutil.copyfileobj(response.raw, out_file)
