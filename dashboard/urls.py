from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_dashboard),
    path('categories/', views.categories),
    path('show_categories/', views.show_categories),
    path('add_categories/', views.add_categories),
    path('logout/', views.logout),
    path('delete_category/', views.delete_category, name='delete_category'),
]