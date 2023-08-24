from django.urls import path, include
from . import views


urlpatterns = [
    path('start', view=views.start),
    path('sign_up', view=views.sign_up),
    path('login', view=views.login),
    path('c', view=views.create_goals_group),
    path('a', view=views.add_goal),
    path('g', view=views.get_goal),
]
