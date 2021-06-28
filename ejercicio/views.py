from django.http.response import HttpResponse
from django.shortcuts import render
import random


def home(request):
    return render( request,'ejercicio/home.html',{'nombre': 'Axel Gonza'})

def create_password(request):
    caracteres = list('abcdefghijklmñopqrstvwxyz')
    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMÑOPQRSTVWXYZ'))
    if request.GET.get('number'):
        caracteres.extend(list('123456789'))
    if request.GET.get('special'):
        caracteres.extend(list('!#$%&@'))
    length = int(request.GET.get('length',8))
    pswd = ''
    for x in range (length):
        pswd += random.choice(caracteres)
    return render(request,'ejercicio/password.html',{'password':pswd})