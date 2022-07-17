from django.shortcuts import render,HttpResponse

# Create your views here.
#this is called url dispatching
def login (request):
    return render(request, "login.html" )
def signup (request):
    return render(request, "signup_login.html" )
def index (request):
    variables = {
        'site_name' : 'Myntra'
    }
    return render(request, "index_base.html" , context=variables)
def categories (request):
    return render(request, "categories_base.html")
def products (request):
    return render(request, "products_base.html")
def orders (request):
    return render(request, "orders_base.html" )

    # return HttpResponse("This is orders page")