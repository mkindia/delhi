from os import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import add_order,order_item,dispatched_transfer_order

urlpatterns = [
    path('add_order/',add_order, name='addorder'),
    path('order_item/',order_item, name='orderitem'),
    path('disp_trans/', dispatched_transfer_order, name='disp_trans')
    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
