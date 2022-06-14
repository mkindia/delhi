from django.shortcuts import redirect, render
from django.core import serializers
from items.models import Item,Item_Variant
from django.http import JsonResponse
from .forms import itemGroupForm,unitForm,initems
#from .serializers import item_variants_serializars
import json

# Create your views here.

def add_item(request):
    if request.user.is_authenticated:

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                     data = json.loads(request.body.decode("utf-8"))
                     item_id = data['item_id']
                     #print(c_name)

                     item_varients=[]
                     for item_varient in Item_Variant.objects.filter(item_id=1):
                            item_varients.append({'varient_id':item_varient.id,'varient_name':item_varient.item_variant_name})
                   
                     data={'clients':item_varients}
                     return JsonResponse(data)
        
        
        item_fm=initems
        return render(request,'items/add_item.html',{'items_fm':item_fm})

def fetch_itemvariant(request,item_id):
    
    if request.user.is_authenticated:
        #variants=[]

        itemvariants=list(Item_Variant.objects.values().filter(item_id=item_id))
        #serializar=serializers.serialize('json',variants)
       
        return JsonResponse(itemvariants,safe=False)

    else:
        return redirect('/')