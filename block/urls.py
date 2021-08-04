from django.urls import path
from block.views import home, about, info

urlpatterns = [
    path('', home),
    path('about', about),
    path('info', info)
]