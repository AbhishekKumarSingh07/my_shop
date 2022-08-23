from rest_framework import serializers
from .models import Customers 
from .models import Product_Type 
from .models import Products 
from .models import Purchase 
from .models import Sell


class CustomerSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField()
    customer_first_name = serializers.CharField(max_length=15)
    customer_middle_name = serializers.CharField(max_length=15)
    customer_last_name = serializers.CharField(max_length=15)
    customer_email_id = serializers.CharField(max_length=35)
    customer_dob = serializers.DateField(format='%Y-%m-%d')
    customer_phone_number = serializers.CharField(max_length=13)

    class Meta:
        model = Customers
        fields = ('__all__')


