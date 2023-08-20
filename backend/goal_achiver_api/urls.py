from django.urls import path, include
from . import views


urlpatterns = [
    path('start', view=views.start)
]
