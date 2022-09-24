from os import name
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import add_order, dispatch_transfer,order_item,edit_dispatched_transfer_order,item_order_status, order_status_edit

urlpatterns = [
    path('api/',include('orders.api.urls')),
    path('add_order/',add_order, name='addorder'),
    path('order_item/',order_item, name='orderitem'),
    path('item_order_status/<pk>/', item_order_status, name='item_order_status'),
    path('order_status_edit/<pk>/', order_status_edit, name='order_status_edit'),
    path('edit_disp_trans/<id>/', edit_dispatched_transfer_order, name='edit_disp_trans'),
    path('dispatch_transfer/<pk>/<bal>/',dispatch_transfer,name='dispatch_transfer')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
