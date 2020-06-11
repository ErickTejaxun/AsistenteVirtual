#ACHO 2020 NLU
#Acción que se ejecutan luego de que nuestro bot
#Reconoce las intenciones del usuario. 
import time
import paho.mqtt.client as mqtt
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from random import seed
from random import random
from datetime import datetime
from datetime import date

seed(1)
mensajes =[0,0,0]
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("acho/nlu")

def execute(client, intent, payload):
    client.publish(intent, payload)

def on_message(client, userdata, msg):          
    mensajes[0]=str(msg.payload)        
    print(msg.topic+" "+mensajes[0])


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")
        return []


#TV----------
class ActionStateTv(Action):
    def name(self) -> Text:
        return "action_statetv"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:  
        print("Consultando el estao de la pantalla")    
        execute(client, "acho/tv/status", "--")   
        time.sleep(1)
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return []

#Turn on TV---------
class ActionTurnOnTv(Action):
    def name(self) -> Text:
        return "action_turnontv"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/tv/power", "on")        
        time.sleep(1)
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return []

#Turn Off TV------------
class ActionTurnOffTv(Action):
    def name(self) -> Text:
        return "action_turnofftv"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/tv/power", "off") 
        time.sleep(1)       
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return [] 


#Manejo de las persianas------------------------  
class ActionUpBlind(Action):
    def name(self) -> Text:
        return "action_upblind"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/blind/up", "") 
        time.sleep(1)       
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return [] 

class ActionUpFewBlind(Action):
    def name(self) -> Text:
        return "action_upfewblind"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/blind/up/few", "") 
        time.sleep(1)       
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return []  

class ActionDownBlind(Action):
    def name(self) -> Text:
        return "action_upblind"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/blind/up", "") 
        time.sleep(1)       
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return []                

class ActionDownFewBlind(Action):
    def name(self) -> Text:
        return "action_downfewblind"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/blind/down/few", "") 
        time.sleep(1)       
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return []  

class ActionStatusBlind(Action):
    def name(self) -> Text:
        return "action_getstateblind"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/blind/status", "") 
        time.sleep(1)       
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return []  


class ActionTurnOffLights(Action):
    def name(self) -> Text:
        return "action_turnofflights"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/lights/off/all", "") 
        time.sleep(1)       
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return []  

class ActionTurnOnLights(Action):
    def name(self) -> Text:
        return "action_turnonlights"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/lights/on/all", "") 
        time.sleep(1)       
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return []        

class ActionTurnOnSpeakers(Action):
    def name(self) -> Text:
        return "action_turnonspeakers"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/speakers/on", "on") 
        time.sleep(1)       
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return []             



class ActionTurnOffSpeakers(Action):
    def name(self) -> Text:
        return "action_turnoffspeakers"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/speakers/off", "off") 
        time.sleep(1)       
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return [] 

class ActionGetVolumen(Action):
    def name(self) -> Text:
        return "action_getvolumen"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/speakers/status", "--") 
        time.sleep(1)       
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return []         

class ActionUpVolumen(Action):
    def name(self) -> Text:
        return "action_upvolumen"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/speakers/up", "10") 
        time.sleep(1)       
        partes = str(mensajes[0]).split("\'")
        if len(partes) >=1 : 
            dispatcher.utter_message(text=mensajes[0])
        if len(partes)==2:
            dispatcher.utter_message(text=mensajes[1])
        return []     

class ActionDownVolumen(Action):
    def name(self) -> Text:
        return "action_downvolumen"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:             
        execute(client, "acho/speakers/down", "10") 
        time.sleep(1)   
        dispatcher.utter_message(text=mensajes[0])
        return []    
 

class ActiongetTime(Action):
    def name(self) -> Text:
        return "action_getTime"
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")                
        mensaje = "La hora actual es " + current_time        
        dispatcher.utter_message(text=mensaje)
        return []
#VGw_g#j_;u:>v_-        

class ActiongetDate(Action):
    def name(self) -> Text:
        return "action_getDate"
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        today = date.today()        
        current_date = today.strftime("%d/%m/%Y")                     
        mensaje = "La hora actual es " + current_date        
        dispatcher.utter_message(text=mensaje)
        return []

class ActionLoginInici(Action):
    def name(self) -> Text:
        return "action_login_init"
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']          
        mensaje = 'Sin nombre de usuario'     
        print('-------------------------------------\n')
        print(tracker.latest_message)                
        cont = 0         
        username = ''
        password = ''
        for e in entities:
            if cont==0:
                if e['entity'] == 'username':                
                    username = e['value']
            if cont>0:
                if e['entity'] == 'password' or e['entity'] == 'username':                
                    password = e['value'] 
            cont = cont +1    
        print(username +'-\t-'+password)           
        if (username == 'acho' or username == 'erick'):                    
            if password == 'acho-unex':
                mensaje = 'Bienvenido usuario '+username + ' ¿qué deseas realizar?'
            else:
                mensaje = 'La contraseña es incorrecta'
        else:
            mensaje = 'El usuario '+username+ ' no existe en el sistema'  

        dispatcher.utter_message(text=mensaje)
        return []
    
class ActionGetWeather(Action):
    def name(self) -> Text:
        return "action_get_weather"
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        today = date.today()        
        current_date = today.strftime("%d/%m/%Y")                     
        mensaje = "La hora actual es " + current_date        
        dispatcher.utter_message(text=mensaje)
        return []

## Iniciamos el client mosquito y nos suscribimos al topic
# acho/nllu
client = mqtt.Client("mqtt_simulado")           
client.on_message = on_message 
client.connect("localhost")
client.loop_start()
client.subscribe("acho/nlu")


