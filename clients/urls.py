from os import name
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import admin_dashboard,add_client,add_consignee,genrate_client_token,send_email

urlpatterns = [
    path('api/',include('clients.api.urls')),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('add_client/', add_client, name='add_client'),
    path('add_consignee',add_consignee,name='add_consignee'),
    path('genrate_client_token/',genrate_client_token,name='genrate_client_token'),
    path('send_email/',send_email,name='send_email')
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
