# html5把不换行的一段文本写在两行， 那么抓过来就会自动添加换行啊 这个肿么破
# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

#recursive : bool型 True:查找所有子标签以及后代标签 False:只查找一级标签

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
#namelist = bsObj.findAll("span", {"class":"green"})             
#for name in namelist:
    #print(name)
    #获得文本只需 print(name.get_text())

#text用标签的文本内容去匹配
#namelist = bsObj.findAll(text = "the prince")
#for name in namelist:
#    print(name)
#print(len(namelist))

#keywords 选择具有指定属性的标签
allText = bsObj.findAll(id="text")
print(allText[0].get_text())
