#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 2/12/2024

# Third party imports
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about", views.about_view, name="about"),
    path("property", views.property_view, name="property"),
    path("checkin", views.checkin_view, name="checkin"),
    path("explore", views.explore_view, name="explore"),
]
