from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h3>Main page</h3>")

def about(request):
    return HttpResponse("<h3>About</h3><br><a href='http://127.0.0.1:8000'>Home</a>")
