"""
The code is used for scraping title and synopsis of movie from IMDB.
An example of a URL:https://www.imdb.com/title/tt0137523/

"""

import requests
from bs4 import BeautifulSoup
import re


def getDataFromImdb(url):
    beautifulSoupObj = buildBeautifulSoup(url)
    title = beautifulSoupObj.find("h1", {"data-testid": "hero-title"
                                                        "-block__title"}).text
    beautifulSoupObj = buildBeautifulSoup(url + "plotsummary")
    synopsis = beautifulSoupObj.findAll(id=re.compile("^synopsis"))[1].text

    return title, synopsis


def buildBeautifulSoup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.97 Safari/537.36',
        'cache-control': 'private, max-age=0, no-cache'
    }
    request = requests.get(url, headers=headers)
    if request.status_code == 200:
        return BeautifulSoup(request.text, "html.parser")
    else:
        return None


print(getDataFromImdb("https://www.imdb.com/title/tt0137523/"))
