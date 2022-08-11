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
    list_display = ['variant_name','con_factor','alternate_unit','client_price_a',
    'client_price_b','client_price_c','client_price_d','comment']
