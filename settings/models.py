from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company')
    phone_numbers = models.TextField(max_length=150)
    address = models.TextField(max_length=150)
    subtitle = models.CharField(max_length=300)
    emails = models.TextField(max_length=150)
    call_us = models.CharField(max_length=50)
    email_us = models.EmailField()
    fb_link = models.URLField(max_length=200,null=True,blank=True)
    tw_link =  models.URLField(max_length=200)
    inst_link =  models.URLField(max_length=200)
    
    
    def __str__(self):
        return self.name