from courseApp.models import Course
from courseApp.serializers import CourseSerializers
from rest_framework import generics, mixins


class CourseList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CourseDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
