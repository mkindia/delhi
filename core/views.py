from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views.decorators.cache import cache_control
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.conf.urls.static import static

import uuid
import json
from .forms import *
from .models import *
from items.models import Item,Item_Variant,Unit
from clients.models import Client, Client_Token,Consignee
import os

# for sending mail
def mail_for_verify_user(subject,message,email,url,token):

       subject = subject

       if url != None :
              message = f'{message} http://127.0.0.1:8000/{url}/{token}/'

       else :
              message = f''+message

       
       from_email = settings.EMAIL_HOST_USER
       recipient_list = [email]
       send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):                          
       if not request.user.is_authenticated:            
              return render(request,'core/home.html',{'user_name':'Login'})
       else:
              
              clients=Client.objects.filter(user_id=request.user)
              consignes = Consignee.objects.filter(client_id__in=clients)             
              if request.user.is_user:
                     user_client=Client.objects.get(user_id=request.user)
                     client_name = user_client.client_name
                     client_id = user_client.id
              item_arry =[]
              item_variants_arry = []
              unit_arry =[]            
              for i in Item.objects.all():                     
                     item_arry.append({'item_id':i.id,'item_name':i.item_name})
              items=json.dumps(item_arry)
              for iv in Item_Variant.objects.all():
                     item_variants_arry.append({'variant_id':iv.id,'variant_name':iv.variant_name})
              item_variants =json.dumps(item_variants_arry)
              for u in Unit.objects.all():
                     unit_arry.append({'unit_id':u.id,'unit_name':u.unit_name})        
              unit=json.dumps(unit_arry)
              
              admin_context ={'client':clients,
                            'consigne':consignes,
                            'items':items,
                            'item_variants':item_variants,
                            'unit':unit,
                            'orders':'Pandan/2 @120/Pcs.%0asinhasn 2no. : 150 Pcs. @320/Kg.'}
              
              if request.user.is_admin :                    
                     return render(request,'clients/admin_dashboard.html',admin_context)
              if request.user.is_staff :                    
                     return render(request,'core/staff_dashboard.html',{'client':clients})
              else  :                     
                     return render(request,'clients/client_dashboard.html',{'client_id':client_id,'client_name':client_name})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup(request): 
    fm=UsersCreationForm
    if request.method == "POST":           
           fm = UsersCreationForm(request.POST)
           if fm.is_valid():                     
                     try:
                            c=request.POST.get('token')
                            uv=Client_Token.objects.get(token=c)
                            if(uv.is_verified):
                                   messages.error(request,'User Allready Created for this Token')
                            else:
                                   uv.is_verified=True
                                   uv.save()
                                   cid=Client.objects.get(id = uv.client_id_id)
                                   nu=fm.save()
                                   cid.user_id.add(nu)
                                   token=uuid.uuid4()
                                   ver_obj=User_Verification(user_id=nu,client_id=uv.client_id_id,email=nu.email,token=token)
                                   ver_obj.save()         
                                   mail_for_verify_user('Verify Your account','Hi Click on Link To Verify Your Account',nu.email,'account_verify',token)
                                   messages.success(request,'Account Verify mail Sent to'+' '+ nu.email)  
                                   request.session.flush()
                                   request.session.clear_expired()
                                   return redirect('/')
                     except:
                                   uv=None
                                   messages.error(request,'Invalid Token')                     
                                   
               
           
          
    return render(request,'core/signup.html',{'fm':fm})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signin(request):
        fm=Userauthform    
        if not request.user.is_authenticated:
               if request.method == 'POST':
                      fm = Userauthform(request=request, data=request.POST)
                      if fm.is_valid():
                             uname = fm.cleaned_data['username']
                             upass = fm.cleaned_data['password']
                             #print(uname)
                             vuser = authenticate(username=uname, password=upass)
                             if vuser is not None:
                                 login(request, vuser)
                                 request.session['accesskey'] = 'accesskey'
                                 messages.success(request,'Wellcome ' +'[ '+ request.user.first_name + ' ' + request.user.last_name + ' ]')
                                 """
                                 if request.user.is_admin:                                        
                                        return redirect('/')
                                 elif request.user.is_staff:
                                        return redirect('/')
                                # messages.success(request,suer)
                                 else:                                                                      
                                    return redirect('/')                                  
                                   """
                                 return redirect('/')
                             else:
                                    return redirect('/')
                      else: 
                             messages.success(request,"Invalid username or password.")
                             return redirect('/')            
               else:
                     
                      return render(request,'core/signin.html',{'fm':fm})
                         
        else:
               
               return redirect('/')
            
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_logout(request):
    logout(request)
    request.session.flush()
    request.session.clear_expired()
    return redirect('/')
                                                                                  
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def account_verify(request,token):      
       af=User_Verification.objects.filter(token=token).first()
       if af != None:
              if af.token == token and af.is_verified == False :
                     cu=Custom_User.objects.filter(email=af.email).first()
                     if cu != None :
                            af.is_verified=True
                            af.date_varified = timezone.now()
                            cu.is_user=True 
                            cu.is_active=True
                            af.save()
                            cu.save()
                            messages.success(request,"Account Verified Success Please Login "+'[ '+ str(af.email) + ' ]')           
                            return redirect('/')
              else :
                     
                     return redirect('/errorpage/pagexpire')
       else :
              
              return redirect('/errorpage/pagexpire')

def pass_change(request,token):
       af=Password_Change.objects.filter(token=token).first()
       if af != None:
              if af.token == token and af.is_changed == False :
                     if request.method == 'POST': 
                            fm=UserSetPasswordForm(data=request.POST, user=af.user_id)
                            if fm.is_valid():                                  
                                   af.is_changed = True
                                   af.date_changed = timezone.now()
                                   af.save()
                                   fm.save()                                  
                                   messages.info(request,"You Can Login Using New Password")
                                   return redirect('/')
                            else:
                                   return render(request,'core/set_pass.html',{'fm':fm,'header':'Set Password'})
                     else:
                             fm=UserSetPasswordForm(user=af.user_id)
                             return render(request,'core/set_pass.html',{'fm':fm,'header':'Set Password'})
              else :
                     return redirect('/errorpage/Pagexpired/')       
       else :
              return redirect('/errorpage/Pagexpired/')       

def profile_change(request,mode):
       if not request.user.is_authenticated:
              return redirect('/')
       else:             
              pk = Custom_User.objects.get(pk=request.user.id)
              if mode=='details':
                     fm=UserProfile_changeform(instance=pk)
              if mode == 'img':
                     fm=UserProfile_imgform()

              if mode =='delimg':
                            fm=UserProfile_imgform(request.POST,request.FILES,instance=pk)
                            if pk.user_img != '' and pk.user_img != None :                                   
                                   os.remove(pk.user_img.path)
                                   pk.user_img=None
                                   pk.save()
                                   return redirect('/')       

              if request.method == 'POST':                    

                     if mode == 'img':
                            fm=UserProfile_imgform(request.POST,request.FILES,instance=pk)
                            if pk.user_img != '' and pk.user_img != None :                                   
                                   os.remove(pk.user_img.path)
                                   if fm.is_valid():                                   
                                          fm.save()
                                          messages.success(request,f"Profile Image Success")
                                          return redirect('/')                                        
                                   else:
                                          messages.success(request,f"Profile Update not Success")
                                          return render(request,'core/edit_profile.html',{'fm':fm,'header':'Set Profile','mode':mode})
                            else:      
                                   if fm.is_valid():                                   
                                          fm.save()
                                          messages.success(request,f"Profile Update Success")
                                          return redirect('/')                                      
                                   else:
                                          messages.success(request,f"Profile Update not Success")
                                          return render(request,'core/edit_profile.html',{'fm':fm,'header':'Set Profile','mode':mode})
                            
                     if mode == 'details':
                            fm = UserProfile_changeform(instance=pk,data=request.POST)

                            if fm.is_valid():
                                   fm.save()
                                   messages.success(request,f"Profile Update Success")
                                   return redirect('/')                                               
                            else:
                                   messages.success(request,f"Profile Update not Success")
                                   return render(request,'core/edit_profile.html',{'fm':fm,'header':'Set Profile','mode':mode})
                             
              return render(request,'core/edit_profile.html',{'fm':fm,'header':'Set Profile','mode':mode})       


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def forget_pwd(request):

       if request.method == 'POST':
              uname=request.POST.get('username')
              
              getuser = Custom_User.objects.filter(user_name=uname)
              if getuser.exists():
                            for udetail in getuser:
                                   uemail=udetail.email
                                   uid=udetail.id
                                   uverify=udetail.is_active
                            if not uverify:
                                   messages.info(request,'User Not Verified Please Check mail')
                                   return render(request,'core/forget_pwd.html',{'header':'Forget Password'})
                                          
              else:                     
                     messages.info(request,'User Not Found')
                     return render(request,'core/forget_pwd.html',{'header':'Forget Password'})
             
                     
                  
              token = uuid.uuid4()
              lastrequest=Password_Change.objects.filter(user_id=uid).last()
              if lastrequest != None:                            
                     if lastrequest.is_changed == False  :                            
                            messages.info(request,"Please check your registered Email ")
                            mail_for_verify_user('Recover Your Password','Please click on link to new password',uemail,'pass_change',lastrequest.token)
                            return redirect('/')
                     else : 
                            cu_id = Custom_User.objects.only('id').get(user_name=uname)                                 
                            ver_obj=Password_Change(user_id=cu_id,email=uemail,token=token)                     
                            ver_obj.save()  
                            mail_for_verify_user('Recover Your Password','Please click on link to new password',uemail,'pass_change',token)                     
                            messages.info(request,"Please check your registered Email ")
                            return redirect('/')
              else: 
                     cu_id = Custom_User.objects.only('id').get(user_name=uname)
                     ver_obj=Password_Change(user_id=cu_id,email=uemail,token=token)                     
                     ver_obj.save()
                     mail_for_verify_user('Recover Your Password',uemail,'pass_change','Please click on link to new password',token)                    
                     messages.info(request,"Please check your registered Email ")                    
                     return redirect('/')
              
       else:
              return render(request,'core/forget_pwd.html',{'header':'Forget Password'})

def forget_uname(request):
       if request.method == 'POST':
              email=request.POST.get('email')
              getuser = Custom_User.objects.filter(email=email)
              if getuser.exists():
                     for udetails in getuser:
                            uname=udetails.user_name
                            uemail=udetails.email
              else:
                     messages.info(request,'Regestered email not found')
                     return render(request,'core/forget_uname.html',{'header':'Forget Username'})

              token = uuid.uuid4()
              mail_for_verify_user('your User name','your User Name Is :- '+uname,email,None,token)                     
              messages.info(request,"Please check your registered mail " + uemail)
              return redirect('/')
       else :
              return render(request,'core/forget_uname.html',{'header':'Forget Username'})
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def change_pass(request):     
       
       if request.user.is_authenticated:
              if request.method == 'POST':
                     fm=ChangePasswordForm(data=request.POST, user=request.user)
                     if fm.is_valid():                            
                            fm.save()
                            update_session_auth_hash(request,fm.user)      
                            return redirect('/')
                     else:
                            fm = ChangePasswordForm(request.user)              
                            return render(request,'core/change_pass.html',{'fm':fm,'header':'Change Password'})

              else:
                     fm = ChangePasswordForm(request.user)              
                     return render(request,'core/change_pass.html',{'fm':fm,'header':'Change Password'})
       else:
                     
              return render(request,'errorpage.html',{'type':'Page Not Found'})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def errorpage(request,errortype):
       return render(request,'error/errorpage.html',{'type':errortype})
