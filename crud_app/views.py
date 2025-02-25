from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from crud_app.models import User
from crud_app.serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# Get single use
@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# Create a new user
@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update an existing user
@api_view(['PUT'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a user
@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)