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
servidormqtt = "greia-iot.udl.cat"
usuario = "greiablgr"
contrasena = "gr314blgr"
topicolee = "greiablgr/meteo/*"



# Funciones de conexión y mensaje
# Al recibir CONNACK desde el servidor
def on_connect(client, userdata, flags, rc):
    # Inicio o renovación de subscripción
    client.subscribe(topicolee)
    #client.publish(topicolee,"preuba de conexion")
    #print("agua paso por aqui")

# el tópico tiene una publicación
def on_message(client, userdata, msg):
    print(str(msg.payload))
    #print("cate que no la vi")


MetoblgClient = mqtt.Client()
MetoblgClient.on_connect = on_connect
MetoblgClient.on_message = on_message
#Conectarse con el servidor MQTT
MetoblgClient.username_pw_set(username=usuario,password=contrasena)
MetoblgClient.connect(servidormqtt)

MetoblgClient.loop_forever()

    

