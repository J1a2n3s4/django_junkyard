from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('products/<str:name_url>/', views.product_page, name="product"),
    path('buyproduct/<str:name_url>/', views.buy, name="buyproduct"),
    path('login', views.login_page, name="login_page"),
    path('register', views.register, name="register")
]