from django.urls import path
from .views import home, domain_info

app_name='blog'

urlpatterns = [
	path('', home, name='home'),
	path('domain', domain_info, name='domain'),
]
