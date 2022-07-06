
from pyexpat import model
from django import forms
from django.contrib.auth import models
from django.core.validators import RegexValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import Item_Order_Status
from django.db.models import fields


from django.core.exceptions import ValidationError

class order_dispatchForm(forms.ModelForm):
    class Meta:
        model = Item_Order_Status
        fields ='__all__'