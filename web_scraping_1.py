

from ast import Num
import string
import re
import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import numpy as np
import ssl

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
DatosDeTabla= np.full(len(tagsTD),string)
# limpiza de informacion no importante y llenado del arrelgo DatosDeTabla
p = 0
for tag in tagsTD:
    if tag.string ==None:
        fonts=tag.find_all('font')
        for font in fonts:
            if len(font.contents) >=1:
                DatosDeTabla[p]=str(font.contents[0])
        p=p+1
    else:  
        DatosDeTabla[p]=tag.string
        p=p+1
# creo dos tablas para gauardar los datos y que tipo de dato es 
TipDatos=np.array(["tipo"])
datos=np.array(["datos"])
# lleno las nuevas tablas con la informacion, dotos es la tabla mas importanante 
for i in range(DatosDeTabla.size):
    if i % 2 == 0:
        datos=np.append(datos,DatosDeTabla[i])
    else:
        TipDatos=np.append(TipDatos,DatosDeTabla[i])

# vista de los resultados --ELIMINAR
TipDatos=np.append(TipDatos,"fin")
for i in range(datos.size):
    print(TipDatos[i], datos[i])
