from courseApp.models import Course
from courseApp.serializers import CourseSerializers
from rest_framework import viewsets


class CourseViewsets(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


