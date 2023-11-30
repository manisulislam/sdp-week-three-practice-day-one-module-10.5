

from django.urls import path
from navigation import views

urlpatterns = [
    
    path("", views.home),
    path("about/", views.about),
    path("contact/", views.contact),
    path("courses/", views.courses),
    
    
]
