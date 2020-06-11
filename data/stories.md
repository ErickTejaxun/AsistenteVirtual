## iniciar sesion
* greet
  -utter_saludo
* login
  -action_login_init
  > sesion_iniciada

## preguntar por el clima
> sesion_iniciada
* getWeather
  -action_get_weather

## preguntar por tv
> sesion_iniciada
* statetv
  - action_statetv

## preguntar por la hora
* getTime
  - action_getTime

## preguntar por la fecha
* getDate
  - action_getDate

## saludar
> sesion_iniciada 
* greet 
 - utter_saludo

## despedir
> sesion_iniciada
* goodbye
 - utter_despedir


## encender tv
> sesion_iniciada
* turnontv
  - action_turnontv

## apagar tv
> sesion_iniciada
* turnofftv
  - action_turnofftv

## buscar en internet
> sesion_iniciada
* search
  - utter_search

## buscar en youtube
> sesion_iniciada
* searchyoutube
  - utter_searchyoutube
  
## lanzar google
> sesion_iniciada
* rungoogle
  - utter_rungoogle

## encender speakers
> sesion_iniciada
* turnonspeakers
  - action_turnonspeakers

## apagar speakers
> sesion_iniciada
* turnoffspeakers
  - action_turnoffspeakers  

## obtener volumen speakers
> sesion_iniciada
* getvolumen
  - action_getvolumen

## subir volumen speakers
> sesion_iniciada
* upvolumen
  - action_upvolumen

## bajar volumen speakers
> sesion_iniciada
* downvolumen
  - action_downvolumen

## encender luces
> sesion_iniciada
* turnonlights
  - action_turnonlights

## apagar luces
> sesion_iniciada
* turnofflights
  - action_turnofflights

## estado de las persianas
> sesion_iniciada
* getstateblind
  - action_getstateblind

## estado motor de las persianas
> sesion_iniciada
* stateengineblind
  - utter_getstateengineblind

## subir persianas
> sesion_iniciada
* upblind
  - action_upblind

## bajar persianas
> sesion_iniciada
* downblind
  - action_downblind

## subir poco las persianas
> sesion_iniciada
* upfewblind
  - action_upfewblind

## bajar poco las persianas
> sesion_iniciada
* downfewblind
  - action_downfewblind

## detener motor persianas
> sesion_iniciada
* stopblind
  - utter_stopblind

## ejecutar skype
> sesion_iniciada
* runskype
  - utter_runskype

## ejectuar navegador
> sesion_iniciada
* runfirefox
  - utter_runfirefox


