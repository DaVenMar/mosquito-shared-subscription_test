#!/bin/bash
#Client MQTT
echo "Build docker image mqtt client test"
sudo docker build -f eclipse-mosquito/dockerfile -t mqtt-lb-server .
sudo docker build -f mqtt-pub/dockerfile -t client-mqtt-pub .
sudo docker build -f mqtt-sub/dockerfile -t client-mqtt-sub .
#DEPLOY
echo "deploy images"
sudo docker-compose up -d --scale mqttclient=4