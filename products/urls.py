from django.urls import path
from .views import ProductsList , ProductsDetail


urlpatterns = [
    path('',ProductsList.as_view()),
    path('<slug:slug>/',ProductsDetail.as_view()),
]
