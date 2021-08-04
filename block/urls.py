from django.urls import path
from block.views import home, about

urlpatterns = [
    path('', home),
    path('about', about)
]