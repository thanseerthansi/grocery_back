from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    category = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
class ProductModel(models.Model):
    product_name = models.CharField(max_length=100,null=True)
    category = models.ForeignKey(CategoryModel,on_delete=models.DO_NOTHING,blank=True)
    image = models.ImageField(upload_to='Image',blank=True)
    price= models.FloatField(default=0.0)
    offer_price = models.FloatField(default=0.0)
    is_packet = models.BooleanField(default=True)
    stock_available = models.FloatField(0.0) 
    stock_in_kg = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    