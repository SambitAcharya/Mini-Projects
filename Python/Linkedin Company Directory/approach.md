## Development Environment

**System**:	Mac OS X 10.9.5    
**Python**: 2.7.5

## Approach 

The problem was to retrieve data related to all the companies on LinkedIn. Mainly, the names of the companies and the
url to their company pages.

The task was fairly simple as i just had to make a crawler to crawl all the pages, with [this](https://www.linkedin.com/directory/companies/) page as the seed.

The crawler was made using [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/) and [Requests](http://docs.python-requests.org/en/latest/) and the same piece of code was reused for every page because of the similar HTML structure of the page.
