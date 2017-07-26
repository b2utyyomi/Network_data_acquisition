#HTTPError: web page doesn't exist on the server or the server does not exist
#URLError: the url is wrong

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
def getTitle(url):
    #first, check if the url exists
    try:   
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
