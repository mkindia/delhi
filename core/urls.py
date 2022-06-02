from os import name
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home,signin,signup,user_logout,change_pass,forget_pwd,forget_uname,pass_change,profile_change,errorpage,account_verify

urlpatterns = [   
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('user_logout/', user_logout, name="user_logout"),    
    path('changepass/', change_pass, name='changepass'),
    path('forget_pwd/', forget_pwd, name='forget_pwd'),
    path('forgetuname/', forget_uname, name='forgetuname'),
    path('pass_change/<token>/', pass_change, name='pass_change'),
    path('profile_change/<mode>/', profile_change ,name='profile_change                                                                                                                                         '),
    path('errorpage/<errortype>/', errorpage, name='errorpage'),
    path('account_verify/<token>/',account_verify,name='account_verify'),
    path('clients/', include('clients.urls')),
    path('orders/', include('orders.urls')),
    path('items/',include('items.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
