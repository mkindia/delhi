
from http import client
from pyexpat.errors import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_control
from django.contrib import messages
from clients.models import Client, Consignee
from items.models import Item,Item_Variant, Unit
import json

# Create your views here.
#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_order(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':           
            consignee=request.POST.get('consignee_input').strip()

            tr = consignee.replace(" ","").split("/")
            try:
                con_id = Consignee.objects.get(consignee_name=tr[0])                           
                         
            except:
                con_id=None
            
           
            return render(request,'orders/order_item.html/',{'consignee':consignee,'con_id':con_id})
        try:
           
            client=Client.objects.filter(user_id=request.user)           
            consigne = Consignee.objects.filter(client_id__in=client) # for selected clents
           
            return render(request,'orders/add_order.html',{'clients':client,'consignes':consigne})
        except:
            client=None
            consigne=None
            
            return render(request,'orders/add_order.html')


    else :
        return redirect('/')
        
#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def order_item(request):
    
    if request.user.is_authenticated:
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = json.loads(request.body.decode("utf-8"))
            #print(len(data))
            #print(len(data[0]))
            #print(data[len(data)-1]['con_id'])
            #print(data[len(data)-1]['item_id'])

            for item in data:
                print(item['cli_id'])
                print(item['con_id'])
                print(item['item_id'])
                print(item['item_variant_id'])
            #con_id = data['item_name']
            order_id=None
            clientsall=[]

            
            for cli in Client.objects.all():
                clientsall.append({'id':cli.id,'name':cli.client_name})
            
            #print(data)
            #print(con_id)
            if order_id ==None:
                data={'clients':clientsall}           
            else:
                data={'clients':clientsall}             
           
            return JsonResponse(data)
                       
        else :
            
            client=Client.objects.filter(user_id=request.user)
            units=Unit.objects.all()          
            consigne = Consignee.objects.filter(client_id__in=client) # client_id__in = client filter use
            Items=Item.objects.all()
            return render(request,'orders/order_item.html/',{'clients':client,'consignes':consigne,'items':Items,'units':units})
    
    else :

        return redirect('/')