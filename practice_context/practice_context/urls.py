
from django.contrib import admin
from django.urls import path,include
from practice_context import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("geeks/",include("geeks.urls")),
    path("earthly/",include("earthly.urls"))
]
