from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return HttpResponse('Домашка по 4 занятию')

def redirect_view(request):
    response = redirect('/redirect-success/')
    return response