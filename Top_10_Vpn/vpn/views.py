from django.shortcuts import render
from django.http import HttpResponse
from vpn.form import Vpn_Form

def home(request):
    dict = {'age':15}
    return render(request,'main.html',dict)

def Form(request): 
    vpn_form = Vpn_Form()
    dict = {
        'form':vpn_form,
        'good':'boy',
     
    }
    return render(request,'api/vpn_form.html',dict)   

