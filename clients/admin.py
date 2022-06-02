from dataclasses import fields
from django.contrib import admin
from clients.models import *

# Register your models here.
@admin.register(Client)
class Client(admin.ModelAdmin):
      list_display = ('id','client_name')


@admin.register(Transport)
class Transport(admin.ModelAdmin):
      list_display=('transport_name',)

@admin.register(State)
class State(admin.ModelAdmin):
      list_display=('country_name','state_name',)

@admin.register(Station)
class Station(admin.ModelAdmin):
      list_display=('state_name','station_name',)



@admin.register(Consignee)
class Consignee(admin.ModelAdmin):
      list_display =('consignee_name', 'client_id','station','transport','is_client')

@admin.register(Client_Token)
class Consignee(admin.ModelAdmin):
      list_display =('client_id','token','is_verified')