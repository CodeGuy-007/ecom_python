from django.shortcuts import render,HttpResponse

# Create your views here.
#this is called url dispatching
def index (request):
    context = {
        'var1' : 'this is sent :)'
    }
    return render(request, "index.html" , context)
def categories (request):
    return HttpResponse("This is categories page")
def products (request):
    return HttpResponse("This is products page")
def orders (request):
    return render(request, "orders.html" )

    # return HttpResponse("This is orders page")