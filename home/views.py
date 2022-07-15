from django.shortcuts import render,HttpResponse

# Create your views here.
def index (request):
    return HttpResponse("This is home page")
def categories (request):
    return HttpResponse("This is categories page")
def products (request):
    return HttpResponse("This is products page")
def orders (request):
    return HttpResponse("This is orders page")