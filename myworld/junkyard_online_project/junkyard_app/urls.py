from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('products/<str:name_url>/', views.product_page, name="product")
]