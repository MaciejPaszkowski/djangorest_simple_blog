from django.urls import path

from . import views

urlpatterns = [
    path("", views.HelloPostView.as_view(), name="hello_post"),
    path("categories/", views.CategoryView.as_view(), name="categories"),
    path("categories/<uuid:id>/", views.CategoryIdView.as_view(), name="category"),
]
