from django.urls import path
from .views import ProductsList , ProductsDetail


app_name='products'

urlpatterns = [
    path('',ProductsList.as_view(),name='product_list'),
    path('<slug:slug>/',ProductsDetail.as_view()),
]
