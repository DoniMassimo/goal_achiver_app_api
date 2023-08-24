from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CounterGoal, LimitCounterGoal, StarsGoal, GoalsGroup, Goal

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']
        
        

class GoalSerializer(serializers.ModelSerializer):
    def to_representation(self, child):
        if isinstance(child, CounterGoal):
            serializer = CounterGoalSerializer(child)
        elif isinstance(child, LimitCounterGoal):
            serializer = LimitCounterGoalSerializer(child)
        elif isinstance(child, StarsGoal):
            serializer = StarsGoalSerializer(child)
        return serializer.data
    
    class Meta(object):
        model = Goal     
        fields = '__all__'   

class GoalsGroupSerializer(serializers.ModelSerializer):
    goal = GoalSerializer(many=True) 
    
    class Meta(object):
        model = GoalsGroup
        fields = ['title', 'goal']


class CounterGoalSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CounterGoal
        fields = '__all__'

class LimitCounterGoalSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = LimitCounterGoal
        fields = '__all__'

class StarsGoalSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = StarsGoal
        fields = '__all__'