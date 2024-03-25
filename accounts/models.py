from django.db import models
import uuid
from portals.models import BaseModel
# from portals.choices import *
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
# from portals.choices import RoleChoices


# class UserRole(BaseModel):
#     role_name  = models.CharField(choices=RoleChoices.choices,max_length=25,unique=True,)
#     def __str__(self) -> str:
#         return self.role_name

# Create your models here.

class User(AbstractBaseUser):
    id               = models.UUIDField(default=uuid.uuid4,primary_key=True)
    email            = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username         = models.CharField(max_length = 50)
    # user_type        = models.CharField(choices=RoleChoices.choices,max_length=25,default=RoleChoices.USER)
    is_admin         = models.BooleanField(default=False)
    created_on       = models.DateTimeField(auto_now_add=True,editable=False)
    updated_on       = models.DateTimeField(auto_now=True)
    otp              = models.PositiveIntegerField(null= True, blank=True)

    objects    = UserManager()
    
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def __str__(self) -> str:
        return self.email

# class Admin1(models.Model):
#     id         = models.UUIDField(default=uuid.uuid4,primary_key=True)
#     email      = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     username         = models.CharField(max_length = 50)
#     password         = models.CharField(max_length = 16)

#     def save(self,*args, **kwargs):
#         # check the record count if it is one then update the existing one otherwise save the record 
#         count = Admin1.objects.count()
#         print(count)
#         if count == 0  :
#             return super(Admin1,self).save(*args, **kwargs)
#         else :
#             obj = Admin1.objects.all()
#             obj.delete()
#             return super(Admin1,self).save(*args, **kwargs)
        

class Enquiry(BaseModel):
    user = models.ForeignKey(User, on_delete =models.CASCADE, related_name="enquiries")
    organization = models.CharField(max_length=50)
    name         = models.CharField(max_length=50)
    email        = models.EmailField(
        verbose_name = 'email_address',
        max_length=255,
        unique=True,
    )
    designation  = models.CharField(max_length=50, blank=True, null= True)
    contact_no   = models.CharField(max_length=20, blank=True, null= True)
    comments     = models.CharField(max_length=50, blank=True, null= True)