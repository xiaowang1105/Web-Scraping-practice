# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 23:29:47 2017

@author: wx961
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs0bj = BeautifulSoup(html,"lxml")

""" children or descendants tag
for child in bs0bj.find("table",{"id":"giftList"}).children:
    print(child)
    
for child in bs0bj.find("table",{"id":"giftList"}).descendants:
    print(child)
"""

for sibling in bs0bj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)