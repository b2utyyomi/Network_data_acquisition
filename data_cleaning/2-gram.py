# n-gram:文字或语言中的n个连续的单词组成的序列
# sorted(iterable[, cmp[, key[, reverse]]])
# students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# sorted(students, key=lambda student : student[2])
# sorted(students, key=operator.itemgetter(2)) 
# sorted函数也可以进行多级排序，例如要根据第二个域和第三个域进行排序，可以这么写：
# sorted(students, key=operator.itemgetter(1,2)) 

from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import string
import re
import operator
'''会得到很多零乱的数据    xxxx\n\n\nxxxx  这样的
def ngrams(input, n):
    input = input.split(' ')
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output
'''

def cleanInput(input):
    input = re.sub('\n+', ' ', input).lower()
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item)>1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    input = cleanInput(input)   
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = " " .join(input[i:i+n]) # 连成字符串
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output

# html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
# bsObj = BeautifulSoup(html, "lxml")
# content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = ngrams(content, 2)
sortedNgrams = OrderedDict(sorted(ngrams.items(), key=operator.itemgetter(1), reverse = True))
print(sortedNgrams)
print("2-grams count is: "+str(len(sortedNgrams)))

