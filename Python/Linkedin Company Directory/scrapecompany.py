from bs4 import BeautifulSoup
import requests

def getSoupObject(url):

    source_code = requests.get(url)
    html_text = source_code.text
    soup = BeautifulSoup(html_text)

    return soup

def getCompaniesByPlace(urls):

    for index,url in enumerate(urls):
        soup = getSoupObject(url)

        urls  = []
        names = []

        for item in soup.findAll('li',{"class":"content"}):
            name = item.string
            print name
            names.append(name)
            link = item.find('a')
            url  = link.get('href')
            print url
            urls.append(url)
        print '\n'*10

def getIndustryDataByPlace(urls,names):

    for index,url in enumerate(urls):
        soup = getSoupObject(url)

        urls  = []
        names = []

        for item in soup.findAll('li',{"class":"content"}):
            name = item.string
            # print name
            names.append(name)
            link = item.find('a')
            url  = link.get('href')
            # print url
            urls.append(url)

        getCompaniesByPlace(urls)


def getDataByIndustry():

    url  = 'https://www.linkedin.com/directory/companies/'
    soup = getSoupObject(url)

    urls  = []
    names = []

    for item in soup.findAll('li',{"class":"content"}):
        name = item.string
        names.append(name)
        link = item.find('a')
        url  = link.get('href')
        urls.append(url)

    getIndustryDataByPlace(urls,names)


getDataByIndustry()
