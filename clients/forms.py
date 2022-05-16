from django import forms

from .models import Client_Group,Client,Client_Token,Consignee,Transport,Station

class Client_Form(forms.ModelForm):
    client=forms.CharField(label='Client Name',widget=forms.TextInput(attrs={'class':'inputstyle', 'style':'text-transform:capitalize;'}))
    client_group=forms.ModelChoiceField(queryset=Client_Group.objects.all(),widget=forms.Select(attrs={'class':'inputstyle','style':'text-transform:capitalize;'}))

    class Meta:        
        model = Client
        fields = ['client_name','client_group']

        #widgets ={'client_group':forms.Select(attrs={'class':'inputstyle','text-transform':'capitalize'})}

class Consignee_form(forms.ModelForm):
    consignee_name=forms.CharField(label='Consignee Name',widget=forms.TextInput(attrs={'class':'inputstyle', 'style':'text-transform:capitalize;'}))
    client_id=forms.ModelChoiceField(label='Client',queryset=Client.objects.all(),widget=forms.Select(attrs={'class':'inputstyle', 'style':'text-transform:capitalize;'}))
    transport=forms.ModelChoiceField(queryset=Transport.objects.all(),widget=forms.Select(attrs={'class':'inputstyle', 'style':'text-transform:capitalize;'}))
    station=forms.ModelChoiceField(queryset=Station.objects.all(),widget=forms.Select(attrs={'class':'inputstyle', 'style':'text-transform:capitalize;'}))

    class Meta:
        model = Consignee
        fields = ['client_id','consignee_name','transport','station']

class Transport_Form(forms.ModelForm):
    class Meta:
        model = Transport
        fields = '__all__'

class Consignee_Transport_form(forms.ModelForm):
    transport=forms.ModelChoiceField(queryset=Transport.objects.all(),widget=forms.Select(attrs={'class':'inputstyle', 'style':'text-transform:capitalize;'}))
    station=forms.ModelChoiceField(queryset=Station.objects.all(),widget=forms.Select(attrs={'class':'inputstyle', 'style':'text-transform:capitalize;'}))

    class Meta:
        model = Consignee
        fields = ['transport','station']

