from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html', {})

def password(request):
    list_lower = list('abcdefghijklmnopqrstuvxyz')
    list_upper = list('ABCDEFGHIJKLMNOPQRSTUVXYZ')
    list_num = list('0123456789')
    list_special = ('+-*/!?#$%')
    password_generator = ''

    length =  int(request.GET.get('length')) #Estoy diciendole a request q me de el valor que obtuve del formulario o casilla llamada 'length', el valor se debe convertir a entero
    if request.GET.get('upper'):
        list_lower.extend(list_upper)

    if request.GET.get('special'):
        list_lower.extend(list_special)

    if request.GET.get('num'):
        list_lower.extend(list_num)

    for i in range(length):
        password_generator += random.choice(list_lower)

    return render(request, 'generator/password.html', {'password_generator': password_generator},)


def about(request):
    return render(request, 'generator/about.html', {} )