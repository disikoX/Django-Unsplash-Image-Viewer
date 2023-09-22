from django.shortcuts import render
from . import forms
from django.http import HttpResponse
from .models import User
import requests
from django.http import JsonResponse


def index(request):
    return render(request, 'templates/mainApp/index.html')

def form_name_view(request):
    form = forms.FormName()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        new_user = User(username=username,password=password)
        new_user.save()
    
    
    return render(request,'templates/mainApp/form_page.html',{'form':form}) #Nom du fichier faux

def random_image(request):
       # Replace 'YOUR_UNSPLASH_ACCESS_KEY' with your actual Unsplash access key
       access_key = 'Pydg9u8CGnUZ3VVpgrIXPU8Yrj77i2pfCvvIlJXyicc'
       url = f'https://api.unsplash.com/photos/random?client_id={access_key}'

       response = requests.get(url)
       data = response.json()

       image_url = data['urls']['regular']
       context = {'image_url': image_url}

       return render(request, 'index.html', context)





