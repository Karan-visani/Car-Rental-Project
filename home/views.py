from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest

# Create your views here.
def home(request :HttpResponse):
    if request.COOKIES.get('email') is None:
        return redirect('/users/login')
    return render(request,'home.html')


def logout(request: HttpRequest):
    response = redirect('/users/login')
    response.delete_cookie('email')
    
    return response

def about(request: HttpRequest):
    return render(request,'AboutUs.html')