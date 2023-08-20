from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

@api_view(['GET'])
def start(request):
    print(request.data)
    return Response({"message": "Hello, world!"})

@api_view(['POST'])
def sign_up(request):
    serilizer = UserSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token':token.key, 'user':serilizer.data})
    return Response(serilizer.errors)

@api_view(['POST'])
def login(request):
    print(request.data)
    user = get_object_or_404(User, username=[request.data['username']])
    if not user.check_password(request.data['password']):
        return Response({'detail':'password wrong'}, status=status.HTTP_404_NOT_FOUND)
    token = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(isinstance=user)
    return Response({'token':token.key, 'user':serilizer.data})
