# 获取标签属性用regex是极好滴
# 注意获取全部属性是 myTag.attrs 获取某个属性 myTag.attrs["XXX"]  or myTag["XXX"]
# 获得图片的相对路径 <img src="../img/gifts/img3.jpg">
# regular expression
# image["src"]这里和以前不大一样哈 images是一个字典哪 以前都是列表的。。。 那就对比一下
# 哈哈 速成的是不行 列表的它获取的是整个标签加上之间的文本 字典哪 键值对嘛 name[key]自然等于value 它获取的是值啊
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html1 = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html1)
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts\/img.\.jpg")})
for image in images:
    #print(image.get_text()) 什么都没有 因为没有文本啊
    #print(image)            整个标签
    print(image["src"])

print()
for image in images:
    print(image.attrs["src"])

html2 = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html2)
print()
namelist = bsObj.findAll("span", {"class":"green"})
for name in namelist:
    #print(name["class"])
    print(name)
