# 收集维基百科编辑者的地理位置
# To be improved...

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import json

random.seed(datetime.datetime.now())
# get next random entry(词条)
def getLinks(arcticleUrl):
    html = urlopen("http://en.wikipedia.org"+arcticleUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

# get editLink
def getEditLink(startPage):
    html = urlopen("http://en.wikipedia.org"+startPage)
    bsObj = BeautifulSoup(html, 'lxml')
    return bsObj.find("span",{"class":"wb-langlinks-edit wb-langlinks-link"}).find("a")

# get all users' ips (only those users who didn't use their accounts)
# pageUrl = "https://www.wikidata.org/wiki/Special:EntityPage/Q28865#sitelinks-wikipedia"
# 我试图从PageUrl中提取出Q28865来跳转到"https://www.wikidata.org/w/index.php?title=Q28865&offset=20170322143010&action=history"
# 但是offset找不到 也许在别的情况里面这个会是个好办法 但是很不幸 这次很糟糕 还是直接提取链接方便
# 也只是写起来方便而已 要打开好几次网页 有点麻烦吧 待我博览群书之后 也许会有好结果
# 呵 当真相浮出水面之后 我真想删了上面那几行 但是理智他阻止了我
def getHistoryIPs(pageUrl):
    str1 = pageUrl
    list1 = str1.split('/')
    list2 = list1[5].split('#')
    ID = list2[0]
    historyUrl = "https://www.wikidata.org/w/index.php?title="+ID+"&offset=&limit=500&action=history"
    print("history url is: "+historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "lxml")
    ipAddresses = bsObj.findAll("a", {"class":"mw-userlink mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

# 利用freegeoip.net查ip地址
def getAddress(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_name")+", "+responseJson.get("region_name")

# 打印地址信息
def printAddress(uncomplete_Url):
    editLink = getEditLink(uncomplete_Url)
    href = editLink.attrs['href']
    historyIPs = getHistoryIPs(href)
    for historyIP in historyIPs:
        country = getAddress(historyIP)
        if country is not None:
            print(historyIP + " is from " + country)
        else:
            print("Sorry, We can't find it!")

startPage = "/wiki/Python_(programming_language)"
printAddress(startPage)
links = getLinks(startPage)
while(len(links)>0):
    newLink = links[random.randint(0, len(links)-1)].attrs['href']
    printAddress(newLink)
    links = getLinks(newLink)
