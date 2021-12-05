
from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm , AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):  
  password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'inputstyle'}))
  password2=forms.CharField(label='ReEnter Password',widget=forms.PasswordInput(attrs={'class':'inputstyle'}))
  email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'inputstyle'}))
  first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle','text-transform':'capitalize'}))
  last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle'})) 

  class Meta:
    model = CustomUser
    fields = ('email','first_name','last_name')  

  

class CustomUserChangeForm(UserChangeForm):

  class Meta:
    model = CustomUser
    fields = ('email','first_name', 'last_name')

class Userauthform(AuthenticationForm):
  username=forms.CharField(label='Email',widget=forms.TextInput(attrs={'class':'inputstyle'}))
  password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'inputstyle'}))
  class Meta:
    model=CustomUser
    fields=('first_name')
   


   

"""class UserAdminCreationForm(forms.ModelForm):
        password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'inputstyle'}))
        password2=forms.CharField(label='ReEnter Password',widget=forms.PasswordInput(attrs={'class':'inputstyle'}))
        email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'inputstyle'}))
        class Meta:
          model = User        
          fields = ('email',)

        def clean_password2(self):
          password1=self.clean.data.get("password1")
          password2=self.clean.data.get("password2")
          if password1 and password2 and password1 != password2:
            raise forms.ValidationError("password don't match")
          return password2

        def save(self,commit=True):
          user=super(UserCreationForm,self).save(commit=False)
          user.set_password(self.cleaned_data["password1"])
          if commit:
            user.save()
          return user  

         
          
class UserAdminChangeForm(forms.ModelForm):
  password = ReadOnlyPasswordHashField()
  class Meta:
    model=User
    fields=('email','password','active','admin')

  def clean_password(self):
    return self.initial["password"]   
class userloginform(AuthenticationForm):
           
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'inputstyle'}))   """     
        
