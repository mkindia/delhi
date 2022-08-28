from django import forms
from django.contrib.auth import models
from django.core.validators import RegexValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.forms import (
   PasswordChangeForm, 
   UserCreationForm, 
   UserChangeForm ,
    AuthenticationForm,SetPasswordForm )


from .models import *

from django.core.exceptions import ValidationError

class UserProfile_imgform(forms.ModelForm):
  user_img=forms.ImageField(label='',widget=forms.FileInput(attrs={'class':'inputstyle'}))
  class Meta:
    model=Custom_User
    fields=['user_img',]
    
class UserProfile_changeform(forms.ModelForm):
                                         
  email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'inputstyle'}))
  first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle','text-transform':'capitalize'}))
  last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle'})) 
 
  class Meta:
    model = Custom_User
    fields = ['first_name','last_name','email']
   
class UserDetailsform(forms.ModelForm):
  class Meta:
    model = Custom_User
    fields = '__all__'

class UserSetPasswordForm(SetPasswordForm):
  new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'inputstyle'}))
  new_password2=forms.CharField(label='ReEnter Password',widget=forms.PasswordInput(attrs={'class':'inputstyle'})) 
  class Meta:
    fields = ('new_password1','new_password2')

class ChangePasswordForm(PasswordChangeForm):
  old_password=forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={'class':'inputstyle'}))
  new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'inputstyle'}))
  new_password2=forms.CharField(label='ReRnter Password',widget=forms.PasswordInput(attrs={'class':'inputstyle'}))
 
  class Meta:
    model = Custom_User
    fields = ('old_password','new_password1', 'new_password2')  
    

class UsersCreationForm(UserCreationForm):
  username_validator = UnicodeUsernameValidator()
  password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'inputstyle'}))
  password2=forms.CharField(label='ReEnter Password',widget=forms.PasswordInput(attrs={'class':'inputstyle'}))
  user_name = forms.CharField(label='username', max_length=150,widget=forms.TextInput(attrs={'class':'inputstyle'}),      
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={'unique': "A user with that username already exists.",
        })
  email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'inputstyle'}))
  first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle','text-transform':'capitalize'}))
  last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle'})) 
  phone_number=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'inputstyle', 'type':"tel", 'pattern':'[7-9]{1}[0-9]{9}','placeHolder':'10 digit mobile no.'}))  
  class Meta:
    model =  Custom_User
    fields = ('user_name','email','first_name','last_name','phone_number')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

  

class UsersChangeForm(UserChangeForm):

  class Meta:
    model = Custom_User
    fields = ('email','first_name', 'last_name')

class Userauthform(AuthenticationForm):
  username=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle'}))
  password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'inputstyle'}))  
  class Meta:
    model=Custom_User
    fields=('first_name')
