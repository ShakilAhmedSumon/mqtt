import paho.mqtt.client as mqtt
import time
import json


def on_message(client,userdata,msg):
    bytes_value = msg.payload
    print(bytes_value)
    my_json = bytes_value.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    text_data = data["Decision"]
    print(text_data)
    # prediction = predict(text_data)
    # print(prediction)
    text_data = data["start_time"]
    print(text_data)
    # prediction = predict(text_data)
    # print(prediction)


client = mqtt.Client()
client.connect("13.59.190.62")

topic_response = "sentiment/comment/response"
client.subscribe(topic_response) 
client.on_message = on_message
client.loop_forever()




