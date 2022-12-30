from django.shortcuts import render
from . models import Product
from django.views.generic import ListView , DetailView




class ProductsList(ListView):
        model = Product
        context_object_name = 'products'

class ProductsDetail(DetailView):
        model = Product
        context_object_name = 'item'







# def product_list(request):    
#         products=Product.objects.all()
#         return render (request,'products.html',{'products':products})



# def product_detail(request,id):
#         detail=Product.objects.get(id=id)
#         return render (request,'product_detail.html',{'item':detail})

