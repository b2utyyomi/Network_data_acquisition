#  urlparse.urlparse(urlstr, scheme='', allow_fragments=True)
#  函数urlparse()的作用是将URL分解成不同的组成部分，它从urlstr中取得URL，并返回元组 (scheme, netloc, path, params, query, fragment)。
# 如果urlstr中没有提供默认的网络协议或者下载规划时，可以使用default_scheme. 
# allowFrag标识一个URL是否允许使用零部件。
# scheme://net_loc/path;params?query#fragment

# scheme    网络协议或者下载规划
# net_loc   服务器位置（可能存在用户信息）
# path      斜杠（/）限定文件或者CGI应用程序的路径
# params    可选参数
# query     连接符（&）连接键值对
# fragment  拆分文档中的特殊锚

# net_log 可以进一步拆分成多个部件，格式如下：
# user:passwd@host:port
# user    登录名
# passwd  用户的密码
# host    web服务器运行的机器名或地址
# port    端口号


# Problem: urllib.error.HTTPError: HTTP Error 403: Forbidden
# 服务器禁止爬虫访问 网站为了防止这种非正常的访问,会验证请求信息中的UserAgent(它的信息包括硬件平台、系统软件、应用软件和用户个人偏好),如果UserAgent存在异常或者是不存在,那么这次请求将会被拒绝(如上错误信息所示)
# Solution: 在请求中加入UserAgent的信息即可 
# 可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询  
#  headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}
#  req = urllib.request.Request(url=chaper_url, headers=headers)  
#  urllib.request.urlopen(req).read()  

from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.request import Request

from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# 获取所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []
    # 找出所有以“/”开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    #找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    req = Request(url=startingPage, headers=headers)
    html = urlopen(req).read()
    bsObj = BeautifulSoup(html, "lxml")
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("No external links, looking around the site for one")
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: " + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")

