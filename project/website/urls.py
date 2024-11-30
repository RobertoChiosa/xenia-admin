from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("property", views.property, name="property"),
    path("checkin", views.checkin, name="checkin"),
    path("explore", views.explore, name="explore"),
]
