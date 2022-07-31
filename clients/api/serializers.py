from rest_framework import serializers
from clients.models import Client,Consignee

class consigneeSeializers(serializers.ModelSerializer):   
    class Meta:
        model=Consignee
        fields = ('client_id','id','consignee_name')

class clientSeializers(serializers.ModelSerializer):   
    con = consigneeSeializers(many = True, read_only = True) 
    class Meta:
        model=Client
        fields = '__all__'
