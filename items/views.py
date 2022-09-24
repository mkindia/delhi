from django.shortcuts import redirect, render
from items.models import Item,Item_Variant,Item_Group
from django.http import JsonResponse

def add_item(request):
    if request.user.is_authenticated:
        item_groups=Item_Group.objects.all()       
        return render(request,'items/add_item.html',{'item_groups':item_groups})

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