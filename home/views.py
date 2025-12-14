from django.shortcuts import render, redirect
from django.http import HttpRequest
from app1.models import Categories


def home(request: HttpRequest):
    if request.COOKIES.get('email') is None:
        return redirect('/users/login')

    all_categories = Categories.objects.all()
    return render(request, 'home.html', {'categories': all_categories})

def logout(request: HttpRequest):
    response = redirect('/users/login')
    response.delete_cookie('email')
    return response


def about(request: HttpRequest):
    return render(request, 'AboutUs.html')


def categories(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        category_image = request.FILES.get('category_image')

        if category_name and category_image:
            Categories.objects.create(
                category_name=category_name,
                category_image=category_image,
            )
        return redirect('/categories/')

    
    all_categories = Categories.objects.all()
    return render(request, 'categories.html', {'categories': all_categories})



