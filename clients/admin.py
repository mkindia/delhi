from dataclasses import fields
from django.contrib import admin
from clients.models import *

# Register your models here.
@admin.register(Client)
class Client(admin.ModelAdmin):
      list_display = ('id','client')

@admin.register(Client_Group)
class Client_Group(admin.ModelAdmin):
      list_display=('group_name',)

@admin.register(Transport)
class Transport(admin.ModelAdmin):
      list_display=('transport_name',)


@admin.register(Consignee)
class Consignee(admin.ModelAdmin):
      list_display =('consignee_name', 'client_id','station','transport','is_client')

