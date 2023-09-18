from django.shortcuts import render
from . import forms
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'templates/mainApp/index.html')

def form_name_view(request):
    form = forms.FormName()
    return render(request,'templates/mainApp/form_page.html',{'form':form}) #Nom du fichier faux