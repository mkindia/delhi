

from orders.models import Consignee_Order, Item_Order_Status,Item_Order
#from clients.models import Client,Consignee
from orders.api.serializers import itemOrderStatus_serializers,consigneeOrder_serializers, order_item_serializers
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
#from rest_framework.decorators import action

from rest_framework import status
from rest_framework import viewsets


class CustomPermissions(BasePermission):
    def has_permission(self, request, view):
        if (request.user.is_authenticated):
            return True
        return False

class itemOrderStatus(viewsets.ModelViewSet):

    queryset = Item_Order_Status.objects.all()
    serializer_class =itemOrderStatus_serializers
    permission_classes = (CustomPermissions,)
    http_method_names = ['get','post']

class ios_by_client_id(viewsets.ModelViewSet):   
    serializer_class =itemOrderStatus_serializers   
    permission_classes = (CustomPermissions,)
    http_method_names = ['get']

    def get_queryset(self):       
        query_set = Item_Order_Status.objects.all()       
        return query_set

    def retrieve(self, request, *args, **kwargs):
        params= kwargs       
        clients=Item_Order_Status.objects.filter(client_id=params['pk'])
        serializer=itemOrderStatus_serializers(clients,many=True)
        return Response(serializer.data)

class order_item(viewsets.ModelViewSet):
    queryset = Item_Order.objects.all()
    serializer_class=order_item_serializers
    permission_classes = (CustomPermissions,)
    http_method_names = ['get','post','put','patch']

    def create(self, request, *args, **kwargs): # for multiple instace creation
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class item_order_by_consignee_id(viewsets.ModelViewSet):
    queryset = Item_Order.objects.all()
    serializer_class=order_item_serializers
    permission_classes = (CustomPermissions,)
    http_method_names = ['get',]

    def retrieve(self, request, *args, **kwargs):
        params= kwargs       
        consignee=Item_Order.objects.filter(consignee_id=params['pk'])
        serializer=order_item_serializers(consignee,many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs): # for multiple instace creation
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
        
class consignee_order_by_client_id(viewsets.ViewSet):
    def list(self,request):
        con_ord = Consignee_Order.objects.all()
        serializer = consigneeOrder_serializers(con_ord,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
            try:
                con_ord=Consignee_Order.objects.filter(client_id=pk)              
                serializer=consigneeOrder_serializers(con_ord,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            except Consignee_Order.DoesNotExist :
                con_ord=None
                return Response({"msg":"Status Not Found",},status=status.HTTP_400_BAD_REQUEST)


class order_item_by_order_id(viewsets.ViewSet):
    
    def list(self,request):
        ord_item = Item_Order.objects.all()
        serializer = order_item_serializers(ord_item,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        ord_item = Item_Order.objects.filter(pk=pk)
        serializer = order_item_serializers(ord_item,many=True)
        return Response(serializer.data)
    
    