from rest_framework import viewsets
from .models import Set, Exercise
from .serializers import ExerciseSerializer, SetSerializer, UserSerializer
from django.contrib.auth.models import User


class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
