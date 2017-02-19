# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 16:29:41 2017

@author: wx961
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page1.html")
bs0bj =BeautifulSoup(html.read(),"lxml")
print (bs0bj.h1)