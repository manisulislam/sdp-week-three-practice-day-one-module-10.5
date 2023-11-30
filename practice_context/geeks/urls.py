from django.urls import path
from geeks import views

urlpatterns=[
    path("",views.home),
    path("home/",views.home),
    
]