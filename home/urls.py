from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.home),
    path('logout/',views.logout),
    path('about/',views.about)

]