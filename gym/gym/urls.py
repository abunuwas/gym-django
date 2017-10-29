from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^accounts/', include('accounts.urls'), name='accounts'),
    url(r'^routines/', include('routines.urls'), name='routines'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token, name='api_auth'),
]
