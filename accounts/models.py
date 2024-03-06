from django.db import models
import uuid
from portals.models import BaseModel
from portals.choices import *

# class UserRole(BaseModel):
#     role_name  = models.CharField(choices=RoleChoices.choices,max_length=25,unique=True)

#     def __str__(self) -> str:
#         return self.role_name

class User(models.Model):
    id         = models.UUIDField(default=uuid.uuid4,primary_key=True)
    email      = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username         = models.CharField(max_length = 50)
    password         = models.CharField(max_length = 16)
    # user_role        = models.ForeignKey(UserRole,on_delete=models.CASCADE,)


    def __str__(self) -> str:
        return self.username
    
class Admin1(models.Model):
    id         = models.UUIDField(default=uuid.uuid4,primary_key=True)
    email      = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    password         = models.CharField(max_length = 16)

