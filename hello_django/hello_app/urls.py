from django.urls import path
from . views import *
urlpatterns = [
    path('hello/',print_hello)
]