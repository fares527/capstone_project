from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('projects.urls')),
    path('api-token-auth/', auth_views.obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)