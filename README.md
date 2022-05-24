## 1. Introduction

MQTT Shared subscriptions sandbox

In this test environment you will be able to start up a shared subscription to the same [Eclipse Mosquitto](https://mosquitto.org/) topic by several clients. The messages sent by the publish container in the topic will be divided among all the subscribers with the same client name.

Check the configured load balancer live by viewing the clients' logs.

## 2. Requirements


1. [Docker](https://docs.docker.com/get-docker/)
2. [Docker compose](https://docs.docker.com/compose/install/)

## 3. Getting Started


You can run the environment on a linux system with the following commands

````
cd mosquito-shared-subscription_test
sh test-share-mqtt.sh
````

You can run the environment manually by executing the command lines of the sh file one by one

The publish container will start to send a string of numbers sequentially based on the number of loops executed

Can check the configured load balancer live by viewing the clients' logs.

## 4. Monitoring


Execute the following code to visualize the logs in each of the clients. You can see that each customer receives a different message.
````
# Client 1
docker logs mosquito-shared-subscription_test_mqttclient_1

# Client 2
docker logs mosquito-shared-subscription_test_mqttclient_2

# Client 3
docker logs mosquito-shared-subscription_test_mqttclient_3
````

