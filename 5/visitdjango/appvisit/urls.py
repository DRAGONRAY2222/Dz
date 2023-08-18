from django.urls import path
from .views import index

urlpaterns = [
    path('', index)
]