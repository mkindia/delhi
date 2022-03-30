from email import message
from pyexpat import model
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json
import uuid
from .models import Client,Consignee,Transport,Station
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


# Create your views here.
def admin_dashboard(request):
    clients = Client.objects.all()
    return render(request,'clients/admin_dashboard.html/',{'client':clients})

def add_client(request):
       client=Client_Form
       consignee_trs=Consignee_Transport_form
       if request.method == 'POST':
         
         try:
              cli_name=Client.objects.get(client=request.POST.get('client'))
              messages.warning(request,'Client All ready exist ' + '[ ' +cli_name.client+ ' ]')
              return redirect('/clients/add_client/')
         except :
              cli_name = None
              client=Client_Form(request.POST)
              consignee_trs=Consignee_Transport_form(request.POST)
              trans_id = Transport.objects.only('id').get(id=int(request.POST.get('transport')))
              station_id= Station.objects.only('id').get(id=int(request.POST.get('station')))
              client=client.save()
              client.user_id.add(request.user.id)        
              consignee=Consignee(client_id=client,consignee_name=request.POST.get('client'),transport=trans_id,station=station_id,is_client=True)             
              consignee.save()              
              messages.success(request,'Client Added Success')        
        

         
         return redirect('/clients/add_client/') 
         
     
         

       return render(request,'clients/add_client.html/',{'client':client,'transport':consignee_trs})

def add_consignee(request):

       if request.method == 'POST':
             
              
              con=Consignee_form(request.POST)
              if con.is_valid():                     
                     #cons_name=con.cleaned_data['consignee_name']
                     #cli_id=con.cleaned_data['client_id']
                     con.save()
                     messages.error(request,'consignee add success')      
              else:
                     messages.error(request,'consignee already exists.')          


      
       consignee_form =  Consignee_form

       return render(request,'clients/add_consignee.html/',{'trans_form':consignee_form})
