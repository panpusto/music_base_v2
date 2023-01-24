from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    # debug
    path('__debug__/', include('debug_toolbar.urls')),
    # admin
    path('admin/', admin.site.urls),
    # user management
    path('accounts/', include('allauth.urls')),
    # api
    path('api/v1/', include('apis.urls')),
    path('api-auth/', include('rest_framework.urls')),
    #schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path("api/schema/redoc/", SpectacularRedocView.as_view(
        url_name="schema"), name="redoc",),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(
        url_name="schema"), name="swagger-ui"),
    # local apps
    path('', include('pages.urls')),
    path('genres/', include('genres.urls')),
    path('labels/', include('labels.urls')),
    path('musicians/', include('musicians.urls')),
    path('bands/', include('bands.urls')),
    path('musiciantoband/', include('musiciansbands.urls')),
    path('albums/', include('albums.urls')),
    path('reviews/', include('reviews.urls')),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
