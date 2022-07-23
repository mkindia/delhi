
from django.db import router
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from orders.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ios_by_client_id',views.ios_by_client_id,basename='ios_by_client_id')
router.register('con_ord_by_cli',views.consignee_order_by_client_id,basename='con_ord_by_cli')
router.register('order_item_by_order_id',views.order_item_by_order_id,basename='order_item_by_order_id')
urlpatterns = [
    path('', include(router.urls)),
   
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
