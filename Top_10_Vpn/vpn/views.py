from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    dict = {'age':15}
    return render(request,'main.html',dict)
