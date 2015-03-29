from bs4 import BeautifulSoup
import requests

def getSoupObject(url):

    source_code = requests.get(url)
    html_text = source_code.text
    soup = BeautifulSoup(html_text)

    return soup

def getUrlsFromPage(url):

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

    return urls

def getNameAndLogo(urls):

    for url in urls:
        # print url
        soup = getSoupObject(url)
        print soup
        # title = soup.find('img',{'class':'image'})
        # print title.get(src)

def getCompaniesByPlace(urls):

    # urls = getNameAndUrl(urls)

    # print urls

    for index,url in enumerate(urls):
        # soup = getSoupObject(url)
        #
        # urls  = []
        # names = []
        #
        # for item in soup.findAll('li',{"class":"content"}):
        #     name = item.string
        #     print name
        #     names.append(name)
        #     link = item.find('a')
        #     url  = link.get('href')
        #     print url
        #     urls.append(url)
        # print '\n'*10
        urls = getUrlsFromPage(url)
        getNameAndLogo(urls)

def getIndustryDataByPlace(urls):

    for index,url in enumerate(urls):
        # soup = getSoupObject(url)
        #
        # urls  = []
        # names = []
        #
        # for item in soup.findAll('li',{"class":"content"}):
        #     name = item.string
        #     # print name
        #     names.append(name)
        #     link = item.find('a')
        #     url  = link.get('href')
        #     # print url
        #     urls.append(url)


        urls = getUrlsFromPage(url)

        getCompaniesByPlace(urls)


def getDataByIndustry():

    url  = 'https://www.linkedin.com/directory/companies/'
    # soup = getSoupObject(url)
    #
    # urls  = []
    # names = []
    #
    # for item in soup.findAll('li',{"class":"content"}):
    #     name = item.string
    #     names.append(name)
    #     link = item.find('a')
    #     url  = link.get('href')
    #     urls.append(url)
    urls = getUrlsFromPage(url)

    getIndustryDataByPlace(urls)


getDataByIndustry()
