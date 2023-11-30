from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d={"value": 3,
       "jai":"I'm jai", 
       "name":"anis", 
       "date":datetime.datetime.now(),
       "it":"",
       "info":[
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
        ],
       "number":31,
       "file":12546597465611,
       "lst":[1,5,6,9,15,21,14],
       'st':["anis","islam","anis"],
       "numbers":["one",
                  "two",
                  "three",
                  "four"],
       "versity":"Daffodil International University",
       
       
       }
    return render(request, 'geeks/home.html',d)