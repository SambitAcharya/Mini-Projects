'''

Created for Mini-Projects Repository

Problem: Getting the data to form a dictionary of SMS abbreviations

Implementation: This scraper acquires data from http://www.webopedia.com/quick_ref/textmessageabbreviations.asp
for the creation of the dictionary by using BeautifulSoup

@author: Sambit

'''

#Imports
import requests
from bs4 import BeautifulSoup

toappend = ""
url = 'http://www.webopedia.com/quick_ref/textmessageabbreviations.asp'

# Creating the Beautiful Soup object
source_code = requests.get(url)
html_text = source_code.text
soup = BeautifulSoup(html_text)
soup = soup.table.tbody

#Iterating to get to the desired element
for link in soup.findAll('tr'):
    for abbr in link.findAll('td'):
        for txt in abbr.findAll('p'):
            toappend+=txt.text+" - "
    toappend = toappend[:-2]
    toappend+="\n"

# Saving the data to a file for further processing
abbreviations = open("abbreviation.txt",'w')
abbreviations.write(toappend.encode('utf-8').strip())
abbreviations.close()

# One or two elements had to be fixed manually for the program to work correctly. Use the abbreviations.txt file to get the correct results. 
#This scraper is going to generate abbreviation.txt which will have most of the data
