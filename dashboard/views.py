from django.shortcuts import render,redirect
from django.http import HttpRequest
from app1.models import Categories




def view_dashboard(request: HttpRequest):
    return render(request, 'dashboard.html')


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


def show_categories(request: HttpRequest):
    all_categories = Categories.objects.all()
    return render(request, 'showcategory.html', {'categories': all_categories})

def add_categories(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        category_image = request.FILES.get('category_image')

        if category_name and category_image:
            Categories.objects.create(
                category_name=category_name,
                category_image=category_image,
            )
        return redirect('/dashboard/show_categories')

    
    all_categories = Categories.objects.all()
    return render(request, 'categories.html', {'categories': all_categories})


def delete_category(request):
    id = request.GET.get("id")

    if not id:
        return redirect('/dashboard/show_categories')

    category = Categories.objects.filter(id=id).first()
    if category:
        if category.category_image:
            category.category_image.delete(save=False)
        category.delete()

    return redirect('/dashboard/show_categories')