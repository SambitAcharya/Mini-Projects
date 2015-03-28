# try:
#     import Image
# except ImportError:
from PIL import Image
import pytesseract
import re
# path = r'/Users/Sambit/Mini-Projects/Python/Scrape Euler/praveen97uma.png'
path = 'ksharma377'
img = Image.open(path+'.png')
c=img.crop((5,40,75,60))
# c=img.crop((45,40,75,60))
# c.show()
a = pytesseract.image_to_string(c)
a = re.sub("[^0-9]", "", a)

print a
