
from clients.models import Client,Consignee
from clients.api.serializers import clientSeializers,consigneeSeializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import BasePermission

class CustomPermissions(BasePermission):
    def has_permission(self, request, view):
        if (request.user.is_authenticated):
            return True
        return False


class clients(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = clientSeializers
    permission_classes = (CustomPermissions,)
    http_method_names = ['get','post']

class consignee(viewsets.ModelViewSet):
    queryset = Consignee.objects.all()
    serializer_class = consigneeSeializers
    permission_classes = (CustomPermissions,)
    http_method_names = ['get','post']

class consignee_by_client_id(viewsets.ModelViewSet):
    queryset = Consignee.objects.all()
    serializer_class = consigneeSeializers
    permission_classes = (CustomPermissions,)
    http_method_names = ['get','post']

    def list(self,request):
        con = Consignee.objects.all()
        serializer = consigneeSeializers(con,many=True)        
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        params= kwargs       
        consignee=Consignee.objects.filter(client_id=params['pk'])
        serializer=consigneeSeializers(consignee,many=True)
        return Response(serializer.data)
