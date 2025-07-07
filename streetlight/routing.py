# websocket_app/routing.py

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/ldr/$', consumers.LDRConsumer.as_asgi()),
    re_path(r'ws/pir/$', consumers.PIRConsumer.as_asgi()),
    re_path(r'ws/led/$', consumers.LEDConsumer.as_asgi()),
]
