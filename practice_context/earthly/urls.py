from django.urls import path

from earthly import views

urlpatterns=[
    path("",views.home_earthly),
    path("home/",views.home_earthly)
]