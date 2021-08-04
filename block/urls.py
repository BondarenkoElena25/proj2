from django.urls import path
from block.views import home, about, info, templ

urlpatterns = [
    path('', home),
    path('about', about),
    path('info', info),
    path('templ', templ),
]