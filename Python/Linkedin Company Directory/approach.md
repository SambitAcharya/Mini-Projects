## Development Environment

**System**:	Mac OS X 10.9.5    
**Python**: 2.7.5

## Approach 

The problem was to retrieve data related to all the companies on LinkedIn. Mainly, the names of the companies and the
url to their company pages.

The task was fairly simple as i just had to make a crawler to crawl all the pages, with [this](https://www.linkedin.com/directory/companies/) page as the seed.

The crawler was made using [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/) and [Requests](http://docs.python-requests.org/en/latest/) and the same piece of code was reused for every page because of the similar HTML structure of the page.

##Issues

**1)** The issue was scraping a particular company's page. The html code wasn't returned by soup. Here is the code which was executed.

```python

from bs4 import BeautifulSoup
import requests
url = 'https://www.linkedin.com/company/ahi-development'
source_code = requests.get(url)
html_text = source_code.text
soup = BeautifulSoup(html_text)
print soup

```

And this was the output

```html

<html><head>
<script type="text/javascript">
window.onload = function() {
  var newLocation = "";
  if (window.location.protocol == "http:") {
    var cookies = document.cookie.split("; ");
    for (var i = 0; i < cookies.length; ++i) {
      if ((cookies[i].indexOf("sl=") == 0) && (cookies[i].length > 3)) {
        newLocation = "https:" + window.location.href.substring(window.location.protocol.length);
      }
    }
  }

  if (newLocation.length == 0) {
    var domain = location.host;
    var newDomainIndex = 0;
    if (domain.substr(0, 6) == "touch.") {
      newDomainIndex = 6;
    }
    else if (domain.substr(0, 7) == "tablet.") {
      newDomainIndex = 7;
    }
    if (newDomainIndex) {
      domain = domain.substr(newDomainIndex);
    }
    newLocation = "https://" + domain +  "/uas/login?trk=sentinel_org_block&session_redirect=" + encodeURIComponent(window.location)
  }
  window.location.href = newLocation;
}
</script>
</head></html>
```
This is not the same as the page source. As no html was returned, all the soup operations failed and scraping the logo of the company couldn't be done.

**2)** Slow and flaky internet connection

Since the data to be scraped is large, it took a lot of attempts to get all the data.
