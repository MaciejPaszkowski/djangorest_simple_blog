from django.contrib import admin
from django.urls import include, path
from settings import API_URI_PREFIX

# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view as swagger_get_schema_view


# schema_view=swagger_get_schema_view(
#     openapi.Info(
#         title="Django Rest Blog API",
#         default_version="1.0.0",
#         description="Api documentation for djangorestblog "
#     ),
#     public=True,

# )

urlpatterns = [
    path(f"{API_URI_PREFIX[1:]}/post/admin/", admin.site.urls),
    path(f"{API_URI_PREFIX[1:]}/post/auth/", include("authentication.urls")),
    path(f"{API_URI_PREFIX[1:]}/post/", include("posts.urls")),
    # path('swagger/schema/', schema_view.with_ui('swagger',),name="swagger-schema"),
]
