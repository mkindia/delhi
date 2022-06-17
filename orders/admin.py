from dataclasses import fields
from django.contrib import admin
from .models import Item_Order,Consignee_Order,Item_Order_Status

# Register your models here.
@admin.register(Item_Order)
class Item_Order(admin.ModelAdmin):
     list_display = ('id','client_id','consignee_id','order_id','item_id','item_variant_id','item_veriant_price','item_qty','order_unit')

@admin.register(Consignee_Order)
class Consignee_order(admin.ModelAdmin):
     list_display = ('id','client_id','consignee_id','order_type')

@admin.register(Item_Order_Status)
class Item_Order_Status(admin.ModelAdmin):
    list_display = ('item_order_id','date','item_qty','status')