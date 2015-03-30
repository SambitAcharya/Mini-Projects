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
        names.append(name)
        link = item.find('a')
        url  = link.get('href')
        urls.append(url)

    return urls

def getCompaniesByPlace(urls):

    for index,url in enumerate(urls):
        soup = getSoupObject(url)

        urls  = []
        names = []

        for item in soup.findAll('li',{"class":"content"}):
            name = item.string
            names.append(name)
            link = item.find('a')
            url  = link.get('href')
            urls.append(url)
            string = name + ' - ' + url + '\n'
            print string
            file.write(string.encode('utf8'))
        

def getIndustryDataByPlace(urls):

    for index,url in enumerate(urls):
        urls = getUrlsFromPage(url)
        getCompaniesByPlace(urls)


def getDataByIndustry():

    url  = 'https://www.linkedin.com/directory/companies/'
    urls = getUrlsFromPage(url)

    getIndustryDataByPlace(urls)

def main():
    
    getDataByIndustry()

file = open('companies2.txt','a')
if __name__ == '__main__':
    main()