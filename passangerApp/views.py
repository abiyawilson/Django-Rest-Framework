from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from passangerApp.models import Passanger
from rest_framework.response import Response
from passangerApp.serializers import PassagerSerializers


@api_view(['GET', 'POST'])
def get_passanger_list(request):
    if request.method == "GET":
        passangers = Passanger.objects.all()
        serializer = PassagerSerializers(passangers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = PassagerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_passanger_details(request, pk):
    try:
        passanger = Passanger.objects.get(pk=pk)
    except Passanger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PassagerSerializers(passanger)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = PassagerSerializers(passanger, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        passanger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
