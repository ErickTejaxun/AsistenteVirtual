#!/bin/sh



#validete the number and consistecy of our histories
rasa data validate --fail-on-warnings --max-history 100


#first train or model
#rasa train


#test stories
#rasa test --stories tests/conversation_tests.md --fail-on-prediction-errors



rasa test nlu --cross-validation


# run the web server bot
#rasa run --enable-api --log-file out.log