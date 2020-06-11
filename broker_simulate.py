
import paho.mqtt.client as mqtt
import time


estado_tv = 0 # Inicia apagado
estados_encendido_apagado = ["Encendido","Apagado"]
estado_bocinas = 0 #Inicia apagado
nivel_volumen = 0 # Inicia con un volumen 0
nivel_persiana = 0
estados_elementos = [0,0,0,0,0,0,0,0]
#[0.estado_tv, 1.estado_bocinas, 2.nivel_volumen, 3.nivel_persiana,4.statebliend,5.Luces]
# El callback cuando el cliente se conecta al broker
def on_connect(client, userdata, flags, rc):  
    print("Connected with result code {0}".format(str(rc)))  # Debug
    client.subscribe("acho/#")  # Nos suscribimos a toso los tópicos
    print("Suscrito al tópico acho/#") 

# El callback cuando haya una publicación recibida desde el servidor
#mosquitto_sub -h localhost -t ACHO/# para suscribirse
#mosquitto_pub -h localhost -t ACHO/tv/power -m "on" para enviar mensajes
def on_message(client, userdata, msg):      
    mensaje = "" 
    #print(msg.topic)
    payload = str(msg.payload)
    partes = payload.split("\'")    
    #Manejo de estado del monitor
    if(msg.topic == 'acho/tv/power'):        
        estado_tv = estados_elementos[0]
        if partes[1]=='on':                                                  
            if(estado_tv==1):
                estado_tv = 1
                mensaje = 'El monitor se encuentra prendido'
            else:
                estado_tv = 1
                mensaje = 'Se ha prendido el monitor'
        else:
            if(estado_tv==1):
                estado_tv = 0
                mensaje = 'Se ha apagado el monitor'
            else:
                estado_tv = 0
                mensaje = 'El monitor se encuentra apagado'  
        estados_elementos[0] = estado_tv
    
    #Manejo de estado del monitor
    if(msg.topic == 'acho/tv/status'):        
        estado_tv = estados_elementos[0]
        if(estado_tv==1):                
            mensaje = 'El monitor se encuentra prendido.'
        else:            
            mensaje = 'El monitor se encuentra apagado.'


    #Manejo de las persianas
    if(msg.topic == 'acho/blind/up'):
        nivel_persiana = estados_elementos[3]
        if(nivel_persiana<10):    
            if (nivel_persiana +3 )<=10:
                nivel_persiana = (nivel_persiana +3 )
            else:
                nivel_persiana = 10
            mensaje = 'Subiendo la persiana. Ahora se encuentra al nivel ' +str(nivel_persiana) +' /10.'
            estados_elementos[3] = nivel_persiana
        else:
            mensaje = 'No se pueden subir más las persinas. Nivel '+str(nivel_persiana) +"/10."


    if(msg.topic == 'acho/blind/up/few'):
        nivel_persiana = estados_elementos[3]
        if(nivel_persiana<10):    
            nivel_persiana = nivel_persiana + 1
            mensaje = 'Subiendo la persiana. Ahora se encuentra al nivel ' +str(nivel_persiana) +" /10."
            estados_elementos[3] = nivel_persiana
        else:
            mensaje = 'No se pueden subir más las persinas. Nivel '+str(nivel_persiana) +"/10."

    if(msg.topic == 'acho/blind/down'):
        nivel_persiana = estados_elementos[3]
        if(nivel_persiana>0):            
            if (nivel_persiana -3 )>=0:
                nivel_persiana = (nivel_persiana - 3 )
            else:
                nivel_persiana = 0
            mensaje = 'Bajando la persiana. Ahora se encuentra al nivel ' +str(nivel_persiana) +" /10."
            estados_elementos[3] = nivel_persiana
        else:
            mensaje = 'No se pueden bajar más las persinas. Nivel '+str(nivel_persiana) +"/10."    

    if(msg.topic == 'acho/blind/down/few'):
        nivel_persiana = estados_elementos[3]
        if(nivel_persiana>0):    
            nivel_persiana = nivel_persiana -1
            mensaje = 'Subiendo la persiana. Ahora se encuentra al nivel ' +str(nivel_persiana) +" /10."
            estados_elementos[3] = nivel_persiana
        else:
            mensaje = 'No se pueden subir más las persinas. Nivel '+str(nivel_persiana) +"/10."   
    
    #command = 'acho/blind/status' 
    if(msg.topic == 'acho/blind/status'):
        nivel_persiana = estados_elementos[3]            
        mensaje = 'Nivel de la persiana: '+str(nivel_persiana) +"/10."             

    #Run firefox
    if(msg.topic == 'acho/linux-commandos/firefox'):
        mensaje = 'Ejecutando firefox'
    
    #Manejo del motor
    if(msg.topic == 'acho/blind/stop'):
        state_engine = estados_elementos[4]
        if state_engine == 0:
            mensaje = "La persiana no está en movimiento"
        else:
            mensaje = "La persiana se ha detenedio"
            state_engine = 0
        estados_elementos[4] = state_engine

    if(msg.topic == 'acho/blind/status'):
        state_engine = estados_elementos[4]
        mensaje = 'El motor de la persiana se encuentra '+ estados_encendido_apagado[state_engine]
        
    #Manejo de luces
    if(msg.topic == 'acho/lights/on/all'):
        state_lights = estados_elementos[5]
        if state_lights == 0:
            state_lights = 1
            mensaje = 'Prendiendo las luces'
        else:
            mensaje = 'Las luces de robolab están encendidas'
        estados_elementos[5] = state_lights

    if(msg.topic == 'acho/lights/on/all'):
        state_lights = estados_elementos[5]
        if state_lights == 0:            
            mensaje = 'Las luces de robolab se encuentran apagadas.'
        else:
            mensaje = 'Apagando las luces de robolab'
        estados_elementos[5] = state_lights
    


    #Run firefox
    if(msg.topic == 'acho/linux-commandos/google'):
        mensaje = 'Abriendo página de búsqueda'   
   
    #Youtube
    if(msg.topic == 'acho/linux-commandos/youtube'):
        mensaje = 'Comensando búsqueda en youtube de ' + str(partes[1])

    #Wikipedia
    if(msg.topic == 'acho/linux-commandos/wikipedia'):
        mensaje = 'Comensando búsqueda en wikipedia de ' + str(partes[1])     

    #Estado de la television
    if(msg.topic == 'acho/tv/status'):
        estado_tv = estados_elementos[0]
        mensaje = 'La televisión se encuentra '+estados_encendido_apagado[estado_tv]

    #Speakers
    if(msg.topic == 'acho/speakers/on'):
        state_speakers= estados_elementos[1]
        nivel_volumen = estados_elementos[2]
        if (state_speakers == 0):
            mensaje = 'Prendiendo equipo de sonido de robolab.'
            state_speakers = 1
        else:
            mensaje = 'El equipo de sonido de robolab ya se encuentra prendido.'
        estados_elementos[1] = state_speakers

    if(msg.topic == 'acho/speakers/status'):
        state_speakers= estados_elementos[1]
        nivel_volumen = estados_elementos[2]
        if (state_speakers == 0):
            mensaje = 'El equipo de sonido de robolab se encuentra apagado.'            
        else:
            mensaje = 'El nivel de volumen del equipo de sonido es de ' + str(nivel_volumen)
        
    if(msg.topic == 'acho/speakers/up'):
        state_speakers= estados_elementos[1]
        nivel_volumen = estados_elementos[2]
        if (state_speakers == 0):
            mensaje = 'El equipo de sonido de robolab se encuentra apagado'            
        else:
            if(nivel_volumen + 10) <=100:
                nivel_volumen = nivel_volumen +10
                mensaje = 'Subiendo volumen. El volumen actual es de ' +str(nivel_volumen)+ "/100."
            else:
                nivel_volumen =100
                mensaje = 'El volumen está al máximo. El volumen actual es de ' +str(nivel_volumen)+ "/100."
        estados_elementos[2] = nivel_volumen 


    if(msg.topic == 'acho/speakers/down'):
        state_speakers= estados_elementos[1]
        nivel_volumen = estados_elementos[2]
        if (state_speakers == 0):
            mensaje = 'El equipo de sonido de robolab se encuentra apagado'            
        else:
            if(nivel_volumen - 10) >=0:
                nivel_volumen = nivel_volumen -10
                mensaje = 'Subiendo volumen. El volumen actual es de ' +str(nivel_volumen)+ "/100."
            else:
                nivel_volumen =0
                mensaje = 'El volumen está al mínimo. El volumen actual es de ' +str(nivel_volumen)+ "/100."
        estados_elementos[2] = nivel_volumen                        
    
    #print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg
    #Mandamos el mensaje
    if(msg.topic!="acho/nlu"):
        client.publish("acho/nlu", mensaje) 
    #print("topic origen: "+ msg.topic + "\t"+mensaje)    



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
