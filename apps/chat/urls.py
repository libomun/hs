from django.urls import path
from .views import *

app_name = 'chatbot'
urlpatterns = [
    path('', chatbot_view, name='chatbot'),
]