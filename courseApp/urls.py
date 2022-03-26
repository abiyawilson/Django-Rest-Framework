from rest_framework.routers import DefaultRouter

from courseApp import views

router = DefaultRouter()
router.register('course', views.CourseViewsets)
