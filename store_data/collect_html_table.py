# 获取HTML表格并写入CSV文件

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, 'lxml')

# 结果是一个字符串
link = bsObj.find("link")
print(link.attrs["href"])

# 结果是一个列表 为啥尼 我猜测 多个字符串就会变成列表
# <table class="wikitable sortable jquery-tablesorter" style="text-align: center; font-size: 85%; width: auto; table-layout: fixed;">
# 打印结果竟然是 [wikitable, sortable], 那么jquery-tablesorter去哪了
str1 = bsObj.find("table")
print(str1.attrs["class"])

# 结果可以正常打印 width: 12em     ### class真是奇怪啊
str2 = bsObj.find("th")
print(str2.attrs["style"])

table = bsObj.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")
csvFile = open("/media/hadoop/TAEKWOON/PYTHON/Net_data/store_data/wiki_table.csv", "wt", newline = '', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()

