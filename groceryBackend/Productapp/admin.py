from django.contrib import admin
from Productapp.models import CategoryModel, ProductModel

# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(ProductModel)