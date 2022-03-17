
from tkinter import UNITS
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
    def __str__(self):
        return self.group_name

class Unit(models.Model):    
    unit_name = LowerCase(max_length=100)
    def __str__(self):
        return self.unit_name

    
class Item(models.Model):
    item_group=models.ForeignKey(Item_Group,on_delete=models.CASCADE)
    item_name=LowerCase(max_length=100,unique=True)
    item_unit=models.ForeignKey(Unit,related_name='unit_item', on_delete=models.SET_NULL,null=True,blank=True)
    con_factor = models.PositiveIntegerField(default=1,blank=True,null=True)
    alternate_unit = models.ForeignKey(Unit,related_name='alternate_unit', on_delete=models.SET_NULL,null=True,blank=True)
    hsn_sac = LowerCase(max_length=50,blank=True,null=True)
    item_price=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.item_name



class item_Variant(models.Model):
    item_variant = models.ForeignKey(Item,on_delete=models.CASCADE)
    variant= LowerCase(max_length=100)
    def __str__(self):
        return self.variant