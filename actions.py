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


class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")
        return []

class ActionStateTv(Action):
    def name(self) -> Text:
        return "action_statetv"    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mensaje = "La pantalla está " + str(random())
        dispatcher.utter_message(text=mensaje)
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