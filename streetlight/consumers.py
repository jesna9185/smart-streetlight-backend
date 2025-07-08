from channels.generic.websocket import AsyncWebsocketConsumer
import json

# consumers.py


class LDRConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("ldr_group", self.channel_name)
        await self.accept()

    async def send_ldr_data(self, event):
        await self.send(text_data=json.dumps({"ldr": event["value"]}))

class PIRConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("pir_group", self.channel_name)
        await self.accept()

    async def send_pir_data(self, event):
        await self.send(text_data=json.dumps({"pir": event["value"]}))

class LEDConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("led_group", self.channel_name)
        await self.accept()

    async def send_led_data(self, event):
        await self.send(text_data=json.dumps({
            "led": event["value"],
            "topic": event.get("topic", "")
        }))
