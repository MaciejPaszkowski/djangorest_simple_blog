from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import renderers
from rest_framework.schemas import get_schema_view
from settings import API_URI_PREFIX

urlpatterns = [
    path(f"{API_URI_PREFIX[1:]}/post/admin/", admin.site.urls),
    path(f"{API_URI_PREFIX[1:]}/post/auth/", include("authentication.urls")),
    path(f"{API_URI_PREFIX[1:]}/post/", include("posts.urls")),
    # path('swagger/schema/', get_schema_view(title='API Schema', description='Guide for the REST API'),name="swagger_schema"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # path('swagger-ui',TemplateView.as_view(
    #     template_name='docs.html',
    #     extra_context={'schema_url':"swagger_schema"}
    # ), name='swagger-ui'),
    path(
        "swagger-ui",
        SpectacularSwaggerView.as_view(template_name="docs.html", url_name="schema"),
        name="swagger-ui",
    ),
]
