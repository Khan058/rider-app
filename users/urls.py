from django.urls import path
from . import views

urlpatterns = [
    path('riders/', views.riders, name='riders'),
]
