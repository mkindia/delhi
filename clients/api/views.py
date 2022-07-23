from xml.etree.ElementTree import Comment
from django.shortcuts import render
from clients.models import Client,Consignee
from clients.api.serializers import clientSeializers,consigneeSeializers
from rest_framework.response import Response

from rest_framework import status
from rest_framework import viewsets

class clients(viewsets.ViewSet):
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

   
class consignee_by_client_id(viewsets.ViewSet):
    def list(self,request):
        con = Consignee.objects.all()
        serializer = consigneeSeializers(con,many=True)        
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        con=Consignee.objects.filter(client_id=pk)
        serializer=consigneeSeializers(con,many=True)
        return Response(serializer.data)
