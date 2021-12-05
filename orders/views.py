from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.http import JsonResponse
import json
from .forms import *
from .models import *

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
       if not request.user.is_authenticated:
              return render(request,'core/home.html',{'user_name':'Login'})
       else:
              user_full_name=request.user.first_name + " " + request.user.last_name
              return render(request,'core/home.html',{'user_name':user_full_name})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup(request):
    fm=CustomUserCreationForm
    if request.method == "POST":           
           fm = CustomUserCreationForm(request.POST)
           if fm.is_valid():
                 # data= json.loads(request.body)                
                 # print(data.get('post_id1'))
                  fm.save()
                  request.session.flush()
                  request.session.clear_expired()
                  return redirect('/')
           else:
                  
                  return render(request,'core/signup.html',{'fm':fm})
    if request.method == "PUT":
           data= json.loads(request.body)              
           print(data.get('post_id'))
           fm=CustomUserCreationForm
          
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
                             vuser = authenticate(username=uname, password=upass)
                             if vuser is not None:
                                 login(request, vuser)
                                 request.session['accesskey'] = 'accesskey'
                                 superuser=request.user.is_superuser
                                # messages.success(request,suer)
                                 if superuser :
                                        print(request.user.first_name)
                                                                
                                 return redirect('/')
                             else:
                                    
                                    return redirect('/')
                      else: 
                             messages.success(request,"Invalid username or password.")
                             return redirect('/')            
               else:
                     
                      return render(request,'core/signin.html',{'fm':fm})
                         
        else:
               request.session.flush()
               request.session.clear_expired()
               return render(request,'core/signin.html',{'fm':fm})
               #return redirect('/')
        #return redirect('/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_logout(request):
    logout(request)
    request.session.flush()
    request.session.clear_expired()
    return redirect('/')
