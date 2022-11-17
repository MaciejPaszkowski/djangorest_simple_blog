from django.contrib import admin
from django.urls import include, path

from djangorestblog.settings import API_URI_PREFIX

urlpatterns = [
    path(f"{API_URI_PREFIX[1:]}/admin/", admin.site.urls),
    path(f"{API_URI_PREFIX[1:]}/auth/", include("authentication.urls")),
    path(f"{API_URI_PREFIX[1:]}/post/", include("posts.urls")),
]
