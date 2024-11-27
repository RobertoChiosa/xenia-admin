
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("host_id/", views.host_upload),
]
