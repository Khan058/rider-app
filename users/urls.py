from django.urls import path
from . import views

urlpatterns = [
    path('riders/', views.riders, name='riders'),
    path('riders/register/', views.register_rider, name='register_rider'),
]
