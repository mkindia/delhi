from rest_framework.permissions import BasePermission

from core.models import Custom_User
from items.models import Item_Group,Item,Unit,Item_Variant
from items.api.serializers import itemGroupSerializers,itemSerializers,unitSerializers,itemVariantSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class CustomPermissions(BasePermission):

    def has_permission(self, request, view):
        if (request.user.is_admin or request.user.is_staff and request.user.is_authenticated):
            return True
        return False

class itemgroup(viewsets.ModelViewSet):
   
    queryset = Item_Group.objects.all()
    serializer_class = itemGroupSerializers
    permission_classes = (CustomPermissions,)
    http_method_names = ['get','post']
    
class items(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = itemSerializers
    permission_classes = (CustomPermissions,)
    http_method_names = ['post','get']
  
    """
    def perform_create(self, serializer):
        serializer.save()
    """

class item_variant(viewsets.ModelViewSet):
    queryset=Item_Variant.objects.all()
    serializer_class = itemVariantSerializers
    permission_classes=(CustomPermissions,)
    http_method_names = ['post','get']