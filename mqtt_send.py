import paho.mqtt.client as mqtt
import time
import json


client = mqtt.Client()
client.connect("13.59.190.62")
client.publish("sentiment/comment/response",payload = json.dumps({"Decision":"no vugijugi", "start_time": str(time.time())}))
client.loop_forever()