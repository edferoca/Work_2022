from ast import Num
import string
import re #filtrar cadenas
import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup #scaraping
import numpy as np #arrreglos y organizacion
import ssl #certificados dde navegacion web SSL
import pandas as pd

# ignora los certificados SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Adquiere  la direccion web y convierte en un objeto BeautifulSoup 
url = "http://www.meteobalaguer.com/"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Encuentra los tags td para obtneer la informacion de la tabla
tagsTD=soup.find_all('td')
# Crea una matriz con todos los datos de la tabla
DatosDeTabla= np.array([])
# limpiza de informacion no importante y llenado del arrelgo DatosDeTabla

for tag in tagsTD:
    if tag.string ==None:
        fonts=tag.find_all('font')
        for font in fonts:
            if len(font.contents) >=1:
                DatosDeTabla=np.append(DatosDeTabla,font.contents[0])
        
    else:  
        DatosDeTabla=np.append(DatosDeTabla,tag.string)
       
Datos=np.array([])
for datos in DatosDeTabla:
    try:
        if len(re.findall('\d+',str(datos)))>=1:
            Datos=np.append(Datos,datos)
        
    except:
        print("estano")

Datos=np.delete(Datos,[14,21,22,24],0)
#for data in Datos:
print(Datos)
print(Datos.size)

