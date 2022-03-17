from os import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('add_order/',add_order, name='addorder'),
    path('order_item/',order_item, name='orderitem'),
    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
