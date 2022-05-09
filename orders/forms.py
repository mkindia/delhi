
from django import forms
from django.contrib.auth import models
from django.core.validators import RegexValidator
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.db.models import fields


from django.core.exceptions import ValidationError