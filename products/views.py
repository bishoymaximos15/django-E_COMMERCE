from django.shortcuts import render , redirect
from . models import Product , ProductReviews , Brand , Category
from django.views.generic import ListView , DetailView
from .forms import ReviewForm



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
        

def add_review(request,slug):
        product = Product.objects.get(slug=slug)
        form = ReviewForm(request.POST)

        if form.is_valid():
                myform = form.save(commit=False)
                myform.product = product
                myform.save()
                
        return redirect(f'/products/{slug}/') 




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
