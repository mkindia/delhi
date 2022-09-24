from asyncio.windows_events import NULL
from email.policy import default
from django.db import models


from clients.models import Client,Consignee
from items.models import Item,Item_Variant

# Create your models here.
class LowerCase(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LowerCase, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class Consignee_Order(models.Model):    
    client_id=models.ForeignKey(Client,on_delete=models.CASCADE)
    consignee_id = models.ForeignKey(Consignee,on_delete=models.CASCADE)
    order_type = LowerCase(max_length=30,blank=True, null=True,default='or')
    create_date=models.DateField(auto_now_add=True,null=True,blank=True)    
    date = models.DateField(null=True,blank=True)
    Item_Order_Status_id=models.PositiveIntegerField(null=True,blank=True)
    comment =LowerCase(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.pk)
   
class Item_Order(models.Model):   
    client_id = models.ForeignKey(Client,on_delete=models.CASCADE)
    consignee_id = models.ForeignKey(Consignee,on_delete=models.CASCADE)
    client_group = LowerCase(max_length=10,default='d')
    order_date = models.DateField()  
    item_id = models.ForeignKey(Item,on_delete=models.PROTECT)   
    item_variant_id = models.ForeignKey(Item_Variant,on_delete=models.PROTECT)   
    item_veriant_price = models.DecimalField(default=1.1,max_digits=7,decimal_places=2)
    price_per_unit = LowerCase(max_length=30,blank=True, null=True,default='kg') 
    item_qty = models.DecimalField(default=0,max_digits=7,decimal_places=1)
    packing_type = LowerCase(max_length=30,blank=True, null=True,default='cr')
    order_type = LowerCase(max_length=30,blank=True, null=True,default='or')
    item_order_status_id = models.PositiveBigIntegerField(blank=True,null=True,default=NULL)
    create_date = models.DateField(auto_now_add=True,null=True,blank=True)
    comment = LowerCase(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.pk)
   

class Item_Order_Status(models.Model):    
    client_id = models.ForeignKey(Client,on_delete=models.CASCADE)
    consignee_id = models.ForeignKey(Consignee,related_name='consignee_id',on_delete=models.CASCADE)   
    item_order_id = models.ForeignKey(Item_Order,on_delete=models.CASCADE)
    transfer_id = models.ForeignKey(Consignee,related_name='tranfer_id', on_delete=models.CASCADE,blank=True,null=True)     
    date=models.DateField()   
    item_qty = models.DecimalField(default=0,max_digits=7,decimal_places=1)
    create_date = models.DateField(auto_now_add=True,null=True,blank=True)
    status = LowerCase(max_length=30,blank=True, null=True,default='dis')
    item_order_trn_id = models.PositiveBigIntegerField(blank=True,null=True,default=NULL)  
    docket_number = LowerCase(max_length=50,blank=True,null=True)
    state = LowerCase('state',max_length=64, blank=True, null=True)
    station = LowerCase('station',max_length=64,null=True,blank=True)
    transport = LowerCase('transport',max_length=64,null=True,blank=True)
    private_marka = models.CharField(max_length=100,null=True,blank=True)
    comment = LowerCase(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.pk)

