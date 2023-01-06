from distutils.command.upload import upload
from time import timezone
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager


# Create your models here.

flagChoices=(
    ("new","new"),
    ("features","features"),
    ("sale","sale"),
)
class Product(models.Model):
    name=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=400)
    image =models.ImageField(upload_to ='product')
    price=models.FloatField()
    description=models.TextField(max_length=10000)
    vediolink=models.URLField()
    SKU=models.IntegerField()
    flag =models.CharField(max_length=12,choices=flagChoices)
    brand = models.ForeignKey('Brand',on_delete=models.SET_NULL,null=True,blank=True,related_name='product_brand')
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,blank=True,related_name='product_category')
    tags = TaggableManager()
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
         return self.name
     
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)   
       super(Product, self).save(*args, **kwargs) 
        
        
class ProductImage(models.Model):
    product = models.ForeignKey(Product,related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/') 
    
    def __str__(self):
        return str(self.product)
     


class ProductReviews(models.Model):
       product = models.ForeignKey(Product , on_delete=models.CASCADE, related_name='product_review' , null=True,blank=True)
       name=models.CharField(max_length=100)
       date=models.DateTimeField(default=timezone.now)
       image=models.ImageField(upload_to ='reviews')
       rate=models.IntegerField()
       reviews=models.TextField(max_length=300)
    
       def __str__(self):
           return self.name
             
           

class Brand (models.Model):
     name=models.CharField(max_length=100)
     image=models.ImageField(upload_to ='brand')
     
     def __str__(self):
          return self.name
             
           

class Category(models.Model):
       name=models.CharField(max_length=100)
       image=models.ImageField(upload_to ='category')

       def __str__(self):
          return self.name
             
           


