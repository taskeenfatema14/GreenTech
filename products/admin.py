from django.contrib import admin

# Register your models here.
from django.contrib import admin
from products.models import *

# Register your models here.


admin.site.register(Product)
admin.site.register(ProductItem)
admin.site.register(Brochure)