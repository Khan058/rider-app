from django.urls import path
from . import views

urlpatterns = [
    path('earnings/', views.earnings_overview, name='earnings'),
]
