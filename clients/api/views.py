
from clients.models import Client,Consignee
from clients.api.serializers import clientSeializers,consigneeSeializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import BasePermission

class CustomPermissions(BasePermission):
    def has_permission(self, request, view):
        if (request.user.is_admin or request.user.is_staff and request.user.is_authenticated):
            return True
        return False


class clients(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = clientSeializers
    permission_classes = (CustomPermissions,)
    http_method_names = ['get','post']


    """
    def list(self,request):
        clients = Client.objects.all()
        serializer = clientSeializers(clients,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        print(self.action)      
        if pk is not None:
            try:
                cli=Client.objects.get(id=pk)
                cli = Client.objects.get(id=pk)
                serializer=clientSeializers(cli)
                return Response(serializer.data,status=status.HTTP_200_OK)
            except Client.DoesNotExist :
                cli=None
                return Response({"msg":"Client Not Found",},status=status.HTTP_400_BAD_REQUEST)
    """
   
class consignee_by_client_id(viewsets.ViewSet):
    def list(self,request):
        con = Consignee.objects.all()
        serializer = consigneeSeializers(con,many=True)        
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        con=Consignee.objects.filter(client_id=pk)
        serializer=consigneeSeializers(con,many=True)
        return Response(serializer.data)
