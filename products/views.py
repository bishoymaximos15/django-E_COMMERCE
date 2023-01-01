from django.shortcuts import render
from . models import Product , ProductReviews
from django.views.generic import ListView , DetailView




class ProductsList(ListView):
        model = Product
        context_object_name = 'products'

class ProductsDetail(DetailView):
        model = Product
        context_object_name = 'item'



        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["reviews"] = ProductReviews.objects.filter(product=self.get_object())
            context['related'] = Product.objects.filter(category=self.get_object().category)
            return context
        



# def product_list(request):    
#         products=Product.objects.all()
#        sdfsdfsf
#         return render (request,'products.html',{'products':products})



# def product_detail(request,id):
#         detail=Product.objects.get(id=id)
#         return render (request,'product_detail.html',{'item':detail})

