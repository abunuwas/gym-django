from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'sets', views.SetViewSet, base_name='sets-list')
router.register(r'exercises', views.ExerciseViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
