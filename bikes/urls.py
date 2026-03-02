from django.urls import path
from . import views

urlpatterns = [
    path('bikes/', views.bikes_list, name='bikes_list'),
    path('bikes/register/', views.register_bike, name='register_bike'),
    path('bikes/<int:bike_id>/edit/', views.edit_bike, name='edit_bike'),
]
