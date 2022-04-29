
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json
import uuid

from core.models import Custom_User
from .models import Client, Client_Group, Client_Token,Consignee,Transport,Station
from .forms import Client_Form,Consignee_Transport_form,Consignee_form

# for sending mail
def mail_for_verify_user(subject,email,url,message,token):

       subject = subject

       if url != None :
              message = f'{message} http://127.0.0.1:8000/{url}/{token}/'

       else :
              message = f''+message

       
       from_email = settings.EMAIL_HOST_USER
       recipient_list = [email]
       send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_dashboard(request):
    clients = Client.objects.all()
    return render(request,'clients/admin_dashboard.html/',{'client':clients})

def add_client(request):

       if request.user.is_authenticated:
     
              c_g = Client_Group.objects.all()
              station=Station.objects.all()
              trns=Transport.objects.all() 
       
              if request.method == 'POST':
              
                     try:                            
                            cli_name=Client.objects.get(client_name=request.POST.get('client').lower())             
                            messages.warning(request,'Client All ready exist ' + '[ ' +cli_name.client_name+ ' ]')                     
                            #return redirect('/clients/add_client/')
                     except :
                            cli_name = None
                            try:
                                          
                                   g_id=request.POST.get('client_group')
                                   g_inst=Client_Group.objects.only('id').get(id=g_id)         
                                   
                                   t_id=request.POST.get('transport')
                                   t_inst=Transport.objects.only('id').get(id=t_id)

                                   s_id=request.POST.get('station')
                                   s_inst=Station.objects.only('id').get(id=s_id)
                                   
                                   client=Client.objects.create(client_name=request.POST.get('client'),client_group=g_inst)
                            
                                   client.user_id.add(request.user.id)

                                   consignee=Consignee.objects.create(client_id=client,consignee_name=request.POST.get('client'),transport=t_inst,station=s_inst,is_client=True)             
                                   #consignee.save()    
                                          
                                   messages.success(request, 'Client Added Success')        
                            except :

                                   messages.warning(request,'Data_error')
                                   return render(request,'clients/add_client.html/',{'c_g':c_g,'transport':trns,'station':station})                             

                     
                     
                     
              
                     
                     
              return render(request,'clients/add_client.html/',{'c_g':c_g,'transport':trns,'station':station})

       else :
              return redirect('/')

def genrate_client_token(request):
       if request.user.is_authenticated:

              if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                     data = json.loads(request.body.decode("utf-8"))
                     c_id = data['client_id']
                    
                     
                     try:
                            c_inst= Client_Token.objects.get(client_id=c_id)
                            data={'client':c_inst.id,'token':c_inst.token,'securetoken':'196b57c0-c730-404c-9326-a53fe2ebc1e0'}
                            print(c_inst)
                            return JsonResponse(data)
                     except:
                            c_inst=None
                            data={'token':'Token : Not Genrated'}
                            return JsonResponse(data)
                           
              
              if request.method == 'POST':
                     client=request.POST.get('client')
                     try:
                            c_f= Client_Token.objects.get(client_id=client)
                            messages.warning(request,'Client Has Already Token '+'[ '+ c_f.token +' ]')
                     except:
                            c_f=None
                            c_inst= Client.objects.only('id').get(id=client)                                               
                            c_token=Client_Token.objects.create(client_id=c_inst,token=uuid.uuid4())
                            messages.success(request,'Token Genrated')
                    
              client=Client.objects.filter(user_id=request.user.id)
              return render(request,'clients/genrate_client_token.html',{'clients':client})
       else:
              return redirect('/')

def add_consignee(request):

       if request.user.is_authenticated:
              client=Client.objects.filter(user_id=request.user.id)
              station=Station.objects.all()
              trns=Transport.objects.all() 
                     
              if request.method == 'POST':
              
                     
                     con=Consignee_form(request.POST)
                     if con.is_valid():         
                          
                            con.save()
                            messages.error(request,'Consignee add success')      
                     else:
                            messages.error(request,'Consignee already exists.')          


                           

              return render(request,'clients/add_consignee.html/',{'clients':client,'stations':station,'transports':trns})
       else:
              return redirect('/')