
from django.db import router
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from clients.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('clients',views.clients,basename='clients')
router.register('consignee',views.consignee,basename='consignee')
router.register('consignee_by_client_id',views.consignee_by_client_id,basename='consignee_by_client_id')

urlpatterns = [
    path('', include(router.urls)),
   
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
