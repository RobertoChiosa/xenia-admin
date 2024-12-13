#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 6/12/2024
# Third party imports
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path

from . import views

urlpatterns = [
    path("<int:host_id>/home", views.home),
    path("<int:host_id>/profile", views.profile),
    path("login/", views.login),
    path("apartments/", views.apartments),
    path("reservations/", views.reservations),
    path("<int:host_id>/contratto-locazione/", views.contratto_locazione),
    path(
        "<int:property_id>/report/scheda",
        views.generate_pdf_report_scheda,
        name="generate_pdf_report_scheda",
    ),
]
