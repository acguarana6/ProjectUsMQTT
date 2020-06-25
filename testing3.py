import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)


########################################
#broker_address="192.168.1.184"
broker_address="broker.mqttdashboard.com"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_connect = on_connect
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address, port=1883, keepalive=15, bind_address="") #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","OFF")
client.on_log=on_log
time.sleep(4) # wait
client.loop_stop() #stop the loop