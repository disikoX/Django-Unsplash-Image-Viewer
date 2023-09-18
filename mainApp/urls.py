from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path("",views.index,name='index'), 
    path("formpage/",views.form_name_view,name ='form_name'),
]