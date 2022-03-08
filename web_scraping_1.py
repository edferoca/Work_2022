# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from ast import Num
import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import numpy as np
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://www.meteobalaguer.com/"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags=soup.find_all('td')
array= np.zeros(len(tags))


for tag in tags:
    if tag.string ==None:
        fonts=tag.find_all('font')
        for font in fonts:
            if len(font.contents) >=1:
                print(font.contents[0])
                

                #for i in font.contents:
                #    print(font.contents[i])
    else:  
        print(tag.string)
print(array)