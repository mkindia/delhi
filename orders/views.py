from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_control


from clients.models import Client, Consignee
from items.models import Item,Item_Variant, Unit
from .models import Consignee_Order,Item_Order,Item_Order_Status
from .forms import order_dispatchForm
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
            
           
            if request.method == 'POST':
                data = json.loads(request.body.decode("utf-8"))
                order_created=False       
                for item in data:
                    client_instance=Client.objects.only('id').get(id=item['cli_id'])        
                    con_instance=Consignee.objects.only('id').get(id=int(item['con_id']))
                    item_instance= Item.objects.only('id').get(id=int(item['item_id']))
                    item_variant_instance= Item_Variant.objects.only('id').get(id=int(item['item_variant_id']))
                    order_date=item['date']
                    
                    if order_created == False : 
                        order_created = True
                        create_order= Consignee_Order.objects.create(client_id=client_instance,
                                                            consignee_id=con_instance,
                                                            date=order_date)
                    Item_Order.objects.create(client_id=client_instance,
                                            consignee_id=con_instance,
                                            date=order_date,                                           
                                            item_id=item_instance,                                           
                                            item_variant_id=item_variant_instance,                                           
                                            item_veriant_price=item['item_price'],
                                            price_per_unit=Unit.objects.only('unit_name').get(unit_name=item['per']),
                                            item_qty=item['qty'],
                                            order_unit=Unit.objects.only('unit_name').get(unit_name=item['unit']))
               # create_order.save()
                #con_id = data['item_name']
                order_id=None
                clientsall=[]

                
                for cli in Client.objects.all():
                    clientsall.append({'id':cli.id,'name':cli.client_name})
                
                #print(data)
                #print(con_id)
               
                return JsonResponse(data,safe=False)
            if request.method == 'PUT':

                data = json.loads(request.body.decode("utf-8"))                
                is_client = Consignee.objects.get(pk=data['con_id'])
                items=list(Item_Order.objects.filter(consignee_id=data['con_id']).values())
                selected_consignes=list(Consignee.objects.filter(client_id=is_client.client_id).values())
                msg='client not found'
               # print(items)
                data={'items':items,'msg':msg,'selected_consignes':selected_consignes}

                return JsonResponse(data,safe=False)
                                    
        else :            
            client=Client.objects.filter(user_id=request.user)
            units=Unit.objects.all()          
            consigne = Consignee.objects.filter(client_id__in=client) # client_id__in = client filter use
            Items=Item.objects.all()
            return render(request,'orders/order_item.html/',{'clients':client,'consignes':consigne,'items':Items,'units':units})
    
    else :

        return redirect('/')

def item_order_status(request):
     if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            if request.method == 'PUT':
                data = json.loads(request.body.decode("utf-8"))
               # print(data['order_item_id'])
                
                Item_Order_status=Item_Order_Status.objects.filter(item_order_id=data['order_item_id'])
                item_qty=0
                for qty in Item_Order_status:
                    if qty.item_qty != None:
                        item_qty += qty.item_qty
                    else:
                        item_qty=0
                item_order_status ={'item_qty':item_qty,'order_item_id':data['order_item_id']}
                return JsonResponse(item_order_status)

def dispatched_transfer_order(request):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            if request.method == 'PUT':
                data = json.loads(request.body.decode("utf-8"))
                
                disform = order_dispatchForm
                return render(request,'orders/dispatch_transfer.html',{'fm':disform})

    else :
        return redirect('/')