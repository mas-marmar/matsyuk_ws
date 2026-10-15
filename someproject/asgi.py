import os
from channels.routing import ProtocolTypeRouter 
from someapp.websocket_routing import router
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'someproject.settings')

django_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        'http': django_app,
        'websocket': router
    }
)
