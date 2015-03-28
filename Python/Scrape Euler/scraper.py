from PIL import Image
import pytesseract
import re
path = 'ksharma377'
img = Image.open(path+'.png')
c=img.crop((5,40,75,60))
a = pytesseract.image_to_string(c)
a = re.sub("[^0-9]", "", a)

print a
