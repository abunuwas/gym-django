from django.contrib.auth.models import User
from django.db import models


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


class Exercise(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField()
    set = models.ForeignKey(Set, on_delete=models.CASCADE)