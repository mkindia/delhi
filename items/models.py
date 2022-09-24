
from email.policy import default
from enum import unique
from random import choices
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
    
class Item(models.Model):   
    item_group=models.ForeignKey(Item_Group,on_delete=models.PROTECT)
    item_code = LowerCase(max_length=100,blank=True,null=True)   
    item_name=LowerCase(max_length=100,unique=True)
    item_img = models.ImageField(upload_to='item', blank=True, null=True)
    item_unit=LowerCase(max_length=30)
    hsn_sac = LowerCase(max_length=50,blank=True,null=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)
    item_discraption = LowerCase(max_length=200,blank=True,null=True)    
    comment = LowerCase(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.item_name



class Item_Variant(models.Model):    
    item_id = models.ForeignKey(Item,on_delete=models.PROTECT)
    variant_code = LowerCase(max_length=100,blank=True,null=True)
    variant_name= LowerCase(max_length=100)
    item_variant_img = models.ImageField(upload_to='itemvariant', blank=True, null=True)
    weight_kg = models.DecimalField(default=1,max_digits=7,decimal_places=3,null=True,blank=True)
    height_cm = models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)
    length_cm = models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)
    width_cm = models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)
    depth_cm = models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)
    variant_color = LowerCase(max_length=50,blank=True,null=True)
    master_packing = models.DecimalField(default=1,max_digits=4,decimal_places=0,null=True,blank=True)
    price=models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)
    client_price_a=models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)
    client_price_b=models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)
    client_price_c=models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)
    client_price_d=models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)
    variant_stock = models.DecimalField(default=1,max_digits=7,decimal_places=2,null=True,blank=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)
    variant_discraption = LowerCase(max_length=200,blank=True,null=True)  
    comment = LowerCase(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.variant_name
