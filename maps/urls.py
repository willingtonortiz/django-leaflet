from django.urls import path
from .views import default_map, send_data, ramapi

urlpatterns = [
    path('', default_map, name='default'),
    path('send_data', send_data, name='send_data'),
	path('test', ramapi, name='ramapi')
]

