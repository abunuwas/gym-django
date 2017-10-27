from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Exercise, Set


class Exercise(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise


class Set(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Set


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
