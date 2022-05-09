
from multiprocessing.connection import Client
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.validators import UnicodeUsernameValidator 



# for input data in lowercase
class LowerCase(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LowerCase, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class UsersManager(BaseUserManager):

    def create_user(self,user_name, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not user_name:
            raise ValueError('Users must have an User name')

          
        user = self.model(
            user_name=user_name,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            
        )       
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,user_name, email, first_name, last_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(user_name,email=email, first_name=first_name, last_name=last_name, password=password,
          
        )
        user.is_admin = False
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

class Custom_User(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()
    user_name = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email=models.EmailField(blank=True, null=True, verbose_name='email address',max_length=255,unique=True,)
    first_name=LowerCase(blank=True, null=True,max_length=150, verbose_name='first name')
    last_name=LowerCase(blank=True, null=True,max_length=150, verbose_name='last name')
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{9,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], null=True, blank=True,  max_length = 16, unique = True)
    user_img = models.ImageField(upload_to='user', blank=True, null=True)       
    password = models.CharField(max_length=150)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_user =  models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)   
    date_joined = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    
    USERNAME_FIELD = 'user_name'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email','first_name','last_name']

    objects = UsersManager()

    def __str__(self):
        return self.user_name

   
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_staff 
    
    @property
    def admin(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def user(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_user 
    

class Password_Change(models.Model):
    user_id = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    email=models.EmailField(blank=True, null=True, verbose_name='email address',max_length=255,)
    token = models.CharField(max_length=250)    
    is_changed = models.BooleanField(default=False)
    date_changed = models.DateTimeField(auto_now_add=True, blank=True,null=True)

class Permissions(models.Model):
    permission_name = LowerCase(max_length=100,)
    des=LowerCase(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.permission_name

class User_Permissions(models.Model):
    user=models.OneToOneField(Custom_User,on_delete=models.CASCADE)
    user_permissions=models.ManyToManyField(Permissions)
    

class User_Verification(models.Model):
    user_id = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    client_id = models.PositiveIntegerField(blank=True,null=True,unique=True)  
    email=models.EmailField(blank=True, null=True, verbose_name='email address',max_length=255,)
    token = models.CharField(max_length=250)
    is_verified = models.BooleanField(default=False)
    date_varified = models.DateTimeField(auto_now_add=True, blank=True,null=True)