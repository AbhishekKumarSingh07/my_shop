from django.contrib import admin

from .models import Customers 
from .models import Product_Type 
from .models import Products 
from .models import Purchase 
from .models import Sell

# Register your models here.

admin.site.register(Customers)
admin.site.register(Product_Type)
admin.site.register(Products)
admin.site.register(Purchase)
admin.site.register(Sell)
