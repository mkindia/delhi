from os import name
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import add_order,order_item,edit_dispatched_transfer_order,item_order_status

urlpatterns = [
    path('api/',include('orders.api.urls')),
    path('add_order/',add_order, name='addorder'),
    path('order_item/',order_item, name='orderitem'),
    path('item_order_status/', item_order_status, name='item_order_status'),
    path('edit_disp_trans/<id>/', edit_dispatched_transfer_order, name='edit_disp_trans'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
