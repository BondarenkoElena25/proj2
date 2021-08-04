from django.urls import path
from block.views import home
urlpatterns = [
    path('', home)
]