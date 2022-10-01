
from rest_framework import serializers
from items.models import Item_Group,Item,Item_Variant,Unit,Packing_Unit

class unitSerializers(serializers.ModelSerializer):   
    class Meta:
        model=Unit
        fields = '__all__'

class packing_unitSerializers(serializers.ModelSerializer):   
    class Meta:
        model=Packing_Unit
        fields = '__all__'

class itemGroupSerializers(serializers.ModelSerializer):   
    class Meta:
        model=Item_Group
        fields = '__all__'

class itemSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Item
        fields='__all__'



class itemVariantSerializers(serializers.ModelSerializer):
    class Meta:
        model=Item_Variant
        fields='__all__'


