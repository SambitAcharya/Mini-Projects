'''

Created For Mini Projects Repository

Problem: Design a web crawler

Implementation: The code has been written to crawl a popular forum and collect the
title of the topics after visiting the topic page.

@author: Sambit

'''

#imports
import requests
from bs4 import BeautifulSoup

#Functions

# Function to crawl pages and get data.
def forum_crawler(max_pages):

    '''

        @param Input: Number of pages the crawler needs to crawl.
        @return Output: List of all the topics upto @param pages.

    '''

    page=1
    topics = []

    while page <= max_pages:

        url = 'https://www.daniweb.com/software-development/python/114/' + str(page)

        # Printing @variable source_code will give the status code for the process
        source_code = requests.get(url)

        # Returns the HTML source from the URL to @variable html_text
        html_text = source_code.text

        # Creating a Beautiful Soup object from @variable html_text
        soup = BeautifulSoup(html_text)

        # Finding all the links with class 'item-name' and printing them out.
        for link in soup.findAll('a',{"itemprop" : "url discussionUrl"}):
            href = 'https://www.daniweb.com'+link.get('href')
            topic = get_individual_topic_title(href)
            print(topic)
            topics.append(topic)

        page+=1

    return topics


# Function to get the individual topic title.
def get_individual_topic_title(topic_url):

    '''

        @param Input: URL of the topic page.
        @return Output: Title of the topic in @param page.

    '''

    source_code = requests.get(topic_url)
    html_text  = source_code.text
    soup = BeautifulSoup(html_text)

    for topic_name in soup.findAll('h1', {"itemprop" : "headline"}):
        return topic_name.string



#Main Function

def main():

    #Storing the input in @variable NUMBER_OF_PAGES
    NUMBER_OF_PAGES = int(input("Enter number of pages to crawl.\n"))

    if NUMBER_OF_PAGES <= 0:
        print("Number Of Digits set as negative or zero.")
        print("Number Of Digits set to 1")
        NUMBER_OF_PAGES = 1

    topics = forum_crawler(NUMBER_OF_PAGES)

    #Printing the output to the console.
    print(topics)

main()
