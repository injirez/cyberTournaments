from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from .yasg import urlpatterns as yasgUrls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('dota/', include('Dota.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += yasgUrls