from django.urls import path

from courseApp.views import CourseList, CourseDetail

urlpatterns = [
    path('', CourseList.as_view()),
    path('<int:pk>/', CourseDetail.as_view()),
]