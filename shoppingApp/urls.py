from django.urls import path

from shoppingApp import views

urlpatterns = [
    path('customer/', views.CustomerList.as_view()),
    path('customer/<int:pk>', views.CustomerDetails.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>', views.OrderDetails.as_view()),

]
