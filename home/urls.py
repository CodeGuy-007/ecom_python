from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',  views.index , name="home"),
    path('categories',  views.categories , name="categories"),
    path('products',  views.products , name="products"),
    path('orders',  views.orders , name="orders"),
    path('login',  views.signin , name="login"),
    path('signup',  views.signup , name="signup"),

]