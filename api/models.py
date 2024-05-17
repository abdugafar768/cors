from django.db import models

class Task(models.Model):
    user = models.CharField(max_length=50)
    task = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=False)
