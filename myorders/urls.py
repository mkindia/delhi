from django.contrib import admin
from django.db import router
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from clients.api import views 
from orders.api import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
   # path('client/', include('clients.api.urls')),
   # path('ios/', include('orders.api.urls')),   
   # path('items/',include('items.urls'))
   
   
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
