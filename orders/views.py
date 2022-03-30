from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_control
from clients.models import Client, Consignee 
import json

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_order(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':           
            consignee=request.POST.get('consignee_input').strip()

            tr = consignee.replace(" ","").split("/")
            try:
                con_id = Consignee.objects.get(consignee_name=tr[0])               
               
            except:
                tr_id=None
            
           
            return render(request,'orders/order_item.html/',{'consignee':consignee,'con_id':con_id})

        return render(request,'orders/add_order.html')
    else :
        return redirect('/')
        
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def order_item(request):
    
    if request.user.is_authenticated:
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = json.loads(request.body.decode("utf-8"))
            con_id = data['consignee_id']
            
            print(data)
            print(con_id)
            data={'consignee':con_id}
            return JsonResponse(data)
                       
        else :
           return render(request,'orders/order_item.html/')
    
    else :

        return redirect('/')