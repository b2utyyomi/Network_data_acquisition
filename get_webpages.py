#看网页源代码 看得 眼都花了 额 暂时只会书上的例子啊 我发挥想象力改的就没有一个抓#成功的 很尴尬啊
import urllib.request
import lxml.etree
from lxml.cssselect import CSSSelector
url = 'http://blog.csdn.net/hshl1214/article/details/45816777'
response = urllib.request.urlopen(url)
html = response.read()
parser = lxml.etree.HTMLParser(encoding='utf-8')
doctree = lxml.etree.fromstring(html, parser)
span = CSSSelector("span.link_postdate")
temp = span(doctree)[0].text
print('The information is', temp, sep='\n')
