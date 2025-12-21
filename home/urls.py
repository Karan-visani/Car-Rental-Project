from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.home),
    path('logout/',views.logout),
    path('about/',views.about),
    path('categories/',views.categories),
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicle/<int:id>/', views.vehicle_detail, name='vehicle_detail'),
]