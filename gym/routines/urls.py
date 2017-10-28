from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'sets', views.SetViewSet)
router.register(r'exercises', views.ExerciseViewSet)
router.register(r'useres', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
