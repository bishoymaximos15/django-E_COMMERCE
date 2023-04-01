from django.shortcuts import render
from . models import Product , ProductReviews , Brand , Category
from django.views.generic import ListView , DetailView




class ProductsList(ListView):
        model = Product
        context_object_name = 'products'
        paginate_by = 50
        queryset = Product.objects.all()[:10]

class ProductsDetail(DetailView):
        model = Product
        context_object_name = 'item'



        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["reviews"] = ProductReviews.objects.filter(product=self.get_object())
            context['related'] = Product.objects.filter(category=self.get_object().category)
            return context
        


class BrandList(ListView):
        model = Brand
        paginate_by = 50


class BrandDetail(ListView):
        model = Product
        paginate_by= 2 
        template_name = 'products/brand_detail.html'
        
        def get_queryset(self):
            brand = Brand.objects.get(id=self.kwargs['pk'])
            data = Product.objects.filter(brand=brand)
            return data
    
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["brand"] = Brand.objects.get(id=self.kwargs['pk'])
            return context
        
        


class CategoryList(ListView):
        model = Category
        paginate_by = 50
