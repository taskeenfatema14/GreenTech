from django.db import models
from portals.base import BaseModel
# Create your models here.

class Product(BaseModel):
    image = models.ImageField(upload_to="category",blank=True,null=True,)
    title = models.CharField(max_length=50,blank=True,null=True,) 

    
class ProductItem(BaseModel):
    product      = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='prodectitems', )
    description  = models.CharField(max_length=200,)
    image        = models.ImageField(upload_to="category",blank=True,null=True,)
    title        = models.CharField(max_length=50,blank=True,null=True,)

class Brochure(BaseModel):
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    brochure     = models.FileField(upload_to="brochure",blank=True,null=True,)  #blank,null=True should be removed before production



