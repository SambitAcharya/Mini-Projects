from bs4 import BeautifulSoup
import requests

def getIndustryData():

    url = 'https://www.linkedin.com/directory/companies/'
    source_code = requests.get(url)
    html_text = source_code.text
    soup = BeautifulSoup(html_text)
    urls = []
    for item in soup.findAll('li',{"class":"content"}):
        link = item.find('a')
        url  = link.get('href')
        urls.append(url)


getIndustryData()
