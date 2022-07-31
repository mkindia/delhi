
from django.db import router
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from items.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('itemgroup',views.itemgroup,basename='itemgroup')
router.register('items',views.items,basename='items')
router.register('item_variant',views.item_variant,'item_variant')

urlpatterns = [
    path('', include(router.urls)),
   
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
