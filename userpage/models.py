from django.db import models
from products.models import Product
from django.contrib.auth.models import User  # jasle login garcha ra tesle nai add to cart garna ko laagi user lai import gareko 
from django.core.validators import *
# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

# order now
class Order(models.Model):
    PAYMENT=(
        ('Cash On Delivery','Cash On Delivery'),
        ('Esewa','Esewa'),
        ('Khalti','Khalti'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_price=models.IntegerField(null=True)
    status=models.CharField(default='Pending',max_length=200)
    payment_method=models.CharField(max_length=100,choices=PAYMENT)
    payment_status=models.BooleanField(default=False,null=True)
    phone_no=models.CharField(max_length=20,validators=[MinLengthValidator(9),MaxLengthValidator(15)])
    address=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
