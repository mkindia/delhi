

from email import message
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

from pymysql import NULL


from core.models import Custom_User
from .models import Client, Client_Token,Consignee,Transport,Station,State
from .forms import Client_Form,Consignee_Transport_form,Consignee_form

# for sending mail
def mail_for_verify_user(subject,message,email,url,token):

     

       if url != None :
              message = f'{message} http://127.0.0.1:8000/{url}/{token}/'

       else :
              message = f''+message

       
       from_email = settings.EMAIL_HOST_USER
       to_email = [email]
       send_mail(subject=subject,message=message,from_email=from_email,recipient_list=to_email)

def send_email(request):
       if request.user.is_authenticated:
              if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                     data = json.loads(request.body.decode("utf-8"))
                     try:
                            cli_email=Client.objects.get(id=data['client_id'])
                            sub=data['subject']
                            msg=data['message']
                            if cli_email.email == None or cli_email.email == '':
                                   msg = 'Client not Found any email please check'
                            else:                                  
                                   mail_for_verify_user(sub,msg,cli_email.email,None,'nottoken')                                  
                                   msg = 'Email sent to Client'

                            data={'message':msg}
                            return JsonResponse(data)
                     except:
                            cli_email=None
                            data={'message':'something went wrong'}
                            return JsonResponse(data)


                   

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_dashboard(request):
    clients = Client.objects.all()
    return render(request,'clients/admin_dashboard.html/',{'client':clients})

#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_client(request):

       if request.user.is_authenticated:              
              if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                     data = json.loads(request.body.decode("utf-8"))
                     c_name = data['c_name']
                     g_name = data['g_name']
                     s_name = data['s_name']
                     t_name = data['t_name']
                     m_no = data['m_no']
                     clientsall=[]
                     for cli in Client.objects.all():
                                   clientsall.append({'id':cli.id,'name':cli.client_name})
                     try:
                            cli_name=Client.objects.get(client_name=c_name.lower())                            
                            msg = 'Client All ready exist ' + '[ ' +cli_name.client_name+ ' ]'
                            if cli_name.phone_number == m_no:
                                   msg = 'phone allready exist'                           
                            data = {'message':msg,'clients':clientsall}
                            return JsonResponse(data)
                     except:                                               
                            cli_name=NULL
                            try:   
                                   ph=Client.objects.get(phone_number=m_no)
                                   msg = 'phone allready exist'
                                   data = {'message':msg,'clients':clientsall}
                                   return JsonResponse(data)
                            except:
                                   client=Client.objects.create(client_name=c_name,client_group=g_name,phone_number=m_no)
                            
                                   client.user_id.add(request.user.id)
                                   consignee=Consignee.objects.create(client_id=client,consignee_name=c_name,transport=t_name,station=s_name,is_client=True)             
                                   consignee.save()  
                                   msg='success'
                                   data={'message':msg,'clients':clientsall}
                                   return JsonResponse(data)
              
              
              
              state=Consignee.objects.order_by('state').values('state').distinct()
              station = Consignee.objects.order_by('station').values('station').distinct()
              transport = Consignee.objects.order_by('transport').values('transport').distinct()
              if request.method == 'POST':
                                        
                     next = request.POST.get('next', '/')
                     print(next +'hello')
                     try:                            
                            cli_name=Client.objects.get(client_name=request.POST.get('client').lower())             
                            messages.warning(request,'Client All ready exist ' + '[ ' +cli_name.client_name+ ' ]')
                            
                                  
                            #return redirect('/clients/add_client/')
                           
                            
                            if next == '' or next == None :                                 
                             #      return HttpResponseRedirect(next)
                                   return redirect('/clients/add_client/')
                            else :
                                  return redirect(next) 
                     except :
                                   print('frist error')
                                   cli_name = None
                           
                                   group_name=request.POST.get('client_group')
                                   
                                   #g_inst=Client_Group.objects.only('id').get(id=g_id)         
                                   
                                   transport=request.POST.get('transport')
                                   
                                   #t_inst=Transport.objects.only('id').get(id=t_id)

                                   station=request.POST.get('station')
                                   
                                   #staion_n = Station.objects.get(station_name=s_id)

                                   p_no= request.POST.get('mnumber')
                                   #print(p_no+g_id+t_id+s_id)
                                  
                                  # client=Client.objects.create(client_name=request.POST.get('client'),client_group=group_name,phone_number=p_no)
                            
                                  # client.user_id.add(request.user.id)
                                  # consignee=Consignee.objects.create(client_id=client,consignee_name=request.POST.get('client'),transport=transport,station=station,is_client=True)             
                                   #consignee.save()    
                                   
                                   messages.success(request, 'Client Added Success')   
                                   if next == '' or next == None :                                
                             
                                          return redirect('/clients/add_client/')
                                   else :
                                          return redirect(next)                                 
                                                                        
                                   """
                                   print('errror')
                                   messages.warning(request,'Data_error')
                                   return render(request,'clients/add_client.html/',{'state':state,'transport':transport,'station':station})                             
                                   """
              else:       
            
                     return render(request,'clients/add_client.html/',{'state':state,'transport':transport,'station':station})

       else :
              return redirect('/')

#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def genrate_client_token(request):
       if request.user.is_authenticated:

                            
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

              if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                     data = json.loads(request.body.decode("utf-8"))
                     c_id = data['client_id']                    
                     
                     try:
                            c_inst= Client_Token.objects.get(client_id=c_id)
                            data={'client':c_inst.id,'token':c_inst.token,'securetoken':'196b57c0-c730-404c-9326-a53fe2ebc1e0'}                            
                            return JsonResponse(data)
                     except:
                            c_inst=None
                            data={'token':'Token : Not Genrated'}
                            return JsonResponse(data)
                           

              client=Client.objects.filter(user_id=request.user.id)
              return render(request,'clients/genrate_client_token.html',{'clients':client})
       else:
              return redirect('/')

#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_consignee(request):

       if request.user.is_authenticated:
              client=Client.objects.filter(user_id=request.user.id)             
              state=Consignee.objects.order_by('state').values('state').distinct()
              station = Consignee.objects.order_by('station').values('station').distinct()
              trns = Consignee.objects.order_by('transport').values('transport').distinct()
              user_client_name=None
              if request.user.is_user:
                     user_client=Client.objects.only('user_id').get(user_id=request.user.id)
                     user_client_name=user_client.client_name
              Con=False
              if request.method == 'POST':
                     cli_id=Client.objects.get(client_name=request.POST.get('client_id'))                                       
                     cli=Consignee.objects.filter(client_id=cli_id.id)
                     con_name= request.POST.get('consignee_name')
                     for cl in cli:                            
                            in_con=cl.consignee_name                                              
                            if in_con == con_name :                                                              
                                  Con=True
                                  messages.error(request,'Consignee already exists.')
                                  return render(request,'clients/add_consignee.html/',{'clients':client,'state':state ,'stations':station,'transports':trns})
                           
                     if Con == False:
                                   client_id=Client.objects.only('id').get(id=cli_id.id)                        
                                   con_station=request.POST.get('station')
                                   con_transport=request.POST.get('transport')
                                   con=Consignee(client_id=client_id,consignee_name=con_name,station=con_station,transport=con_transport)
                                   con.full_clean()
                                   con.save()
                                   messages.success(request,'Consignee add success')      
                                   return render(request,'clients/add_consignee.html/',{'clients':client,'state':state ,'stations':station,'transports':trns})
                           

              return render(request,'clients/add_consignee.html/',{'clients':client,'user_client_name':user_client_name,'state':state ,'stations':station,'transports':trns})
       else:
              return redirect('/')