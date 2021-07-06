from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from .yasg import urlpatterns as yasgUrls


urlpatterns = [
    path('Dota/', include('Dota.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += yasgUrls