# mqtt.py
import os
import django
import threading
import paho.mqtt.client as mqtt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Initialize Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smartlight_backend.settings")
django.setup()

channel_layer = get_channel_layer()

# Callback when a message is received from MQTT
def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(f"📩 MQTT → {topic}: {payload}")

    if topic == "streetlight/ldr":
        async_to_sync(channel_layer.group_send)(
            "ldr_group",
            {
                "type": "send_ldr_data",
                "value": payload
            }
        )
    elif topic.startswith("streetlight/pir"):
        async_to_sync(channel_layer.group_send)(
            "pir_group",
            {
                "type": "send_pir_data",
                "value": payload
            }
        )
    elif topic.startswith("streetlight/led") and topic.endswith("/status"):
        async_to_sync(channel_layer.group_send)(
            "led_group",
            {
                "type": "send_led_data",
                "value": payload,
                "topic": topic
            }
        )
    else:
        print(f"⚠️ Unknown topic: {topic}")

# Function to start the MQTT client
def start_mqtt():
    client = mqtt.Client(protocol=mqtt.MQTTv311, userdata=None, transport="tcp")
    client.on_message = on_message
    client.connect("test.mosquitto.org", 1883, 60)

    # Topics to subscribe to
    topics = [
        "streetlight/ldr",
        "streetlight/pir1",
        "streetlight/pir2",
        "streetlight/pir3",
        "streetlight/pir4",
    ] + [f"streetlight/led{i}/status" for i in range(1, 9)]

    for topic in topics:
        client.subscribe(topic)
        print(f"📡 Subscribed to: {topic}")

    client.loop_start()  # ✅ non-blocking and safe in thread

# Start MQTT client in a separate thread
mqtt_thread = threading.Thread(target=start_mqtt, daemon=True)
mqtt_thread.start()

# Block forever
import time
while True:
    time.sleep(1)