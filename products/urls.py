from django.urls import path
from .views import ProductsList , ProductsDetail,BrandList,CategoryList,BrandDetail


app_name='products'

urlpatterns = [
    path('',ProductsList.as_view(),name='product_list'),
    path('brands',BrandList.as_view(),name='brand_list'),
    path('brands/<int:pk>',BrandDetail.as_view(),name='brand_detail'),
    path('category',CategoryList.as_view(),name='category_list'),
    path('<slug:slug>/',ProductsDetail.as_view()),
]
