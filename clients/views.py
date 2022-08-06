
from django.shortcuts import redirect, render
from django.http import JsonResponse 
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.cache import cache_control
from django.contrib import messages

import json
import uuid
from .models import Client, Client_Token,Consignee


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
              """     
              if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                     if request.method == 'POST':
                            data = json.loads(request.body.decode("utf-8"))
                            c_name = data['c_name']
                            g_name = data['g_name']
                            s_name = data['s_name']
                            t_name = data['t_name']
                            m_no = data['m_no']
                            email = data['email']
                            clientsall=[]
                            for cli in Client.objects.all():
                                          clientsall.append({'id':cli.id,'name':cli.client_name})
                            try:
                                   cli_name=Client.objects.get(client_name=c_name.lower())                            
                                   msg = 'Client All ready exist ' + '[ ' +cli_name.client_name+ ' ]'
                                   if cli_name.phone_number == m_no:
                                          msg = 'phone allready exist'
                                   if cli_name.email == email :
                                          msg = 'email allready exist'                        
                                   data = {'message':msg,'clients':clientsall}
                                   return JsonResponse(data)
                            except:                                               
                                   cli_name=None
                                   try:   
                                          ph=Client.objects.get(phone_number=m_no)
                                          msg = 'phone allready exist'
                                          data = {'message':msg,'clients':clientsall}
                                          return JsonResponse(data)
                                   except:
                                          client_ob=Client.objects.create(client_name=c_name,client_group=g_name,phone_number=m_no,email=email)
                                          consignee_ob=Consignee.objects.create(client_id=client_ob,consignee_name=c_name,transport=t_name,station=s_name,is_client=True)  
                                          client_ob.user_id.add(request.user.id)
                                          superuser=Custom_User.objects.get(is_staff=True)
                                          client_ob.user_id.add(superuser.id)                                                
                                          msg='Client Creation Success'
                                          data={'message':msg,'clients':clientsall}
                                          return JsonResponse(data)
                     
              
              """
              state=Consignee.objects.order_by('state').values('state').distinct()
              station = Consignee.objects.order_by('station').values('station').distinct()
              transport = Consignee.objects.order_by('transport').values('transport').distinct()
              return render(request,'clients/add_client.html/',{'state':state,'transport':transport,'station':station})

       else :
              return redirect('/')

#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def genrate_client_token(request):
       if request.user.is_authenticated:

                            
              if request.method == 'POST':
                     client=request.POST.get('client')
                     try:
                            c_f= Client_Token.objects.get(client_name=client)
                            messages.warning(request,'Client Has Already Token '+'[ '+ c_f.token +' ]')
                     except:
                            c_f=None
                            c_inst= Client.objects.only('client_name').get(client_name=client)                                               
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
              return render(request,'clients/add_consignee.html/',{'clients':client,'stations':station,'transports':trns})
       else:
              return redirect('/')