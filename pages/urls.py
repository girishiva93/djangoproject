from django.urls import path
from . import views # here . refers all data

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
]