from django.shortcuts import render
from products.models import Product , Brand , ProductReviews

def home(request):
    
    brands = Brand.objects.all()
    sale = Product.objects.filter(flag='sale')[:10]
    features = Product.objects.filter(flag='features')[:6]
    new = Product.objects.filter(flag='new')[:10]
    reviews = ProductReviews.objects.all()[:6]
    
    return render(request,'settings/home.html',{
        'sale' : sale , 
        'features' : features , 
        'new' : new , 
        'brands' : brands , 
        'reviews':reviews
    })