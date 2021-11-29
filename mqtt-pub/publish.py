from typing import List
import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected
        Connected = True
 
    else:
 
        print("Connection failed")
 
Connected = False
 
broker_address= "server-mqtt"
port = 1883
 
client = mqttClient.Client("mqtt-pub")
client.on_connect= on_connect
client.connect(broker_address, port=port)
 
client.loop_start()
 
while Connected != True:  
    time.sleep(0.1)
 
try:
    count = 0
    while True:
        
        count = count + 1
        value = count
        client.publish("topic",str(value))
        time.sleep(1.5)
 
except KeyboardInterrupt:
 
    client.disconnect()
    client.loop_stop()