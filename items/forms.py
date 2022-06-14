from django import forms
from .models import Item_Group,Item,Unit

class itemGroupForm(forms.ModelForm):   
    class Meta:
        model=Item_Group
        fields=['group_name',]

class unitForm(forms.ModelForm):
    class Meta:
        model=Unit
        fields=['unit_name',]


class initems(unitForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle','text-transform':'capitalize'}))

    class Meta(unitForm.Meta):

        fields='__all__'
       