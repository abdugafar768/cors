from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    