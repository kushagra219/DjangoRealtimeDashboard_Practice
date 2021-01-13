"""
ASGI config for djangoRT project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from django.urls import path
from firstApp import consumers
# import firstApp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'justchat.settings')

websocket_urlpatterns = [
    path('ws/pollData/', consumers.DashConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns,
        )
    ),
    # Just HTTP for now. (We can add other protocols later.)
})
