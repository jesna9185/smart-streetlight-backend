import paho.mqtt.client as mqtt
import requests

# MQTT settings
broker = "test.mosquitto.org"
topic = "streetlight/#"  # all topics under streetlight/

# Django API
API_URL = "http://127.0.0.1:8000/api/sensordata/"

def on_connect(client, userdata, flags, rc):
    print("MQTT Connected with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    sensor_type = msg.topic.split("/")[-1]
    value = msg.payload.decode()

    print(f"Received from MQTT: {sensor_type} = {value}")

    data = {
        "sensor_type": sensor_type,
        "value": value
    }
    try:
        response = requests.post(API_URL, data=data)
        print("→ Sent to Django:", response.status_code)
    except Exception as e:
        print("Failed to send to Django:", e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)
client.loop_forever()
