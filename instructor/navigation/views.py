from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'navigation/about.html')

def contact(request): 
    return render(request, 'navigation/contact.html')


def home(request):
    return render(request, 'navigation/home.html')


def courses(request):
    return render(request, 'navigation/courses.html')