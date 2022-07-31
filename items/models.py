
from email.policy import default
from enum import unique
from django.db import models


# Create your models here.
class LowerCase(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LowerCase, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class Item_Group(models.Model):
    group_name =LowerCase(max_length=100,unique=True)
    group_des = LowerCase(max_length=200)
    comment = LowerCase(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.group_name

class Unit(models.Model):    
    unit_name = LowerCase(max_length=100,unique=True)
    short_unit_name =LowerCase(max_length=10,unique=True)
    comment = LowerCase(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.unit_name

    
class Item(models.Model):
    item_group=models.ForeignKey(Item_Group,on_delete=models.PROTECT)
    item_name=LowerCase(max_length=100,unique=True)   
    item_unit=models.ForeignKey(Unit,on_delete=models.PROTECT)
    hsn_sac = LowerCase(max_length=50,blank=True,null=True)   
    comment = LowerCase(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.item_name



class Item_Variant(models.Model):
    item_id = models.ForeignKey(Item,on_delete=models.PROTECT)
    variant_name= LowerCase(max_length=100)   
    con_factor = models.DecimalField(default=1,max_digits=7,decimal_places=2, blank=True,null=True)
    alternate_unit = models.ForeignKey(Unit,on_delete=models.PROTECT,null=True,blank=True)   
    variant_price_a=models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)
    variant_price_b=models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)
    variant_price_c=models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)
    variant_price_d=models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)   
    comment = LowerCase(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.variant_name
