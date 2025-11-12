from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Role


# Create your views here.
def login_page(request :HttpRequest):
    if request.method == 'GET':
        return render(request, 'login.html')
    return login(request)

def login(request :HttpRequest):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if email is None or password is None:
        return HttpResponse("Email and Password are compulsory")
    
    user = User.objects.filter(email=email).first()
    if user is None:
        return HttpResponse("Wrong Email or Password")
    
    is_password_valid = check_password(password, user.password_hash)
    if not is_password_valid:
        return HttpResponse("Wrong email or password")
    
    return HttpResponse("Logged in Successfully")


def signup_page(request :HttpRequest):
    if request.method == 'GET':
        return render(request,'signup.html')
    return signup(request)

def signup(request :HttpRequest):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if email is None or password is None :
        return HttpResponse("Email and Password are compulsory")
    
    if User.objects.filter(email=email).exists():
        return HttpResponse("Sorry, this email is not available")
    
    customer_role = Role.objects.get(name="Customer")

    user = User()
    user.email = email
    user.password_hash = make_password(password)
    user.role = customer_role
    user.save()

    return HttpResponse("Successfully Signed Up") 