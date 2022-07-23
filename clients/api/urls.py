
from django.db import router
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from clients.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('clients',views.clients,basename='clients')
router.register('consignees',views.consignee_by_client_id,basename='consignees')



urlpatterns = [
    path('', include(router.urls)),
   
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
