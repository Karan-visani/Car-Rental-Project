from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from app1.models import Categories,Vehicle


def home(request: HttpRequest):
    if request.COOKIES.get('email') is None:
        return redirect('/users/login')

    all_categories = Categories.objects.all()
    vehicles = Vehicle.objects.all()
    return render(request, 'home.html', {
        'categories': all_categories,
        'vehicles': vehicles
        })

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
        return redirect('/home/categories/')

    
    all_categories = Categories.objects.all()
    return render(request, 'categories.html', {
        'categories': all_categories
        })


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles.html', {'vehicles': vehicles})


def vehicle_detail(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})


