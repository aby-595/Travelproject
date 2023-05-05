from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('about.html', views.about, name='about'),
    path('index.html', views.index, name='index')

]
