from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, GoalsGroupSerializer, LimitCounterGoalSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import LimitCounterGoal, GoalsGroup
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
    user = User.objects.get(username=request.data['username'])
    print(user)
    if not user.check_password(request.data['password']):
        return Response({'detail':'password wrong'}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    # if serializer.is_valid():
    #     return Response({'token':token, 'user':serializer.data})
    # else:
    # return Response(serializer.errors)
    return Response({'token':token.key, 'user':serializer.data})

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def create_goals_group(request):
    goals_group_ser = GoalsGroupSerializer(data=request.data)
    if goals_group_ser.is_valid():
        goals_group_ser.save()
    return Response({})

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def add_goal(request):
    lg = LimitCounterGoal(title='a', limit=5, goals_group=GoalsGroup.objects.get(title='f'))
    lg.save()
    return Response({})
    
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def get_goal(request):
    lc = GoalsGroup.objects.get(title='f')
    lc_ser = GoalsGroupSerializer(lc)
    return Response(lc_ser.data)




