from django.urls import path
from .views import index, chat_page, api_proxy

urlpatterns = [
    path('', index, name='index'),  # This will render your index.html when you access the root URL
    path('chat/', chat_page, name='chat_page'),
    path('api_proxy/', api_proxy, name='api_proxy'),
]
