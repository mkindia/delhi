from dataclasses import fields
from rest_framework import serializers
from orders.models import Item_Order_Status,Consignee_Order,Item_Order

class itemOrderStatus_serializers(serializers.ModelSerializer):   
    class Meta:
        model=Item_Order_Status
        fields = '__all__'

class consigneeOrder_serializers(serializers.ModelSerializer):
    class Meta:
        model = Consignee_Order
        fields = '__all__'
        
class order_item_serializers(serializers.ModelSerializer):   
    class Meta:
        model = Item_Order
        fields = '__all__'