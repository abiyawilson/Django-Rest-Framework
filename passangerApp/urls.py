from django.urls import path

from passangerApp import views

urlpatterns = [
    path('', views.get_passanger_list),
    path('<int:pk>/', views.get_passanger_details),
]