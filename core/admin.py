from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


from core.models import Custom_User,Password_Change
 

#from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

class UsersCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Custom_User
        fields = ('user_name',)

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


class UsersChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Custom_User
        fields = ('email', 'password', 'is_active', 'is_staff', 'is_user')



class UsersAdmin(BaseUserAdmin):
    form = UsersChangeForm
    add_form = UsersCreationForm   
    list_display = ('user_name','email', 'first_name', 'last_name', 'is_admin','is_staff','is_user','is_active','date_joined')
    list_filter = ('user_name',)
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info',{'fields':('user_img','first_name','last_name',)}),
        ('Permissions', {'fields': ('is_admin','is_staff', 'is_active', 'is_user')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name','email', 'first_name' , 'last_name' , 'password1', 'password2', 'is_admin','is_staff', 'is_active')}
        ),
    )
    search_fields = ('user_name',)
    ordering = ('user_name',)
    filter_horizontal = ()


admin.site.register(Custom_User, UsersAdmin)
admin.site.unregister(Group) 
    
@admin.register(Password_Change)
class PasswordChange(admin.ModelAdmin):
    list_display = ('user_id','email','token','is_changed','date_changed')

@admin.register(Permissions)
class Permissions(admin.ModelAdmin):
    list_display =('permission_name',)

@admin.register(User_Permissions)
class User_Permissions(admin.ModelAdmin):
    list_display =('user',)

@admin.register(User_Verification)
class UserVerifyAddmin(admin.ModelAdmin):
    list_display =('user_id', 'client_id','email','token','is_verified', 'date_varified')