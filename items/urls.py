from os import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import add_item,fetch_itemvariant

urlpatterns = [
   
    path('add_item/', add_item, name='add_item'),
    path('fetch_itemvariant/<item_id>/',fetch_itemvariant,name='fetch_itemvariant'),
  
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
