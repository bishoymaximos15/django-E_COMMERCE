from django.urls import path
from .views import ProductsList , ProductsDetail


urlpatterns = [
    path('',ProductsList.as_view()),
    path('<int:pk>/',ProductsDetail.as_view()),
]
