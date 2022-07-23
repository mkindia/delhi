from os import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import add_order,order_item,dispatched_transfer_order,item_order_status

urlpatterns = [
    path('add_order/',add_order, name='addorder'),
    path('order_item/',order_item, name='orderitem'),
    path('item_order_status/', item_order_status, name='item_order_status'),
    path('disp_trans/', dispatched_transfer_order, name='disp_trans'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
