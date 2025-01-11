from blog.views import (
  BlogDeleteView,
  BlogCreateView,
  BlogListView,
  BlogUpdateView
)
from django.urls import path

urlpatterns = [
    path("", BlogListView.as_view(), name="list"),
    path("create/", BlogCreateView.as_view(), name="create"),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="delete"),
]
