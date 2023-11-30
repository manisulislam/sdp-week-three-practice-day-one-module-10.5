from django.shortcuts import render

# Create your views here.
def home_earthly(request):
    return render(request,'earthly/earthly.html')