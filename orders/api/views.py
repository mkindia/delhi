from http import client
from urllib import request
from orders.models import Consignee_Order, Item_Order_Status,Item_Order
from clients.models import Client,Consignee
from orders.api.serializers import itemOrderStatus_serializers,consigneeOrder_serializers, order_item_serializers
from rest_framework.response import Response
from rest_framework.permissions import BasePermission

from rest_framework import status
from rest_framework import viewsets , generics

from orders.views import item_order_status

class CustomPermissions(BasePermission):
    def has_permission(self, request, view):
        if (request.user.is_admin or request.user.is_staff and request.user.is_authenticated):
            return True
        return False

class itemOrderStatus(viewsets.ModelViewSet):

    queryset = Item_Order_Status.objects.all()
    serializer_class =itemOrderStatus_serializers
    permission_classes = (CustomPermissions,)
    http_method_names = ['get','post']


    """
    def list(self,request):
        ios = Item_Order_Status.objects.all()
        serializer = itemOrderStatus(ios,many=True)
        return Response(serializer.data)

    def post(self,request):
        post_data = request.data
        print(post_data['client_id'] + ' ' + post_data['consignee_id'])
        print(post_data['order_item_id'] + ' ' + post_data['dispatch_qty']+' '+ post_data['dispatch_date'])
        cli_instance=Client.objects.only('id').get(id=post_data['client_id'])        
        con_instance=Consignee.objects.only('id').get(id=int(post_data['consignee_id']))
        itemOrder_instance=Item_Order.objects.only('id').get(id=post_data['order_item_id'])
        Item_Order_Status.objects.create(
            client_id=cli_instance,
            consignee_id=con_instance,
            item_order_id=itemOrder_instance,
            date=post_data['dispatch_date'],
            item_qty=post_data['dispatch_qty'],status=post_data['status'])

        if post_data['trs_id'] != None:
            trs_id = post_data['trs_id']
        else:
            trs_id = None      
        
        return Response(post_data,status=status.HTTP_200_OK)
    """
class ios_by_client_id(viewsets.ModelViewSet):   
    serializer_class =itemOrderStatus_serializers   
    permission_classes = (CustomPermissions,)
    http_method_names = ['get','post',]

    def get_queryset(self):
        #queryset = super(ios_by_client_id, self).get_queryset()   
        query_set = Item_Order_Status.objects.all()       
        return query_set
    def retrieve(self, request, *args, **kwargs):
        params= kwargs       
        clients=Item_Order_Status.objects.filter(client_id=params['pk'])
        serializer=itemOrderStatus_serializers(clients,many=True)
        return Response(serializer.data)

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
        ord_item = Item_Order.objects.filter(order_id=pk)
        serializer = order_item_serializers(ord_item,many=True)
        return Response(serializer.data)