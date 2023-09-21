from django.shortcuts import render
from . import forms
from django.http import HttpResponse
from .models import User
import requests
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'templates/mainApp/form_page.html')

def form_name_view(request):
    form = forms.FormName()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        new_user = User(username=username,password=password)
        new_user.save()
    
    
    return render(request,'templates/mainApp/form_page.html',{'form':form}) #Nom du fichier faux

#def Image(self,request,image):
    url ="https://api.unsplash.com?q={}&appid=<Pydg9u8CGnUZ3VVpgrIXPU8Yrj77i2pfCvvIlJXyicc>".format(image)
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

def Image(request):
    # Get the query parameter 'q' from the request's GET parameters
    query = request.GET.get('q', '')  # Default to empty string if 'q' is not provided

    # Construct the URL with the API key in the request headers
    url = "https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": "Client-ID <API-key>"
    }
    params = {
        "query": query
    }

    # Send the GET request to Unsplash API
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        # Handle API error responses here
        error_data = {"error": "Unable to fetch images"}
        return JsonResponse(error_data, status=response.status_code)

