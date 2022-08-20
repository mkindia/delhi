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
class unit(viewsets.ModelViewSet):
    queryset=Unit.objects.all()
    serializer_class = unitSerializers
    permission_classes=(CustomPermissions,)
    http_method_names =['get']

class itemgroup(viewsets.ModelViewSet):
   
    queryset = Item_Group.objects.all()
    serializer_class = itemGroupSerializers
    permission_classes = (CustomPermissions,)
    http_method_names = ['get','post']
    
class items(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = itemSerializers
    permission_classes = (CustomPermissions,)
    http_method_names = ['post','get','put']
  
    """
    def perform_create(self, serializer):
        serializer.save()
    """

class item_variant(viewsets.ModelViewSet):
    queryset=Item_Variant.objects.all()
    serializer_class = itemVariantSerializers
    permission_classes=(CustomPermissions,)
    http_method_names = ['post','get']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class item_varient_by_item_id(viewsets.ModelViewSet):
    serializer_class =itemVariantSerializers    
    http_method_names = ['get']

    def get_queryset(self):       
        query_set = Item_Variant.objects.all()       
        return query_set
        
    def retrieve(self, request, *args, **kwargs):
        params= kwargs       
        clients=Item_Variant.objects.filter(item_id=params['pk'])
        serializer=itemVariantSerializers(clients,many=True)
        return Response(serializer.data)