from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):
    CONDITION_FIELD=(
        ("new","new"),
        ("old","old"),
    )
    name=models.CharField(max_length=50)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField()
    category=models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    description=models.TextField(max_length=500)
    image=models.ImageField(upload_to='main_product/', blank=True, null=True)
    price=models.DecimalField(max_digits=40, decimal_places=5)
    condition=models.CharField( max_length=50,choices=CONDITION_FIELD)
    brand=models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    slug=models.SlugField(blank=True, null=True)
    def save(self,*args,**kwargs):
        if not self.slug and self.name:
            self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)
            
    def __str__(self):
        return self.name
    
class Category(models.Model):
    category_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='products/', blank=True, null=True)
    slug= models.SlugField(blank=True, null=True)
    def save(self,*args,**kwargs):
        if not self.slug and self.category_name:
            self.slug=slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)
    def __str__(self):
        return self.category_name
    
    
    class Meta:
        verbose_name= 'category'
        verbose_name_plural='categories'
    

class Brand(models.Model):
    brand_name= models.CharField(max_length=50)
    class Meta:
        verbose_name='brand'
        verbose_name_plural='brands'

    def __str__(self):
        return self.brand_name
    
class ProductImages(models.Model):
    product=models.ForeignKey('Product', on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to='products/', blank=True, null=True)
    class Meta:
        verbose_name='product image'
        verbose_name_plural='product images'
    def __str__(self):
        return self.product.name
    