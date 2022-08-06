from email.policy import default
from django.db import models


from clients.models import Client,Consignee
from items.models import Item,Unit,Item_Variant

# Create your models here.
class LowerCase(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LowerCase, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class Consignee_Order(models.Model):
    order_type=[('order','order'),
                ('purchase','purchase'),
                ('transferred','transferred')]
    client_id=models.ForeignKey(Client,on_delete=models.CASCADE)
    consignee_id = models.ForeignKey(Consignee,on_delete=models.CASCADE)
    order_type = LowerCase(max_length=30,blank=True, null=True, choices=order_type,default='order')
    create_date=models.DateField(auto_now_add=True,null=True,blank=True)    
    date = models.DateField(null=True,blank=True)
    Item_Order_Status_id=models.PositiveIntegerField(null=True,blank=True)
    comment =LowerCase(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.pk)
   
class Item_Order(models.Model):
    order_type=[('order','order'),
                ('purchase','purchase'),
                ('transferred','transferred')] 
    client_id=models.ForeignKey(Client,on_delete=models.CASCADE)
    consignee_id=models.ForeignKey(Consignee,on_delete=models.CASCADE)
    date = models.DateField()
   # order_id = models.ForeignKey(Consignee_Order,on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item,on_delete=models.PROTECT)   
    item_variant_id = models.ForeignKey(Item_Variant,on_delete=models.PROTECT)   
    item_veriant_price = models.DecimalField(default=1.1,max_digits=7,decimal_places=2)
    price_per_unit_id = models.ForeignKey(Unit,related_name='per_unit',on_delete=models.PROTECT)  
    item_qty = models.DecimalField(default=0,max_digits=7,decimal_places=1)
    order_unit_id = models.ForeignKey(Unit,related_name='order_unit',on_delete=models.PROTECT)
    order_type = LowerCase(max_length=30,blank=True, null=True, choices=order_type,default='order')
    create_date=models.DateField(auto_now_add=True,null=True,blank=True)
    comment = LowerCase(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.pk)
   

class Item_Order_Status(models.Model):
    order_status=[('cancelled','cancelled'),
                ('dispatched','dispatched'),
                ('transferred','transferred'),]

    client_id=models.ForeignKey(Client,on_delete=models.CASCADE)
    consignee_id=models.ForeignKey(Consignee,related_name='consignee_id',on_delete=models.CASCADE)
    #order_id = models.ForeignKey(Consignee_Order,on_delete=models.CASCADE) 
    item_order_id = models.ForeignKey(Item_Order,on_delete=models.CASCADE)
    transfer_id = models.ForeignKey(Consignee,related_name='tranfer_id', on_delete=models.CASCADE,blank=True,null=True)     
    date=models.DateField()   
    item_qty = models.DecimalField(default=0,max_digits=7,decimal_places=1)
    create_date=models.DateField(auto_now_add=True,null=True,blank=True)
    status = LowerCase(max_length=30,blank=True, null=True, choices=order_status,default='dispatched')
    docket_number = LowerCase(max_length=50,blank=True,null=True)
    comment = LowerCase(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.pk)

class Item_Order_Transfer(models.Model):
    client_id=models.ForeignKey(Client,on_delete=models.CASCADE)
    consignee_id=models.ForeignKey(Consignee,on_delete=models.CASCADE)
    #order_id = models.ForeignKey(Consignee_Order,on_delete=models.CASCADE)
    item_order_id = models.ForeignKey(Item_Order,on_delete=models.CASCADE)
    status_id = models.ForeignKey(Item_Order_Status,on_delete=models.CASCADE)
    date=models.DateField()
    item_id = models.ForeignKey(Item,on_delete=models.PROTECT)   
    item_variant_id = models.ForeignKey(Item_Variant,on_delete=models.PROTECT)   
    item_veriant_price = models.DecimalField(default=1.1,max_digits=7,decimal_places=2)
    price_per_unit = models.ForeignKey(Unit,related_name='Item_Order_Transfer_per_unit',on_delete=models.PROTECT)     
    item_qty = models.DecimalField(default=0,max_digits=7,decimal_places=1)
    order_unit = models.ForeignKey(Unit,related_name='Item_Order_Transfer_order_unit',on_delete=models.PROTECT)
    create_date=models.DateField(auto_now_add=True,null=True,blank=True)
    comment = LowerCase(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.pk)