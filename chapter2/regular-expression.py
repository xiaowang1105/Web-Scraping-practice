# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:20:46 2017

@author: wx961
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

"""
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs0bj = BeautifulSoup(html,"lxml")

images = bs0bj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])
"""

html = urlopen("https://www.ece.cornell.edu/ece/people/faculty.cfm")
bs0bj = BeautifulSoup(html,"lxml")

print(bs0bj.findAll("img",{"src":"/engineering/customcf/iws_ai_faculty_display/ai_images/ea85.jpg"})

images = bs0bj.findAll("img",{"src":re.compile("\/engineering\/customcf\/iws_ai_faculty_display\/ai_images\/[a-z0-9]\.jpg")})
print(images)
for image in images:
    print(image["src"])    