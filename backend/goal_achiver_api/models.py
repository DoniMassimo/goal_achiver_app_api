from django.db import models
from django.contrib.auth.models import User

class GoalsGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
        

class Goal(models.Model):
    title = models.TextField()
    goals_group = models.ForeignKey(GoalsGroup, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True

class CounterGoal(Goal):
    counter = models.IntegerField(default=0)

class LimitCounterGoal(Goal):
    counter = models.IntegerField(default=0)
    limit = models.IntegerField(default=0)

class StarsGoal(Goal):
    stars = models.IntegerField(default=0)