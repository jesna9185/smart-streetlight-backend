import os
import django
import paho.mqtt.client as mqtt

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from api.models import SensorData

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("streetlight/#")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()

    sensor_type = topic.split("/")[-1]
    print(f"Received {sensor_type} = {payload}")
    SensorData.objects.create(sensor_type=sensor_type, value=payload)

# Use updated protocol to avoid warning
client = mqtt.Client(protocol=mqtt.MQTTv311)

client.on_connect = on_connect
client.on_message = on_message

# Try alternative broker if needed
client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()