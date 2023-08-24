from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserGoalsGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True) 


class GoalsGroup(models.Model):    
    title = models.TextField()
    id = models.AutoField(primary_key=True) 
    creation_date = models.DateField(default=timezone.now)
    #user_goals_groups = models.ForeignKey(UserGoalsGroups, on_delete=models.CASCADE)
    

class Goal(models.Model):
    id = models.AutoField(primary_key=True) 
    title = models.TextField()
    goals_group = models.ForeignKey(GoalsGroup, on_delete=models.CASCADE)
    
    
class CounterGoal(Goal):
    counter = models.IntegerField(default=0)

class LimitCounterGoal(Goal):
    counter = models.IntegerField(default=0)
    limit = models.IntegerField(default=0)

class StarsGoal(Goal):
    stars = models.IntegerField(default=0)
    
    
class GoalsGroupTemplate(models.Model): # template to create goals group with standard data
    id = models.AutoField(primary_key=True) 
    goals_group = models.OneToOneField(GoalsGroup, on_delete=models.CASCADE, related_name='template')