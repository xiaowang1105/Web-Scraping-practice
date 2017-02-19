# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:36:53 2017

@author: wx961
"""

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
def getTittle(url):
    try:
        html = urlopen(url)
    except (HTTPError , URLError) as e:
        return None
    try:
        bs0bj = BeautifulSoup(html.read(), "lxml")
        title = bs0bj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTittle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)