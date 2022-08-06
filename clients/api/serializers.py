from rest_framework import serializers
from clients.models import Client,Consignee

class consigneeSeializers(serializers.ModelSerializer):   
    class Meta:
        model=Consignee
        fields = '__all__'

class clientSeializers(serializers.ModelSerializer):   
    con = consigneeSeializers(many = True, read_only = True) 
    class Meta:
        model=Client
        fields = '__all__'
