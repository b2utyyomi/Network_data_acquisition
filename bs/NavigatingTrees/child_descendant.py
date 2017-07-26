#这里输出的子标签太多了吧 感觉不太对呢 待解决  等等等等 我大概明白了 格式问题吧 像之前的换行一样的问题
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

# print children
for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)
print()
# print descendants
for descend in bsObj.find("table", {"id":"giftList"}).descendants:
    print(descend)
