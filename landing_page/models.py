from django.db import models

from django.core.validators import FileExtensionValidator
from portals.models import BaseModel

# Create your models here.

class LandingImage(BaseModel):
    image = models.ImageField(upload_to="landing_page",blank=True,null=True,)
    video = models.FileField(upload_to="landing_page", blank=True, null=True, validators=[FileExtensionValidator(['mp4', 'avi', 'mov'])])


class Category(BaseModel):
    image = models.ImageField(upload_to="category")
    title = models.CharField(max_length=20)
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

class Product(BaseModel):
    image = models.ImageField(upload_to="category",blank=True,null=True,)
    title = models.CharField(max_length=20,blank=True,null=True,) 
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)

class ProductItem(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='prodectitems', )
    description = models.CharField(max_length=20,)
    image = models.ImageField(upload_to="category",blank=True,null=True,)
    title = models.CharField(max_length=20,blank=True,null=True,)


class Brochure(BaseModel):
    productitem = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='brochure')
    detail  = models.TextField()
    image   = models.ImageField(upload_to="brochure",blank=True,null=True,)
