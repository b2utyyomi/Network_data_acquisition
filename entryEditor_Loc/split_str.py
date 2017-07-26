# seperate "Q28865" from str1
str1 = "https://www.wikidata.org/wiki/Q28865#sitelinks-wikipedia"
list1 = str1.split('/')
list2 = list1[4].split('#')
ID = list2[0]
print(ID)
