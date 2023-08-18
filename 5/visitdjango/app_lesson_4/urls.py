from django.urls import path
from .views import index, redirect_view

urlpaterns = [
    path('', index),
    path('/lesson_4/', redirect_view)

]






