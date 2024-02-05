from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    # re_path(r"ws/forum/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    path("ws/forum/<str:room_name>", consumers.ChatConsumer.as_asgi()),
]