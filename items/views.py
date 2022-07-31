from django.shortcuts import redirect, render
from django.core import serializers
from items.models import Item,Item_Variant,Item_Group,Unit
from django.http import JsonResponse
from .forms import itemGroupForm, itemsForm,unitForm,initems
#from .serializers import item_variants_serializars
import json

# Create your views here.

def add_item(request):
    if request.user.is_authenticated:
        item_groups=Item_Group.objects.all()
        item_units=Unit.objects.all()

        return render(request,'items/add_item.html',{'item_groups':item_groups,'item_units':item_units})

def add_item_variant(request):
    if request.user.is_authenticated:
        item_names=Item.objects.all()

        return render(request,'items/add_item_variant.html',{'item_names':item_names,})

def fetch_itemvariant(request,item_id):
    
    if request.user.is_authenticated:
        #variants=[]

        itemvariants=list(Item_Variant.objects.values().filter(item_id=item_id))
        #serializar=serializers.serialize('json',variants)
       
        return JsonResponse(itemvariants,safe=False)

    else:
        return redirect('/')