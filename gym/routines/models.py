from django.contrib.auth.models import User
from django.db import models


class Exercise(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField()


class Set(models.Model):
    id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField()
    repetitions = models.IntegerField()
    weight = models.FloatField()
    # pound | kg
    weight_unit = models.CharField(max_length=20)
    # good | medium | bad
    performance = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
