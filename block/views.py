from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h3>Main page</h3><br><a href='http://127.0.0.1:8000/about'>About</a><br><a href='http://127.0.0.1:8000/info'>info</a>")

def about(request):
    return HttpResponse("<h3>About</h3><br><a href='http://127.0.0.1:8000'>Home</a><br><a href='http://127.0.0.1:8000/info'>info</a>")

def info(request):
    return HttpResponse("<h3>Information</h3><br><a href='http://127.0.0.1:8000'>Home</a><br><a href='http://127.0.0.1:8000/about'>About</a>")

def templ(request):
    ar = [1,2]
    temp = 'Hello template'
    is_good = True
    data =  {'temp': temp,
             'is_good': is_good,
             'ar':ar}
    return render(request, 'block/index.html', data)