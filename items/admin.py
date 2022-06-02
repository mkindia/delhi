from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Item_Group)
class Item_Group(admin.ModelAdmin):
    list_display = ['group_name',]

@admin.register(Unit)
class Unit(admin.ModelAdmin):
    list_display = ['unit_name',]

@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display = ['item_name',]

@admin.register(Item_Variant)
class Item_Variant(admin.ModelAdmin):   
    list_display = ['item_variant_name','con_factor','alternate_unit','item_variant_price','item_variant_price_a',
    'item_variant_price_b','item_variant_price_c','item_variant_price_d','item_variant_price_e','item_variant_price_f','comment']
