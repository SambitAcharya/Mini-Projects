## Development Environment

**System**:	Mac OS X 10.9.5    
**Python**: 2.7.5

## Approach 

The problem was to retrieve data related to all the companies on LinkedIn. Mainly, the names of the companies and the
url to their company pages.

The task was fairly simple as i just had to make a crawler to crawl all the pages, with [this](https://www.linkedin.com/directory/companies/) page as the seed.

The crawler was made using [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/) and [Requests](http://docs.python-requests.org/en/latest/) and the same piece of code was reused for every page because of the similar HTML structure of the page.

##Issues

**1)**The issue was scraping a particular company's page. The html code wasn't returned by soup. Here is the code which i executed.

```python

from bs4 import BeautifulSoup
import requests
url = 'https://www.linkedin.com/company/ahi-development'
source_code = requests.get(url)
html_text = source_code.text
soup = BeautifulSoup(html_text)
print soup

```
