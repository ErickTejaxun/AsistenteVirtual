#Natural Language Processor for ACHO
# -*- coding: utf-8 -*-
# Get the data from mosquito suscription and reward to rasa. 
#

import time
import paho.mqtt.client as mqtt
import os 
import subprocess
from subprocess import Popen, PIPE


def start_bot_rasa():
    print("Starting rasa bot.")
    print("1. Starting ngk redirect server")

    #Agregando permisos de ejecución
    os.spawnlp(os.P_NOWAIT, 'chmod', 'chmod', '+x', './ngrok')

    #Run this if run telegram
    ##os.spawnlp(os.P_NOWAIT, 'ngrok', './ngrok', 'http', '5005')
    time.sleep(5)

    print("2. Run rasa endpoint for the action bot")   
    os.spawnlp(os.P_NOWAIT, 'rasa', 'rasa', 'run', 'actions')
    
    """process = subprocess.Popen(['rasa', 'run', 'actions'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()    
    print (stdout)
    """
    time.sleep(10)
    print('3. Run rasa bot')
    os.spawnlp(os.P_NOWAIT, 'rasa', 'rasa', 'run')
    time.sleep(10)
    """processRunRasa = subprocess.Popen(['rasa', 'run', 'actions'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
    stdout, stderr = processRunRasa.communicate()
    stdout, stderr
    """

            


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
    client.publish(msg.payload,msg.payload)

start_bot_rasa()
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