from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('news', news, name='news'),
    path('publish', publish, name='publish'),
    path('vmeste', vmeste, name='vmeste'),
    path('npa', npa, name='npa'),
    path('visited', visited, name='visited'),
    path('', index, name='index'),
    path('', index, name='index'),
    path('', index, name='index'),
]