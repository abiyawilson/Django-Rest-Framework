from courseApp.models import Course
from courseApp.serializers import CourseSerializers
from rest_framework import generics, mixins


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
