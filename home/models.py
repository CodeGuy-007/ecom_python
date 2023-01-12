from django.db import models
import datetime

# Create your models here.

class Product_category(models.Model):
    p_cat_name = models.CharField("product category name",max_length=60, unique=True)
    p_cat_desc = models.TextField("product category description in detail",max_length=1000)

class Product_inventory(models.Model):
    p_inv_qty = models.PositiveIntegerField("inverntory quantity of the product")
    p_last_add_qty = models.PositiveIntegerField("last added quantity of product in units", blank= True, null= True)

class Discount(models.Model):
    dis_name = models.CharField("name of the discount applied to products if any",max_length=30, blank=True, null=True)
    dis_desc = models.TextField("description of discount", max_length=1000, blank=True, null=True)
    dis_per = models.DecimalField( max_digits=4, decimal_places=2)
    dis_active = models.BooleanField("current status of the discount",default=True)

class User(models.Model):
    user_name = models.CharField(max_length=30, unique=True, blank=False)
    password = models.CharField(max_length=15, blank=False)
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length=30)
    phone = models.PositiveIntegerField()
    created_at = models.TimeField(default=datetime.datetime.now())
    modified_at = models.TimeField(blank=True , null=True)
    

class Product(models.Model):
    p_name = models.CharField("product name",max_length=120)
    p_desc = models.CharField("product detailed description",max_length=1000)
    category_id = models.ForeignKey(Product_category, on_delete=models.RESTRICT, blank=True, null=True)
    inventory_id = models.ForeignKey(Product_inventory, on_delete=models.RESTRICT)
    p_price = models.DecimalField("mrp of the product",max_digits=9, decimal_places=2)
    discount_id = models.ForeignKey(Discount, models.SET_NULL, blank=True, null=True,)

class Order_detail(models.Model):
    user_id = models.ForeignKey(User, models.CASCADE)
    ord_tot = models.DecimalField("Total value of the order", max_digits=9, decimal_places=2)
    payment_id = models.ForeignKey('Payment_detail', models.RESTRICT)

class Order_item(models.Model):
    order_id = models.ForeignKey(Order_detail, models.CASCADE)
    product_id = models.ForeignKey(Product, models.RESTRICT)
    quantity = models.PositiveIntegerField("quantity of the product in this order", )

class Payment_detail(models.Model):
    SUCCESSFUL ="S"
    PENDING = "P"
    FAILED = "F"
    PAYMENT_STATUS = [
        (SUCCESSFUL, 'Successful'),
        (PENDING, 'Pending'),
        (FAILED, 'Failed')
    ]
    order_id =  models.ForeignKey(Order_detail, models.CASCADE)
    pay_amt = models.PositiveIntegerField("the amount paid by the customer")
    transaction_id = models.PositiveIntegerField("id receieved from payment gateway")
    pay_sta = models.CharField("Payment status  as S/P/F", max_length=1, choices=PAYMENT_STATUS)


class Saved_address(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    address_line_1 = models.CharField(max_length=60)
    address_line_2 = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.PositiveIntegerField()

class Cart_item(models.Model):
    product_id= models.ForeignKey(Product, on_delete= models.RESTRICT)
    prod_cart_qty = models.PositiveIntegerField(default=1)

    