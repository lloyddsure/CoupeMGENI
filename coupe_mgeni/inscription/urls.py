from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home),
    path('', views.inscription, name='Inscription'),
]
