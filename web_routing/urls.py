from django.urls import path

from . import views


urlpatterns = [
    path("<path:page_path>", views.index, name="index"),
]