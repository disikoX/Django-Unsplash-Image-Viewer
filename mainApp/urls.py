from django.urls import path,include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path("",views.form_name_view,name ='form_name'),
    path("index",views.index, name='index'),
]
urlpatterns += staticfiles_urlpatterns("/static")