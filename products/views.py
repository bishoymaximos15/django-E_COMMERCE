from django.shortcuts import render
from . models import Product , ProductReviews , Brand , Category
from django.views.generic import ListView , DetailView




class ProductsList(ListView):
        model = Product
        context_object_name = 'products'
        paginate_by = 1

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
        paginate_by = 1

class CategoryList(ListView):
        model = Category
        paginate_by = 1
