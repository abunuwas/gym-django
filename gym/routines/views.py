from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework_jwt import authentication

from .models import Set, Exercise
from .serializers import ExerciseSerializer, SetSerializer, UserSerializer


class SetViewSet(viewsets.ModelViewSet):
    serializer_class = SetSerializer

    authentication_classes = (authentication.JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Set.objects.filter(user=self.request.user)

    def perform_create(self):
        serializer.data.owner = self.request.user
        super(SetViewSet, self).perform_create(serializer)


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
