#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 6/12/2024
# Third party imports
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("host_id/", views.host_upload),
    path("apartments/", views.apartments),
    path("contratto-locazione/", views.contratto_locazione),
    path(
        "<int:property_id>/report/scheda",
        views.generate_pdf_report_scheda,
        name="generate_pdf_report_scheda",
    ),
]
