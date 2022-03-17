from django.db import models
from clients.models import *
from items.models import *

# Create your models here.
class LowerCase(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LowerCase, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class Consignee_Order(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    consignee=models.ForeignKey(Consignee,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    des =LowerCase(max_length=200)
    
class Item_Order(models.Model):
    order=models.ForeignKey(Consignee_Order,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.SET_NULL,null=True,blank=True)
    item_price=models.PositiveIntegerField(default=1.1)
    price_per_unit=models.ForeignKey(Unit,related_name='price_per_unit',on_delete=models.SET_NULL,null=True,blank=True)
    item_variant = models.ForeignKey(item_Variant,on_delete=models.SET_NULL,null=True,blank=True)
    item_qty = LowerCase(max_length=100,null=True,blank=True)
    item_unit = models.ForeignKey(Unit,related_name='item_unit',on_delete=models.SET_NULL,null=True,blank=True)
    comment = LowerCase(max_length=200,null=True,blank=True)

class Dispatched_Item_Order(models.Model):
    item_order=models.ForeignKey(Item_Order,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.SET_NULL,null=True,blank=True)
    item_price=models.PositiveIntegerField(default=1.1)
    per_unit=LowerCase(max_length=100,null=True,blank=True)
    item_variant = LowerCase(max_length=100,null=True,blank=True)
    item_qty = LowerCase(max_length=100,null=True,blank=True)
    item_unit = LowerCase(max_length=100,null=True,blank=True)
    dispatched_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    docket_number = LowerCase(max_length=100,blank=True,null=True)
    comment = LowerCase(max_length=200,null=True,blank=True)