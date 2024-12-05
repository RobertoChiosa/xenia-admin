#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 4/12/2024

# Third party imports
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
