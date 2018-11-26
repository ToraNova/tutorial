#!/usr/bin/python3
# imports
import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect("0.0.0.0", 1883, 60)
client.loop_start()

time.sleep(1) #wait for connection
try:
	while True:
		print("Test string: ",end='')
		sendstr = input()
		print("Sending ",sendstr)
		client.publish("alertpy/alrt", sendstr)
except KeyboardInterrupt:
	print("Exit.")
	exit(0)
