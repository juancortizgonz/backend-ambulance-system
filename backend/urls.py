from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("api/v1/auth/", include("authenticationapi.urls")),
    # path('api/v1/notifications/', include('notifications.urls')),
    path("api/v1/", include("api.urls")),
    path('admin/', admin.site.urls),

    # Swagger Docs
    path("api/v1/schema/", SpectacularAPIView.as_view(), name='schema'), # Download a file
    path("api/v1/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path("api/v1/schema/redoc/", SpectacularRedocView.as_view(url_name='schema'), name="redoc"),
]
