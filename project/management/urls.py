#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 5/12/2024

# Third party imports
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("host_id/", views.host_upload),
    path("apartments/", views.apartments),
]
