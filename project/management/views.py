#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 6/12/2024
import os

import requests
from django.contrib.admin.views.decorators import staff_member_required

# Third party imports
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from fpdf import FPDF
from reportlab.pdfgen import canvas

from .models import Property


# Create your views here.


def index(request):
    return HttpResponse("Management resources")


def host_upload(request):
    return HttpResponse("Hello, world. Here you can update your data.")


def apartments(request):
    response = requests.get(
        "https://login.smoobu.com/api/apartments",
        headers={
            "Content-type": "application/json",
            "Api-Key": os.getenv("APIKEY"),
        },
    )
    print(response)
    data = response.json()
    for apt in data["apartments"]:
        response_single = requests.get(
            f"https://login.smoobu.com/api/apartments/{apt['id']}",
            headers={
                "Content-type": "application/json",
                "Api-Key": os.getenv("APIKEY"),
            },
        )
        location = response_single.json()["location"]
        timeZone = response_single.json()["timeZone"]
        # insert if not existing and update if existes
        if not Property.objects.filter(smoobu_id=apt["id"]).exists():
            Property(
                name=apt["name"],
                smoobu_id=apt["id"],
                street=location["street"],
                zip=location["zip"],
                city=location["city"],
                country=location["country"],
                latitude=location["latitude"],
                longitude=location["longitude"],
                time_zone=timeZone,
            ).save()
        else:
            Property.objects.filter(smoobu_id=apt["id"]).update(
                name=apt["name"],
                smoobu_id=apt["id"],
                street=location["street"],
                zip=location["zip"],
                city=location["city"],
                country=location["country"],
                latitude=location["latitude"],
                longitude=location["longitude"],
                time_zone=timeZone,
            )

    return render(request, "management/apartments.html")


def contratto_locazione(request):
    prop = Property.objects.filter(id=1).first()
    context = {
        "name": prop.name,
        "street": prop.street,
        "zip": prop.zip,
        "city": prop.city,
        "country": prop.country,
    }
    return render(request, "management/contratto_locazione.html", context)


def generate_pdf_report_scheda(request, object_id):
    # Fetch the object by ID
    obj = get_object_or_404(Property, id=object_id)

    # Create the HTTP response with PDF headers
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="report_{obj.id}.pdf"'

    # Create a PDF canvas
    p = canvas.Canvas(response)

    # Set title and metadata
    p.setTitle(f"Report for {obj.name}")
    p.drawString(100, 800, f"Property Report for {obj.name}")
    p.drawString(100, 780, f"ID: {obj.id}")

    # Close the PDF and finalize the response
    p.showPage()
    p.save()

    return response
