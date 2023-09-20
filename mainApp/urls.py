from django.urls import path,include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path("",views.index,name='index'), 
    path("formpage/",views.form_name_view,name ='form_name'),
    path("Image",views.Image),
]
urlpatterns += staticfiles_urlpatterns("/static")