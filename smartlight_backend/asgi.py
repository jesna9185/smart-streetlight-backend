# smartlight_backend/asgi.py

import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.layers import get_channel_layer
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import streetlight.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartlight_backend.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            streetlight.routing.websocket_urlpatterns
        )
    ),
})
