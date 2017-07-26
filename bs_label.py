#比之前的HTMLParser和SGMLParser要简洁不少
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), "lxml")  # here, the book write like this: bsObj = BeautifulSoup(html.read()), but there is a warning, so I changed
print(bsObj.title)
