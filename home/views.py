from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from ecom_django_mysql import settings
from django.core.mail import send_mail


# custom funtion for password validation
def password_check(passwd):
      
    SpecialSym =['$', '@', '#', '%']
    val = True
      
    if len(passwd) < 6:
        print('length should be at least 6')
        val = False
          
    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False
          
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

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

        # Signup form validations commented for ease in development        
        '''
        if User.objects.filter(username=username):
            messages.error(request, "Username is taken! Please try with another one")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered")
            return redirect('signup')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username cannot contain special characters such as [!@#$%]")
            return redirect('signup')

        if not password_check(password):
            messages.error(request, "Password entered didn't fulfill one or more of the given requirements. \nKindly try again with another password!")
            return redirect('signup')
        '''


        myuser = User.objects.create_user(username,email,password)

        myuser.phone= phone

        myuser.save()

        messages.success(request, "Your account has been created successfully !")

        # welcome email contents

        subject ="Welcome to demo ecom store"
        message = "Hello " + myuser.username + "! \n" + "Welcome to our store \nthis is a confirmation email \nClick on the link below to confirm the email with this account \n\nThanking you, \nTeam Demo-ecom"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('login')

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