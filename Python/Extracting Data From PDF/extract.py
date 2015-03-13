import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

filename = 'table-1.10'
htmlfile = open(filename+'.html','w+')
files = {'f':(filename+'.pdf',open(filename+'.pdf','rb'))}
response = requests.post("https://pdftables.com/api?key=akp6nuf0ymip", files=files)
response.raise_for_status()

for chunk in response.iter_content(chunk_size=1024):
    if chunk:
        htmlfile.write(chunk)
    htmlfile.flush()
htmlfile.close()

htmldata = ''
with open(filename+'.html','r') as htmlfile:
    htmldata+=htmlfile.read()
soup = BeautifulSoup(htmldata,'html.parser')

rows = tables[0].find_all('tr')
start = 0
stop = 0

for row in rows:
    if 'STATES' in str(row):
        break
    start+=1
stop = start
for row in rows[start:]:
    if 'TOTAL (ALL INDIA)' in str(row):
        break
    stop+=1
