
from rest_framework import serializers
from items.models import Item_Group,Unit,Item,Item_Variant

class itemGroupSerializers(serializers.ModelSerializer):   
    class Meta:
        model=Item_Group
        fields = '__all__'

class itemSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Item
        fields='__all__'

class unitSerializers(serializers.ModelSerializer):
    class Meta:
        model=Unit
        fields='__all__'

class itemVariantSerializers(serializers.ModelSerializer):
    class Meta:
        model=Item_Variant
        fields='__all__'


