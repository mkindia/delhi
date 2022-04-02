from email.policy import default
from enum import unique
from http import client
from xml.parsers.expat import model
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from core.models import Custom_User

# Create your models here.

class LowerCase(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LowerCase, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class Client_Group(models.Model):
    group_name = LowerCase(max_length=100)    
    group_des = models.CharField(max_length=150,blank=True,null=True)
    def __str__(self):
        return str (self.group_name)

class Client(models.Model) :
    user_id = models.ManyToManyField(Custom_User)
    client = LowerCase(max_length=100, unique=True)
    client_group = models.ForeignKey(Client_Group,on_delete=models.SET_NULL,null=True,blank=True)
    business_name = models.CharField(max_length=150,blank=True, null=True)
    address_1 = models.CharField("address line1", max_length=128, blank=True, null=True)
    address_2 = models.CharField("address line2", max_length=128, blank=True, null=True)
    address_3 = models.CharField("address line3", max_length=128, blank=True, null=True)
    address_4 = models.CharField("address line4", max_length=128, blank=True, null=True)
    city = LowerCase("city", max_length=64, default="delhi", blank=True, null=True)
    state = LowerCase("state", max_length=64, default="delhi", blank=True, null=True)
    zipcode = models.CharField("zipcode", max_length=10, default="", blank=True, null=True)
    email=models.EmailField(blank=True, null=True, verbose_name='email address',max_length=255,unique=True)   
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{9,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], null=True, blank=True,  max_length = 16, unique = True)    
    client_des = models.CharField(max_length=150,blank=True,null=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True ,null=True)
    def __str__(self):
        return str (self.client )

class Transport(models.Model):
    transport_name = LowerCase(max_length=100)
    transport_code = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=300,blank=True,null=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{9,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], null=True, blank=True,  max_length = 16, unique = True)    
    def __str__(self):
        return self.transport_name

class State(models.Model):
    country_name =LowerCase(max_length=100,default='india',blank=True, null=True)
    state_name=LowerCase(max_length=100)
    def __str__(self):
        return self.state_name

class Station(models.Model):
    state_name = models.ForeignKey(State, on_delete=models.CASCADE)
    station_name = LowerCase("station", max_length=100,blank=True, null=True)
    def __str__(self):
        return self.station_name

class Consignee(models.Model):
    client_id = models.ForeignKey(Client,on_delete=models.CASCADE)
    consignee_name = LowerCase(max_length=150, unique=True ,
    error_messages={
            'unique': "A consignee already exists.",
        },)
    station=models.ForeignKey(Station,on_delete=models.CASCADE)
    transport=models.ForeignKey(Transport,on_delete=models.CASCADE)            
    private_marka = models.CharField(max_length=100,null=True,blank=True)
    is_client = models.BooleanField(default=False) 
    
    def __str__(self):
        return self.consignee_name

