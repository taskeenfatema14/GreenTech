from django.db import models 
from .constants import * 



class RoleChoices(models.TextChoices):
    ADMIN        = ADMIN,ADMIN 
    USER         = USER, USER
