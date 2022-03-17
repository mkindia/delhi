from django.shortcuts import redirect, render

# Create your views here.

def add_order(request):
    if request.user.is_authenticated:
        
       

        return render(request,'orders/add_order.html')

    else :

        return redirect('/')

    

        

def order_item(request):
    
    if request.user.is_authenticated:

        print('hello')

        return render(request,'orders/order_item.html')
    
    else :

        return redirect('/')