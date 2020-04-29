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
