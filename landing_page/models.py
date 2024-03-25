from django.db import models

from django.core.validators import FileExtensionValidator
from portals.models import BaseModel

# Create your models here.

class LandingImage(BaseModel):
    image = models.ImageField(upload_to="landing_page",blank=True,null=True,)
    video = models.FileField(upload_to="landing_page", blank=True, null=True, validators=[FileExtensionValidator(['mp4', 'avi', 'mov'])])


class Category(BaseModel):
    image = models.ImageField(upload_to="category")
    title = models.CharField(max_length=20)        # can create validation for not accepting same title card category...
    link = models.URLField(blank=True, null=True)  



    # def save(self,*args, **kwargs):
    #     # check the record count if it is one then update the existing one otherwise save the record 
    #     count = Category.objects.count()
    #     print(count)
    #     if count == 0  :
    #         return super(Category,self).save(*args, **kwargs)
    #     else :
    #         obj = Category.objects.all()
    #         obj.delete()
    #         return super(Category,self).save(*args, **kwargs)


