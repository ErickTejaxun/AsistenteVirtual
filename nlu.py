#!/usr/bin/env python3


#Natural Language Processor for ACHO
# -*- coding: utf-8 -*-
# Get the data from mosquito suscription and reward to rasa.
#

import time
import paho.mqtt.client as mqtt
import os
import subprocess
from subprocess import Popen, PIPE
import requests
import json
import os


# api-endpoint rasa
URL = "http://localhost:5005/model/parse"



def start_bot_rasa():
    print("Starting rasa bot.")
    print("1. Starting ngk redirect server")
    pathActual  = os.path.dirname(__file__)
    
    #Agregando permisos de ejecución
    #os.spawnlp(os.P_NOWAIT, 'chmod', 'chmod', '+x', pathActual+'/ngrok')

    #Run this if run telegram
    
    #os.spawnlp(os.P_NOWAIT, 'ngrok', pathActual+'/ngrok', 'http', '5005')
    #time.sleep(5)

    print("2. Run rasa endpoint for the action bot")
    #os.spawnlp(os.P_NOWAIT, 'rasa', 'rasa', 'run', 'actions')
    time.sleep(10)


    print('3. Run rasa bot')
    #rasa run --enable-api --log-file out.log
    #os.spawnlp(os.P_NOWAIT, 'rasa', 'rasa', 'run','--enable-api','--log-file','out.log')
    time.sleep(10)



##############
## MenQTT
###########

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe("acho/nlp/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if(msg.topic=="acho/nlp"):
        print("topic nlp recibido")
    print("publicar topico", msg.payload)
    payload = {"text": str(msg.payload)}
    headers = {'Content-Type': "aplication/json",}

    payload = {"text": str(msg.payload)}

    headers = {'Content-Type': "application/json",}
    response = requests.request("POST", URL, data=json.dumps(payload), headers=headers)


    data = response.json()
    print(data['intent']['name'])
    intent = data['intent']['name']
    execute(client, intent, intent)


# This execute the command by the intent that bot identify
# client is a client of mosquitto
# intent the intent
# search th argumento of search with google, youtube.
def execute(client, intent, search):
    command = ''
    if intent == 'statetv':
        command = 'acho/tv/power'

    if intent == 'upblind':
        command = 'acho/blind/up'

    if intent == 'upfewblind':
        command = 'acho/blind/up/few'

    if intent == 'runskype':
        command == 'acho/linux-commands/skype'

    if intent == 'runfirefox':
        command == 'acho/linux-commandos/firefox'

    if intent == 'downblind':
        command == 'acho/blind/down'

    if intent == 'downfewblind':
        command = 'acho/blind/down/few'

    if intent == 'stopblind':
        command = 'acho/blind/stop'

    if intent == 'turnonlights':
        command = 'acho/lights/on/all'

    if intent == 'turnontv':
        command = 'acho/tv/power'

    if intent == 'turnofflights':
        command = 'acho/lights/off/all'

    if intent == 'turnofftv':
        command = 'acho/tv/power'

    if intent == 'search':
        command = 'acho/linux-commands/google'

    if intent == 'searchyoutube':
        command = 'acho/linux-commands/youtube'

    if intent == 'searchwiki':
        command = 'acho/linux-commands/wikipedia'

    if intent == 'rungoogle':
        command = 'acho/linux-commands/google'

    if intent == 'statetv':
        command = 'acho/tv/status'

    if intent == 'turnonspeakers':
        command = 'acho/speakers/on'

    if intent == 'getvolumen':
        command = 'acho/speakers/status'

    if intent == 'upvolumen':
        command = 'acho/speakers/up'
        search ='up'

    if intent == 'downvolumen':
        command = 'acho/speakers/down'

    if intent == 'getstateblind':
        command = 'acho/blind/status'

    if intent == 'stateengineblind':
        command = 'acho/blind/engine'

    client.publish(command, search)


#start_bot_rasa()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.connect("salareuniones.local", 1883, 60)
client.connect("localhost")
print ("Connected to Mosquitto broker")

while True:
	try:
		client.loop_forever()
	except:
		time.sleep(5)
