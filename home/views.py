from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
#this is called url dispatching
def index (request):
    variables = {
        'site_name' : 'Myntra'
    }
    return render(request, "index_base.html" , context=variables)
def signin (request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username , password=password)


        if user is not None:
            login(request,user)
            username = user.username
            # return render(request,'Authentication/index_base.html')
            return render(request, "index_base.html",{'username':username})
        
        else:
            messages.error(request,"Incorrect Creditentials! try again")
            return redirect('login')

    return render(request, "Authentication/login.html" )
def signup (request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        myuser = User.objects.create_user(username,email,password)

        myuser.phone= phone

        myuser.save()

        messages.success(request, "Your account has been created successfully created!")

        return redirect('signin')

    return render(request, "Authentication/signup_login.html" )

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('/')




def categories (request):
    return render(request, "categories_base.html")
def products (request):
    return render(request, "products_base.html")
def orders (request):
    return render(request, "orders_base.html" )

    # return HttpResponse("This is orders page")