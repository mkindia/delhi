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
    order_type=[('sales','sales'),
                ('purchase','purchase'),]

    client_id=models.ForeignKey(Client,on_delete=models.CASCADE)
    consignee_id = models.ForeignKey(Consignee,on_delete=models.CASCADE)
    order_type = LowerCase(max_length=30,blank=True, null=True, choices=order_type,default='sales')
    create_date=models.DateField(auto_now_add=True,null=True,blank=True)    
    date = models.DateField(null=True,blank=True)
    comment =LowerCase(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.pk)
   
class Item_Order(models.Model):   
    client_id=models.ForeignKey(Client,on_delete=models.CASCADE)
    consignee_id=models.ForeignKey(Consignee,on_delete=models.CASCADE)
    order_id = models.ForeignKey(Consignee_Order,on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item,on_delete=models.PROTECT)   
    item_variant_id = models.ForeignKey(Item_Variant,on_delete=models.PROTECT)   
    item_veriant_price = models.DecimalField(default=1.1,max_digits=7,decimal_places=2)
    price_per_unit = models.ForeignKey(Unit,related_name='per_unit',on_delete=models.PROTECT)  
    item_qty = models.DecimalField(default=0,max_digits=7,decimal_places=3)
    order_unit = models.ForeignKey(Unit,related_name='order_unit',on_delete=models.PROTECT)
    create_date=models.DateField(auto_now_add=True,null=True,blank=True)
    comment = LowerCase(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.pk)
   


class Item_Order_Status(models.Model):
    order_status=[('cancelled','cancelled'),
                ('dispatched','dispatched'),
                ('transferred','transferred'),]

    #client_id=models.ForeignKey(Client,on_delete=models.CASCADE)
    #consignee_id=models.ForeignKey(Consignee,on_delete=models.CASCADE)  
    item_order_id = models.ForeignKey(Item_Order,on_delete=models.CASCADE)
    #transfer_id = models.ForeignKey(Item_Order_Transfer,on_delete=models.CASCADE,blank=True,null=True)     
    date=models.DateField()   
    item_qty = models.DecimalField(default=0,max_digits=7,decimal_places=3)
    create_date=models.DateField(auto_now_add=True,null=True,blank=True)
    status = LowerCase(max_length=30,blank=True, null=True, choices=order_status,default='dispatched')
    docket_number = LowerCase(max_length=50,blank=True,null=True)
    comment = LowerCase(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.pk)

class Item_Order_Transfer(models.Model):
    client_id=models.ForeignKey(Client,on_delete=models.CASCADE)
    consignee_id=models.ForeignKey(Consignee,on_delete=models.CASCADE)
    item_order_id = models.ForeignKey(Item_Order,on_delete=models.CASCADE)
    status_id = models.ForeignKey(Item_Order_Status,on_delete=models.CASCADE)
    date=models.DateField()
    #item_name = LowerCase(max_length=200)
    #item_variant = LowerCase(max_length=200)
    #item_price = models.DecimalField(default=1.1,max_digits=7,decimal_places=2)
    #price_per_unit = LowerCase(max_length=200)   
    item_qty = models.DecimalField(default=0,max_digits=7,decimal_places=3)
    #item_unit = LowerCase(max_length=200)
    create_date=models.DateField(auto_now_add=True,null=True,blank=True)
    comment = LowerCase(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.pk)