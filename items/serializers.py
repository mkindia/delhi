from email.policy import default
from rest_framework import serializers

from items.models import Item_Variant

class item_variants_serializars(serializers.Serializer):
    id=serializers.IntegerField()
    item_variant_name=serializers.CharField(max_length=200)   
    item_variant_price=serializers.DecimalField(default=1,max_digits=7,decimal_places=2)
    item_variant_price_a=serializers.DecimalField(default=1,max_digits=7,decimal_places=2)
    item_variant_price_b=serializers.DecimalField(default=1,max_digits=7,decimal_places=2)
    item_variant_price_c=serializers.DecimalField(default=1,max_digits=7,decimal_places=2)
    item_variant_price_d=serializers.DecimalField(default=1,max_digits=7,decimal_places=2)
    item_variant_price_e=serializers.DecimalField(default=1,max_digits=7,decimal_places=2)
    item_variant_price_f=serializers.DecimalField(default=1,max_digits=7,decimal_places=2)
