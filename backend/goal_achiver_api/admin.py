from django.contrib import admin
from .models import LimitCounterGoal, GoalsGroup, Goal

admin.site.register(Goal)
admin.site.register(GoalsGroup)
