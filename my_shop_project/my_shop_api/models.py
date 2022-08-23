from django.db import models

# Create your models here.
class Customers(models.Model):
    """
    Customer model class with attributes like columns which we need to have in database. 
    """
    customer_id = models.AutoField(primary_key=True)
    customer_first_name = models.CharField(max_length=15)
    customer_middle_name = models.CharField(max_length=15)
    customer_last_name = models.CharField(max_length=15)
    customer_email_id = models.CharField(max_length=35)
    customer_dob = models.DateField(max_length=10)
    customer_phone_number = models.CharField(max_length=13)


class Product_Type(models.Model):
    """
    Product type model class with attributes like columns which we need to have in database.
    """
    product_type_id = models.AutoField(primary_key=True)
    product_type_name = models.CharField(max_length=15)


class Products(models.Model):
    """
    Products model class with attributes like columns which we need to have in database.
    """
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=15)
    product_type = models.ForeignKey(Product_Type, on_delete=models.CASCADE)
    product_description = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.PositiveIntegerField()


class Sell(models.Model):
    """
    Sell model class with attributes like columns which we need to have in database. 
    """
    transaction_sell_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    sell_amount = models.DecimalField(max_digits=15, decimal_places=2)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_quantity = models.PositiveIntegerField()


class Purchase(models.Model):
    """
    Purchase model class with attributes like columns which we need to have in database.
    """
    transaction_purchase_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    purchase_amount = models.DecimalField(max_digits=15, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_quantity = models.PositiveIntegerField()