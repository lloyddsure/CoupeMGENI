from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('article/<int:id>', views.lire, name='lire')
]
