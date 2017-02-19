# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:55:15 2017

@author: wx961
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html,"lxml")

"""
nameList = bs0bj.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())
"""

"""    
headList = bs0bj.findAll({"h1","h2","h3","h4","h5","h6"})
for heads in headList:
    print(heads.get_text())
"""

"""
nameList2 = bs0bj.findAll(text="the prince")
print(len(nameList2))
"""

"""
allText = bs0bj.findAll(id="text")
print(allText)
print(allText[0].get_text())
"""