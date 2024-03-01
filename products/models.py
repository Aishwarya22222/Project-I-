from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.FloatField()
    stock=models.IntegerField()
    product_description=models.TextField()
    product_image=models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.product_name 
    

