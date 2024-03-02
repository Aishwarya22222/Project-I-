from django.db import models
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.FloatField()
    stock=models.IntegerField()
    product_description=models.TextField()
    product_image=models.FileField(upload_to='static/uploads',null=True)
    Category = models.ForeignKey(Category,on_delete = models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.product_name 
