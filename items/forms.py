from select import select
from tkinter.ttk import Style
from django import forms
from .models import Item_Group,Item,Unit

class itemGroupForm(forms.ModelForm):   
    class Meta:
        model=Item_Group
        fields=['group_name',]

class itemsForm(forms.ModelForm):
 
    item_group=forms.ModelChoiceField(label='Item Group',queryset=Item_Group.objects.all(),widget=forms.Select(attrs={'class':'inputstyle', 'style':'text-transform:capitalize;'}))
    item_name=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle','text-transform':'capitalize'}))
    item_unit=forms.ModelChoiceField(label='Item Unit',queryset=Unit.objects.all(),widget=forms.Select(attrs={'class':'inputstyle', 'style':'text-transform:capitalize;'}))    
    hsn_sac=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle','text-transform':'capitalize'}))
    comment=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle','text-transform':'capitalize'}))
    
    class Meta:
        model=Item
        fields='__all__'

class unitForm(forms.ModelForm):
    class Meta:
        model=Unit
        fields=['unit_name',]


class initems(unitForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle','text-transform':'capitalize'}))

    class Meta(unitForm.Meta):

        fields='__all__'
       