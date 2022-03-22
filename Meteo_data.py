from ast import Num
import string
import re
from time import time #filtrar cadenas
import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup #scaraping
import numpy as np #arrreglos y organizacion
import ssl #certificados dde navegacion web SSL
import pandas as pd #dataframe para bases de datos
import paho.mqtt.client as mqtt # para comunicacion MQTT

# Parametros para la conexión MQTT
servidormqtt = "193.144.12.68"
usuario = "greiablgr"
contrasena = "gr314blgr"
topicolee = "greiablgr/meteo/*"

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
DataFromtagstd= np.array([])
#  llenado del arrelgo DataFromtagstd con la infromacion de cada <td> del html
for tag in tagsTD:
    if tag.string ==None:
        fonts=tag.find_all('font')
        for font in fonts:
            if len(font.contents) >=1:
                DataFromtagstd=np.append(DataFromtagstd,font.contents[0])     
    else:  
        DataFromtagstd=np.append(DataFromtagstd,tag.string)
#Array Data con los datos numericos de la tabla del html guardada en DataFromtagstd       
Datos=np.array([])
for datos in DataFromtagstd:
    try:
        if len(re.findall('\d+',str(datos)))>=1:
            datos = re.sub("\°","",datos)
            datos = re.sub("C","",datos)
            Datos=np.append(Datos,datos)      
    except:
        x=1
#elimino los valores que no son importantes y que saltaron el filtro anterior  y organiso el vector comomatriz para el pandas
Datos=np.delete(Datos,[14,21,22,24],0)
Datos=Datos.reshape(1,-1)
#creo un array con los nombres de las columnas para pasrlo a pandas
Columns=['Temperatura actual','Temperatura maxima (desde media noche)','Temperatura minima (desde media noche)','Velocidad del viento (diez minutos)','Direccion del viento (diez minutos)','Temperatura aparente','Rafagas máxima (última hora)','Ragfagas máxima (desde medianoche)','Máximo media de un minuto (desde medianoche)','Lluvia (última hora)','Lluvia (desde medianoche)','Lluvia este mes','Lluvia hasta la fecha este año','Luvia máxima por minuto (última hora)','Lluvia máxima por hora (últimas 6 horas)','Lluvia ayer','Punto de rocio','Humedad','Barometro corregido a msl','Cambio de presion','Cambio de presion (últimas 12 horas)','Cambio de presion (últimas 6 horas)','Current solar','Current UV','Máximo solar','Máximo UV (desde medianoche)','Sunshine hours for the year','Sunshine hours for the month']
#creo un pandas con toda la informacion solicitada
Data=pd.DataFrame(Datos,columns=Columns)


#reviso como quede el dataframe Data. ELIMINAR
print(str(Datos[0]))





# Funciones de conexión y mensaje
# Al recibir CONNACK desde el servidor
def on_connect(client, userdata, flags, rc):
    # Inicio o renovación de subscripción
    #client.publish(topicolee,str(Datos[0][0]))
    x=1

    

# el tópico tiene una publicación
def on_message(client, userdata, msg):
    print(str(msg.payload))

MetoblgClient = mqtt.Client()
MetoblgClient.on_connect = on_connect
MetoblgClient.on_message = on_message
#Conectarse con el servidor MQTT
MetoblgClient.username_pw_set(username=usuario,password=contrasena)
MetoblgClient.connect(servidormqtt)

MetoblgClient.loop_start()
MetoblgClient.publish(topicolee,str(Datos[0][0]))
MetoblgClient.publish(topicolee,str(Datos[0][1]))
MetoblgClient.publish(topicolee,str(Datos[0][5]))
MetoblgClient.loop_stop()



    


