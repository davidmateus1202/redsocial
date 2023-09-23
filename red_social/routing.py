from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application



import chat.routing

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket' : AuthMiddlewareStack(
        URLRouter(chat.routing.websocket_urlpatterns)
    )
})