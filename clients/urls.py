from os import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('add_client/', add_client, name='add_client'),
    path('add_consignee',add_consignee,name='add_consignee')  
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
