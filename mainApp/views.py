from django.shortcuts import render
from . import forms
from django.http import HttpResponse
from .models import User

# Create your views here.

def index(request):
    return render(request, 'templates/mainApp/index.html')

def form_name_view(request):
    form = forms.FormName()
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        new_user = User(email=email,password=password)
        new_user.save()
    
    
    return render(request,'templates/mainApp/form_page.html',{'form':form}) #Nom du fichier faux