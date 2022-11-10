from django.urls import path

from . import views

urlpatterns = [
    path("", views.HelloPostView.as_view(), name="hello_post"),
]
