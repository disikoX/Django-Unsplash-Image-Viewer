from django.shortcuts import render
from . import forms
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'templates/mainApp/index.html')

def form_name_view(request):
    form = forms.FormName()
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        
        if form.is_valid():
            print("VALIDATION SUCCESS !")
            print("EMAIL: "+form.cleaned_data['email'])
            print("PASSWORD: "+form.cleaned_data['password'])

    
    
    return render(request,'templates/mainApp/form_page.html',{'form':form}) #Nom du fichier faux