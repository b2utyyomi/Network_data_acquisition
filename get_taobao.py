#  啊  好感动 抓下来了 
import urllib2
from sgmllib import SGMLParser

class ListName(SGMLParser):

    def __init__(self):
        self.is_li=""
        self.name=[]
        SGMLParser.__init__(self)

    def start_li(self,attrs):
        self.is_li=1
    def end_li(self):
        self.is_li=""

    def handle_data(self,data):
        if self.is_li:
            self.name.append(data)

if __name__ == '__main__':
    urls=urllib2.urlopen('https://www.taobao.com/markets/tbhome/market-list').read()
    listname=ListName()
    listname.feed(urls)
    for item in listname.name:
       if item!='\n':
          print item
   # print listname.name    #########write like this, the result will be ASCII
