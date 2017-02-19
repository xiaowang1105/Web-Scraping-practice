# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:32:36 2017

@author: wx961
"""

from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print (html.read())