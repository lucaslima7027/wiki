from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.showEntry, name="showEntry"),
    path("new-page/edit", views.newPage, name="newPage")
]
