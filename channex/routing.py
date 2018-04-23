from django.urls import path

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from home.consumers import HomeConsumer

application = ProtocolTypeRouter({  # pylint: disable=invalid-name
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('home/stream/', HomeConsumer)
        ])
    ),
})
