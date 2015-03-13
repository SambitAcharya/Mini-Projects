import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

filename = 'table-1.10'
htmlfile = open(filename+'.html','w+')
files = {'f':(filename+'.pdf',open(filename+'.pdf','rb'))}
response = requests.post("https://pdftables.com/api?key=akp6nuf0ymip", files=files)
response.raise_for_status()

print response.text
# for chunk in response.iter_content(chunk_size=1024):
#     if chunk:
#         htmlfile.write(chunk)
#     htmlfile.flush()
# htmlfile.close()
