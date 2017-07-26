#Lambda表达式本质上是一个函数 可作为其他函数的变量使用 一个函数不是定义成f(x, y)，而是定义成f(g(x), y), 或f(g(x), h(x))的形式

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")

taglist = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for tag in taglist:
    print(tag)
