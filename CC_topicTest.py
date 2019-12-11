import time
from datetime import date

# Imports for MQTT
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# Set MQTT broker and topic
broker = "test.mosquitto.org" # Broker

#topicTest = "test/time"       # send messages to this topic
topicBowl = "CatConnect/Cat/Bowl"
topicHere = "CatConnect/Cat/Here"

############### MQTT section ##################

# when connecting to mqtt do this;
def on_connect(client, userdata, flags, rc):
	if rc==0:
		print("Connection established. Code: "+str(rc))
	else:
		print("Connection failed. Code: " + str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe(topicBowl)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	
def on_publish(client, userdata, mid):
	print("Published: " + str(mid))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect(broker, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()


# Loop that publishes message
while True:
	# Assigning a string for transmission
	statusBowl = "Empty"
	statusHere = "Not"  

	client.publish(topicBowl, str(statusBowl))
	client.publish(topicHere, str(statusHere))

	time.sleep(2.0) # Set delay
	statusBowl = "Full"
	statusHere = "Yes"

	client.publish(topicBowl, str(statusBowl))
	client.publish(topicHere, str(statusHere))

	time.sleep(2.0) # Set delay