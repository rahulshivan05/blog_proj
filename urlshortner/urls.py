from django.urls import path
from .views import *

app_name="urlshortner"

urlpatterns = [
	path('', index),
	path('create', create, name='create'),
	path('<str:pk>', go, name='go'),
]