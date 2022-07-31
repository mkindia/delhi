from os import name
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import add_item, add_item_variant,fetch_itemvariant
#from items.api import views as apiviews

urlpatterns = [
    path('api/', include('items.api.urls')),   
    path('add_item/', add_item, name='add_item'),
    path('add_item_variant/', add_item_variant, name='add_item_variant'),
    path('fetch_itemvariant/<item_id>/',fetch_itemvariant,name='fetch_itemvariant'),
  
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
