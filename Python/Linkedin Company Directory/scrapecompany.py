#Imports
from bs4 import BeautifulSoup
import requests

def getSoupObject(url):

    '''
        
        Function to return the BS object after passing the URL.

    '''

    source_code = requests.get(url)
    html_text = source_code.text
    soup = BeautifulSoup(html_text)

    return soup

def getUrlsFromPage(url):

    '''

        Function to scrape the URL's from the page and store them in a list.
        Due to similar page structure's in all the pages, this function is 
        called a lot of times.
            
    '''

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

    '''

        Function to write the required data to the file.

    '''

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

    '''

        Function to get Industry data by place
    
    '''

    for index,url in enumerate(urls):
        urls = getUrlsFromPage(url)
        getCompaniesByPlace(urls)


def getDataByIndustry():

    '''
    
        Function to get data by Industry
    
    '''

    url  = 'https://www.linkedin.com/directory/companies/'
    urls = getUrlsFromPage(url)

    getIndustryDataByPlace(urls)

def main():
    
    getDataByIndustry()

file = open('companies.txt','a') #Code to open the file to write the data to.

if __name__ == '__main__':
    main()